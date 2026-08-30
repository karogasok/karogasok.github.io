---
title: "Incanter, a statistical environment for Clojure - Interview with its creator David Edgar Liebke"
date: 2010-11-24T07:53:00.002Z
publishDate: 2010-11-24T07:53:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/11/incanter-statistical-environment-for.html"
regi_cimkek:
  - "Clojure"
  - "interview"
regi_cimkek_mind:
  - "Clojure"
  - "Incanter"
  - "interview"
  - "statistical programming"
---

This week we interviewd David Edgar Liebke the creator of [Incanter](http://incanter.org/) (a statistical and graphics environment for the JVM). David is a developer and statistician working for [Clojure/core](http://clojure.com/) at [Relevance Inc](http://thinkrelevance.com/). He has a B.S. in cognitive science (UC San Diego), M.S. in applied mathematics and statistics (Georgetown), an M.B.A. (UC Irvine). He's got a nice blog, [Data Sorcery with Clojure](http://data-sorcery.org/), and you can find him on Twitter as [@liebke](http://twitter.com/#%21/liebke).  
  
  
  
  
  
 Számítógépes nyelvészet: Why did you choose [Clojure](http://clojure.org/), a modern Lisp implementation? Lisp has often been thought as the tool for symbolic computation as described in McCarthy's seminal papers ([Recursive Functions of Symbolic Expressions and their Computation by Machine (Part I)](http://www-formal.stanford.edu/jmc/recursive.html), [ A Basis for a Mathematical Theory of Computation](http://www-formal.stanford.edu/jmc/basis.html), [ Towards a Mathematical Science of Computation](http://www-formal.stanford.edu/jmc/towards.html), [Recursive Functions of Symbolic Expressions and their Computation by Machine (Part I)](http://www-formal.stanford.edu/jmc/recursive.html) or in Graham's [The Roots of Lisp](http://www.paulgraham.com/rootsoflisp.html). The Bible of Lisp and Prolog programmers, [Norvig's PAIP](http://norvig.com/paip.html), has no chapter on probabilistic/statistical reasoning. In addition people tend to forget that [R](http://www.r-project.org/) as inspired by [Scheme](http://en.wikipedia.org/wiki/Scheme_%28programming_language%29), belongs to the language family.  
  
 David Edgar Liebke: Yes, the lisp family of languages have historically been thought primarily as a tool for symbolic, rather than numeric, computation. I had in fact spent a lot of time programming traditional AI systems in lisp as an undergraduate and again, years later, when I was learning how to program automated theorem provers. But lisps are extraordinarily good general-purpose programming languages, and their functional approach combined with their interactive development-style, due to their dynamic type system and [REPL](http://en.wikipedia.org/wiki/Read-eval-print_loop), suit the typical data analysis work flow, which involves a great deal of non-numerical work, transforming raw data into something that can stuffed in a matrix. I think this is why both R and [Lisp-Stat](http://www.stat.uiowa.edu/%7Eluke/xls/xlsinfo/xlsinfo.html) have their roots in lisp. Lisp-Stat was, as is obvious by its name, implemented in a lisp, but more surprisingly R is also built on a lisp-like engine written in C.  
  
 Clojure combines the power of lisp with the enormous selection of libraries found in the [Java](http://en.wikipedia.org/wiki/Java_%28programming_language%29)/[JVM](http://en.wikipedia.org/wiki/Java_Virtual_Machine) ecosystem, including the libraries that I built Incanter on, such as the [Colt](http://acs.lbl.gov/software/colt/) numeric library from [CERN](http://public.web.cern.ch/public/) and [Parallel Colt](http://sites.google.com/site/piotrwendykier/software/parallelcolt), an extension that provides multiprocessor support, the [JFreeChart](http://www.jfree.org/jfreechart/) charting library, the [Processing](http://www.processing.org/) visualization library, LaTeX and PDF rendering libraries, [MongoDB](http://www.mongodb.org/) libraries, MS Excel file parsers, and on and on.  
  
 In addition to the large ecosystem, Clojure has a powerful set of concurrency primitives and a growing set of parallel computation functionality that greatly reduce the pain associated with writing programs that can exploit multi-core architectures.  
  
How seamless is the integration of those tools?  
  
 Remarkably seamless, this turns out to be one of Clojure's killer features, the ability to provide concise, dynamic access to existing Java libraries.  
  
 As a reason for creating Incanter, you cite two papers. [Back to the Future](http://www.stat.auckland.ac.nz/%7Eihaka/downloads/Compstat-2008.pdf), which is deals with the problems of scalability and R, and [Lisp-Stat issue](http://www.jstatsoft.org/v13) of the [Journal of Statistical Software](http://www.jstatsoft.org/) that is summarizing the lessons learned from the Lisp-Stat project. Why do these things matter? Why should we take care of scalability?  
  
 Scalability matters because the diversity and volume of data available to analyze is growing at a phenomenal pace. The ability to either pull in data from divergent data sources, or embed your computation in the systems where this data lives will become increasingly important, and Clojure is an excellent fit for either approach.  
  
Linguistics is facing to a paradigmatic change as it is becoming more and more data-intensive. Bender and Good in their white paper, [A Grand Challenge for Linguistics: Scaling Up and Integrating Models](http://faculty.washington.edu/ebender/papers/GrandChallenge.pdf), argue that we should considerably scale up our databases. Most of us take the advice and learned python and/or R and some sort of database (mySQL, but mapreduce implementations are also becoming popular). What can Clojure and Incanter offer to linguists? Why should we consider using it?  
  
 I think learning either [Python](http://www.python.org/) or R is worthwhile; R has become the lingua franca of statistical computing and Python's [Numpy](http://numpy.scipy.org/) and [Scipy](http://www.scipy.org/) libraries are very powerful. Language choice is frequently a function of library availability, so if what you need to do depends on functionality supported in either R or NumPy/SciPy, then those are the obvious choices.  
  
 But I think Clojure is a better general purpose language than R and a better language for multi-core programming than Python; and it has access to a broader set of data sources than either through the libraries available within the JVM ecosystem.  
  
 And Clojure's analytics story is broader than Incanter, other examples include the Infer machine-learning library  
 ([https://github.com/bradford/infer](https://github.com/bradford/infer)), the clojure-openlp library ([https://github.com/dakrone/clojure-opennlp](https://github.com/dakrone/clojure-opennlp)), and the Cascalog library ([https://github.com/nathanmarz/cascalog](https://github.com/nathanmarz/cascalog)) which provides the ability to perform [Datalog](http://en.wikipedia.org/wiki/Datalog)-style queries of data stored within [Hadoop](http://hadoop.apache.org/).  
  
Do you have any feedback about what Incanter is used for?  
  
 I've heard examples of it being used in both stand alone mode to perform exploratory data analysis and chart generation and as an embedded library within a larger system to perform custom calculations and generate data visualizations.  
  
 Clojure has been used more generally for analytics type work in several companies including Flightcaster ([http://flightcaster.com/](http://flightcaster.com/)), Runa ([http://runa.com/](http://runa.com/)), Sonian ([http://www.sonian.com/](http://www.sonian.com/)), Akamai ([http://www.akamai.com/](http://www.akamai.com/)), and at least a couple companies in the financial industry.  
  
What are the next milestones in the development?  
  
 I would like to include functionality that exploits the work I’m doing on parallel ([http://data-sorcery.org/2010/10/23/clojureconj](http://data-sorcery.org/2010/10/23/clojureconj)) and distributed computing in Clojure.
