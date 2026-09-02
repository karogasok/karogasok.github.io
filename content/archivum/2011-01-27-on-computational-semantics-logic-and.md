---
title: "On Computational Semantics, Logic and Linguistics - An Interview with Jan van Eijck"
slug: "on-computational-semantics-logic-and"
date: 2011-01-27T15:45:00.003Z
publishDate: 2011-01-27T15:45:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/01/on-computational-semantics-logic-and.html"
regi_cimkek:
  - "haskell"
  - "interview"
  - "logic"
regi_cimkek_mind:
  - "computational semantics"
  - "haskell"
  - "interview"
  - "logic"
  - "semantics"
---

**We interviewed [Jan van Eijck](http://bit.ly/i2GtWD) who is the co-author of [Computational Semantics with Functional Programming](http://bit.ly/gIaFrd), a recent [title from Cambridge University Press](http://bit.ly/gyxeX9). Prof. van Eijck is a senior researcher at [CWI](http://bit.ly/gPl3RA) (Centre for Mathematics and Computer Science) Amsterdam, and part time full professor of computational linguistics at [Uil-OTS](http://bit.ly/fuWpuF) (Research Institute for Language and Speech), Utrecht.**  
  
  
  
  
**Számítógépes nyelvészet: Please tell us something about yourself.**  
  
 Jan van Eijck: For info about me you can consult my website. Please have a look at  
  
[http://homepages.cwi.nl/~jve/ ](http://homepages.cwi.nl/%7Ejve/)  
  
 If there is something remarkable about my career, it must be that my interests moved in an opposite direction to what is usual. Usually people with a penchant for formal thinking fall in love with maths and science early in life, and then turn to philosophy or literature later on. With me it went the other way around. I started out as a student of cinema, literature and philosophy, but then grew dissatisfied with the difficulty of reaching agreement by means of philosophical dispute.  Then I discovered logic, and fell in love when I started to do my PhD.  My PhD Thesis is on [Montague Grammar](http://bit.ly/gPm8Gd). Still later, I discovered computer science and functional programming. As is pointed out in the CUP book, Montague Grammar and the type systems that are used in functional programming are a natural match.  
  
**Computational Semantics with Functional Programming was published by CUP in October 2010, but you and your co-author Christina Unger published the manuscript online for the public till the print version come out. Why did you choose this method?**  
  
 Yes, the draft manuscript was online for some time. That way, we were able to collect lots of error corrections. In fact, the published book has many bug fixes with respect to the online draft. Without soliciting comments we would never have been able to improve the text to the extent that we did. But, of course, if you put something on internet, you can never remove it again. So we have to accept that the draft version keeps floating around, I guess. We still hope CUP can make a profit on the book. They are a remarkable publishing house, by the way. When working with them we found them extremely supportive and knowledgeable.  They are certainly not only in the business of academic publishing for the money, as some of the others seem to be. If you want to support them, you might want to buy a paper copy of the book.  And if you want to do us a real favour you should consider writing a review of the book, for Amazon, or for some suitable academic journal.  
  
**[The Haskell Road to Logic, Maths and Programming](http://bit.ly/c9wk4p) is very popular in the community, what are the main differences between the old and the new title?**  
  
 The Haskell Road is meant as a general introduction to Logic and Mathematics through functional programming. This started out as a mission together with Kees Doets to give students of mathematics and computer science a better idea of the connections between the various topics they were supposed to master in their Bachelor programme. Kees' idea was to teach them "the language of mathematics", and I managed to convince him that the language of state-of-the-art  functional programming is very close to that language, with the additional advantage that you can use it to program computers. The new book is much more specific. This time we use Haskell to teach a branch of natural language processing: computing meanings for pieces of natural language text. Other textbooks in natural language semantics tend to use Prolog as a tool of choice. We hope our new book illustrates that Haskell is more suited to the task.  
  
**The Netherlands is the center of logic, at least on the continent, and you've got a very rich (and long) tradition of teaching logic. The [GAMUT](http://amzn.to/gP84Ph) is one of the most popular introductory logic books, but nowdays we see a "dynamic turn" in logic. The Haskell Road and Computational Semantics are putting logic into context and connect it to programming (in Haskell). You are involved in a new project, [Logic in Action](http://bit.ly/fWSR6O), which is the English version of Logica in Actie, a text book for the Dutch Open University. This new project is very different from the traditional logic curriculum, you introduce epistemic logic in the fifth chapter, and you treat dynamic logic and games and logic in the subsequent chapters. Why did you choose this way?**  
  
 The Dutch tradition in Logic started with giants like [L.E.J. Brouwer](http://bit.ly/f4VTiy), [Arend Heyting](http://bit.ly/hjOfCm), and [Evert Willem Beth](http://bit.ly/e3RGG9). Brouwer was the founder of [intuitionism](http://bit.ly/fr1I6l) in mathematics, Heyting formalized intuitionistic logic, and Beth co-invented tableau methods, and was a very influential in pushing logic as a tool for studying the foundations of mathematics, although his own interest ranged much wider (he also studied philosophy and psychology). This led to the foundation of an "[Instituut voor Grondslagenonderzoek](http://bit.ly/hrpzYo)", or "Institute for Foundational Research", aimed at studying the foundations of the formal sciences, in particular mathematics. Nowadays, the focus has shifted quite a bit. The chair of Beth is now occupied by [Johan van Benthem](http://bit.ly/90n6hk), and his Institute has given birth to ILLC, the [Institute of Logic, Language and Computation](http://bit.ly/heqlBl), with a much broader compass. And at my own institute, CWI  (Centre for Mathematics and Computer Science), logic has turned into an important source of inspiration for theoretical computer science. The Logic in Action initiative is meant to reflect the wider mission of logic today: our initiative advocates logic as a general formal study of communicative interaction and computation. That's why logic of knowledge, action logic, and logic in game theory play such a prominent part in the new textbook annex internet resource.  People who are interested should definitely visit the website:  
[http://www.logicinaction.org/](http://www.logicinaction.org/)  
 Again, we are not in this for the money. We are preachers, and we deliver our sermon for free.  
  
**Nowdays, everyone is obsessed with data. Linguistics and cognate disciplines are getting more and more statistics oriented. Why should we learn logic? Isn't it old-school? It is a common misconception about semantics that it's just an exercise in typesetting, but what does it offer to a student who has to make tough decisions during the university years and have to learn not only for fun, but preparing for the years when he/she has got to pay the bills.**  
  
 Well, there is much to say about this. First of all, logic-based reasoning and decision making on one hand and statistics-based reasoning and  
 decision making on the other are moving closer and closer these days, and I don't think students have to make a choice. For instance, in epistemic logic (the logic of knowledge), the standard way to treat uncertainty is by means of equivalence relations: if I don't know whether the situation I am in is A or B, this means that I cannot tell the A-situation and the B-situation apart. But this is just a first approximation, of course. A more realistic modelling would use a probability measure over situations: I do not know whether I am in A or in B, but I do know that the A-situation is twice as likely as the B-situation (as in the [Monty Hall puzzle](http://bit.ly/b3lyp2)).  
  
 Next, how useful is it to master abstract thinking? I sometimes get emails from very experienced programmers who tell me that that getting acquainted with Haskell has changed their outlook on their discipline, and given them new inspiration. Haskell can give you a taste for logic, and vice versa. If you like logic, you will like Haskell, and vice versa. Once you fall in love, you will find out what abstraction tastes like. It may change your life forever.  
  
 Finally, getting into abstract disciplines through programming has the virtue of making these disciplines more concrete and approachable.  It stimulates learning by doing. We have tried to make the exercises in the Haskell Road and in the Computational Semantics textbook neither too simple nor too hard. They should stimulate the reader to have a hands-on experience. In the end, the only way to develop true mastery in a topic is by doing, doing, doing. Then observe the results and adjust.  And so on, and so on. This holds for learning carpentry, for learning programming, for learning to play the clarinet. It holds for whatever you choose to do in life.
