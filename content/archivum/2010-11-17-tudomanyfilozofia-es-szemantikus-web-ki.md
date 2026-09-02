---
title: "Tudományfilozófia és szemantikus web"
slug: "tudomanyfilozofia-es-szemantikus-web-ki"
date: 2010-11-17T15:05:00.003Z
publishDate: 2010-11-17T15:05:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/11/tudomanyfilozofia-es-szemantikus-web-ki.html"
regi_cimkek:
  - "filozófia"
  - "szemantikus web"
  - "tudományfilozófia"
regi_cimkek_mind:
  - "filozófia"
  - "szemantikus web"
  - "tudományfilozófia"
---

**A szemantikus web ambiciózus programja azt célozza meg hogy az interneten minden dokumentum tartalmazza saját alapvető interpretációját is. Ez a távoli cél ami még várat magára, ám egyre több tudományterület ontológiája készül el és egyre több terültről áll rendelkezésünkre ún Linked Data (ami nem más mint egy olyan adathalmaz amihez csatolták elemei interpretációját is - de ez nem egy szakszerű definíció). Így felmerül a kérdés, ha adott az ontológia és egy adathalmaz, kell-e még nekünk kutató? Az ontológiát és az érvényes következtetések szabályait alkalmazva lehetséges-e új, eddig még nem ismert összegfüggéseket találni automatizált módon?**  
  
  
  
  
  
**Klasszikus tudományfilozófia**  
  
