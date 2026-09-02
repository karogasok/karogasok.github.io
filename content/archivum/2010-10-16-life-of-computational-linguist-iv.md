---
title: "The life of a computational linguist IV - interview with Alyona Medelyan"
slug: "life-of-computational-linguist-iv"
date: 2010-10-16T16:44:00.001Z
publishDate: 2010-10-16T16:44:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/10/life-of-computational-linguist-iv.html"
regi_cimkek:
  - "computational linguistics"
  - "interview"
regi_cimkek_mind:
  - "computational linguistics"
  - "interview"
---

**This week we interviewed [Alyona Medelyan](http://bit.ly/aE1IL5) who's a Senior Software Engineer & Researcher at the NZ enterprise search company [Pingar](http://bit.ly/cwDCzD) where she's working in the areas of semantic and faceted search, query analysis and search result representation. She's got a nice research blog, the [Topic indexing blog](http://bit.ly/cTzcDD), and you can find her on twitter as [@zelandiya](http://bit.ly/9dGwwA)**

**Számítógépes nyelvészet: Please tell us something about yourself.**

I consider myself fortunate to have chosen to study computational linguistics. Not only there are many interesting unsolved problems in this field, but I also always felt that my knowledge is in demand and that many doors are open because of that. In the past 10 years I lived in Germany, New Zealand and the US, worked for Google and several cool IT start-ups, travelled to conferences in amazing locations, and met many brilliant and inspiring people.

**Which is your favorite linguistic theory and why?**

I like the ideas behind the [prototype theory](http://bit.ly/cmy4HN) which addresses the problem of how people categorize objects. Rather than using a pre-set definition of a category, e.g."a bird is an animal that can fly", a "bird" can be represented as a set of features, e.g. "flies", "feathers", "beak", "wings". A prototype is the most typical representation of a category, which covers most of the features, e.g. "robin" is prototypical, whereas a "kiwi bird" less so. This theory makes you wonder how exactly semantics is encoded in our mind. Machine-learning based categorization operates on similar principals as the prototype theory: First, a set of features is defined, then, the algorithm derives the typical distribution of feature values (whether it's true/false or numerical), and finally, the algorithm uses that learned knowledge to predict the category for an unknown object just by looking at its features.

**Do you have a favourite programming language and/or technology? Why do you prefer it?**

The [Wikipedia dumps](http://bit.ly/cswqyc) regularly released by the Wikimedia Foundation help solve many technological challenges in natural language processing tasks. Please refer to my [blog post](http://bit.ly/agaXGp) for some ideas or to the research survey [Mining Meaning from Wikipedia](http://bit.ly/a4q70W) for a detailed overview.

**As a computational linguist, what do you think about the field; is it a branch of linguistics, a sub-discipline of computer science or is it a science on its own?**

It's an interdisciplinary field like many others, e.g. Bioinformatics, Cognitive science, AI.

**What are you doing in your job? How is it related to computational linguistics?**

I am the lead developer at a New Zealand company called [Pingar](http://bit.ly/aQDStB) operating in the enterprise search domain. I implement prototypes, which then become products and are distributed to customers. In my job, I do quite a bit of programming, but I also get to talk to potential customers and participate in all technical discussions with our partners. My goal is to incorporate the latest research ideas, so I get to research in the areas like [faceted search](http://bit.ly/baxqEK), [text summarization](http://bit.ly/d3UWe6) and [named entity recognition](http://bit.ly/bkKMJ4) -- all computational linguistics areas.

**You wrote your [PhD dissertation](http://bit.ly/9hSw0f) on 'human-competitive topic indexing', and published quite a lot on the topic along with keyphrase extraction, even collaborated with a philosopher on automatic ontology building. Can you summarize the basic idea behind your research? How can a machine based indexing beat human labor and can we trust this method?**

That's a good question. In many natural language processing tasks, evaluating algorithms is challenging, because these tasks are often subjective. People tend to disagree when asked questions like which summary is better, what's the correct translation or which search result is more relevant. In the case of topic indexing, we have the advantage of a clearly-defined task: identify vocabulary terms, which describe the main topics of this text. Plus, historically, it has been the job of professional indexers and librarians. They have came up with a method of evaluating human performance,  
 called inter-indexer consistency. When evaluating my algorithm, [Maui](http://bit.ly/bOuRZB), all I needed to do is to treat it in the same way as a human indexer, i.e. add its results to those produced by several people, and use the inter-indexer consistency to evaluate everyone in this group. If you trust this method, you can trust my results.

**In your opinion, what should a computational linguist's toolbox contain?**

I have always found unix commands for working with text extremely useful. Learn how to use (and pipe) commands like  
 grep, sed, sort, head, less, find (as well as some regular expressions basics), and here's your universal toolbox.
