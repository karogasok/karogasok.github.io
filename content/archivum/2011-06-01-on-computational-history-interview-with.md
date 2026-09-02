---
title: "On Computational History - an interview with William J. Turkel"
slug: "on-computational-history-interview-with"
date: 2011-06-01T04:34:00.001Z
publishDate: 2011-06-01T04:34:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/06/on-computational-history-interview-with.html"
regi_cimkek:
  - "digital humanities"
  - "interview"
regi_cimkek_mind:
  - "digital humanities"
  - "history"
  - "interview"
---

**We interviewed William J. Turkel (associate professor, University of Western Ontario) on computational history. You can learn more about William at [his home page](http://williamjturkel.net/), his discontinued [Digital History Hacks](http://digitalhistoryhacks.blogspot.com/) blog is full of interesting posts, and you can find him on Twitter as [@williamjturkel](http://twitter.com/#%21/williamjturkel).**  

**Számítógépes nyelvésze: William, please tell us something about yourself.**

**William:** I started programming as a kid, and have kept it up over the years. I worked as a programmer while putting myself through degrees in psychology, linguistics, brain & cognitive science, and history, anthropology and STS. I have a real fondness for functional programming, and am doing all of my own work in [Mathematica](http://www.wolfram.com/mathematica/) these days.

**In your post, [Towards a Computational History](http://digitalhistoryhacks.blogspot.com/2008/07/towards-computational-history.html), you say "To some extent we're all digital historians already, as it is quickly becoming impossible to imagine doing historical research without making use of e-mail, discussion lists, word processors, search engines, bibliographical databases and electronic publishing. Some day pretty soon, the "digital" in "digital history" is going to sound redundant, and we can drop it and get back to doing what we all love." Historians are the early adopters of computational methods within the traditional humanities. Why did they get interested in those tools?**

  I fear that very few historians have adopted computational methods yet. Most people who think of themselves as "digital historians" are really only focused on putting history online. Most of them still think of themselves as publishing traditional work in a new medium, perhaps with a few media files or hyperlinks thrown in, to be consumed by a person reading passively in a web browser.  

**Does digital humanities only mean a methodological change? Does have effect on other sides of the scholarly work to, i mean will it change our 'paradigm'? When "[historians] get back to doing what [they] all love" will they find a new science, or just an enhanced one?**

The real revolution follows from the fact that digital sources can serve as inputs to computational processes. So a new science is definitely possible. What is not clear to me is whether or not historians will be the developers or beneficiaries of these new techniques. When geographical records became digital, some geographers got into doing computational work with those sources (i.e., people who work in GIS), and computational geography remained a part of the discipline of geography. When biological records became digital, a lot of computer scientists, physical scientists, and applied mathematicians jumped in to create computational biology/bioinformatics. In many places, this is divorced from traditional biology departments. I suspect the latter trajectory is more likely to be the outcome when computational techniques are applied to history. I think the fact that the [Culturomics](http://www.culturomics.org/) team could not find a historian with whom to collaborate is pretty revealing.

**How do you use computational methods in your daily work?**

These days I am using Mathematica the way that some people use Emacs, as a kind of a programmable environment that I live in. Mathematica has what are called "notebooks": objects that can contain prose, executable code, simulations, data, hyperlinks, images, audio and video, and so on. When I want to do something with an online source, I import it directly into Mathematica and manipulate it algorithmically. As I work, I am building up a large collection of notebooks, but unlike the historian's traditional notebooks, these ones are live, in the sense that they draw from a changing body of sources and contain dynamic elements like tables and graphs that can be updated with the click of a button. More and more, I interact with digital resources through APIs rather than through the browser, and increasingly my work is automated. Web crawlers, for example, can provide a steady stream of sources that are processed by automated filters before I see them. I'm not trying to replace the interpretive work of the historian, just trying to offload the clerical drudgery to machines, so we can concentrate on the tasks that require human insight and care.

One of my ongoing projects involves doing text mining, machine learning and visualization of criminal trials in the [Old Bailey](http://www.oldbaileyonline.org/) with an international team of colleagues. This is a large archive: 127 million words in about 197,000 criminal trials that were held between 1674 and 1913 at London's central criminal court. At this point, my colleagues and I have a large (and growing) collection of Mathematica notebooks that are allowing us to explore the shape of this archive as a whole. It is exciting! Historians have been using records from the Old Bailey for at least the better part of a century, but until very recently, no one had the ability to get a good view of the whole thing.

I am also doing some work with fabrication, turning digital representations back into physical objects using 3D printing ([RepRap](http://reprap.org/wiki/Main_Page)), CNC machining, etc.  

**Reading about your works, I had two associations: data science and data journalism. Does the 'computational turn' mean that historians should become hackers like data scientists, or it rather means they should become power users like data journalism who adapt to a new media and possibilities? (Or another analogy: should historians learn computer science and programming like natural scientists, or should they learn to use sophisticated, task centric tools like social scientists who are using SPSS and etc. and consult with statisticians and technicians a lot?)**

I read a lot of [data science](http://radar.oreilly.com/2010/06/what-is-data-science.html) -- or more traditionally, "statistics" :) -- and a lot of data journalism, too. I think historians, and humanists more generally, have much to learn from both endeavors. For my part, I try to encourage people to take up programming, whatever their disciplinary interests. If you write the tools yourself, you have a much better understanding of how they work and you can tailor the workflow to your own research questions. Not that I believe in re-inventing the wheel. If one programs in Python, for example, it makes a lot of sense to use the Natural Language Toolkit and a data mining / machine learning package like Orange. One of the reasons that I switched to Mathematica is that there are well-developed bodies of mathematics that cover just about any technical domain of interest, and Mathematica is an excellent language for technical generalists since all of the math is already built in. If I need to do something with dynamical systems, combinatorics, image processing, or whatever, I don't have to first install a bunch of libraries and learn how they work.

One thing I really like about data / computational journalism is the emphasis on using APIs and data to create stories. Whether historians want to learn to program or not, there is a lot of data out there waiting for people to make use of it.

**Computational history presupposes historical data. Does the current state of historical data curation make possible to work (with large amount of) data? The reliability of data is always a question, can we trust historical data?**

So much historical stuff is already online, and so much is being added daily, that there are many lifetimes worth of interesting research questions just sitting there, waiting to be asked. The barriers to entry right now are really low in fact, I would say that disciplinary culture forms the main barrier. If you don't care *too* much about what other people think, you can jump right in.

One thing that historians are usually very good at is reading closely and critically, and looking for evidence from multiple sources to confirm a particular interpretation, or to call it into question. So we already have a disciplinary culture that is used to assessing the reliability of sources. A more difficult question is whether our peers are in a position to assess the reliability of our methods. I would say most of them are not, and interdisciplinary peer review is really necessary. Right across the board, not just in the humanities. We have a lot to teach scientists, too. 

**There are many ways to digital humanities and computational history, but what would you advise to the aspiring youngsters who wants to break into the field? Where a young programmer/computer scientist or a student of history could learn about the "other side"?**

Like I say, I encourage everyone to code, and that is a great place to start learning if you don't already know how. I think people coming from a programming or science background often have an interest in the history of science and technology, so that is one place to start reading. (Many of today's better-known digital historians have precisely that background). Much of my own research and teaching is in a field called "big history", which tries to situate what we think we know about the human past in the wider context of what we think we know from the historical sciences like cosmology, geology and evolutionary theory. [David Christian's Maps of Time ](http://www.amazon.com/Maps-Time-Introduction-History-California/dp/0520244761)is an exemplary introduction to the field. Programmers might also enjoy the work of Manuel De Landa, especially his new [Philosophy and Simulation](http://www.amazon.com/Philosophy-Simulation-Emergence-Synthetic-Reason/dp/1441170286/ref=sr_1_1?s=books&ie=UTF8&qid=1306866893&sr=1-1).
