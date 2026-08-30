---
title: "Könyvismertető: Reliable Reasoning - gépi tanulás mindenkinek"
date: 2011-07-14T14:40:00Z
publishDate: 2011-07-14T14:40:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/07/konyvismerteto-reliable-reasoning-gepi.html"
regi_cimkek:
  - "filozófia"
  - "gépi tanulás"
  - "könyvismertető"
  - "python"
regi_cimkek_mind:
  - "filozófia"
  - "gépi tanulás"
  - "könyvismertető"
  - "python"
---

**Manapság a gépi tanulás (leánykori nevén statisztikai tanuláselmélet) egyre elterjedtebb, érthető hát az igény arra hogy egy minnél közérthetőbb könyv segítségével ismerkedhessen meg alapfogalmaival a nagyérdemű. Nem szabad azonban összetéveszteni a bevezetést az ismeretterjesztéssel! Tudjuk hogy a matematikához (és a formális elméletekhez) nincs királyi út, mivel azonban a gépi tanulás már rég olyan területek ajtaján kopogtat mint a társadalomtudományok és a digitális bölcsészet szükség van egy könnyen emészthető bevezető könyvre. A most bemutatásra kerülő kötet ennek teljesen meg is felel, bónuszként pedig szabadon letölthető a nyomtatás előtti nyers verziója.**

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-TXXHoiGsrNY/Th7_J7Lfe_I/AAAAAAAAAgA/3yb1PSRTfUM/s1600/RR.jpg" rel="nofollow noopener">RR.jpg</a></span>](http://3.bp.blogspot.com/-TXXHoiGsrNY/Th7_J7Lfe_I/AAAAAAAAAgA/3yb1PSRTfUM/s1600/RR.jpg)

- **Gilbert Harman - Sanjeev Kulkarni: [Reliable Reasoning: Induction and Statistical Learning Theory](http://mitpress.mit.edu/catalog/item/default.asp?tid=11157&ttype=2)**

- **MIT Press, 2007**

- **114 oldal**

- **ingyenes, nyers verzió [ezen a linken](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.6171&rep=rep1&type=pdf) érhető el**

**Melyik verziót használjam?**

A nyers verzió és a könyv között nincs lényeges különbség, a nyomtatott verzióban javítottak pár hibát és sok helyen hosszabbak a magyarázatok valamint bőségesebb irodalomjegyzéket fűztek az egyes fejezetekhez a szerzők - akiknek ezek fontosak vegyék meg a könyvet, de tanuláshoz bőven elég a pdf verzió. Habár én nem láttam a Kindle kiadást, Enikő elmondása szerint "a képletek és ábrák néha idegesítően rossz minőségűek".

**Egy kis háttér a könyvhöz**

Sokak számára elsőre nem érthető magától hogy miért ír közösen könyvet (és tart közösen kurzust!) egy filozófus és egy villamosmérnök. Nos az ok nagyon egyszerű: a filozófia egyik központi problémája az indukció. A villamosmérnökök egy jelentős része manapság elkezdte megkülönböztetni magát a "klasszikus" ágazattól - hiszen pl. a jelfeldolgozás terén egyre jobban elválik a "hardveres" és az elméleti rész - és információmérnöknek nevezik magukat akik a jelfeldolgozás és információelmélet területén dolgoznak. A közös pont ezekben a tudományokban pedig az indukció, miképp következtethetünk az egyből a sokaságra és mennyire megbízhatók induktív módszereink .

Természetesen a fenti kérdésekkel foglalkozik a statisztika, ennek formálisabb megközelítése a számítógépes statisztika (computational statistics - tehát komputációs/számításelméleti valójában, ahogy a computational linguistics is), ennek algoritmikus vizsgálatát nevezzük statisztikai tanuláselméletnek, és ennek alkalmazott területét hívjuk gépi tanulásnak, de természetesen minden taxonómia esetleges, nincsenek éles határok és sokan szeretnek vitatkozni azon hogy mi micsoda ([ez a kis poszt](http://brenocon.com/blog/2008/12/statistics-vs-machine-learning-fight/) is megvilágítja hogy tkp mindegyik statisztika, csak marketing szempontból jobb kerülni ezt a nevet...) Habár idehaza nem divatos az analitkus filozófia, az angolszász világban azonban manapság nagyon elterjedt kutatási téma az indukció problémája és a statisztikai/valószínűségi elméletek előfeltevéseinek és hatásainak vizsgálata (hiszen egyre több dologban hagyatkozunk ilyen módszerekre, amiket egy ember sem képes teljesen felfogni, pláne kivitelezni, nem csoda ha nagy az érdeklődés).

**Röviden a tartalomról**

Az első fejezet a bemutatja a klasszikus "indukció problémáját" és kontextusba helyezi. Habár én nem értek egyet sok megállapításával (pl. nagyon érdekesen használja az érvelés [reasoning] fogalmát, mintha a két klasszikus, [Reasoning about Knowledge](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=8240) és [Reasoning about Uncertainty](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=9952) kimaradt volna a szerzőknek) nagyon alapos és követhető a szöveg, segít kontextusba helyezni a problémát és a későbbi fejezetek "filozofikusabb" részeihez is remekül kapcsolódik.

A második fejezet technikai megvilágításba helyezi az indukciót és bevezetést nyújt a [Vapnik-Chervonenkis](http://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory) elméltetbe. Érdemes elidőzni ezen a részen, mivel a VC elmélet a könyv magja, ezt tartják a szerzők központi elméletnek amiben az indukció problámája kezelhető. A maradék két fejezetben erre építve először visszakanyarodnak egy kicsit elméletibb irányba majd a [neurális hálók](http://en.wikipedia.org/wiki/Neural_network) és az ún. [support vector machine](http://en.wikipedia.org/wiki/Support_vector_machine) alkalmazott területei következnek.

**Hogyan tovább?**

Ha élvezted a könyvet, akkor két dolgod van

1. További komoly olvasmányokat ajánl neked a [Measuring Measures Learning about Machine Learning ](http://measuringmeasures.com/blog/2010/3/12/learning-about-machine-learning-2nd-ed.html)posztja. Érdemes végigolvasni és komolyan venni a tanácsait a matekkal kapcsolatban.

1. Ismerkedj meg a [scikits.learn](http://scikit-learn.sourceforge.net/) Python könyvtárral. Ez tkp. a gépi tanulás NLTK-ja, remek (habár még nem kész) tutorialokkal.
