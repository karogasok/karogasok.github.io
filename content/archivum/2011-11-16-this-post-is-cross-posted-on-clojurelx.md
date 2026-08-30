---
title: "Why Clojure lx?"
date: 2011-11-16T17:30:00Z
publishDate: 2011-11-16T17:30:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/11/this-post-is-cross-posted-on-clojurelx.html"
regi_cimkek:
  - "Clojure"
  - "linguistics"
regi_cimkek_mind:
  - "Clojure"
  - "linguistics"
  - "manifesto"
---

This post is cross-posted on [clojurelx](http://clojurelx.blogspot.com/), a new project blog

**The NLTK is a natural choice for students of linguistics and computer science. It has matured into a stable project, its users are very active, and it is now used outside of academia. Those who are into functional programming can use the [Scheme Natural Language Toolkit](http://www.snltk.org/), or learn from the [Natural Language Processing for the Working Programmer](http://nlpwp.org/), and those who needs the JVM can turn to [ScalaNLP](http://www.scalanlp.org/). So why brother with Clojure?**

First of all, we are NOT proposing a new framework/library here! Our main goal is to examine what Clojure offers to linguists. Although more and more linguistics departments offer courses in statistics and probability theory, the vast majority of students graduate with some background in discrete maths, mostly taught in an implicit way through a class in syntax and/or semantics (and the same is true for philosophy education). Using computer programs to test our scientific ideas is becoming a common practice in sciences, and this is true for linguists too. [Stefan Th. Gries distinguishes](http://szamitogepesnyelveszet.blogspot.com/2010/11/on-computational-corpus-linguistics.html) linguistic computing from computational linguistics; following him, we think linguistic computing will become a common methodology used in the language sciences.

So, what's the difference between computational linguistics and linguistic computing? Well, there is no clear boundary! We'd say computational linguistics (or natural language processing) is a kind of applied science and engineering, and as such it is more “goal oriented”. [Norvig's recent critique of Chomsky](http://norvig.com/chomsky.html) shows that commercial success is a measure of ideas, but despite the proliferation of statistical methods linguists are still doing research on rule based systems like HPSG, minimalism, etc., and new interdisciplinary research themes have emerged like [Parikh](http://www.sci.brooklyn.cuny.edu/cis/parikh/)'s idea of the [social software](http://www.sci.brooklyn.cuny.edu/cis/parikh/softsen.pdf) (and [game theoretic semantics](http://ibe.eller.arizona.edu/docs/2008/blume/jaeger-semantics.pdf) and [dynamic epistemic logic](http://www.csc.liv.ac.uk/%7Edel/), among others). But what is “pure” research today can become applied research tomorrow. To foster communication between pure and applied research, between linguistic computing and computational linguistics, we need a lingua franca.

As Clojure is the Lisp for the JVM, it is a convenient language for linguists. In the not-so-distant past, Touretzky wrote his [Gentle Introduction to Symbolic Computation](http://www.cs.cmu.edu/%7Edst/LispBook/), an excellent book for beginners in the humanities. Gazdar and Mellish Natural Language Processing in X (where X stands for [Prolog](http://www.informatics.susx.ac.uk/research/groups/nlp/gazdar/nlp-in-prolog/), [Lisp](http://www.informatics.susx.ac.uk/research/groups/nlp/gazdar/nlp-in-lisp/) or [Pop11](http://www.informatics.susx.ac.uk/research/groups/nlp/gazdar/nlp-in-pop11/index.html)) is a good introduction to finite state techniques, grammars, parsing and it even has a chapter on question answering. We don't deny that these techniques are old, but they are still part of the well-educated linguists' body of knowledge. Also, although Norivig's [PAIP](http://norvig.com/paip.html) is a real gem, one cannot argue against the “old” AI paradigm without seeing the past, and those ideas are still important for linguist, philosophers and cognitive scientists. Logic programming is a natural pair of functional programming. The basic techniques of computational linguistics can be expressed in logic programs, and although they have their computational limitations, these little programs has got unquestionable educational value.

Porting the classic into Clojure is not a novel idea, as some Google searching shows that people are turning the classic Lisp books like PAIP or the Structure and Interpretations of Computer Programs into modern Clojure. The core.logic library opens up the possibility to do the same with the Prolog literature.

The most common argument against NLTK is that you can't use mature, industry standard tools like the GATE framework, Stanford core, and openNLP. Clojure's Java interoperability solves this problem. If you are into machine learning, Weka, MALLET and etc. are at your service. The Incanter package provides an R-like statistical library.

With these tools in your hand, you can test your ideas in a language that's very close to what you learned about formal languages. Using Java libraries is like using rapid prototyping material when you are a marble sculptor. And as your works end result can be shared with the computational linguists, you can get more feedback, and even help from the greater community.

That's why we think that Clojure lx is an idea worths exploring. We'd like to test ourselves! Can we use Clojure to express our simple ideas? How easy is it to use Java libraries for a project? If you would like to join us, please send an email to zoltan.varju(at)gmail.com. We welcome everyone, linguists and Clojure hackers, philosphers, digital humanists, everyone who is interested!

**About us**  
[Zoltán Varjú](http://about.me/zoltanvarju) – computational linguist at Weblib LLC, [@zoltanvarju](http://twitter.com/#%21/zoltanvarju), [Számítógépes nyelvészet](http://szamitogepesnyelveszet.blogspot.com/)  
[Richard Littauer](http://www.burntfen.net/hub.php) – MSc computational linguistics student at the University of Saarland, [@richlitt](http://twitter.com/#%21/richlitt)

**Special thanks to**  
 Neil Ashton - [@nmashton](http://twitter.com/#%21/nmashton)