[Carnap](http://bit.ly/c8Mbt7) és a [bécsi kör](http://bit.ly/9Ov1TL) tudományfilozófiai nézetei állnak legközelebb a fent vázolt helyzethez. Ez az ún. klasszikus tudományfilozófia, ami élesen elkülönítette a a felfedezés és a rekonstrukció kontextusát a tudományos tudás elemzése során. A felfedezés kontextusa természetesen nem elhanyagolható tényező, de ezt a klasszikus elmélet a szociológia és pszichológia. Ami megkülönbözteti a tudományos tudást a hétköznapitól, az az hogy a tudományos elméletek bizonyítása is adott (vagy legalábbis elérhető az érdeklődők számára). A bécsi kör tagjai számára a tudományfilozófia épp arról szól miképp épül fel ez az igazolás, miképp rekonstruálja felfedezését egy kutató racionálisan. A rekonstrukció szerintük abból áll hogy 1) a legalapvetőbb állítások megfigyelésekből nyerik jelentésüket, ezek az ún megfigyelési állítások 2) a klasszikus logika szerint jutnak el az érvényes következtetésig. Így a megfigyelések adják az ontológia alapjait, a magasabb fogalmak pedig a klasszikus logika szabályai szerint, a kompozícionalitás elvének megfelelően ezek kombinálásából épülnek fel.  
  
 A szemantikus web esetében az atomi megfigyelési mondatoknak az egyes entitások feleltethetők meg. A klasszikus logika helyett gyakran a reasoning engine (érvelő motor :D) deskripciós logikával él, ám ennek gyakorlati okai vannak és eltekinthetünk ettől. Tegyük fel hogy egy kellően nagy adathalmaz biztosítja az interpretációt, ekkor elvben lehetséges hogy elvben hogy olyan nyílt kérdések tegyünk fel, melyekre előtte nem tudtunk válaszolni. A prologban járatos olvasó bizonyára találkozott már az ÉRDEKES_PREDIKÁTUM(X,Y) lekérdezéssel, amivel arra vagyunk kíváncsiak hogy egy adott adatbázisban mely entitások között áll fenn egy számunkra érdekes predikátum. Ez nem minden esetben nyilvánvaló és nagyon nagy adatbázis esetén gyakran lehetetlen észben vagy papíron eldönteni ilyen kérdéseket. De mit mondhat nekünk egy ilyen választ, mennyire hihetünk benne? Nos csakis annyiban, amennyiben tisztában vagyunk azzal hogy ontológiánk egy zárt világ, csak arról tud információt szolgáltatni ami benne van. Ezen az sem változtat ha zárt vagy nyílt világ feltételezésével él deduktív rendszerünk, azaz hamisnak vagy eldönthetetlennek tartja azt amire a rendelkezésére álló adatok alapján nem tud következtetni.  
  
**Miért bukott el a klasszikus tudományfilozófia?**  
  
 A kérdésre a válasz egyszerű; nagyon hamar kiderül hogy magával az értelmesség kritériumával, a megfigyelés igazolással vagy más néven a verifikációval komoly bajok vannak. Sajnos ez a fogalom maga nem verifikálható, így értelmetlen. Persze egy jó megoldás lenne elfogadni ezt ilyennek és azt mondani hogy ez a metanyelvbe tartozik így rá más szabályok vonatkoznak, de így elismerjük hogy a tudományos tudáson kívül is vannak komoly dolgok (ezt pedig Carnap és társai nem szerették volna). Így [Popper](http://bit.ly/cUUdIv) visszalépet a kályhához, ha rekonstrukció a lényeg és elvérzett az igazolhatóság, akkor fordítsunk egyet a dolgon: az igazolhatóság feltételei egyben kijelölik a cáfolhatóság kritériumait is. Minden tudományos elmélet megcáfolható, ellenben a nem tudományos elméletekkel (Popper ilyennek tartotta a pszichoanalízist, marxizmust és a vallást). Azonban a falszifikáció felvet egy komoly problémát, ha falszifikálok egy elméletet, akkor megváltozik annak eddigi interpretációja is! Ha kiegészítem az elméletemet, akkor egy új jön létre és megint megváltozik annak interpretációja (az ún [Quine-Duhem](http://bit.ly/aDlYPd) tézis értelmében lehetetlen izoláltan tesztelni egy tudományos hipotézist, hiszen megerősítése erősíti, elvetése pedig megváltoztatja az elméletet). [Kuhn](http://bit.ly/9jNW7O) tudományos forradalmak elmélete és hírhedt paradigma fogalma is ezzel a problémával foglalkozik, ám Kuhn rámutat arra hogy a rekonstrukció és a felfedezés kontextusa nem különíthető el élesen. A paradigma magába foglalja a bevett eljárásokat, kijelöli hogy mit tekinthetünk egy elmélet cáfolatának és mit bizonyítékának, az ami racionális rekonstrukció, az tkp egy virágzó paradigma leírása, ám akadnak pillanatok amikor ez a paradigma megváltozik (mind belső, mind külső okok miatt) és paradigma váltás történik (ezt nevezzük tudományos forradalomnak). [Feyerabend](http://bit.ly/cFrJet) egészen odáig ment, hogy elvetette a rekonstrukciót, és a felfedezést hangsúlyozta, a felfedező egyént és annak társadalmi kontextusát, aki csak később, különböző körülmények hatására alkotja meg a "rekonstrukciót". Popper utódja az LSE katedráján, Feyerabend jó barátja, [Lakatos](http://bit.ly/cJcH6o) megpróbálta összeegyeztetni a két megközelítést a tudományos kutatási programok elméletében (ami mostanában ismét kezd divatos lenni tudományfilozófusok körében). Popperhez és Kuhnhoz hasonlóan hangsúlyozza hogy kialakul egy paradigma, vagy központi mag amit rekonstruálhatunk, ám a kutatás során a falszifikációs kísérletek folyamatosan módosítják az elméletet és akár paradigma váltás is lehetséges. Így egy kutatási program nem írható le egy adott rekonstrukcióval, hanem rekonstrukciók sora tudja visszaadni. Ugyanakkor magyarázatot ad arra is hogy miképp lehetséges az hogy az elméletek jelentésváltozáson mennek keresztül, vagy éppen tudományos forradalmak is történhetnek.  
  
 A szemantikus webnek szembe kell néznie a változással. Egyre több adat kerül standard formába, egyre több ontológia születik. Azonban figyelembe kell vennünk hogy ennek során a meglévő rendszerek bővítése is változtat bevett interpretációjukon. A szemantikus technológiák együttműködése során is figyelembe kell vennünk hogy nem a "best of both words" kényelmes állapotát kapjuk, hanem egy új, minőségileg más (és nem jobb vagy rosszabb) "világot" kapunk és szembe kell nézünk azzal hogy bármilyen jó formalizmussal is rendelkezünk, van valami "je ne sais quoi" a dolgok mögött amit nem tudunk megragadni.
