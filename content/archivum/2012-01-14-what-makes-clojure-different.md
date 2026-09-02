---
title: "What makes Clojure different?"
slug: "what-makes-clojure-different"
date: 2012-01-14T08:00:00Z
publishDate: 2012-01-14T08:00:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/01/what-makes-clojure-different.html"
regi_cimkek:
  - "Clojure"
  - "Clojurelx"
regi_cimkek_mind:
  - "Clojure"
  - "Clojurelx"
  - "PAIP"
---

**A friend of mine asked me why Clojure matters and what makes it special and why I think it is good for linguists. This post is the edited version of my answer to my dear friend. Since there are very good books on the market (my favourite is [Clojure in Action](http://www.manning.com/rathore/)) and the internet is full of good tutorials ([4Clojure](https://www.4clojure.com/) is esp. good if you like the learning by doing method) my goal is only to give you a rough picture of functional programming.**

**An example**

We are going to solve a "toy" problem stolen from the first chapter of Peter Norvig's seminal [Paradigms of Artificial Intelligence](http://norvig.com/paip.html). The question is how do you extract first and last names from someone’s full name. Before you think this is too simple and it doesn't worth dealing with, consider names like Robert Downey Jr, Admiral Grace Hopper, and what about Staff Sergeant William "Wild Bill" Guarnere (a character for the Band of Brothers series). Machines should be programmed to solve these problems, and even humans could have problems with names. It took me years to figure out that Martin "Boban" Doktor (a well known Czech Olympic champion sprint canoer) is not a real doctor...

First, we need some data to test our assumptions.

[GitHub Gist](https://gist.github.com/1602834)

The function 'def' associates the symbol 'names' with names (oh, a vector of vectors). A first name is usually just the first word in a name.

[GitHub Gist](https://gist.github.com/1602843)

And the last name is the last word in a name.

[GitHub Gist](https://gist.github.com/1602847)

Let's test our functions. Calling first-name and last-name on my name gives the right answers.

[GitHub Gist](https://gist.github.com/1602871)

We stored out test data in names, and now it's time to test our functions en mass. The higher order function map helps us in doing so. Map takes a function as its first argument and applies it to every member of its second argument.

[GitHub Gist](https://gist.github.com/1602878)

Oooops, the program is having serious problems with "titles" or prefixes. Calling last-name on names gives interesting results too. Our program is not that bad, it captures the basic logic of identifying first and last names, but affixes cause problems. The first name should be the first word in a name if it is not a prefix. Let's store the affixes in vectors.

[GitHub Gist](https://gist.github.com/1605408)

We want to test if the first word of the full name is a member of the titles. We need a function that tests membership.

[GitHub Gist](https://gist.github.com/1605411)

The function member is recursive. First, it test if its second argument is a sequence. The second if gives us a terminating condition, if x and the first element of the second argument are equivalent, it returns the whole second argument. Otherwise it tests the membership again on the rest of the sequence (i.e. everything but the first element of the original sequence). Now, we can redefine our first name function. If the first word of the full name is in the list of prefixes, call first-name on the rest of the full name, otherwise return the first word of the full name.

[GitHub Gist](https://gist.github.com/1605415)

Testing our new function shows it works correctly.

[GitHub Gist](https://gist.github.com/1605418)

We can redefine last-name similarly.

[GitHub Gist](https://gist.github.com/1605423)

Storing names in vectors of strings is very unnatural (at least for humans, I guess machines don't care about these issues). Wouldn’t it be nicer to type names like "Zoltán Varjú" instead of ["Zoltán" "Varjú"]?

First, we need new test data, which is a vector of strings.

[GitHub Gist](https://gist.github.com/1605431)

We want to use our first-name and last-name functions. Can we split a name into individual words? clojure.string provides us a split function (that's why we put (:use [clojure.string :as str :only [split]] :reload) into ns) which splits a string into a vector of strings at a given point. The space character delimits the parts of a name. Our source code looks like this now:

[GitHub Gist](https://gist.github.com/1607641)

Now we can test split from clojure.string.

[GitHub Gist](https://gist.github.com/1607665)

Let's define a split-name function just to save ourself from repetitive strain injury caused by excessive typing.

[GitHub Gist](https://gist.github.com/1607675)

Finally, we test if our functions work on splitted names.

[GitHub Gist](https://gist.github.com/1607686)

**Notes**

I have to note, you can make the code more concise and idiomatic. I hope you can see 1) how can you solve a problem with functions and by combining them 2) you have a basic idea of what is recursion 3) how can you go from a basic problem to an acceptable solution.

**What makes Clojure different?**

Norvig lists eight features that make Lisp different:

1.  built-in support for lists

1.  automatic storage management

1.  dynamic typing

1.  first-class functions

1.  uniform syntax

1.  interactive environment

1.  extensibility

1.  history (see Paul Graham's essays, [What Made Lisp Different](http://www.paulgraham.com/diff.html) and [The Roots of Lisp](http://www.paulgraham.com/rootsoflisp.html))

Clojure is a Lisp on the JVM which makes it unique. The Java Virtual Machine makes it portable, reliable and secure, but there is a new JavaScript based version called [ClojureScript](https://github.com/clojure/clojurescript). [Slime](http://common-lisp.net/project/slime/) is an excellent development environment, leiningen makes project automation easy. Java interoperability means Clojure has got a great collection of libraries for almost everything.

However Clojure is not for complete beginners. The Clojure community is very open and supportive, but asking the right question requires some sort of maturity. As [this](http://www.reddit.com/r/Clojure/comments/n90id/about_how_much_java_do_you_use_or_need_to_know/) Reddit thread explains you shouldn't be a Java expert to pick up the language, even you can learn what you have to know on the go. But you should know at least one 'conventional' language like Python before you start learning Clojure. More propaganda in our [Why Clojure lx?](http://clojurelx.blogspot.com/2011/11/why-clojure-lx.html) post.
