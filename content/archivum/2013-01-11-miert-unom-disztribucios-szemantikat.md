---
title: "Miért unom a disztribúciós szemantikát?"
date: 2013-01-11T10:07:00.001Z
publishDate: 2013-01-11T10:07:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/01/miert-unom-disztribucios-szemantikat.html"
regi_cimkek:
  - "funkcionális programozás"
  - "kategóriaelmélet"
  - "szemantika"
regi_cimkek_mind:
  - "disztribúciós szemantika"
  - "funkcionális programozás"
  - "kategóriaelmélet"
  - "kompozícionalitás"
  - "kvantumlogika"
  - "kvantumszámítás"
  - "szemantika"
---

**Itt vannak a nagy adatok, hát vizsgálhatjuk a disztribúciót orrvérzésig. Firth disztribúciós hipotézisével amúgy nincs baj, Wittgenstein is kacérkodott valami hasonlóval. A másik oldalon ott van a Frege-elve, avagy a kompozícionalitás. Persze szokták mondani hogy a formális szemantika nem más mint "exercise in typesetting". De valahol érezzük, hogy egyik elvvel sem mehetünk el a falig. További érdekesség, hogy nem mondanak egymásnak ellent, a disztribúció a szavakra vonatkozik, a kompozícionalitás pedig az összetett kifejezésekre.**

Szerencsére vannak, akik ezt tovább gondolták. A [Compositional and Distributional Models of Meaning](https://www.cs.ox.ac.uk/activities/CompDistMeaning/) néven futó kutatási program a University of Oxford vezetésével a kvantum-információelmélet és a kategóriaelmélet segítségével hozza közös nevezőre a két elvet. Amit tőlük érdemes olvasni és nézni:

- Clark - Coecke - Sadrzadeh: **[A Compositional Distributional Model of Meaning](http://www.pps.univ-paris-diderot.fr/~mehrs/AAAI_2008.pdf)**

- Coecke - Sadrzadeh - Clark: **[Mathematical Foundations for a Compositional Distributional Model of Meaning](http://arxiv.org/abs/1003.4394)**

- **[Oxford Quantum Talks Archive](http://www.youtube.com/user/OxfordQuantumVideo/videos)** (youtube csatorna)

**[](http://arxiv.org/abs/1003.4394)**

A fentinél sokkal pragmatikusabb a **[Dominic Widdows](http://www.puttypeg.net/)** nevével fémjelzett irányzat (elvégre a Bing egyik kutatójáról van szó). **[Geometry and Meaning](http://szamitogepesnyelveszet.blogspot.hu/2012/05/konyvismerteto-widdows-geometry-and.html)** c. könyvét már ajánlottuk a blogon, ezt ismét csak megerősítjük. Widdows megközelítése sem nélkülözi a kvantumfizikai hivatkozásokat, habár ő a kategóriaelméleti megközelítés helyett az ún. kvantumlogikát preferálja ([**Rédei Miklós tanulmányá**t](http://epa.oszk.hu/00100/00186/00003/9913redei.htm) ajánlom mindenkinek a témában). **[Li és Cunnigham tanulmánya](http://www.sigir.org/forum/2008D/papers/2008d_sigirforum_li.pdf)** pedig remek kis bevezetés a témához, de igazából Widdows honlapján lehet jó anyagokat találni. Aki módszeres bevezetésre vágyik, annak [van Rijsenbergen könyvét ajánljuk](http://szamitogepesnyelveszet.blogspot.hu/2012/10/konyvismerteto-geometry-of-information.html).

A két irányzat közötti különbség első sorban az hogy az oxfordiak elméleti, Widdows pedig gyakorlati vonalon halad. Talán felesleges bűvészkedésnek tűnhet a kategóriaelmélet bevezetése, de ez a fizikában is megkönnyítette a formális elméletekkel történő foglalkozást. A csillagok különös együttállása, vagy a véletlen szeszélye folytán a funkcionális programozás felszálló ágban van és valahogy adja magát hogy az implementáció is ilyen nyelven történjen meg. Sajnos ez még nem valóság, Widdows [semanticvectors](http://code.google.com/p/semanticvectors/) csomagja Javaban íródott - igaz nem is implementál mindent az elméletekből. Az izgalmas dolgok mind a nyelvtechnológia, mind pedig a keresés terén itt fognak történni a következő években és reményeim szerint sokat fogunk funkcionális nyelveken implementálni.
