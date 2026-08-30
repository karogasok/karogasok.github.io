---
title: "The life of a computational linguist I - Interview with Jason Adams"
date: 2010-09-23T12:05:00.003Z
publishDate: 2010-09-23T12:05:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/09/life-of-computational-linguist-i.html"
regi_cimkek:
  - "nyelvtechnológia"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "twitter"
  - "valószínűségszámítás"
regi_cimkek_mind:
  - "nyelvtechnológia"
  - "nyelvtechnológiai ipar"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "twitter"
  - "valószínűségszámítás"
---

**This week we conducted an interview with Jason Adams, a computational linguist who is working on sentiment analysis at [Systino](http://bit.ly/bBtXla). He holds a BS degree in Computer Science from the University of South Carolina, and an MS in Language Technologies from the Carnegie Mellon University. You can find Jason on Twitter as [@ealdent](http://bit.ly/bWFPXS). He's got a blog, [The Mendicant Bug](http://bit.ly/aryrRH), where you can read about nlp, ruby and other stuffs.**

**Szamítógépes nyelvészet: Please tell us something about yourself.**

Jason Adams: I've been married for 10 years to the love of my life.  We have two dogs we treat like children.  I love the outdoors and work in my yard when the Atlanta heat doesn't keep me inside.

**Sz.ny.: As a computational linguist, what do you think about the field; is it a branch of linguistics, a sub-discipline of computer science or is it a science on its own?**

J. A.: I think it depends on who you're talking to.  There are those who focus more on the linguistics and those who seem to ignore it completely.  I can see it belonging to both fields, and I can even see it being classified as a sub-field of cognitive science.

**Sz.ny.: What's your favourite linguistics theory and why?**

J.A.: The [Sapir-Whorf hypothesis](http://bit.ly/aFHUv4) is what got me interested in linguistics to begin with.  Based on the evidence I've seen and papers I've read, I tend to fall on the side of believing the theory is hogwash, but it has a certain romantic appeal that makes it interesting.

**Sz.ny. Do you have a favourite programming language and/or technology? Why do you prefer them?**

J.A.:Ruby is currently my favorite programming language, though the lack of an excellent NLP library like NLTK makes Python a very close second.  I like Ruby because of all the languages I have encountered, it is the easiest to write readable code that makes sense months later when I return to it.

**Sz.ny.: In your opinion, what should a computational linguist's toolbox contain?**

J.A.: Knowledge of [Bayesian statistics](http://bit.ly/dqKNIS) is really the key.  I don't think there is any one technology that you must be familiar with, but if your statistics skills are lacking, you will always be playing catch-up.

**Sz.ny: What are you doing in your job? How is it related to computational linguistics?**

J.A.: The company I work for does customer retention and loyalty software for enterprise and franchise companies.  We obtain lots of free-form survey responses for many different verticals.

I created the voice of the customer system that extracts topics from the free-form survey responses and performs sentiment analysis on them.  The results are visualized for the customers in a way that is well received by people with no text-mining (or even math) backgrounds.  There are many different components that go into such a system.  When random people are filling out surveys, they often neglect spelling and so often key words that identify features are missed simply because of typos.  Automatically correcting the spelling was one area where my background really came in handy.  There are lots of fun things you can do to guess the word someone intended.

**Sz.ny.: You have a really interesting Twitter related site, [TunkRank.com](http://bit.ly/bAz6M8), can you describe the ideas behind it?**

J.A.: I implemented the TunkRank algorithm that [Daniel Tunkelang](http://bit.ly/bRdore) came up with.  It's a recursive algorithm that measures individual influence on Twitter by summing the amount of attention that your followers can give you weighted by the probability of retweeting (propagated throughout the social graph).  So essentially you have a measure that puts a score on the potential impact of your tweets.  I have many future plans with it, including topic-based influence, which I've been working on for a while.  The disadvantage of doing this in my spare time is progress can be slow.  But I'm getting there.

**Sz.ny: What do you think, what are the 'hot topics' in computational linguistics that worths studying for the youngsters and will be used in the systems of the near future?**

J.A.: [Sentiment analysis](http://bit.ly/9wrvGs) is definitely a hot topic in industry right now.  I see it being a mainstay for the years to come, but I don't think it's the most interesting thing going.  People are going to be interested in identifying intentions.  Being able to predict the outcomes of business decisions based on social media is in high demand and I think we've only scratched the surface.
