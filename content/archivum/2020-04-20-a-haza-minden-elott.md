---
title: "A -háza minden előtt"
slug: "a-haza-minden-elott"
date: 2020-04-20T07:34:09Z
publishDate: 2020-04-20T07:34:09Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "wordpress"
forras_cim: "Crow Intelligence blog"
canonical: "https://blog.crowintelligence.org/hu/2020/04/20/a-haza-minden-elott/"
regi_cimkek_mind:
  - "Altair"
  - "Hungarian langauage"
  - "Hungary"
  - "Municipalities"
  - "Python"
  - "QGIS"
---

A magyar nyelv olyan, mint egy kincsesbánya, amelynek használói temérdek új szót alkothatnak. Kreativitásért az elődeinknek sem kellett a szomszédba menniük, amikor elnevezték lakóhelyüket – akár egy elemű, akár több elemű névről legyen szó. Vizsgáljuk meg közelebbről az összetett szóból álló településneveket és térképezzük fel a leggyakoribb utótagokat.

Kutatásunkban arra a kérdésre kerestük a választ, hogy melyek a magyarországi településnevek leggyakoribb utótagjai. Tehát a 3177 magyarországi település közül csak az összetett szavakat (pl. Felsőzsolca) vizsgáltuk, az egyszerű szavakat (pl. Szikszó), beleértve a képzett szavakat (pl. Lőrinci), nem. A többszörösen összetett szavaknál (pl. Bükkszentkereszt) mindig az utolsó összetételi tagot (pl. kereszt) vettük figyelembe. A gépi feldolgozás megkönnyítése érdekében azokat az elemeket kizártuk, amelyek összetételi elemként és betűsorként is előfordultak. Ilyen volt például az -*ér,* amely *Nagyér* esetén utótag, viszont *Kelemér* esetén nem.

Térképre tettük Magyarország összes települését és feltüntettük az utótagját, illetve a lakosainak számát. Ha a település neve nem összetett szó, vagy, ha nemcsak összetétel, hanem karaktersor is lehet, az *Other* kategóriába soroltuk. Az alábbi interaktív térképen mind az utótagok mind a településnevek begépelve és listából is kereshetők. A keresés előtti eredeti állapotot a clear filter-rel állítható vissza. A térkép önálló linkként [itt](https://crow-intelligence.github.io/endings/index.html#2/47.3/19.3) érhető el.

[Beágyazott tartalom](https://crow-intelligence.github.io/endings/index.html#1/47/20)

Az utótagok azonosítása nem volt könnyű feladat, ugyanis nem állt rendelkezésünkre olyan utótag lista, amely Magyarország településneveit tartalmazza. Úgy döntöttünk tehát, hogy a listát mi magunk készítjük el. Ehhez nem kellett mást tennünk, csak átbogarásznunk Magyarország településneveit és minden egyes helységnévről eldöntenünk, hogy egyszerű vagy összetett szó-e. Ha a szó összetett szó volt, levágtuk a mai magyar beszélő által felismerhető legutolsó utótagot. A **mai** magyar beszélő perspektíváját nyelvész kollégáink kedvéért hangsúlyozzuk, hiszen természetesen vannak olyan szavak, amelyek történetileg összetett szavak, illetve összetételi tagok, viszont ma már az egyszerű földi halandók nem ismerik fel őket. Bár a legtöbb utótag értelmes magyar szó (pl. völgy), nem tartottuk feltételnek, hogy a szó szerepeljen a szótárban. Egyedüli szempont az volt, hogy világosan felismerhetőek legyenek a tagok a mai kor emberének (pl. Püspök + ladány).

Miután megkaptuk a 725 szóból álló utótag listánkat, megszámoltunk, mennyi település neve végződik az egyes szavakra és ezek mennyi ember lakóhelyét jelentik. Készítettünk egy listát, amely az utótagokat, azok előfordulását és a hozzájuk tartozó lakosok összegét tartalmazza. Íme:

[Google Docs](https://docs.google.com/spreadsheets/d/e/2PACX-1vQD_iae5zf6XgLi35H2C4YbLrtO2UMaA-aurve1XpHnHNzlHUaXYpcBDuEwgFlwgUKyetnh97LI5Sdh/pubhtml?widget=true&headers=false)

Az alábbi ábrán azt szemléltettük, hogyan alakul a top 40 utónév eloszlása. Könnyen leolvashatjuk a diagramról, hogy a *-háza* a leggyakoribb 66 előfordulással, amelyet a *-fa* és a *-falu* követ.

<span class="lost-media">Hiányzó kép: <a href="https://crowintelligence.org/wp-content/uploads/2020/04/barplot.png" rel="nofollow noopener">barplot.png</a></span>

Ha a következő térképen a közös utótagok területi eloszlását jobban megfigyeljük, nagy általánosságban megállapíthatjuk, hogy egy adott elnevezés nem kizárólagosan egy régióban jelenik meg. Elődeink tehát ugyanazt az utótagot földrajzi elhelyezkedéstől függetlenül Magyarország teljes területén előszeretettel választották lakhelyük elnevezésére. Azt azonban megfigyelhetjük, hogy vannak utótagok, amelyek az ország bizonyos részein koncentrálódnak. Például több -*vár* végződésű település van Nyugat-Magyarországon, mint keleten. Az alábbi térképen szemléltettük a leggyakoribb húsz végződést. Végződés alatt ebben az esetben nem egyszerű betűsort értünk, hanem utótagokat.

<span class="lost-media">Hiányzó kép: <a href="https://crowintelligence.org/wp-content/uploads/2020/04/municipality_endings-1.jpg" rel="nofollow noopener">municipality_endings-1.jpg</a></span>

### Adatok, kód

- Kód[ github](https://github.com/crow-intelligence/municipality_endings)-on.

- [Shapefiles](https://data2.openstreetmap.hu/hatarok/index.php?admin=8)
