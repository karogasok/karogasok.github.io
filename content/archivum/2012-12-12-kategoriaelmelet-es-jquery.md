---
title: "Kategóriaelmélet és jQuery"
date: 2012-12-12T09:14:00.001Z
publishDate: 2012-12-12T09:14:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/12/kategoriaelmelet-es-jquery.html"
regi_cimkek:
  - "kategóriaelmélet"
regi_cimkek_mind:
  - "jquery"
  - "kategóriaelmélet"
---

**A kategóriaelméletet a közkedvelt meghatározás szerint "[general abstract nonsense](http://en.wikipedia.org/wiki/Abstract_nonsense)". Ez persze korántsem jelenti azt, hogy nem lehet gyakorlatias dolgokra használni eredményeit. Pl. [John Bender](http://johnbender.us/) egészen zseniálisan alkalmazta az ún. [loop fusion](http://en.wikipedia.org/wiki/Loop_fusion) technikát a jQuery-ben. De hogy kerül a csizma az asztalra? [Bender working paper](http://johnbender.us/applications-cat-theory/paper-2012-08.pdf)-je így foglalja össze:**

> The jQuery JavaScript library, used on more than 55% of Alexa’s top 10,000 websites makes the manipulation of HTML documents easy and intuitive through fluent method chaining and an intuitive API design. An unfortunate side effect of these user friendly features is that they often incur an otherwise unnecessary performance overhead. While JavaScript execution in desktop browsers has become fast enough to hide much of the problem, the growing complexity of HTML documents and the ubiquity of web enabled mobile devices continue to make performance an important concern when developing JavaScript applications. We address this issue by proposing a category theoretic view of the relationship between jQuery and the Document Object Model. From that view we derive a set of alterations to the jQuery library and demonstrate the performance benefits that result. Additionally we show how the second functor law suggests a set of JavaScript functions and jQuery methods that can be optimized using loop fusion.

Az alábbi videón teljesen érthető formában fejti ki vizsgálódásainak lényegét Bender. Érdemes a lejátszás előtt és után is elolvasni [rövid posztját](http://johnbender.us/2012/02/29/faster-javascript-through-category-theory/).

[YouTube](http://www.youtube.com/embed/PtD-WKSC6ak)
