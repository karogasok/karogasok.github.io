---
title: "R tutorial előtt"
date: 2012-06-02T11:15:00.001Z
publishDate: 2012-06-02T11:15:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/06/r-tutorial-elott.html"
regi_cimkek:
  - "R"
  - "meetup"
regi_cimkek_mind:
  - "R"
  - "meetup"
  - "text mining"
---

**Két hónap múlva egy egész napot szentelünk az R nyelvnek és a tm csomagnak. Már csak 18 szabad hely maradt, ha nem szeretnél lemaradni, [regisztrálj](http://www.meetup.com/Hungarian-nlp/events/65874002/) mihamarabb! A rendezvény ingyenes (köszönet a [Weblib](http://weblib.hu/)nek!), csupán te, a laptopod és némi előkészület szükséges hozzá - ez a poszt ebben szeretne segíteni.**

Ha regisztráltál a rendezvényre, akkor feltételezhető hogy tudsz angolul és nem csak felhasználói szinten értesz a számítástechnikához, hanem vagy magadtól vagy egy bevezető jellegű kurzus keretében már elsajátítottad a programozás alapjait. A tutorialhoz ezen felül csupán arra van szükséged hogy a) telepítsd az R-t gépedre b) egy szövegszerkesztőből vagy IDE-ből tudd kezelni.  
  
**Alapok**

- Telepítsd az operációs rendszerednek megfelelő R disztribúciót (Ubuntu használók nyugodtan apt-get install-t is használhatnak). Az [**R honlapja**](http://www.r-project.org/) eligazít ebben.

- Telepítsd az [**R Studio**](http://rstudio.org/)-t. A legelterjedtebb IDE az R-rel végzett munkára ma az R Studio. Ha van olyan IDE vagy szövegszerkesztő amit szeretsz, akkor egy kis guglizással bizonyára megtalálod a megfelelő beállításokat. (emacs használóknak én az ESS csomagot ajánlom!)

- Indítsd el az R-t (Ubuntuban szimplán az R paranccsal a konzolról, Windowson a start menüből) és telepítsd a tm csomagot az **install.packages("tm")** parancs beírásával. Ennek eredménye egy felugró ablak, amin kiválaszthatsz egy számodra szimpatikus helyet ahonnét leszedi a program automatikusan a csomagot és telepíti neked. Tipp, sokan Ubuntu alatt sudo R-t indítanak telepítés előtt.

**Ingyenes anyagok**

- [**simpleR**](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf) - Verzani nem éppen rövid (114 oldalas) bevezetője a legjobb hogy megismerkedj az R nyelvvel és a statisztikával. Könnyen olvasható, ha elszánt vagy akkor a legjobb bemelegítés a témához.

- [**Singular Value Decomposition Tutorial** ](http://www.cs.wits.ac.za/%7Emichael/SVDTut.pdf)- a tm csomag mátrix algebrai módszerekkel van tele, érdemes átnézni egy kicsit mi áll a háttérben

- [**Word Vectors and Search Engines**](http://www.puttypeg.net/papers/vector-chapter.pdf) - Dominic Widdows [Geometry and Meaning](http://www.puttypeg.net/book/) című zseniális könyvének fejezete ami szintén nagyon hasznos előtanulmány

**Egyéb**

- [**R idősebbeknek és halandóknak**](http://szamitogepesnyelveszet.blogspot.hu/2012/04/r-idosebbeknek-es-halandoknak.html) - ebben a posztban haladób R használati tippek találhatóak

- **R, de miért is használjam [I](http://szamitogepesnyelveszet.blogspot.hu/2010/07/r-de-miert-is-hasznaljam-i.html) és [II](http://szamitogepesnyelveszet.blogspot.hu/2010/07/r-de-miert-is-hasznaljam-ii.html)** - kis háttér hogy miért is fasza az R

- [**Valószínűség, statisztika és nyelv**](http://szamitogepesnyelveszet.blogspot.hu/2010/05/valoszinuseg-statisztika-es-nyelv.html) - nyelvészeti témájú R-es könyveket ajánlok ebben a posztban (ingyeneseket és fizetősöket egyaránt)

- [**Statisztikai túlélőkészlet**](http://szamitogepesnyelveszet.blogspot.hu/2010/04/statisztikai-tulelokeszlet.html) - mert az SVD mellett ez sem árt

- **Könyvek** - ajánlottunk pár könyvet már [itt](http://szamitogepesnyelveszet.blogspot.hu/2011/02/konyvismerteto-foundations-of.html), [itt](http://szamitogepesnyelveszet.blogspot.hu/2012/02/konyvismerteto-drew-conway-john-myles.html), [itt](http://szamitogepesnyelveszet.blogspot.hu/2011/03/konyvismerteto-statistical-analysis.html), és [itt](http://szamitogepesnyelveszet.blogspot.hu/2011/10/konyvismerteto-data-mining-with-rattle.html) olvashatod a posztokat
