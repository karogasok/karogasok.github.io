"""Topic model over the writings.

The corpus is small — a few hundred full-text documents, an order of magnitude
under a newsroom-scale run — so the clustering is tuned tighter than usual:
``min_cluster_size`` in single digits, and ``leaf`` selection, which stops
HDBSCAN collapsing a tight anisotropic embedding space into one giant topic.

Two different views of the same document go into the fit, and confusing them is
the easy mistake:

* the **embedding** is built from the raw text, because the transformer does its
  own morphology and wants real sentences;
* the **document string** handed to BERTopic is the space-joined emtsv lemma
  list, because that is what the c-TF-IDF vectoriser reads when it names a
  topic. Feeding it raw Hungarian would scatter one lemma across a dozen
  inflected surface forms.

:func:`fit_topics` therefore takes both, and they must be in the same order.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:  # pragma: no cover - import cost only paid at runtime
    from bertopic import BERTopic

#: Outlier label used by HDBSCAN and BERTopic alike.
OUTLIER = -1

#: Smallest group of documents allowed to become a topic. Tuned for a corpus of
#: a few hundred documents; the BERTopic default of 10 leaves too little.
MIN_CLUSTER_SIZE = 7

#: Seeded everywhere, so two runs of the pipeline agree.
RANDOM_SEED = 42

#: A lemma must appear in at least this many documents to be a topic term.
MIN_DF = 2

#: Minimum assignment probability for a short document to join a topic.
#: Below this it stays an outlier rather than being forced into a theme.
PROBABILITY_FLOOR = 0.25

#: Share of a document's membership a topic must reach to become one of its
#: labels. Chosen after reading ``scripts/report_multilabel.py``; with 19 topics
#: the uniform prior is 0.053, so this is a little under twice chance.
MULTI_LABEL_FLOOR = 0.10

#: Most labels one document may carry.
MULTI_LABEL_CAP = 3

#: A secondary label must also reach this fraction of the document's strongest
#: score. Without it a diffuse membership vector — which is exactly what HDBSCAN
#: produces for a document sitting near the noise boundary — hands three themes
#: to a document that really has none.
#:
#: Measured against the strongest score rather than the primary's, because the
#: primary usually comes from c-TF-IDF outlier reduction and frequently has a
#: membership score of 0.00. Comparing against zero is a gate that never closes.
MULTI_LABEL_RATIO = 0.5


@dataclass(frozen=True)
class TopicSummary:
    """The three numbers that decide whether a model is worth shipping.

    Attributes:
        n_topics: Number of topics, not counting the outlier bin.
        n_documents: Documents the model was fitted on.
        outlier_share: Fraction of documents left unassigned.
        largest_share: Fraction of documents in the biggest single topic.
    """

    n_topics: int
    n_documents: int
    outlier_share: float
    largest_share: float

    @property
    def healthy(self) -> bool:
        """Whether the model passes the two agreed sanity thresholds.

        A model is unhealthy if more than 40% of documents are outliers, or if
        one topic holds more than a third of the corpus. Either means the
        clustering found structure that is not there.

        Example:
            >>> TopicSummary(8, 300, 0.3, 0.2).healthy
            True
            >>> TopicSummary(2, 300, 0.6, 0.2).healthy
            False
            >>> TopicSummary(3, 300, 0.1, 0.5).healthy
            False
        """
        return self.outlier_share <= 0.40 and self.largest_share <= 1 / 3


def summarise(topics: Sequence[int]) -> TopicSummary:
    """Describe an assignment without needing the model that produced it.

    Args:
        topics: One topic id per document, ``-1`` for outliers.

    Returns:
        The summary. An empty assignment gives all-zero shares.

    Example:
        >>> s = summarise([0, 0, 0, 1, 1, -1])
        >>> s.n_topics, s.n_documents
        (2, 6)
        >>> round(s.outlier_share, 3), round(s.largest_share, 3)
        (0.167, 0.5)
        >>> summarise([]).n_topics
        0
    """
    total = len(topics)
    if total == 0:
        return TopicSummary(0, 0, 0.0, 0.0)
    assigned = [t for t in topics if t != OUTLIER]
    sizes: dict[int, int] = {}
    for topic in assigned:
        sizes[topic] = sizes.get(topic, 0) + 1
    return TopicSummary(
        n_topics=len(sizes),
        n_documents=total,
        outlier_share=(total - len(assigned)) / total,
        largest_share=(max(sizes.values()) / total) if sizes else 0.0,
    )


def is_wordlike(lemma: str) -> bool:
    """Whether a lemma is a word rather than stray punctuation.

    emtsv tags typographic quotes and unrecognised characters as nouns, so
    ``„``, ``“`` and the replacement character U+FFFD all arrived as content
    words and reached the topic terms. One post's link text still carries
    mojibake from the original blog, including a CJK character that emtsv
    cannot represent.

    A lemma qualifies if its **first** character is a letter. Testing whether it
    merely contains one is not enough: ``:D`` would pass on its ``D``, and it
    was a top term for the link-roundup topic. Leading-letter also drops ``10%``
    and percent-encoded URL fragments, while keeping ``R`` and ``nyest.hu``,
    which are real terms in this corpus.

    Args:
        lemma: The lemma to test.

    Returns:
        Whether to keep it.

    Example:
        >>> [is_wordlike(x) for x in ("nyelv", "R", "nyest.hu")]
        [True, True, True]
        >>> [is_wordlike(x) for x in ("„", "\ufffd", ":D", "-", "10%", "")]
        [False, False, False, False, False, False]
    """
    return bool(lemma) and lemma[0].isalpha()


def drop_stopwords(lemma_docs: Sequence[str], stopwords: Iterable[str]) -> list[str]:
    """Remove stopwords from space-joined lemma documents.

    This has to happen here rather than in the vectoriser. ``CountVectorizer``
    takes a ``stop_words`` argument, but **silently ignores it whenever
    ``analyzer`` is a callable** — it emits a warning and carries on. Since the
    analyzer must be ``str.split`` to keep pre-tokenised input intact, passing
    the list there would look like filtering while doing nothing.

    Matching is case-insensitive, because lemmas keep the case emtsv produced
    and the stopword lists are lowercase. Anything :func:`is_wordlike` rejects
    goes too, since stray punctuation is not something a stopword list can
    enumerate.

    Args:
        lemma_docs: Space-joined lemmas, one string per document.
        stopwords: Lemmas to drop.

    Returns:
        The documents with stopwords removed, in the same order.

    Example:
        >>> drop_stopwords(["a nyelv és a gép", "I to nyelv „"], {"a", "és", "i", "to"})
        ['nyelv gép', 'nyelv']
    """
    stops = {word.casefold() for word in stopwords}
    return [
        " ".join(
            word
            for word in document.split()
            if word.casefold() not in stops and is_wordlike(word)
        )
        for document in lemma_docs
    ]


def probability_columns(fitted: Sequence[int]) -> list[int]:
    """Topic ids in the column order of BERTopic's probability matrix.

    BERTopic drops the outlier bin from the matrix and orders the rest
    ascending, so column *j* is the *j*-th smallest non-outlier topic id. There
    is no getter for this; getting it wrong shifts every score by one topic and
    the result looks like a worse model rather than a bug.

    Args:
        fitted: The topic id assigned to each fitted document.

    Returns:
        Topic ids, ascending.

    Example:
        >>> probability_columns([2, 0, -1, 2, 5])
        [0, 2, 5]
        >>> probability_columns([-1, -1])
        []
    """
    return sorted({int(topic) for topic in fitted if topic != OUTLIER})


def labels_above(
    row: Sequence[float],
    columns: Sequence[int],
    *,
    floor: float = MULTI_LABEL_FLOOR,
) -> list[tuple[int, float]]:
    """One document's topics that clear ``floor``, strongest first.

    Args:
        row: The document's membership scores, one per column.
        columns: Topic ids, from :func:`probability_columns`.
        floor: Minimum score. Defaults to :data:`MULTI_LABEL_FLOOR`.

    Returns:
        ``(topic_id, score)`` pairs, descending by score. Ties break towards the
        lower topic id, which is the larger topic, so the ordering is stable.

    Raises:
        ValueError: If ``row`` and ``columns`` disagree on length.

    Example:
        >>> labels_above([0.6, 0.02, 0.15], [0, 1, 2])
        [(0, 0.6), (2, 0.15)]
        >>> labels_above([0.04, 0.03], [0, 1])
        []
    """
    if len(row) != len(columns):
        msg = (
            f"row has {len(row)} scores but there are {len(columns)} topic "
            f"columns; the probability matrix and the topic list disagree"
        )
        raise ValueError(msg)
    above = [
        (int(topic), float(score))
        for topic, score in zip(columns, row, strict=True)
        if score >= floor
    ]
    above.sort(key=lambda pair: (-pair[1], pair[0]))
    return above


def label_set(
    row: Sequence[float],
    columns: Sequence[int],
    primary: int,
    *,
    floor: float = MULTI_LABEL_FLOOR,
    cap: int = MULTI_LABEL_CAP,
    ratio: float = MULTI_LABEL_RATIO,
) -> tuple[list[int], list[float]]:
    """Multi-label a document, its primary label always first.

    ``primary`` is the ``topic_reduced`` label, which came from c-TF-IDF outlier
    reduction rather than from this matrix, so it is not necessarily the argmax.
    It leads anyway: a c-TF-IDF reassignment reads the document's own
    vocabulary, which is better evidence than a membership vector computed in a
    five-dimensional projection.

    Args:
        row: The document's membership scores.
        columns: Topic ids, from :func:`probability_columns`.
        primary: The single label already assigned, or :data:`OUTLIER`.
        floor: Minimum score for a label. Defaults to
            :data:`MULTI_LABEL_FLOOR`.
        cap: Most labels to return. Defaults to :data:`MULTI_LABEL_CAP`.
        ratio: A secondary label must reach this fraction of the strongest
            score in ``row``. Defaults to :data:`MULTI_LABEL_RATIO`.

    Returns:
        ``(topic_ids, scores)``, primary first. A document whose primary is
        :data:`OUTLIER` and whose scores all sit under ``floor`` gets empty
        lists — no theme is the honest answer for a two-sentence blurb.

    Example:
        >>> label_set([0.6, 0.02, 0.4], [0, 1, 2], 0)
        ([0, 2], [0.6, 0.4])

        The ratio gate drops a label that clears the floor but is dwarfed:

        >>> label_set([0.8, 0.11, 0.0], [0, 1, 2], 0)
        ([0], [0.8])

        The primary leads even when another topic scores higher:

        >>> label_set([0.3, 0.5, 0.0], [0, 1, 2], 0)
        ([0, 1], [0.3, 0.5])

        >>> label_set([0.01, 0.01], [0, 1], -1)
        ([], [])
    """
    above = labels_above(row, columns, floor=floor)
    scores = dict(above)
    ids: list[int] = []
    if primary != OUTLIER:
        ids.append(int(primary))
    strongest = above[0][1] if above else 0.0
    gate = strongest * ratio
    for topic, score in above:
        if len(ids) >= cap:
            break
        if topic in ids or score < gate:
            continue
        ids.append(topic)
    return ids, [round(scores.get(topic, 0.0), 4) for topic in ids]


@dataclass(frozen=True)
class LabelSpread:
    """How many labels the documents ended up carrying.

    Attributes:
        counts: Number of labels mapped to number of documents.
        mean: Average labels per document.
        largest: Most labels any one document carries.
        coverage: Share of documents carrying at least one label.
    """

    counts: dict[int, int]
    mean: float
    largest: int
    coverage: float


def label_spread(label_sets: Sequence[Sequence[int]]) -> LabelSpread:
    """Describe a multi-label assignment before anything is written.

    Args:
        label_sets: One list of topic ids per document.

    Returns:
        The spread. An empty corpus gives zeros rather than raising, because
        this is a reporting function and a report of nothing is still a report.

    Example:
        >>> spread = label_spread([[1], [1, 2], [], [3, 4, 5], [2]])
        >>> spread.counts[1], spread.counts[0], spread.largest
        (2, 1, 3)
        >>> round(spread.mean, 2), round(spread.coverage, 2)
        (1.4, 0.8)
        >>> label_spread([]).coverage
        0.0
    """
    total = len(label_sets)
    if total == 0:
        return LabelSpread({}, 0.0, 0, 0.0)
    counts: dict[int, int] = {}
    for labels in label_sets:
        counts[len(labels)] = counts.get(len(labels), 0) + 1
    assigned = sum(1 for labels in label_sets if labels)
    total_labels = sum(len(labels) for labels in label_sets)
    return LabelSpread(
        counts=dict(sorted(counts.items())),
        mean=total_labels / total,
        largest=max(len(labels) for labels in label_sets),
        coverage=assigned / total,
    )


def build_model(
    *,
    min_cluster_size: int = MIN_CLUSTER_SIZE,
    seed: int = RANDOM_SEED,
    min_df: int = MIN_DF,
) -> BERTopic:
    """Assemble a seeded BERTopic configured for lemmatised Hungarian.

    The vectoriser splits on whitespace rather than a word-character pattern, so
    the pre-tokenised lemma stream survives intact and no accented letter is
    dropped on the way in. That choice is why stopwords cannot be handed to the
    vectoriser — see :func:`drop_stopwords`, which the caller must apply first.

    ``language="multilingual"`` is set even though embeddings are always passed
    in precomputed: it decides which backend BERTopic would reach for if that
    ever stopped being true, and the English default would be wrong here.

    Args:
        min_cluster_size: Smallest allowed topic. Defaults to
            :data:`MIN_CLUSTER_SIZE`.
        seed: UMAP random state. Defaults to :data:`RANDOM_SEED`.
        min_df: Minimum document frequency for a term. Defaults to
            :data:`MIN_DF`.

    Returns:
        An unfitted model.

    Raises:
        ValueError: If ``min_cluster_size`` is below 2.
    """
    if min_cluster_size < 2:
        msg = f"min_cluster_size must be at least 2, got {min_cluster_size}"
        raise ValueError(msg)

    from bertopic import BERTopic
    from bertopic.vectorizers import ClassTfidfTransformer
    from hdbscan import HDBSCAN
    from sklearn.feature_extraction.text import CountVectorizer
    from umap import UMAP

    umap_model = UMAP(
        n_neighbors=15,
        n_components=5,
        min_dist=0.0,
        metric="cosine",
        random_state=seed,
    )
    hdbscan_model = HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=1,
        metric="euclidean",
        cluster_selection_method="leaf",
        prediction_data=True,
    )
    vectorizer_model = CountVectorizer(analyzer=str.split, min_df=min_df)
    return BERTopic(
        language="multilingual",
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer_model,
        ctfidf_model=ClassTfidfTransformer(reduce_frequent_words=True),
        calculate_probabilities=True,
        verbose=False,
    )


def fit_topics(
    model: BERTopic,
    lemma_docs: Sequence[str],
    embeddings: np.ndarray,
) -> tuple[list[int], np.ndarray]:
    """Fit the model, keeping the original assignment.

    Args:
        model: An unfitted model from :func:`build_model`.
        lemma_docs: Space-joined lemmas, one string per document.
        embeddings: Unit-length document vectors, row-aligned to ``lemma_docs``.

    Returns:
        The topic ids and the probability matrix.

    Raises:
        ValueError: If the two inputs disagree on length, or either is empty.
    """
    if len(lemma_docs) == 0:
        msg = "cannot fit a topic model on an empty corpus"
        raise ValueError(msg)
    if len(lemma_docs) != len(embeddings):
        msg = (
            f"lemma_docs and embeddings must be row-aligned, got "
            f"{len(lemma_docs)} and {len(embeddings)}"
        )
        raise ValueError(msg)
    topics, probabilities = model.fit_transform(list(lemma_docs), embeddings)
    return list(topics), np.asarray(probabilities)


def assign(
    model: BERTopic,
    lemma_docs: Sequence[str],
    embeddings: np.ndarray,
    *,
    floor: float = PROBABILITY_FLOOR,
) -> list[int]:
    """Place already-unseen documents onto the fitted topics.

    This is how the short pieces — search-blog leads, media blurbs — get a
    theme without having been allowed to define one. A document whose best
    match is weaker than ``floor`` stays an outlier.

    Args:
        model: A fitted model.
        lemma_docs: Space-joined lemmas.
        embeddings: Unit-length vectors, row-aligned to ``lemma_docs``.
        floor: Minimum probability to accept. Defaults to
            :data:`PROBABILITY_FLOOR`.

    Returns:
        One topic id per document.
    """
    return place(model, lemma_docs, embeddings, floor=floor)[0]


def place(
    model: BERTopic,
    lemma_docs: Sequence[str],
    embeddings: np.ndarray,
    *,
    floor: float = PROBABILITY_FLOOR,
) -> tuple[list[int], np.ndarray]:
    """As :func:`assign`, but keeps the probability matrix.

    Args:
        model: A fitted model.
        lemma_docs: Space-joined lemmas.
        embeddings: Unit-length vectors, row-aligned to ``lemma_docs``.
        floor: Minimum probability to accept. Defaults to
            :data:`PROBABILITY_FLOOR`.

    Returns:
        The topic ids and the probability matrix. The matrix is returned
        untouched by ``floor`` — the floor decides the single label, while
        multi-labelling reads the raw scores.
    """
    if len(lemma_docs) == 0:
        return [], np.zeros((0, 0))
    topics, probabilities = model.transform(list(lemma_docs), embeddings)
    probabilities = np.asarray(probabilities)
    strengths = _best_strength(probabilities, len(topics))
    assigned = [
        int(topic) if strength >= floor else OUTLIER
        for topic, strength in zip(topics, strengths, strict=True)
    ]
    return assigned, probabilities


def _best_strength(probabilities: np.ndarray, n: int) -> np.ndarray:
    """Reduce a probability array to one confidence per document.

    ``transform`` hands back a per-topic matrix when the model was built with
    ``calculate_probabilities=True`` and a flat vector of strengths otherwise,
    so both shapes are accepted rather than assumed.

    Args:
        probabilities: Either shape ``(n,)`` or ``(n, n_topics)``.
        n: Expected number of documents.

    Returns:
        Shape ``(n,)`` confidences; ones if the array is unusable.

    Example:
        >>> _best_strength(np.array([[0.1, 0.7], [0.6, 0.2]]), 2).tolist()
        [0.7, 0.6]
        >>> _best_strength(np.array([0.3, 0.9]), 2).tolist()
        [0.3, 0.9]
        >>> _best_strength(np.array([]), 2).tolist()
        [1.0, 1.0]
    """
    if probabilities.size == 0:
        return np.ones(n)
    if probabilities.ndim == 2:
        return probabilities.max(axis=1)
    return probabilities
