---
title: "Probabilisztikus programozás"
date: 2013-03-29T10:05:00.001Z
publishDate: 2013-03-29T10:05:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/03/probabilisztikus-programozas.html"
regi_cimkek:
  - "R"
  - "funkcionális programozás"
  - "gépi tanulás"
  - "haskell"
regi_cimkek_mind:
  - "Church"
  - "R"
  - "funkcionális programozás"
  - "gépi tanulás"
  - "haskell"
  - "probabilisztikus programozás"
  - "scheme"
---

**Az utóbbi napokban a Twitter a [DARPA Probabilistic Programming for Advanced Machine Learning (PPAML) Proposers' Day](http://www.solers.com/BAAinfo-reg/ppaml/)-től hangos. De miért? Rob Zinkov Why [Probabilistic Programming Matters](http://zinkov.com/posts/2012-06-27-why-prob-programming-matters/) posztjában így válaszolja meg a kérdést**

[Probabilistic programming](http://probabilistic-programming.org/) is a newer way of posing machine learning problems. As the models we want to create become more complex it will be necessary to embrace more generic tools for capturing dependencies. I wish to argue that probabilistic programming languages should be the dominant way we perform this modeling, and will demonstrate it by showing the variety of problems that can be trivially modeled with such a language.

Probabilistic programming also has the potential to give machine learning to the masses by making it very easy to specify realistic models for frequently heterogenous data. Too often, simple models are used because they are popular and implementations are freely available. By shifting focus to a language we remove these artificial constraints.

- Aki bele szeretne csapni a lecsóba, annak a [Church](http://projects.csail.mit.edu/church/wiki/Church) nyelvet ajánlom (ami a Scheme család tagja). A [Probabilistic Models of Cognition](http://projects.csail.mit.edu/church/wiki/Probabilistic_Models_of_Cognition) tutorial a mesterséges intelligencia és a kognitív tudomány területéről vett példákon keresztül vezeti be az érdeklődőket a probabilisztikus programozásba.

- Az R nyelv avatott ismerőinek ajánlom [John Myles White posztját](http://www.johnmyleswhite.com/notebook/2010/08/20/using-jags-in-r-with-the-rjags-package/).

- Haskeller-ek a[ haskell.org-on mindent megtalálnak az elinduláshoz](http://www.haskell.org/haskellwiki/Probabilistic_Functional_Programming).

- Erwig és Kollmansberger Functional Pearls-e, a [Probabilistic Functional Programming](http://web.engr.oregonstate.edu/~erwig/papers/PFP_JFP06.pdf), nagyon ötletes példákon keresztül illusztrája a témát és megvilágítja miért természetes választás egy funkcionális nyelv a probabilisztikus programozásra. Haskellerek előnyben!
