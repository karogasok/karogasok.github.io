---
title: "On NLTK and Python - an interview with Jacob Perkins"
date: 2011-04-26T08:04:00.004Z
publishDate: 2011-04-26T08:04:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/on-nltk-and-python-interviwe-with-jacob.html"
regi_cimkek:
  - "computational linguistics"
  - "natural language processing"
  - "nltk"
  - "python"
regi_cimkek_mind:
  - "computational linguistics"
  - "erlang"
  - "functional programming"
  - "natural language processing"
  - "nltk"
  - "python"
---

**Getting into natural language processing has never been easier these days thanks to the popular [natural language toolkit](http://www.nltk.org/) (nltk). Python, nltk and even the book that teaches you nlp are free! Although nltk was designed by its creators with pedagogical considerations, Jacob Perkins ([@japerk](http://twitter.com/#%21/japerk)) showed with his nltk demos that it can serve as a serious API. His blog [http://streamhacker.com](http://streamhacker.com/) has become a standard source of tips and hacks for nltk users, and his ["Python Text Procesing with NLTK 2.0 Cookbook"](https://www.packtpub.com/python-text-processing-nltk-20-cookbook/book) is the natural choice for everyone who wants to be a pro nlp guy.**

**Számítógépes nyelvészet: Please tell us something about yourself.**

**Jacob Perkins:**  I've been hacking on open source software for over a decade now, ever since I decided to install Linux instead of paying for Windows (back in the early 2.0 kernel days). I attended Washington University in St Louis, where I received both a BS and MS in CS, and also worked on [Seahorse](http://projects.gnome.org/seahorse/), which has since become the default Encryption Key Manager for the GNOME Desktop. I didn't actually study NLP at university, though I did study parsing, robotics, and took one class in Linguistics. I actually got into NLP while working on Weotta, but my CS background has turned out to be very helpful. Parsing is of course an essential component of NLP, but it was in mobile robotics that I really understood the importance of statistical machine learning, because you have to combine data from multiple unreliable sensors to get a clear picture of the surrounding environment. Since graduating, I've been trying to make it as an entrepreneur/consultant.

**The industry seems to be conservative and it is using more traditional technologies (which often means Java based tools like the GATE framework, WEKA, OpenNLP, and etc.)  Although more and more developers are using nltk, it is widely know that it was designed for teaching   natural language processing and one can think it is not suitable for ‘real-world’ tasks. Your NLTK Demos project is a good refutation of this view, isn it? Do you think that this situation can change? How are your user using it?**

As long as big companies continue to standardize on Java, I don't see the situation changing much. But it seems like Python is slowly but surely making its way into more and more companies, as more developers realize its benefits. I personally love Python for its simplicity, clarity, "Guido's Time Machine", and its numerous useful 3rd party libraries, of which NLTK is just one. And if you don't know Python, NLTK is a great reason to learn it.

I'm hoping my demos at [http://text-processing.com/demo/](http://text-processing.com/demo/) will help convince people of NLTK's usefulness, by showing off what it's capable of. I think there's been a few developers already that have been convinced by the demos to give NLTK a try. And the API has been getting well over 2000 calls/day lately, and I've been approached about using it for commercial purposes, so there's definitely a need for NLP, no matter what programming language you're using. There's so much text being created these days, that people are looking for anything that will help them organize, aggregate, summarize, etc.

But I think the real problem isn't Java vs Python/NLTK - it's that most developers want to treat NLP as a magic black box, and don't want to learn how it's actually done. I think this explains the popularity of the desktop NLP programs, since they make it easier to do NLP without a deeper understanding. And I understand this motivation, because that was me a few years ago. But if you're going to use NLP as part of your core data processing, you need to take the time to dive in and understand what's going on, how it works, and how to use NLP effectively on your own data. I think the future of NLP is not generic tools & APIs, it'll be training internal models on custom data sets, as that's the best way to get high accuracy results.

**Your [streamhacker.com](http://streamhacker.com/) blog is very popular among nltk users and Python Text Processing with nltk is very similar to your posts. But how was your terrific book born from your posts?**

I wrote a short backstory to the book at [http://streamhacker.com/2010/11/15/beginning-python-text-processing-nltk-cookbook/](http://streamhacker.com/2010/11/15/beginning-python-text-processing-nltk-cookbook/). Basically, Packt sent an email to my local python interest group, I replied with links to a few posts, they asked for a list of ~100 recipes, I provided that, and it went from there. I'd never thought about writing a book before then, but the relative success of [streamhacker.com](http://streamhacker.com/) helped convince me that it was possible. I honestly never expected articles on a niche programming topic like natural language processing to get so much attention. But it means people are interested in NLP, and my articles are useful, so I'm glad to be helping developers get up to speed faster. My most popular articles have been about experiments I performed to determine the most effective methods, and I did these experiments because I couldn't find the specific performance data I was looking for. I tried to keep this same sense of discovery in the cookbook, where many of the recipes built on previous results.

**Your blog also deals with [Erlang](http://www.erlang.org/), and your company’s blog mentions it too. Why are you dealing with a functional language? Why are functional languages becoming popular in natural language processing?**

I got into Erlang originally to write a custom search engine, which I hooked to NLTK using erlport, but the search engine  has since been scrapped in favor of the "plan generator" I explain below. Lately I've been programming mostly in Python, with some javascript where necessary, and I sometimes miss Erlang. Functional programming provides a very useful model, and I believe every programmer should learn a functional language, because it will change the way you write code, for the better. The easiest functions to test & reuse are the ones that are clear, concise, and side-effect free, which is the functional programming ideal. Erlang also provides a great runtime environment that makes parallel & distributed programming very easy, and I often find myself wishing I could use the plists module in my python code.

All that being said, I'm not sure how well functional programming maps to natural language processing. Much of NLP these days involves training, which means constructing some kind of storable & reusable model. That kind of internal state handling lends itself very well to object oriented programming, which is used throughout NLTK. I think FP is more suited to *using* NLP, not *doing* NLP. Once you have your trained model, then you can use a functional programming style to transform your input text into output structures.

**What are you working on at [Weotta](http://weotta.com/)? For what kind of problems are you using your nlp power there?**

At Weotta, we've created a "plan generator" that produces itineraries of things to do in a city, such as "Dinner, Drinks & a Show". It's a kind of multi search engine with both online & offline pieces. The online parts are powered by a custom rule based system, [MongoDB](http://www.mongodb.org/) & [Redis](http://redis.io/), and some [sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis) (using text classification) to ensure quality. But it's the offline code where the real NLP happens, primarily using keyword & text classification. We classify every place & show in our system with various metrics in order to determine what it's appropriate for, and what other kinds of places/shows it can be paired with. Nearly all of our text comes from descriptions and reviews we've scraped off the web, so we also have to do a lot cleaning, parsing, and general data scrubbing to normalize the text. In a sense, we're using NLP for quality control, to ensure we produce good results by eliminating all the bad ones. There's no such thing as PageRank when it comes to local data, and sometimes all you have to go on are a few keywords. When that's the case, you need to pull out your natural language toolkit and get to work :)
