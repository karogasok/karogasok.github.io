---
title: "Könyvismertető: Drew Conway &amp; John Myles White - Machine Learning for Hackers"
date: 2012-02-27T06:00:00Z
publishDate: 2012-02-27T06:00:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/02/konyvismerteto-drew-conway-john-myles.html"
regi_cimkek:
  - "gépi tanulás"
  - "könyvismertető"
regi_cimkek_mind:
  - "Drew Conway"
  - "John Myles White"
  - "Machine Learning for Hackers"
  - "gépi tanulás"
  - "könyvismertető"
---

**Andrew Ng online kurzusa nagyon népszerű volt és a "big data" őrület a gépi tanulást nagyon népszerűvé tette. Akik [beharangozó posztunkon ](http://szamitogepesnyelveszet.blogspot.com/2011/12/kispenzu-onkepzo-stanfordra-menne.html)fellelkesedve (vagy más okból) feliratkoztak Ng óráira mára már bizonyára megkapták az újabb késésről szóló levelet. Az eltökélt tanulni vágyók számára ez a könyv ideális! Nyelvészeknek kifejezetten ajánlott, hiszen viszonylag sok szövegfeldolgozás van benne és az R rejtelmeibe is bevezeti az olvasót. Vigyázat! Ahogy a címe is mutatja nem kezdőknek való könyv!**

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-Gs2pMXRyoxY/T0JF8Q1RxPI/AAAAAAAAAtI/s1HE6jFdtCw/s200/mlbook.jpg" rel="nofollow noopener">mlbook.jpg</a></span>](http://1.bp.blogspot.com/-Gs2pMXRyoxY/T0JF8Q1RxPI/AAAAAAAAAtI/s1HE6jFdtCw/s1600/mlbook.jpg)

- **Drew Conway - John Myles White: Machine Learning for Hackers**

- **O'Reilly Media, 2012**

- **322 oldal**

- **[a kötet megvásárolható a Számítógépes nyelvészet könyvespolcon](http://astore.amazon.com/szamitogepeny-20/detail/1449303714)**

- **[a könyvhöz kapcsolódó github repo](https://github.com/johnmyleswhite/ML_for_Hackers) (a könyvben nem említik, de van :D)**

[Drew Conway](http://www.drewconway.com/Drew_Conway/About.html) a New York University PhD hallgatója, a politikatudomány terén alkalmazza a számítástudomány és a statisztika (gépi tanulás) eszközeit. [John Myles White](http://www.johnmyleswhite.com/) pedig a Princeton pszichológia tanszékén írja doktori értekezését. A tény hogy két olyan ember írta a könyvet akik nem számítástudománnyal vagy matematikával foglalkozik kifejezetten az érthetőséget szolgálja. Nem hemzseg a könyv a felesleges információtól, olyanok írták akik napi munkájuk során használják az adatelemzési technikákat és maguk is megszenvedtek ezek elsajátításával. Egyedüli hátránya ennek hogy nem került bele a könyvbe pl. hol is találhatók a példa kódok (l. fent a linket) és a könyvben található kódrészletek sem éppen hibátlanok. Ez lehet hogy javul mire kijön a könyv a nyomdából, de az elektronikus verzió még tele van ilyenekkel.

A kötet bevallottan nem kezdőknek szól! Minimális statisztikai és programozási előismeretek elengedhetetlenek feldolgozásához. No nem kell sokra gondolni, de minimum egy [Head First Statistics](http://szamitogepesnyelveszet.blogspot.com/2010/12/konyvismerteto-statisztika-es.html) és egy bevezető jellegű [R kurzus/könyv](http://szamitogepesnyelveszet.blogspot.com/2011/03/konyvismerteto-statistical-analysis.html) (vagy egy [olyan ami kifejezetten nyelvészeknek íródott](http://szamitogepesnyelveszet.blogspot.com/2011/02/konyvismerteto-foundations-of.html)) kell ahhoz hogy az ember megértse amit olvas.

Az első fejezet egy kis ismerkedés. Mindenki szeret definíciót hallani, majd az R ismertetése a könyvhöz szükséges csomagok bemutatása (érdemes R 2.14-re upgradelni ha még nem az van a gépünkön) és egy gyorstalpaló programozás következik. Maga a példa nagyon személetes (UFO jelentések elemzése), mivel adatátalakítást, tisztítást és prezentálást is tartalmaz. Viszont a könyvben lévő kód problémás, érdemesebb a github repo-t nézni...

A második fejezet (Data Exloration) még nem kapcsolódik szigorú értelemben a gépi tanuláshoz, de roppant hasznos, egyszerű technikákat mutat be amivel minden előzetes elemzés nélkül "ránézhetünk" adatainkra. Ez után jönnek a klasszikus problémák, amolyan esettanulmányokon keresztül bemutatva. A harmadik fejezetben egy email spam szűrűt készítünk mint a klasszifikáció tipikus esete, a következő fejezetben pedig a Google priority inboxát másolhatjuk le (ez a ranking egyik jó példája). Az ötödik fejezet a regressziót mutatja be egy oldal látogatóinak számát tippeljük meg a rendelkezésre álló adatok alapján, majd a regularizációs és optimalizáció következik sajnos eléggé elnagyoltan, de azt hiszem itt már nem lehet sokat spórolni a mögöttes elméleteken...

A nyolcadik fejezetben áttérünk a nem felügyelt (unsupervised) tanulásra és igazi pénzügyi elemzőnek érezhetjük magunkat egy piaci index készítése közben. Számomra ez egzotikuma miatt is izgalmas része volt a könyvnek - az állandó kód problémákról már ne is beszéljünk! Ezután a multidimensional scaleing módszere kerül terítékre amivel az Egyesül Államok szenátorainak szavazási szokásait helyezzük el egy térben és ebből érdekes következtetéseket vonhatunk le. A tizedik fejezetben az ajánlórendszerekkel ismerkedhetünk meg ami szubjektív véleményem szerint megint csak elnagyoltra sikeredett. Kárpótlásul viszont a közösségi médiában elterjedt gráfok elemzése vár minket az utolsó esettanulmányban, konkrétan egy kis Twitter analitika. Végül pedig gyakorlati tanácsokat kapunk arra nézve mikor melyik módszer a jó választás.

Összegezve a könyv nagyon jó! Alapos munka és sokszor éreztem magam "megszólítva" mint olyan akinek a programozás eszköz csupán a mindennapi munka során nem pedig végcél. A hivatkozások és az ajánlott irodalom nagyon alapos és külön jó hogy pár szóval jelzik a legtöbb mű esetében hogy kit érdekelhet. A vizualizáció hangsúlyos jelenléte is pozitívum, a ggplot2 választása vitatható mivel nem egyszerű csomag, viszont látványos dolgokra képes. Ellenben a hibák miatt nem ajánlom azok számára akiket ez felbosszant, nincs gyakorlatuk abban hogy maguk keressék meg a megoldást (jó edzés régebbi technikai könyveket olvasni és napjainkra adaptálni a példákat!).
