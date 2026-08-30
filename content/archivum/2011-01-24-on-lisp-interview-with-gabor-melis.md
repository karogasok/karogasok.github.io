---
title: "On Lisp - Interview with Gábor Melis"
date: 2011-01-24T12:40:00.004Z
publishDate: 2011-01-24T12:40:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/01/on-lisp-interview-with-gabor-melis.html"
regi_cimkek:
  - "interview"
  - "lisp"
regi_cimkek_mind:
  - "interview"
  - "lisp"
---

**These days we see the renaissance of Lisp. New titles has been (and will be) published. Recently a Hungarian Lisp programmer, Gábor Melis, won the [Google AI contest](http://bit.ly/dHeKLk). He was so kind and gave us an interview. Gábor is a graduate of the [Eötvös Lóránd University](http://bit.ly/hi4lga) with an MSc in Software Architect - Mathematics, and now he is working for [Franz Inc.](http://www.franz.com/) - the vendor of Allegro Common Lisp, a proprietary Common Lisp implementation and AllgegroGraph RDF store. He likes programming contests - and we hope he'll win even more of them. You can read his blog at [http://quotenil.com/](http://quotenil.com/)**  
  
  
  
  
**Számítógépes nyelvészet: Please tell us something about yourself.**  
  
 Gábor Melis: I'm a big fan of mind games: from classical board games like chess and go, through modern board games, to turn based strategy games. I fully meet the laziness criteria for being a good programmer, have a bad memory which, they say, helps writing regular, readable code. AI (or  
 machine learning, stats, data mining, if you prefer) has always been particularly close to me partly due to the coolness and the challenge, partly because of the connection to games.  
  
**As we mentioned, you are a Lisp programmer. When did you meet Lisp  and why did you pick it up?**  
  
 Getting bored with the enterprise stuff, languages, architecture. Thinking that generating code from a toy like UML is sick. Finding myself fighting Java's straightjacket way too often. Many little things came together. I made a habit of learning something new every once in a while, and often it was a language. Languages to learn still on my todo list are, in no particular order: Factor, Haskell, Erlang and Clojure.  
  
**It is a common misconception that Lisp is only for AI and it's also common among Lispers to come up with an argument against this view. Which is yours?**  
  
 The kind of AI that got stuck onto Lisp as chewing gum sticks to your shoes is the one from 25 years ago: think expert systems with lots of symbolic rules and you won't be too far off. It's convenient to write these systems in Lisp just as evolutionary programming is a natural fit. But the conveniences are superficial and other languages can be used almost as effectively.  
  
 In this day and age, I feel there are two main features that really put Lisp apart: being building material for constructing languages (think lightweight domain specific languages) and having an interactive environment that shortens the feedback time during development considerably which is absolutely top priority for someone aiming for efficiency.  
  
 Being fast, having a very powerful object system (CLOS) and the best exception handling support in business doesn't hurt either. It's an all around powerful language that lets you shoot your leg off if you insist.  
  
**Which implementations are you using right now and why?**  
  
 ACL ([http://franz.com](http://franz.com/)) and SBCL ([http://sbcl.org](http://sbcl.org/)). Common Lisp has quite a few implementations and these two are quality ones in the commercial and free software world respectively.  
  
**You are a Consultant at Franz Inc. What does your job involve there?**  
  
 I'm working on the SMP port of ACL. Threads, races, all kinds of nasties. Used to do much the same on SBCL. Coming from high-level programming, it's at the extreme low end for me that's - curiously enough - quite fun.  
  
**What would you advise for beginners: why they should learn Lisp and where can they start?**  
  
 Don't do it. There is a very real danger of getting spoiled by it after which it is rather difficult to enjoy one's day job. For a traditional, multiparadigm Lisp I suggest learning Common Lisp, but for a more opionated approach look into Clojure that runs on the JVM.  
  
 Peter Seibel's [Practical Common Lisp](http://bit.ly/g2R1BB) is the canonical introduction these days.
