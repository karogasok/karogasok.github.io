---
title: "Road-map – or n+1 steps to enlightenment (or loonybind)"
slug: "road-map-or-n1-steps-to-enlightenment"
date: 2011-11-28T18:15:00.002Z
publishDate: 2011-11-28T18:15:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/11/road-map-or-n1-steps-to-enlightenment.html"
regi_cimkek:
  - "Clojure"
  - "Clojurelx"
regi_cimkek_mind:
  - "Clojure"
  - "Clojurelx"
  - "road-map"
---

*This post has been cross posted on [Clojurelx](http://clojurelx.blogspot.com/)*

**As we expressed in our previous post, we'd like to experiment with Clojure. Let us emphasis again, we are NOT developing a new library, we just believe that using Clojure in linguistic computing might be fruitful. In order to prove this assumption (or refute it), we are going to try some tools out, and summarize and share our experiences as blog posts. Here is our tentative road-map.**

**Topics**

We don't want to cover everything since we are neither omniscient, nor experienced Clojure hackers – so take our words with a grain of salt. We've chosen a few “core” topics interesting to us. Naturally, the topics are divided into two categories; “classics” and “using Java power tools”. Please leave a comment; we'd appreciate your thoughts (even your critique!).

**Classics**

Algorithms for Computational Linguistics – we stole the title from the [great (and open) book](http://www.coli.uni-saarland.de/projects/milca/courses/coal/html/) by Striegnitz, Blackburn, Erk, Walter, Burchardt and Tsovaltz. We'd like to approach finite state techniques from two perspectives: logical and functional.

Zipf's law – the well-known distribution – is the guinea pig of linguistic statistics. Inspired by the [ZipfR](http://zipfr.r-forge.r-project.org/) package and [Incanter](http://incanter.org/), we examine some very basic stats about texts, like word length and frequency and we try out plotting our results.

**Java power tools**

[OpenNLP](http://incubator.apache.org/opennlp/) and the [Stanford parser](http://nlp.stanford.edu/software/lex-parser.shtml) are real power tools. Tagging, chunking and parsing are indispensable when we are working with data.

Latent semantics – using [chisel](https://github.com/davidandrzej/chisel) to do LDA analysis with the [MALLET](http://mallet.cs.umass.edu/) package.
