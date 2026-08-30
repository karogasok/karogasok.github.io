---
title: "R, de miért is használjam? - II."
date: 2010-07-29T10:00:00.001Z
publishDate: 2010-07-29T10:00:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/07/r-de-miert-is-hasznaljam-ii.html"
regi_cimkek:
  - "R"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "R"
  - "számítógépes nyelvészet"
---

**Az [előző részben](http://szamitogepesnyelveszet.blogspot.com/2010/07/r-de-miert-is-hasznaljam-i.html) megvizsgáltuk milyen is elvileg egy ideális nyelv egy számítógépes nyelvész számára. Most sorra vesszük hogy ennek mennyiben felel meg az [R](http://www.r-project.org/) statisztikai programozási nyelv.**  
  
**Vegyük végig a pontokat**  
1. A listák beépített támogatása  
Igen, sőt!  
2. Automatikus tárhelyvezérlés  
Ezen sem lepődünk meg, hiszen manapság már egy cool nyelvnek ezt alapból tudnia kell  
3. dinamikus típuskezelés (de mondhatnám hogy dinamikus gépelés)  
Ezzel sem kell sokat törődnöd, nincs String name = "Zoli", nem fogsz egy Integert byte-ba tenni és elvérezni.  
4. első-osztályú függvények  
Elég itt idézni az [R Language Definition](http://cran.r-project.org/doc/manuals/R-lang.html) idevágó részét: "In R functions are objects and can be manipulated in much the same way as any other object. Functions (or more precisely, function closures) " azaz első osztályú függvények a nyelv alapjai.  
5. egységes szintaxis  
Nagyon kevés nyelv van amelyiknek nem egységes a szintaxisa és az R nem tartozik közéjük.  
6. interaktív környezet  
A CommonLISP, Scheme és Python által megkezdett hagyományhoz hűen az R is rendelkezik egy szép interaktív környezettel. Itt talán még intenzívebben használják ezt.  
7. Bővíthetőség  
A Comprehensive R Archive Network szinte minden feladathoz kínál csomagot. Könnyen lehet egy új csomagot installálni és szabadon módosíthatod ha kell cuccot igényeid szerint. (A nyílt forráskód előnye :D)  
8. Történeti háttér és kultúra  
Erről külön is szólni fogunk!  
9. Statisztikai függvények támogatása  
Egy statisztikai programozási nyelv alapból támogatja ezeket, ugye ez nem lepett meg. Ajánlom figyelmedbe a Language Definition dokumentumot.  
10. Speciális adatstruktúrák natív támogatása  
Ha probabilisztikus megközelítésre adjuk fejünket szükségünk lesz a listákon kívül vektorokra, mátrixokra és egyéb félelmetes nevű dolgokra. Ha érdekel mi mindent támogat az R itt egy jó [oldal](http://www.biw.kuleuven.be/vakken/statisticsbyr/someDataStructures.htm).  
  
**Egy kis történeti háttér**  
Az R nyelv az S nyelven alapul amit John Chambers 1975-ben a Bell Labs keretein belül fejlesztette ki. Az informatika területén 35 évesnek lenni matuzsálemi kornak számít, viszont egy stabil és igen hozzáértő kör alakult ki a felhasználókból ez idő alatt. Az R 1993-ban tűnt fel, és létezik még egy S-Plus nevű testvére, amely kereskedelmi szoftver.  
  
Aucklandi atyákat az eredeti S nyelv mellett a Scheme egyszerűsége inspirálta, aminek én mint Scheme rajongó nagyon örülök. A nyelv hamarosan nagyon népszerű lett a statisztikusok körében, így a nyelv egymást követő verziói általában nagyon stabilak.  
  
A kilencvenes évek végén elkezdődött az adatok forradalma. Egyrészt az informatika világa egyre több adatot produkál, (talán ennek hatására) másrészt a humán és társadalom tudományok is egyre jobban a kísérleti és begyűjthető adatok felé fordultak. Egyre többen kezdték el használni különböző statisztikai programcsomagokat ismerték fel azok korlátait is. Az R felhasználói tábora valamikor az ezredforduló körül hirtelen megugrott és azóta is folyamatosan bővül.  
  
Ez a történet csak tovább erősíti a nyelvet. A kemény mag továbbra is szinte változatlan és egyre jobb rendszert fejleszt. A speciális területek művelői egyre több csomagot írnak és publikálna. Az így létrejött nyilvánosság az esetleges hibák felfedezését meggyorsította, a fejlesztők közötti együttműködést elősegítette és még jobb csomagokat eredményezett. Az online fellelhető dokumentáció igen magas színvonalú, habár nagyon technikai jellegű. Úgy tűnik hogy még várnunk kell hogy a "kocka" fejlesztői mag észrevegye ezt és lépjen az érthetőség irányába.  
  
A hosszú történet azzal is jár hogy sok jó könyvet találhatsz (habár ezek általában drágák) és rengeteg publikációt olvashatsz. Könnyű kommunikálni eredményeidet és nem kell sokat magyarázkodnod közben.  
  
**Hátrányok**

1. Az R nem egy egyszerű nyelv

1. aki nem ismeri a lisp dialektusokat annak az R szintaxisa nagyon idegen lehet

1. nehéz egyszerre statisztikát és R programozást tanulni

**Hogyan tovább?**  
Ha szeretnél még többet megtudni a nyelvről, esetleg kipróbálnád és tanulnád érdemes elolvasnod [Valószínűség, statisztika és nyelv](http://szamitogepesnyelveszet.blogspot.com/2010/05/valoszinuseg-statisztika-es-nyelv.html) című korábbi posztomat, ami segít eligazodni hogy hol érdemes kezdeni.
