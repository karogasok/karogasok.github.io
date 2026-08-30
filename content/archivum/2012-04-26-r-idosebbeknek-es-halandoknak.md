---
title: "R idősebbeknek és halandóknak"
date: 2012-04-26T04:00:00Z
publishDate: 2012-04-26T04:00:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/04/r-idosebbeknek-es-halandoknak.html"
regi_cimkek:
  - "R"
regi_cimkek_mind:
  - "R"
---

**Sokan írtak nekünk mostanában hogy elveszve érzik magukat az R nyelv elsajátítása során. Sajnos hiány van a kezdők számára íródott és a könyvek/tutorialok és a "magasabb" szintű irodalom között. Ezen a legtöbben úgy lépnek túl hogy mire túljutnak a bevezető műveken már szert tesznek pár ismerősre, bekapcsolódnak a nyelv köré szerveződött közösség életébe és másoktól sajátítja el a szükséges ismereteket. Hazánkban sajnos ez nem megy olyan könnyen, ezért most pár tippet adunk arra miként induljon el a kedves olvasó.**

Hogy mi merre miért, azt a  [R, de miért is használjam I.](http://szamitogepesnyelveszet.blogspot.com/2010/07/r-de-miert-is-hasznaljam-i.html) és [II.](http://szamitogepesnyelveszet.blogspot.com/2010/07/r-de-miert-is-hasznaljam-ii.html) posztokban már elmondtuk. Tegyük fel hogy  [Valószínűség, statisztika és nyelv](http://szamitogepesnyelveszet.blogspot.com/2010/05/valoszinuseg-statisztika-es-nyelv.html)ben felsorolt művek közül valamelyiken, vagy hasonló mélységű anyagokon már sikeresen végigment az olvasó. A nagy kérdés az hogyan is néz ki a worflow, hogyan dolgozunk akkor az R-rel. Mielőtt a lényegre térek, egy kis filozófiai eszmefuttatás következik amit nyugodtan kihagyhatsz.

Bo Cowgill sokat idézett mondása összegzi legjobban az R-t: "The best thing about R is that it was developed by statisticians. The worst thing about R is that... it was developed by statisticians." Mindenki fel tudja mondani a leckét, bizony nagy cégek is, mint pl. Google, Facebook stb. is használják az R-t, tehát komolyan kell venni. Ez igaz, de sokkal fontosabb kérdés hogy **hogyan és mire használják**. Mint számítógépes statisztikai nyelv bizonyos dolgokra van kihegyezve; spéci adatkezelés (pl. a vektor mint fő adatstruktúra), numerikus módszerek (igaz gyakran C/FORTRAN könyvtárakat wrapper-rel), grafika (vagy plotting). A statisztikai elemzésnek eszköze a programozási nyelv, a lényege annyi hogy a táblázatkezelőkkel vagy pl. az SPSS-sel ellenben sokkal rugalmasabb, jobban alakítható a problémához, gyorsabban frissül és a közösségnek köszönhetően remek támogatást is kapunk hozzá (ha jól tudunk kérdezni). A használati mód eredménye viszont hogy a munka "végterméke" gyakran ún. spagetti kód (Spaghetti code), ami annyit tesz hogy sokkal inkább ad hoc módon összedobott, egy-egy egyedi problémára koncentráló, nem optimalizált barkács mű. Szerintem ez nem baj, de ha komolyan akarjuk venni magunkat túl kell ezen lépnünk.

A kutatás, akár alkalmazott, akár elméleti, egyik lényeges eleme hogy megismételhető legyen. Habár gyakran egy egyedi problémát oldunk meg (pl. egyszerű regresszióval megtippelünk egy jövőbeli értéket), a tudományos vizsgálódás általános törvényszerűségeket, tendenciákat igyekszik felfedni és magyarázni. A kísérletek és mérések eredményei mögé szeretne látni a kutató, s mindezt szeretné kommunikálni (a nagyvilágnak, egy nagy impaktfaktorú periodikában, vagy a főnökei felé).  Első körben az a legegyszerűbb ha ezekre koncentrálunk.

**Workflow**

- **[ProjectTemplate](http://projecttemplate.net/)** - ez a kis könyvtár segít struktúrát adni adatelemzés projektjeidnek. Egy jó kutatás jól szervezett! Egy bevezető kurzuson, vagy egy intro könyvet feldolgozva még elmegy hogy egy könyvtárban legyenek az adataid és a kódod, de egy komoly elemzéshez ez már nem jó út. A ProjectTemplate leveszi a válladról annak terhét hogy magad tervezd meg a projekted könyvtárszerkezetét.

- **[git](http://git-scm.com/) és [github](https://github.com/)** - a verziókövetés is a projekt része, meg kell tanulni az alapokat. Persze ez csak mégy egy játékos amivel bonyolítod az életed, de érdemes rászánni az időt. A github akkor jön jól igazán ha másokkal dolgozol együtt egy feladaton.

- **Adatgondozás** - külön feladat, de ahogy egyre komolyabb dolgokkal foglalkozz úgy válik egyre fontosabbá hogy jók legyenek az adataid és jól legyenek tárolva/feldolgozva. A blogon [nem rég ajánlottuk a Natural Language Annotation for Machine Learning ](http://szamitogepesnyelveszet.blogspot.com/2012/04/book-review-natural-language-annotation.html)könyvet, más pedig tudtommal nincs a témában

**Adatok**

Igen, ha még nem volt elég, most még külön pontot is kap. Meg kell tanulnod hogyan tudsz dolgozni az adatokkal. Itt sincs sok lehetőség, [Phil Spector Data Manipulation with R](http://www.springer.com/statistics/computanional+statistics/book/978-0-387-74730-9) könyve igazítja el az érdeklődő gyerekeket. Van ezer meg egy tutorial, de azt kezdő nem nagyon értheti sajnos.

**Prezentálás**

- [**Sweave**](http://www.statistik.lmu.de/%7Eleisch/Sweave/) - Ugye ismered a LaTeX-et? Ha nem, Dávid írásai [itt](http://szamitogepesnyelveszet.blogspot.com/2011/07/texlatex-iras-es-feldolgozas-i.html) és [itt](http://szamitogepesnyelveszet.blogspot.com/2011/08/texlatex-iras-es-feldolgozas-ii.html) eligazítanak téged. A Sweave segít abban hogy a kódod és a készülő írásod (no meg prezentációd) "együtt legyen", a kódrészletek és ábrák szépen jelenjenek meg a szövegben stb. stb. Ezt tényleg nem olvasni, hanem csinálni kell.

- [**ggplot2**](http://had.co.nz/ggplot2/) - Meg kell valahogy jeleníteni az adatainkat, erre tök jók az alap plot függvények, de lássuk be esztétikailag kihívásokkal küszködnek és nem elég flexibilisek. A ggplot2 segítségével szép és jó grafikonokat, ábrákat készíthetünűk. A ggplot2 a [The Grammar of Graphics](http://www.springer.com/statistics/computanional+statistics/book/978-0-387-24544-7) könyvön alapul, de először inkább talán érdemes a [ggplot2: Elegant Graphics for Data Analysis](http://www.springer.com/statistics/computanional+statistics/book/978-0-387-98140-6)-t elolvasni.

**Programozás**

- **[SciViews](http://sciviews.org/)** - remek test framework-öt alkottak az R-hez

- **[RUnit](http://cran.r-project.org/web/packages/RUnit/index.html)** - kicsi, egyszerű unit test framework. Nekem különös kedvencem, mivel egy dologra koncentrál és azt el is végzi. Egy kis guglizással jó tutorialokat lehet találni. Maga a tesztelés nem áll távol a tudományos tevékenységtől, a filozófiailag járatosabb olvasóknak kvázi alkalmazott popperiánus falszifikációként jellemezhetem a folyamatot.

- [**Software for data Analysis: Programming with R**](http://www.springer.com/statistics/computanional+statistics/book/978-0-387-75935-7) - sajnos nagyon kevés könyv teszi rendben az alapokat az R körül. Hogy lehet hogy az R funkcionális de, vannak benne objektumok, imperatív stílusú iteratív kontroll, S3/S4 object system és egyéb nyalánkságok. Ezek előbb vagy utóbb releváns kérdésekké válnak az R-t tanulók számára, ez a kötet képes egyedül kielégítően megválaszolni ezeket.

Az említett könyvek megvásárolhatóak a [Számítógépes nyelvészet könyvespolcon](http://astore.amazon.com/szamitogepeny-20?_encoding=UTF8&node=19).
