---
title: "A minimalista program I - Elvek, paraméterek és miért is kell minimalizmusra törekednünk"
date: 2010-06-22T08:02:00.001Z
publishDate: 2010-06-22T08:02:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/06/minimalista-program-i-elvek-parameterek.html"
regi_cimkek:
  - "Ubiquity"
  - "elvek és paraméterek"
  - "minimalista program"
  - "nyelvészet"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "Ubiquity"
  - "elvek és paraméterek"
  - "minimalista program"
  - "nyelvészet"
  - "számítógépes nyelvészet"
---

**A minimalizmus megpróbálja a lehetséges emberi nyelvek szerevezőelveinek leírását adni. Ebben két fő elvre támaszkodik; maximális megszorítás mellett (azaz csakis kizárólag az emberi nyelveket szándékozik leírni) a lehető leggazdaságosabban (minél kevesebb szabályt alkalmazva) igyekszik célját elérni. Most nem próbáljuk meg a minimalista programot teljes egészében leírni, hanem csak erre a két alapelvre szorítkozunk.**  
  
(Ez a bejegyzés az olvasók kérésére született. Örömmel teszek eleget kéréseiteknek, de így sajnos a Ubiquity-t bemutató sorozat következő darabja csúszik egy kicsit)  
  
A lehetséges emberi nyelvek összessége valamilyen formában egy kalap alá tartozik már csak az intuíció szerint is. Valamiért azt tapasztaljuk hogy minden egészséges ember (és nagyon sok különböző betegséggel küzdő is) beszél legalább egy nyelvet. Beszédszerveink léte és egyéb biológiai és pszichológiai kutatások is alátámasztják hogy van valamilyen nyelvi képességünk (elég itt csak a különböző specifikus beszédzavarokra gondolnunk).  
  
Chomsky, a minimalista program atyja, feltételezi hogy ez egy univerzális, velünk született képességre utal. Az egyes nyelvek közötti különbségek oka hogy nem egy adott nyelvel jön világra egy újszülött, hanem annak elsajátítását lehetőtévő elvekkel. Ez egy tanuláselméleti érv, amit a pszicholingvisztika szerelmesei szeretnek kutatni, de van egy formális megközelítése is, Gold elmélete.  
  
**Gold elmélete**  
Képzeljünk el egy kísérletet. Van egy szerkezetünk aminek az a dolga hogy a beérkező karakter-sor inputok alapján eldöntse milyen grammatika generálta őket. Amennyiben semmilyen tudással nem vértezzük fel gépünket a beérkező inputok lehetséges természetéről, úgy nem tud megállapodni egy grammatikánál. Legyen S a karakterek véges halmaza, G1, G2, és G3 pedig három grammatika amely S-ből mondatokat generál, G4 pedig egy olyan grammatika amely szimplán generálja mindegyik grammatika lehetséges mondatait. Kezdjük el gépünknek adagolni G1 mondatait, ha elég okos egy idő után felismeri hogy melyik grammatikával van dolga. Ezután adagoljuk neki G2 mondatait, azzal a feltétellel hogy minden korábbi mondat szintén helyes. Ekkor minden további nélkül következtethet arra hogy G4-ről van szó (vagy esetleg egy másik, számunkra ismeretlen grammatikáról), holott nem találkozott G3 mondataival. Bonyolítsuk a dolgot azzal hogy G4 tartalmazza G3-at és nem bővebb , G3 tartalmazza G2-t ám bővebb, G2 pedig G1-et de egyben bővebb is. El tudja dönteni gépünk egy akármekkora mondat halmaz segítségével hogy melyik grammatika tartozik ahhoz? Biztos lehet abban hogy a következő input nem kényszeríti nézetei felülvizsgálatára? Mivel a generálható mondatok száma megszámlálhatóan végtelen mindegyik grammatika esetében, végtelen inputra számíthat a szerkezetünk, és sohasem lehet biztos hogy melyik grammatikát kapta éppen meg.  
  
**Elvek és paraméterek**  
Ahhoz hogy tudjuk milyen grammatikát rendeljünk a beérkező inputokhoz, szükségünk van egyrészt 1) a lehetséges grammatikák ismeretére 2) a grammatikák megkülönböztető jegyeire. Vegyük előre a kettes pontot. Miben térnek el az emberi nyelvek? Ennek kutatása a tipológia területe, amely egyrészt univerzálékat keres (azaz minden emberi nyelvre jellemző tulajdonságokat), másrészt olyan specifikus paramétereket amiben a nyelvek különböznek. A minimalista program a különbözőségekre (több-kevesebb empirikus bizonyossággal) szigorú előfeltevésekkel él. Minden paraméter függetlenek és binárisak. Ez annyit tesz hogy egy adott paraméter vagy megvan egy nyelvben, vagy nem. Ha X paraméter megléte maga után vonja Y-ét, akkor értelmetlen külön kezelni őket, hiszen amúgy is összetartoznak mindig.  
  
Ennek fényében az anyanyelv elsajátítása nem más mint a lehetséges paraméterek értékeinek beállítása (és a lexikon elsajátítása). Hogy ez valóban így van-e az kérdéses (mint minden), minden esetre mellette szól hogy a nyelvet a gyermekek viszonylag hamar, negatív példák nélkül, jórészt saját maguk sajátítják el. Érdemes itt megjegyezni hogy különbség van az egyes természetes nyelvek, és a velünk született nyelv között. Az univerzális grammatika a velünk született képességet, belső nyelvet (I-nyelv/ internal language) írja le. Az paraméterek ezt az általános szabályhalmazt szorítják meg, kijelölve ezzel egy-egy természetes nyelv grammatikáját.  
  
Eddig is láttuk hogy minimalista program szeret gazdaságossági elveket használni. Ilyen például a paraméterek binaritása és függetlensége. Ezekhez hasonlóan szeretné elérni hogy a lehető legkevesebb szabály írja le az I-nyelvet. Ez nem csak elméletileg indokolt (Occam borotvája), hanem gyakorlatilag is egy zsúfolt rendszerbe kell beilleszkednie a nyelvnek. Az elme így is tele van pakolva mindennel, a nyelv pedig egy nem túl régi dolog. Biológiai érvek is szólnak amellett hogy a lehető legkisebbnek képzeljük el hát nyelvi képességünk velünk született szervező elveit. Technikailag is könnyebb ha nem kell sok szabállyal bajlódni, a következő részben ezt vesszük szemügyre.  
  
Összegzés  
A minimalista program nem egy kiforrott kutatási program, hanem egy vállalkozás, ami néha úgy tűnik túl sokat vállal. Viszont nagyon csábító és elegáns. A Ubiquity projekt szépségét számomra pont az adja hogy megpróbálja felhasználni ezt az elméletet és egyszerűbbé tenni a ember-gép interakciót és a lokalizációt is egyben. Habár sokszor úgy mutatják be Chomsky gondolatait hogy ez a "mainstream" irányzat, ez nem igaz. A minimalista program hívei valójában kisebbségben vannak, viszont a többség hozzájuk képest határozza meg magát (a nyelvészek körében egyfajta identifikációs tényező lett az "amiben Chomskyval nem értek egyet" listák készítése).  
  
Fontos azonban belátnunk hogy ennek a megközelítésnek van egy erős esztétikai oldala is. A végletekig vitt egyszerűsítés nem biztos hogy célra vezető, viszont nagyon erős érvek szólnak a biológiai és esztétikai érveken túl hogy nem egy nagy szabályhalmazzal kell kezelnünk a nyelv leírását. A következő részeb ezeket a nagyrészt technikai okokat mutatom majd be.
