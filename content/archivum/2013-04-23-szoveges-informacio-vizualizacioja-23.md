---
title: "Szöveges információ vizualizációja: topic clouds"
date: 2013-04-23T09:48:00.001Z
publishDate: 2013-04-23T09:48:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/04/szoveges-informacio-vizualizacioja_23.html"
regi_cimkek:
  - "vizualizáció"
regi_cimkek_mind:
  - "szófelhő"
  - "topik felhő"
  - "topik modellek"
  - "vizualizáció"
---

A magyar online sajtóból gyűjtöttem be cikkeket, sima nltk snowball stemmelésen mentek át normalizálás során, majd MALLET-et használva 20 elemű topik modellt készítettem. Az egyes topikokhoz leginkább hozzájáruló szavak gyakorisági listájából generáltam szófelhőket. A pytagcloud kifejezetten csúnya, de legalább programmatikusan generálhatóak a képek, a Wordle sokkal szebb. de a gyakorisági táblákat kézzel kell bemásolni a generálás előtt. Az eredményeken látszik, hogy pontosításra szorul a scraper (ti. nem csak a cikkek szövegét szedi ki, hanem még sok menüelemet és reklámot stb) és jobb stemmer sem ártana. Ezek ellenére a tapasztalatom azt mutatja, egészen informatívak a szófelhők - magyarán az adott topikról sokat elárulnak.

[Topic clouds - Wordle](https://plus.google.com/photos/102852068976721430833/albums/5869972176886770129)

[Topic clouds - pytagcloud](https://plus.google.com/photos/102852068976721430833/albums/5869971714814857761)

<span class="lost-media">Hiányzó kép: <a href="http://lh5.ggpht.com/-9UAxqenMvF4/UXZYYdcVh_I/AAAAAAAABNc/O_YmjXjEPdM/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span><span class="lost-media">Hiányzó kép: <a href="http://lh4.ggpht.com/-VqgFIb9N20o/UXZYiLtJfRI/AAAAAAAABNk/Ob2M6ariBWo/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>
