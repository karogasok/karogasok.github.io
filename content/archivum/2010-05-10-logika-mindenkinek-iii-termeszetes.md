---
title: "Logika mindenkinek III - a természetes nyelvek szemantikája"
slug: "logika-mindenkinek-iii-termeszetes"
date: 2010-05-10T19:45:00.001Z
publishDate: 2010-05-10T19:45:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/05/logika-mindenkinek-iii-termeszetes.html"
regi_cimkek:
  - "logika"
  - "szemantika"
regi_cimkek_mind:
  - "drt"
  - "logika"
  - "szemantika"
---

**A [bevezető könyvek](http://szamitogepesnyelveszet.blogspot.com/2010/05/logika-mindenkinek-i-bevezetes.html) bemutatása és az [automata elmélet és kiszámíthatóság problémája](http://szamitogepesnyelveszet.blogspot.com/2010/05/logika-mindenkinek-ii-automatak.html) után elérkezett az idő hogy egy kicsit gyakorlatibb terepre merészkedjünk. A természetes nyelvek szemantikája már gyakorlati terep, de még egy lépéssel a számítógépes alkalmazások előtt vagyunk, de innét már tényleg csak egy lépés. Ha nagyon türelmetlen vagy akkor régebbi blogbejegyzéseimből ajánlom neked a [funkcionális programozásról ](http://szamitogepesnyelveszet.blogspot.com/2010/03/funkcionalis-programozas-nem.html)ill. a [logikai programozásról szólóakat](http://szamitogepesnyelveszet.blogspot.com/2010/03/logikai-programozas-nem-programozoknak.html).**  
  
**A szemantika egy nagyon tág fogalom!**  
Volt már akit meglepett ez a kijelentés, de tényleg igaz. Nem, ebben nincs semmi ellentmondás! OK, jól tudod a szemantika a jelentés tudománya, tehát azzal foglalkozik miképp áll össze egy egy mondat, vagy akár szó vagy bármilyen kifejezés jelentése. Csak nem mindegy mit tekintesz alapnak és az sem hogy milyen elvek mentén kutatod a részek összekapcsolódását egésszé.  
  
A logika alapfogalmait a természetes nyelveken keresztül vezeti minden tankönyv, de ha csak az implikációra gondolunk, érezzük hogy nincs teljes fedés a két fogalom között. Sokáig úgy gondolták hogy a filozófiai analízisen kívül nem is lehet fedésbe hozni logikai eszköztárunkat a nyelvvel - habár ez nem semmi, elég csak Frege Jelentés és jelöletére (és más esszéire) vagy Russel híres On denoting-jára gondolni.  
  
**És jött Montague**  
Aztán jött [Montague](http://en.wikipedia.org/wiki/Montague_grammar), és minden megváltozott. A természetes és mesterséges nyelvek közötti éles választó vonalat a generatív elmélettől ihletve elvetette és arra gondolt hogy a szintaktikai struktúrával párhuzamosan jön létre a szemantikai interpretáció. Jól hangzik?! Nem kell félni, a legtöbb eddig említett könyvben találkozhatsz Montague módszerével, ha más nem intenzionális logikával. A filozófusok és logikusok persze örültek a megközelítésnek (vagy ízekre szedték), de a nyelvészek egy érdekes alfaja fogadta lelkesedéssel igazán. Egy kis idő elteltével egyesek odáig merészkedtek hogy nem egy egy mondat interpretálását akarták megadni, hanem egy-egy diskurzusét (ok igazából pár mondatét) és megszületett a diskurzus reprezentációs elmélet ([DRT](http://en.wikipedia.org/wiki/Discourse_Representation_Theory)).  
  
**Mit olvass?**  
Mivel a dolog nagy részét már ismered, most csak egy rövid felsorolást adok, válasz magadnak egy, esetleg két könyvet a listáról. A lényeg hogy láss egy nyelvészeknek írt logikai bevezetőt, nyelvészek által végig gondolt példákkal.

- Chiercha et all: [Meaning and Grammar](http://www.amazon.com/Meaning-Grammar-2nd-Introduction-Semantics/dp/0262032694/ref=sr_1_15?ie=UTF8&s=books&qid=1273517581&sr=8-15)

- Heim - Kratzer: [Semantics in Generative Grammar](http://www.amazon.com/Semantics-Generative-Blackwell-Textbooks-Linguistics/dp/0631197133/ref=pd_bxgy_b_text_b)

- Larson - Segal: [Knowledge of Meaning](http://www.amazon.com/Knowledge-Meaning-Introduction-Semantic-Theory/dp/0262621002/ref=pd_sim_b_49)

Ha ez megvan akkor a Montague grammatika klasszikus bevezetőjét és a DRT alapművét kell kézbevenni.

- Kamp - Reyle: [From Discourse to Logic](http://www.amazon.com/Discourse-Logic-Introduction-Model-theoretic-Representation/dp/0792310284/ref=pd_sim_b_7)

- Dowty et all: [Introduction to Montague Semantics](http://www.amazon.com/Introduction-Montague-Semantics-Linguistics-Philosophy/dp/9027711410/ref=pd_sim_b_10)

Nos ha ez mind megvan, akkor már csak egy kiegészítőre van szükséged:

- Portner - Partee : [Formal Semantics: The Essential Readings](http://www.amazon.com/Formal-Semantics-Essential-Readings-Linguistics/dp/0631215425/ref=sr_1_1?ie=UTF8&s=books&qid=1273519928&sr=8-1)

Ha unod a sok könyvet, akkor olvasd csak ezt! Ebből láthatod hogy mit is csinálnak ezen a területen.  
  
**Összegezve**  
  
Mostanában nem cool logikával foglalkozni és a szabály-alapú megközelítéssel sem gyakran találkozunk méjnstrímben, de

- a logikai megközelítés még él

- a hibrid modellek elterjedtek/visszatértek

- az algoritmusok megértéséhez jól jön a logika ismerete

- pedagógiai szempontból hasznos a programnyelvek elsajátítása előtt/közben logikát tanulni

**Vége**  
Rövid ajánlóm végére értem. Köszönöm hogy olvastatok :D Nagyon jól esett hogy kértétek a sorozatot és az is hogy infósok érdeklődtek. Mivel a blogot olyanoknak szánom akik egyedül vagy kevés segítséggel indulnak neki ennek a szép tudománynak, a későbbiekben is fogok még ilyen "könyvismertetőket" írni. Mivel személyes élmények alapján írok és azt hiszem a humán tudományok felől érkezők ezen a téren nagy nehézségekbe ütközhetnek, az ő szempontjukból közelítem meg a témáimat (és örülök hogy a reáliák tanulói is hasznosnak találják mindezt.)
