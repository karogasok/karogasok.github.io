---
title: "Prismatic"
slug: "prismatic"
date: 2012-12-13T12:47:00.001Z
publishDate: 2012-12-13T12:47:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/12/prismatic.html"
regi_cimkek:
  - "nlp"
regi_cimkek_mind:
  - "Prismatic"
  - "ml"
  - "nlp"
  - "termékfejlesztés"
  - "topik modell"
---

**A [Prismatic](http://getprismatic.com/) tkp. remek példa több dologra is. Mi a keresés jövője? Van valami igazán izgalmas felhasználása az NLP-nek és az ML-nek? Lehet egy terméket teljesen egy funkcionális nyelvre alapozni? A perszonalizációval együtt járó filter bubble jelensége ellen tehetünk valamit?**

A Prismatic első ránézésre egy a sok hírolvasó eszköz közül ami a közösségi oldalon megjelenő híreket aggragálja. De nem egészen erről van szó! A Prismatic saját magát "discovery engine"-nek hívja és a hírek tálalását csak az első lépésnek tartja. A közösségi médiában megjelenő tartalmakat tkp. arra használják, hogy kitalálják a felhasználó ízlését és azt hogy milyen filtert épít maga köré. Sajnos arról nem lehet sokat megtudni miképp is működik ez az újdonságot behozó elem, de aki már eltöltött pár órát a Prismatic-en, az tapasztalatból tudja hogy egész jól működik.

A [cég blogja](http://blog.getprismatic.com/) is mutatja, mennyire átgondoltan halad a termékfejlesztés. Tulajdonképpen talán a Prismatic az egyetlen cél, ahol holisztikusan koncentrálnak egy adott problémára. Nagyon erős vizióval rendelkeznek arról [hogyan is kell az ML és az NLP eredményeit felhasználni egy termékben](http://strata.oreilly.com/2012/04/great-machine-learning-products.html) és arról [hogyan is néz ki az alkalmazott kutatás](http://cacm.acm.org/blogs/blog-cacm/157645-a-funny-thing-happened-on-the-way-to-academia/fulltext). Az alapoktól egészen a mutatós svájci designt idéző webes megjelenésig átgondoltak mindent ([itt](http://blog.getprismatic.com/blog/2012/4/23/digital-modernism-done-right.html) és [itt](http://blog.getprismatic.com/blog/2012/4/18/content-focused-design-type-edition.html) érdemes erről olvasni). Érdemes megnézni TC Founder Stories alapítóval készített interjúját.

[YouTube](http://www.youtube.com/v/wGtnMD2ZmEo&fs=1&source=uds)

Ma a legtöbb kereső rendszer az ún term-document matrix megoldáson alapul. A Prismatic az ún [topik modellekre](http://en.wikipedia.org/wiki/Topic_model) szavaz ellenben ([bővebben erről itt](http://blog.getprismatic.com/blog/2012/4/17/clustering-related-stories.html)). Ezek nagyon hasonlóak a címkéző, vagy tagelő megoldásokhoz, de sokkal pontosabban működnek és írják le egy-egy dokumentum látens szemantikáját. A topik modellek a keresésben - több technikai probléma megoldásán túl - lehetővé teszik hogy "csoportosítsák" a találatokat és egyfajta összefoglalót adjanak tartalmukról. Így kerülhető el a duplikációk és a hasonló hírek szűrése, ill. kereshetők hasonló tartalmak. Habár a topik modellek már egy évtizede megjelentek, a Prismatic egyike az első ipari alkalmazóknak.

A "filozófia" mellett természetesen a fejlesztésben is jólátgondolt elveik vannak. Elsőre talán furcsa, hogy a Clojure-t választották, de [ez még érthető is](http://szamitogepesnyelveszet.blogspot.hu/2012/12/mire-jo-funkcionalis-programozas.html) (plána, nekem, aki szeretem a Clojure nyelvet). Ami sokkal meglepőbb hogy nem igazán használnak Java cuccokat, inkább maguk írnak meg mindent amire szükségük van. Clojure körökben idézetté vált az "avoid large, monolithic frameworks" mottó (de persze inkább keresünk egy wrapper-t, vagy írunk magunk, semhogy a Prismatic-et követve saját numerikus könyvtárat dobjunk össze :D), ami az abstraction principle-re utal. Ezt az architektúrára is átvitték, a technikai részletek iránt érdeklődőknek ajánlom [a High Scalability-n megjelent részletes írás](http://highscalability.com/blog/2012/7/30/prismatic-architecture-using-machine-learning-on-social-netw.html)t erről.

[Úgy tűnik, működőképes](http://techcrunch.com/2012/12/05/prismatic/) ez a szigorúan termékközpontú fejlesztés. Jó lenne látni több kezdeményezést, ami ennyire fókuszáltan és tudatosan vezet be a piacra egy alapvetően elméleti megoldást.
