---
title: "Natural Language Processing for the Working Programmer - interview with the authors"
slug: "natural-language-processing-for-working"
date: 2011-04-28T11:36:00.003Z
publishDate: 2011-04-28T11:36:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/natural-language-processing-for-working.html"
regi_cimkek:
  - "computational linguistics"
  - "haskell"
  - "interview"
  - "natural language processing"
regi_cimkek_mind:
  - "computational linguistics"
  - "haskell"
  - "interview"
  - "natural language processing"
---

**These days we are the eyewitnesses of the data boom. More and more linguists turn to statistical and probabilistic methods and start using the quasi-standard tools of data analysis like R, Python and databases (SQL and those noSQL stuffs). It wasn’t easier to get into natural language processing, the nltk toolkit and the book is freely available and there are other great books on the market that teach you the basics and more advanced techniques. Although this huge success, more and more nlp company choose a functional programming language as a tool of development and the [Natural Language Processing for the Working Programmer](http://nlpwp.org/) book (which is presenting the basic ideas of nlp in Haskell, and it is in draft version) got a lot of attention in the community. We interviewed the authors of the book; Daniël de Kok and Harm Brouwer.**

```
Daniël and Harm, please tell us something about yourselves.

Daniel: I am a Dutchman who works as a PhD candidate at the University of Groningen on a project that implements
a sentence generator using the Alpino grammar and lexicon for Dutch. Recently, I have worked on reversible models
for parse disambiguation and fluency ranking. I also have teaching duties,giving a course on NLP (computational
 grammars and parsers) to undergraduates.

I enjoy music, particularly jazz and composers such as Zorn and Zappa. I also like (recreational) cycling, climbing, and Zen.

You can find my website at:

http://danieldk.eu/

Feel free to ask me questions:

me@danieldk.eu

Harm: I did my BA degree in computational linguistics, and got a MSc in cognitive neuroscience and cognitive modeling.
Currently, I am doing a PhD in computational psycholinguistics, with a strong focus on neurocomputational modeling.
Besides being a researcher, I taught logic programming (Prolog) to undergraduate computational linguistics students.
 Of course, I also work on the NLPWP book when I can. In my spare time, I like reading on psychology, neuroscience,
 philosophy of mind, and programming.

You can find my website at:

http://www.hbrouwer.eu

Or drop me a line:

me@hbrouwer.eu

Choosing Haskell as a language for presenting the ideas behind statistical natural language processing isn’t that obvious.
 Why did you choose it?

As you mentioned in your introduction, in the 90s we have seen a shift of interest in computational linguistics from
knowledge-based methods to data-driven methods. Along this change we saw a shift in programming languages. Where
knowledge-driven systems were commonly written in languages such as Prolog, nowadays computational linguists write
 data-driven solutions in languages like Perl, Python, R, or Java.

However, we believe that there will ultimately be a synthesis of knowledge-based and data-driven methods. Functional
languages such as Haskell provide a sweet spot between these approaches. On the one hand, it is easy to use typical
Prolog constructs, such as structural matching and backtracking (choice points). On the other hand, data processing is
in Haskell's DNA, given the prevalent use of higher-order functions such as folds and maps.

An advantage of Haskell is that it often leads to short and elegant solutions. If exploited appropriately, this is also an
educational advantage, since examples will not become dreadful.

Of course, Haskell is not the only language in the intersection of knowledge-based and data-driven approaches. Another
candidate that comes to mind are languages in the ML family such as OCaml and F#. However, we just liked Haskell a
 bit more.

Haskell isn’t famous as a language for nlp, the list of nlp libraries is quite short compared to other languages . How can you get along without the support of extensive libraries?

This is a serious problem for using Haskell in computational linguistics.There are also weak spots in related functionality,
 such as machine learning and statistics. For this reason we encourage people to release modules that they think are
 useful to others. We also recommend people who are interested in NLP in Haskell to join the haskell-nlp mailing list:

http://projects.haskell.org/cgi-bin/mailman/listinfo/nlp

That said, we are amazed about the tremendous growth of Hackage over the past years. In areas that used to be weak
spots, for instance web frameworks, there are now lots mature packages. We hope that we will see comparable growth in
 the NLP area.

As a start, we will also release the source code to the book on Hackage.

Haskell has often been thought as a member of the Lisp family hence the tool of symbolic computation. Do you
think that Haskell can break out from this niche and occupy a position similar to the place of R or Python?

In terms of popularity, we do not think that Haskell will ever exceed languages such as Python or Ruby. Many of the
 powerful concepts of Haskell (lazy evaluation, purity, monads) will be too difficult to grasp for the average programmer.

Of course, the question is, does Haskell need to be that popular? To us it seems more important that the ecosystem is
 sustainable.  In other words, it would be nice if Haskell programmers have the opportunity to earn their bread and butter
with their favorite language.

What can the purely functional paradigm give us?

Enlightenment :-)

If you are not familiar with functional or logic programming, learning such a language can drastically change your
 perspective on programming in general. For instance, consider Haskell's isolation of side-effects. Initially, Haskell's
purity may drive you insane if you come from an imperative paradigm. But once it makes sense, it seems very logical
to 'tag' impure values using the IO type.

We still vividly remember our first Prolog lab, where we had to write a little crossword puzzle solver. Both of us literally
stared at the screen for an hour, and then suddenly it all made sense, and we wrote the solution down in five minutes.

Try for yourself, Learn Prolog Now! Exercise 2.4:

http://cs.union.edu/~striegnk/learn-prolog-now/html/node21.html#l2.ex4

Although the book is in draft version, it captured the attention of several people. How do you progress with
 manuscript? When will you finish the project?

The pace of writing is a bit slow due to work and other distractions. Nonetheless, new material is added monthly, and we
 are determined to finish the manuscript this or next year. Also, we still need to find a publisher.

What kind of feedback did you get from the readers so far?

We were honestly overwhelmed by the amount of encouragement. We also received many useful corrections and
suggestions. If you would like to contribute any changes to the book, feel free to fork our repository on GitHub and
issue a pull request:

https://github.com/nlpwp/book/

Also, one of our readers started a blog where he works through material from the book. His blog is a good read, and
gave us insight what potential readers would stumble over:

http://haskell.krowland.net/?cat=5
```
