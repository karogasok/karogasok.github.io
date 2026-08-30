---
title: "Könyvismertető - Mining the Social Web [frissítve]"
date: 2011-02-01T13:51:00.003Z
publishDate: 2011-02-01T13:51:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/02/konyvismerteto-mining-social-web.html"
regi_cimkek:
  - "könyvismertető"
  - "nltk"
  - "python"
regi_cimkek_mind:
  - "könyvismertető"
  - "közösségi média"
  - "nltk"
  - "python"
  - "social web"
---

**A közösségi média rengeteg adatot generál és szerencsére a különféle API-okon keresztül ezekhez bárki hozzáférhet. Azonban nem olyan egyszerű belevágni ezek elemzésébe. Matthew A. Russel könyve ehhez nyújt praktikus segítséget, rengeteg példával és jó minőségű kóddal támogatva mely saját elemzéseink kiindulópontjául is szolgálhat. Mindent összevetve a kötet remek, azonban bármennyire is próbál egyszerű lenni, nem árt ha az olvasó jártas a programozás terén (python), ismeri a legalapvetőbb számítógépes nyelvészeti alapfogalmakat (még jobb ha az nltk-t is), valamennyire ismeri a szemantikus webet és egy kicsit az átlagosnál többet tud a közösségi oldalakról.**

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/_SM9YHwWrX6M/TUgQdPTAR-I/AAAAAAAAAZ0/-lm7wF9tmiM/s200/mtsw.jpeg" rel="nofollow noopener">mtsw.jpeg</a></span>](http://3.bp.blogspot.com/_SM9YHwWrX6M/TUgQdPTAR-I/AAAAAAAAAZ0/-lm7wF9tmiM/s1600/mtsw.jpeg)

- [Matthew A. Russel: Mining the Social Web](http://oreil.ly/hobBaT)

- O'Reilly, 2011

- 360 oldal

A kötet az elemzéshez szükséges eszközök teljes tárházát felvonultatja, a vizualizációtól a számítógépes nyelvészeti eszközökig nagyon sok dologgal ismerkedhet meg az olvasó, azonban ez a sokszínűség egyáltalán nem tolakodó (viszont az előszóban ígért kezdő barátságot szerintem lehetetlenné teszi). A szerző remek érzékkel épp csak annyit mutat meg ezekből ami praktikusan kell, se többet se kevesebbet. Én ezt azért tartom fontosnak mert sokakat nem érdekelnek ezek a technikai részletek, vagy egyszerűen nincs elég idejük bíbelődni velük. Azonban ha valaki tényleg el akar mélyedni a közösségi média elemzésében, nem árt ha jobban utána jár a dolgoknak. A legjobb úgy tekinteni a kötetre mint a nagy sikerű [Programming Collective Intelligence](http://oreil.ly/fj8Pcs) és a [Programming the Semantic Web](http://oreil.ly/iiWD19) testvérére, nem árt továbbá az nltk könyvet (print verzióban [Natural Language Processing with Python](http://oreil.ly/gnDxnj), ingyenesen hozzáférhető verzióban simán [nltk könyv](http://bit.ly/hFpsPf) néven fut) és a Cookbook-ot ([Python Text Processing with NLTK Cookbook](http://bit.ly/gOz4vq) és szerzőjének [blogját](http://bit.ly/ew2ZgK))  hozzácsapni gyűjteményünkhöz ha komolyan foglalkoztat minket a terület. (És nem árt fontolóra venni a [MongoDB](http://www.mongodb.org/) vagy a [CouchDB](http://couchdb.apache.org/) elsajátítását, ami nem könnyű feladat, viszont ingyenesen hozzáférhető könyvek segítik ezt.)  
  
 Ahogy említettük a könyvhöz tartozik egy remek kód tár is amit a github-on érhetünk el ([itt](http://bit.ly/hsOwka)). Ez pedig ismét felveti az eszközök bőségét, az egyszerű kezdő bajba lehet a kód megszerzésével (szerencsére simán is letölthető, de mennyivel szebb git-tel, és mennyire jó gyakorlat ha saját munkánkat is verziókövetjük!). Habár a kód nagyon jó, nem minden esetben egyezik a kötetben található példa a repo-ból leszedettel, ami szintén gond lehet kezdőknek. Érdemes megjegyezni hogy a szerző felteszi hogy az olvasó *nix rendszeren dolgozik, és habár Windows-ra vagy OS X-re is lehet telepíteni mindent ami kell az egyes fejezetek végig vételéhez, ehhez nem árt ha kellően jártasak vagyunk oprendszerünk dolgaiban.  
  
 A könyv tíz fejezete logikusan épül egymásra. Aki az első bevezető fejezetet végig tudja követni, az hasonló dolgokra számíthat a következőkben. A második fejezetben a microformats nyelvekkel ismerkedhetünk meg, majd a legalapvetőbb és legősibb netes érintkezési formát a e-mailt elemezhetjük a harmadik fejezetben. A negyedik és ötödik fejezetben a Twitter elemzésében mélyedhetünk el (akit ez mélyebben érdekel, az a szerző hamarosan megjelenő [21 Recipes for Mining Twitter](http://oreil.ly/gEb67y) füzetét is hasznosnak fogja találni). Személyes kedvencem a hatodik fejezet melyben a LinkedIn hálózatok elemzésébe tekinthetünk be, itt a klaszter technika és a geográfiai elemzés nagyon jól sikerült. A hetedik fejezet a Google Buzz elemzésén keresztül mutatja be legalapvetőbb szövegelemzési technikákat (pl. kollokációk, bigrammok).  A nyolcadik fejezetben belecsap a szerző a lecsóba, és a blogok számítógépes nyelvészeti elemzésének vázlatát mutatja be. Habár nagyon jónak tartom, nem biztos hogy egy nltk pipeline építése követhető annak aki nem játszot legalább egy keveset az nltk-val. Hasonlóan a dokumentumok automatikus összefoglalása érdekes és hasznos dolog, viszont talán nem annyira egyértelmű háttértudás nélkül. A kilencedik fejezetben a Facebook adatok elemzésébe tekinthetünk bele, biztos vagyok abban hogy sokak számára ez a legérdekesebb rész, azonban itt sokkal inkább azon van a hangsúly hogy miképp vizualizálhatjuk a társadalmi hálókat. Azonban ha valaki eljutott eddig a fejezetig, akkor már nem lehet gond hogy saját maga elemezze az adatokat. Az utolsó fejezet egy kitekintés a szemantikus web irányában, ha valakit komolyan érdekel a közösségi média elemzése érdemes ezen a területen elmélyedni, amihez jó útmutató a kötet irodalomjegyzéke.  
  
**Frissítés**  
 Nem rég fedeztem fel a David Easley és Jon Kleinberg [Networks, Crowds, and Markets](http://bit.ly/hwBERQ) könyvét amely természetes kiegészítője az ismertetett kötetnek. A publikálás előtti végső vázlat szabadon elérhető [a könyv honlapján](http://bit.ly/fauXsZ). Érdemes a szerzők [Networks](http://bit.ly/hcrTFF) kurzusának leírást is megtekinteni.
