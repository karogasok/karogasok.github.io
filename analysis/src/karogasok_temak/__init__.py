"""Topic model, keywords and themes over the Varjú Károgások corpus.

Only the light modules are re-exported here. :mod:`karogasok_temak.topics` and
:mod:`karogasok_temak.embed` pull in torch and BERTopic, which cost seconds to
import, so they stay behind an explicit import.
"""

from karogasok_temak.corpus import Document, load_corpus
from karogasok_temak.emtsv import Token, analyse, is_content_word, lemmatize
from karogasok_temak.keywords import Keyword, corpus_counts, document_keywords
from karogasok_temak.stopwords import hungarian_stopwords

__all__ = [
    "Document",
    "Keyword",
    "Token",
    "analyse",
    "corpus_counts",
    "document_keywords",
    "hungarian_stopwords",
    "is_content_word",
    "lemmatize",
    "load_corpus",
]
