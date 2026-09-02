---
title: "Chomsky, Norvig és a tudomány"
slug: "chomsky-norvig-es-tudomany"
date: 2011-05-28T11:34:00.002Z
publishDate: 2011-05-28T11:34:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/05/chomsky-norvig-es-tudomany.html"
regi_cimkek:
  - "Chomsky"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "Chomsky"
  - "Norvig"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
---

**Peter Norvig a Google tudományos guruja, a legszélesebb körben használt mesterséges intelligencia tankönyv szerzője, a NASA volt kutatója, a Lisp közösség csodált vezéregyénisége tegnap úgy érezte [hozzá kell szólnia](http://norvig.com/chomsky.html) Chomsky megjegyzéséhez, amiről már a [Chomsky és a statisztika](http://szamitogepesnyelveszet.blogspot.com/2011/05/vissza-jovobe-avagy-miert-veszitett.html) írásunkban szóltunk. Norvig érvei súlyosak, és bevallom nem akarom mentegetni Chomsky megjegyzését - amit nem is tudok hova tenni, én sokkal inkább úgy gondolom hogy a cikk írója nem értett valamit, vagy az öreg unta már a konferenciázgatást - de úgy gondolom hogy csúsztatás figyelhető meg az érvekben.**

**Tiszta tudományok vs alkalmazott tudományok**

Talán nem árt ott kezdeni hogy ki is Peter Norvig. No nem a CV-jét fogjuk itt megimételni, azt bárki megkeresheti a neten. Sokkal inkább érdekes hogy pályája kezdetén még az ún szabály-alapú módszerek voltak elterjedve, nem csoda hogy ő is ezekkel kezdett foglalkozni anno, s ezen a területen ért el nagyon nagy sikereket. Paradigms of Artificaial Intelligence könyve 1992-ben jelent meg, azonban máig meghatározó minden Lisp programozó és mesterséges intelligenciával foglalkozó szakember számára. Norvig nem az a szobatudós fajta, elég megnézni a róla készült videókat, vagy interjúkat és láthatjuk hogy egy laza, hawaii inges arccal állunk szembe. A kilencvenes évek elején/közepén elkezdtek hódítani a statisztikai módszerek és pont ebben az időben Norvig kilép az akadémia világából és az ipar felé fordul (már a PAIP-on is mint a Sun Microsystems kutatója szerepel). A [Coders at Work](http://books.google.com/books?id=nneBa6-mWfgC&printsec=frontcover&dq=coders+at+work&hl=en&ei=18DgTfuTBI_s-gb539DaBg&sa=X&oi=book_result&ct=result&resnum=1&ved=0CCkQ6AEwAA#v=onepage&q&f=false) kötetben nagyon érdekesen nyilatkozik erről az időszakról. Az akadémiai közegben egy probléma véglelges megoldását, de legalábbis az ahhoz vezető út egy darabját kell megtalálni, ellenben az ipar azzonnali ám nem tökéletes, hanem elfogadható megoldást követel.

A fenti szemléletmód és a statisztikai módszerek térnyerés változtatta meg Norvig gondolkodását - szerintem legalábbis magyarázhatjuk utólag ezzel a történteket. Vegyünk egy párhuzamot hogy jobban lássuk mi történt! Norvig közeli munkatársa, [Fernando Pereira](http://www.cis.upenn.edu/%7Epereira/) a prolog programozó körében népszerű Prolog and Natural Language Analysis könyv egyik szerzője volt és nagyon sokáig a keményvonalas szabály-alapú megközelítés híve volt, majd később Norvig-gal közösen jegyezte az [Unreasonable Effectiveness of Data](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en//pubs/archive/35179.pdf)-t, ill. ő írta a [Formal grammar and information theory: together again?](http://www.cis.upenn.edu/%7Epereira/papers/rsoc.pdf) című "cult paper"-t is.

Nyilván való hogy valami történt amiért ilyen nagyon okos emberek elfordultak egy irányzattól. A fenti sztori lényege éppen azt a célt szolgálja hogy bemutassa ennek legfőbb okát; ti. hogy az alkalmazott tudományok és az ipari felhasználás felé fordultak. Mit is mond Norvig ellenben:

> And while it may seem crass and anti-intellectual to consider a financial measure of success, it is worth noting that the intellectual [offspring](http://en.wikipedia.org/wiki/Telecommunication) of Shannon's theory create several trillion dollars of revenue each year, while the [offspring](http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=chomsky&x=0&y=0) of Chomsky's theories generate well under a billion.

Ez nem csak az ő véleménye, a vita régóta folyik, [Jeremy Kahn is hasonló érveket használt](http://trochee.net/2011/05/broadsheets-from-the-empirical-underground/).

> Among the empirical linguists (and the physicists!), most:

> - work with machinery that costs a lot of money

> - are friendly with engineers, including industry contractors

> - get paid relatively well

> - find work outside the academy easily

> - are best rewarded when their research “*just works*“

Azt hiszem remekül látszik a különbség! A tudomány és a mérnöki munka sokban hasonlít, de nagyon különbözik is. Egy adott cél elérése, a lehető legtökéletesebb eredménnyel adott korlátok (pl. idő, pénz, szakértelem, technikai adottságok, stb) mellett. Ez nagyon hasznos dolog, és nem lehet teljesen elválasztani a tudománytól és nem szabad eltekintenünk a köztük lévő interakcióktól, de tévedés összekeverni a tudományos kutatással.

Vegyük ellenben a matematikát vagy a logikát. Mennyire lenne elfogadható ha egy elméletük "csak működne"? Ha az integrálszámítás csak az esetek 95%-ban adna helyes eredményt, vagy ha egy statisztikai tétel bizonyítása helyett azt mondanánk hogy nagy valószínűséggel helyes. A tudományoknak van egy "tiszta" formája, amit nem fizetnek persze meg és nem adnak rögtön válaszokat de attól még hasznosak. Ezeknek bizony része hogy rákérdeznek a nyilvánvalóra, vagy hogy néha a laikusok szerint teljesen hülyeségeket beszélnek.

Valamikor a XIX. század vége felé egy fiatal matematikus azon gondolkodott hogy tényleg biztosak lehetünk-e matematikai tudásunkban. Később mások is el kezdtek ezen agyalni. Frege megalkotta a modern, klasszikus logikát, Russel kapcsolatba lépett vele és felfedezte a híres paradoxont, Hilbert megalkotta híres kutatási programját, Gödel felfedezte híres (és gyakran félre értett) tételét. Turing és Church lefektette a számításelmélet alapjait, majd a második világháborúban ezek a zavaros elméletek hirtelen nagyon fontosak lettek, a rejtjelek feltörésétől az utánpótlási vonalak megszervezéséig mindenre használták a korai számítógépeket és napjainkban nem is tudnánk nélkülük élni.

Nem szabad elfelejtenünk hogy Chomsky ennek a hagyománynak a folytatója! Az ő elődei már segítettek megnyerni legalább egy háborút és bizony évi több milliárd dolláros profitot termelnek - csak éppen másoknak.

**A kultúra fogalmával élni és visszaélni**

Norvig Leo Breiman Statistical Modeling: Two Cultures írását hozza fel példának arra hogy vannak jó és rossz statisztikusok, a rosszak szűk látókörűek és mint egy skinneriánus csak leírják az input-output mintákat. Ezzel ellentétben vannak a jók akik ún algoritmikus modellekkel dolgoznak - ez lenne a statisztikai tanuláselmélet (no meg a gépi tanulás is). Ez lenne amit Chomsky nem szeret és nem fogad el, mivel érthetetlen. Szerintem nem így van, hiszen [Skinner kritikájában](http://www.chomsky.info/articles/1967----.htm) éppen az első típusú érevlést szedte darabjaira az öreg.

Az algoritmikus elméletek nagyon jók és szépek és Norvig szerint kicsit nevetséges azt kérdezgetni hogy de miért is működnek jól, ha már egyszer jól működnek az elégséges bizonyíték kell hogy legyen helyességükre nézve. De valóban így áll ez a dolog? Valóban érvénytelen kérdést tesz fel Chomsky és tényleg akkora hülyeség egy elméleten számon kérni hogy érthető (értsd belátható, átlátható és levezethető legyen)?

Tény és való két kultúra létezik a statisztikusok körében. Egy kicsit sarkítva, vannak akik tanultak kalkulust és talán még diszkrét matekot, meg egy kis számításelméletet algoritmusokkal megspékelve, meg azok akik csak statisztikát és kutatásmódszertant (társadalomtudósok, és igen gyakran nyelvészek, még gyakrabban közgazdászok, pszichológusok tartoznak ide). Azonban itt Norvig megint csúsztat! Az algoritmikus tanuláselmélet egyrészt leír egy jelenséget, jó egy-egy modell megalkotására, másrészt viszont maga is lehet elemzés tárgya, mégpedig szép diszkrét elemzést végezhetünk rajta!

Nem kell messzire merészkednünk, Aumann Interactive epistemology [I](http://www.ma.huji.ac.il/raumann/pdf/Interactive%20epistemology1.pdf) és [II](http://www.ma.huji.ac.il/raumann/pdf/Interactive%20epistemology2.pdf) cikke éppen ezt mutatja be! Gierasimczuk kutatásai pedig pontosan a tanuláselmélet empisztemológiai oldalával foglalkoznak (pl. [Bridging learning theory and dynamic epistemic logic](http://staff.science.uva.nl/%7Egrossi/DyLoPro/Material/gierasimczuk09bridging.pdf)). Ezen kutatások lényege dióhéjban annyi hogy egy dolog leírni valamit, más dolog megvizsgálni hogy miképp működik a rendszer. A legjobb analógiát a játékelmélet adja, ami megmutatja a legjobb stratégiát és segít döntést hozni, stb. Az episztemikus logika viszont arra ad választ hogy miképp változik a "játékosok" tudása, milyen feltételek mellett ismerhet meg egy adott információt, adhatja az tovább stb.

Így elérkezünk a dolog végére - Chomskyt nyilván való hogy nem is érdeklik az alkalmazhatóság keretei. Őt bizony az episztemológiai keret izgatja és egy igen izgalmas és sokak által használhatónak talált keretet sikerült megalkotnia. Azonban ellenben sok más kutatóval ó nem állítja hogy megtalálta volna az igazságot! A minimalista program nevében is utal arra hogy egy kutatási program, nem pedig kőbevésett tan - ellenben a gyakran nagyon élesen fogalmazó ellenoldallal ő tényleg tudja és érti a Popperi tudományfelfogást...

A kultúra fogalmával illene egy kicsit visszafogottabban bánnia a sikeres kutatónak! Ha már úgy érzi hogy nyert, akkor nem lenne elegánsabb szó nélkül hagyni a dolgot? Chomsky elkapott és talán félreértett megjegyzése és pár korai (ötvenes és hatvanas évekbeli) érve még mindig nagy ellenkezést vált ki, közben Noam meg elvan magának, teszi a dolgát és ahogy sokan mások a jövő nemzedékeire bízza mit kezd majd alapkutatásaival...
