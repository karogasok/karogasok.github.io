---
title: "Word Cram - an interview with its creator Dan Bernier"
slug: "word-cram-interview-with-its-creator"
date: 2010-11-10T10:53:00.002Z
publishDate: 2010-11-10T10:53:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/11/word-cram-interview-with-its-creator.html"
regi_cimkek:
  - "interview"
regi_cimkek_mind:
  - "interview"
  - "text visualization"
  - "wordcram"
---

**This week we interviewed Dan Bernier, the creator of [WordCram](http://bit.ly/bRq2ZR). Dan runs a nice blog, the [Invisible Blocks](http://bit.ly/8YLsOC), and you can find him on twitter as [@danbernier](http://bit.ly/9S4j21), if you want to get info on WordCram, follow [@wordcram](http://bit.ly/bpasqE).**  
  
  
  
  
  
**Számítógépes nyelvészet: Why did you start the project?**  
  
 Dan Bernier: I started working on what became WordCram after seeing Algirdas Rascius' ["Scattered Letters"](http://bit.ly/bqWAcC) on [http://openprocessing.org](http://bit.ly/9FbVVk), a beautiful little sketch that randomly places captial letters without overlapping them. If you haven't seen it, you should check it out - it's regularly the most "favorited" sketch on the site. I'd seen [http://wordle.net](http://bit.ly/cIZBN2) a few years before, and thought I'd use Algirdas' approach for detecting overlapping letters to generate my own Wordles. I was able to get some pretty good results, but the code was slow, so it never seemed worth sharing with anyone.  
  
 Then I bought [O'Reilly's Beautiful Visualization](http://oreil.ly/avP8JA). I chose it over its sibling book, [Beautiful Data](http://oreil.ly/clrUqs), almost entirely because it had a chapter on Wordle (You can read Jonathan's [chapter as a PDF](http://bit.ly/cdjnGb)), by Wordle's creator, Jonathan Feinberg. In it, he explained some of the tricks he used to make Wordle so fast - mostly hierarchical bounding boxes. I thought, if these tricks could speed up *my* code enough, I'd release it as a Processing library. WordCram is still a bit slower than Wordle, but I got it far enough along back in late August that I decided to release it.  
  
**What kind of design goals do you have in your mind?**  
  
 I want WordCram to be easy to use, but flexible enough to create any kind of word cloud, so it's designed as a configurable engine: you plug components together to control text parsing, how words are counted, how they're colored, how big they should be, where they should be placed, and it comes with a bunch of pre-built components that seem useful to me. But on top of that is a thin layer that simplifies the construction, and provides sensible defaults.  
  
 Many Processing users are new to programming, so I want WordCram's API to be simple and clear, without unnecessary abstractions. I'm trying to keep my method names clear, and to follow conventions, so a WordCram user has less to learn and remember. And Processing's design is very consistent, very smooth - you can tell they're designers, it's well thought-out - so I want WordCram's API to stand up well next to Processing's.  
  
 I want it to be fast enough, about as fast as Wordle. It's not there yet. But most WordCram users I talk to are using it off-line, and don't mind waiting.  
  
**What's inspired your project?**  
  
 Processing, Wordle, and Algirdas Rascius' "Scattered Letters".  
  
 Wordle is a lot of fun to play with. I think people are often a little bit surprised by what it shows them about their text, and that's a great thing for a visualization to do, provide that mix of recognition and surprise.  
  
 "Scattered Letters" achieves a great effect with a really simple technique. Though WordCram no longer detects overlaps the same way "Scattered Letters" does, I never would've started WordCram had I not seen it, and how it works.  
 Processing is probably my favorite piece of software. It's kept the fun in programming for me, even when the day-job gets dull or frustrating.  
  
**What kind of applications use wordcram?**  
  
 People mainly use it as an open, programmable Wordle: they want to use Wordle in a project, but they can't automate it easily; and Wordle is copyrighted, so they can't legally use the images.  
  
[http://the-digital-reader.com](http://bit.ly/cEs9v2) is using WordCram to generate covers for e-books (see [here](http://bit.ly/aqoPJc)), which is pretty cool. And the [Texas Tribune](http://bit.ly/9eJOOv) wanted to build an app where you could make a word cloud from a candidate's ads, or even compare the word clouds for two candidates' ads, showing each candidate's words in a different color. That never worked out, though, which is too bad.  
  
**How far the present state of wordcram from your goals?**  
  
 There's a ways to go. For the 1.0 release, I'd like it to be very fast, with a well-baked API, and good examples and documentation. I'd like to have more built-in components -especially text sources, like a RSS reader, a Twitter stream, and a Delicious user's tags. That stuff's not too far off.  
  
 I'd like to add the ability to look up the word at a given (x,y) coordinate, which should let users hook up mouse interaction -either for clicking on words, or hovering over them. Imagine a WordCram of Senators' names, and mousing over one pops up a box with their voting record, their party and state, or whatever. Or one from a large text document, and hovering on a word shows what other words it most often appears next to.  
  
 I think the last big goal is laying the words out in an arbitrary shape, like [http://www.tagxedo.com/](http://bit.ly/c3g1tq).  
  
**What's the next milestone in the development**  
  
 The 0.3 release just came out November 7, and that was mostly about loading web pages, improving the API, and documentation. So I think the next release will probably focus more on the internals: performance improvements, more pre-built components, and maybe PDF rendering...though I really have to see whether that's feasible first. Maybe I'll add those mouse coordinates, too.
