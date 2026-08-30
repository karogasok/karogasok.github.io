---
title: "Első magyar NLP meetup"
date: 2012-05-04T05:14:00.001Z
publishDate: 2012-05-04T05:14:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/05/elso-magyar-nlp-meetup.html"
regi_cimkek:
  - "meetup"
regi_cimkek_mind:
  - "meetup"
---

**Összeállt a program! Május 10-én 19 órától Hungarian NLP meetup! [Itt kell regisztrálni.](http://www.meetup.com/Hungarian-nlp/)**

**Előadások**

Dr. Székely Gábor - Herczog Zoltán: **Digitális filológia**

A kétnyelvű (manysi-magyar, stb.) vagy többnyelvű (manysi-magyar-orosz-angol, stb.) szövegek számítógépes adatbevitelének és feldolgozásának elvi tisztázása a számítógépes oldalról nagy segítség lenne. A nyelvészet oldaláról a következőket kellene tisztázni. A forrásnyelv (manysi) mondatonkénti adatbevitele jelenti az első lépést, ehhez meg kell adni a finnugor karakterek bevitelének könnyű begépelését a billentyűkészleten gyorsan elérhető betűkkel. A finnugor mellékjeles betűk (pl. â) számítógépes betűkészletének átgondolása a finnugor nyelvész feladata, de segítséget kell kérni a számítógépes nyelvésztől. A későbbi adatfeldolgozást figyelembe kell venni (pl. betűrendbe rendezés). Az lenne a jó, ha a feldolgozó programok ismernék a UNICODE kódolást, ez már nagyrészt megoldott, de mindig vannak meglepetések, hogy nem működik a kódolás. Az XML jelölő nyelvet alkalmaztuk a mondatpárok egyberendezésére, erre már van egy programunk, ami működik. A mondatot alkotó szavak előállítására is kellene egy program, ha a forrásnyelvi mondat szavai és a célnyelvi fordítás egy-az-egyben megfelel, csak akkor lehetséges a szavakra bontás. Meg kell állapodni a nyelvészeti kategóriák egységesítéséről, ez a nyelvész feladata, a kategóriák (pl. főnév, ige, melléknév, stb; vagy igerag, birtokos személyrag, igeidőjel, stb.) lekérdezése, az adott szöveg mondatainak programmal való kategóriákba rendezése lenne a nyelvészeti elemzés gyorsításának eredménye.

Pataki Máté: **Fordítási plágiumok**

Azonos nyelven íródott dokumentumokat már több mint tíz éve tudunk automatikus eszközökkel összehasonlítani, köztük plágiumot keresni, viszont a technológia – a természetes nyelvi eszközök és a számítógépek kapacitása – csak most jutott el arra a szintre, hogy hatékonyan kereshetünk azonosságokat két különböző nyelven írott szöveg között is. A fordítási plágiumok problémája nem újkeletű, de csak az idegennyelv-tudás széleskörű elterjedésével számíthatunk tömeges előfordulására. A diákok egyre nagyobb hányada beszél ma már minimum egy idegen nyelvet olyan szinten, hogy képes elolvasni, feldolgozni egy idegen nyelvű szakmai cikket – ami elvárás is felé – ugyanakkor ez megteremti a lehetőséget a forrásmegjelölés nélküli tartalmak, gondolatok átvételére. Az elmúlt egy év alatt egy kutatás keretében arra kerestük a választ, hogy megtalálhatóak, felismerhetőek-e a fordítási plágiumok. Ennek során egy olyan algoritmust fejlesztettünk ki, amely képes egy nagyméretű, idegennyelvű adatbázisból kikeresni egy magyar nyelvű dokumentumban idézett, lefordított szövegrészeket. Előadásomban rövid áttekintést adok a többnyelvű keresők működéséről, és egy demó keretében bemutatom a KOPI mögött lévő új keresőt is.

Szekeres Péter: **Polaritásmérés magyar nyelvű webes szövegekben**

A számítógépes véleményelemzés üzleti relevanciájának rövid áttekintése után általános illetve a magyar nyelvre jellemző szövegfeldolgozási nehézségeket, kihívásokat mutatok be. Ezt követően először beszélek a lemmatizálásról, mint a szó/kifejezés alapú polaritásmérés kulcsfontosságú előfeldolgozási lépéséről, majd véleményelemzési algoritmusokat mutatok be. Az egyes ismert véleménymérési kutatások megoldásainak pontosságát össze is vetem egymással, majd az előadás végén a webes szövegek polaritásmérésének előrejelző és döntéstámogató képességét illusztrálom.

**Intézményi/céges bemutatkozók**

Vincze Veronika: **Számítógépes nyelvészet Szegeden**

Az SZTE Nyelvtechnológiai Csoportjánál 1998 óta folynak nyelvtechnológiai kutatások elsődlegesen az információkinyerés, korpuszépítés és nyelvi elemző eszközök fejlesztése területén.  
 A legfontosabb alkalmazási területek az információkinyerés üzleti hírekből, biológiai publikációkból, orvosi jelentésekből és az internetről (például fórumokból, blogokból). A kézzel egyértelműsített Szeged Korpusz és TreeBank, a Magyar WordNet, a SzegedNE és egyéb korpuszok kifejlesztése lehetővé tették gépi tanuláson alapuló módszerek alkalmazását magyar nyelvű szövegek szintaktikai és szemantikai elemzésére. A csoport rendelkezik az elemzésekhez szükséges alaptechnológiákkal (szófaji elemző /POS-tagger/, szintaktikai elemző, tulajdonnév-felismerő és kategorizáló, jelentés-egyértelműsítő) mind magyar, mind angol nyelvre.

Szekeres Péter: **Neticle Kft.**

A Neticle fő szolgáltatásának célja márkákról, cégekről, termékekről és versenytársakról szóló webes szöveges tartalmak, vélemények **közel valós idejű** feldolgozása a **teljes webről** (és közösségi médiumokról). A webes szöveges információk elemzésével, szofisztikált értékelésével és különböző dimenziók mentén történő összegzésével és **vizualizálásával tény alapú döntéshozatal támogatása** a felhasználó vállalati pozíciójára és igényeire szabva.

Jóföldi Endre: **WebLib Kft.**

A WebLib intelligens, nyelvészeti alapokra építő keresési és szövegbányászati megoldások kutató fejlesztője.
