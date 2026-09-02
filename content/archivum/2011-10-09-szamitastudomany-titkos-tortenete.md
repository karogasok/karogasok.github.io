---
title: "A számítástudomány \"titkos\" története dióhéjban"
slug: "szamitastudomany-titkos-tortenete"
date: 2011-10-09T16:32:00.002Z
publishDate: 2011-10-09T16:32:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/10/szamitastudomany-titkos-tortenete.html"
regi_cimkek:
  - "Turing"
regi_cimkek_mind:
  - "Church"
  - "Frege"
  - "Turing"
  - "számítástudomány"
  - "titkos történet"
---

**A címet Steve Blank [poszt-sorozatától](http://steveblank.com/category/secret-history-of-silicon-valley/) és [előadásától](http://steveblank.com/secret-history/) loptam előre megfontolt szándékkal. Blank zseniálisan meséli el miképp jelent meg a vállalkozói kultúra a Szilícium-völgyben, hogyan működött együtt a tudományos világ az üzleti élet és a biztonságpolitika. Azonban ez a történetnek csak az egyik fele. A 19. század vége felé valami egészen forradalmi történt, olyan ami megváltoztatta a világot mivel a számítógépek megalkotásához és a komputációs modellezés megjelenéséhez vezetett.**

Walder [Proofs Are Programs](http://bit.ly/mx23Ie) esszéjében írja:

> For my money, Gentzen’s natural deduction and Church’s lambda calculus are on a par with Einstein’s relativity and Dirac’s quantum physics for elegance and insight.

A 19. századra a matematika megalapozása központi kérdéssé vált. Ebben a légkörben egy fiatal matematikus, aki nem mellesleg rajongott Kantért, megalkotta Begriffsschrift (azaz Fogalomírás) című művét, amivel nem kisebb tettet ért el mint hogy kimozdította az Arisztotelész óta szinte mozdulatlan logikát évezredes szendergéséből. Persze szinte visszhangtalan marad műve, de akadtak páran akik felismerték hogy történt valami. Frege jelölésmódja habár nagyon intuitív, szinte kezelhetetlen (és kinyomtathatatlan) de mégis magával ragadó. Sikerül túllépnie a szillogizmusokon és egy elsőrendű nyelvet alkotnia ami tkp. a mai klasszikus logika kalkulusa. A Függvény és fogalom című tanulmányában már egy informális szemantikát is ad elképzeléseihez, amit végül a Jelentés és jelöletben fejt ki teljesen. A matematikai függvény fogalmát általánosítva vezeti be a predikátum és argumentum fogalmakat, ezzel ki is jelölve a modern, halmazelméleti szemantika irányát. Később az Aritmetika alaptörvényeinek írása során Russel derít fényt a róla elnevezett paradoxonra. Azonban ez nem temeti maga alá az új tudományt, hanem a későbbi típuselméleti megközelítések magvát jelenti.

A Russel paradoxon  is arra hívja fel a figyelmet hogy jobban kell koncentrálni a matematika alapjaira. Az aritmetika alapjaiban Frege egy sokkal olvasmányosabb formában veti fel a megalapozás kérdését, és kötelezi el magát a logicizmus mellett. Ez az irányzat minden matematikai alapfogalmat szeretne logikailag egzakt formában leírni. Frege kísérlete a halmazok számosságából kiindulva próbálja az aritmetikát megalapozni (mint később kiderült nem is volt ez egy elhibázott irány). Cantor naiv halmazelméletében is gondokat okoz azonban Russel paradoxona, és nagy erőket kell bevetni hogy ne űzettessenek ki a paradicsomból a matematikusok, de szerencsére sikerül megvédeni ezt a terepet.

Hilbert Fregevel ellenben egy formalista programmal állt elő; miért kellene interpretálnunk egyáltalán formális elméleteinket, legyen elég annyi hogy egy adott szabályrendszer kijelöli az érvényes levezetéseket, tök mindegy hogy narancsokon, geometriai pontokon értelmezzük azokat. Gentzen egy ilyen formális rendszert adott meg, egy kalkulust ami viszont remekül egybecseng intuíciónkkal és akár egy informális interpretációját is adhatjuk.

Gödel tételeit lassan mindenki idézi és lassan csak reméljük hogy legalább minden második ráhivatkozó ember érti legalább a lényegét: egy jól összerakott, ellentmondásoktól mentes formális rendszerben nem vezethetünk le minden igaz állítást. Attól függ honnét nézzük, van aki szereti kiemelni hogy akkor akadnak olyan mondatok melyek igazak de nem levezethetőek, másokat viszont az érdekel hogy ami igaz és levezethető, az "automatikusan", pusztán pár viszonylag egyszerű szabály követésével levezethetőek. Hilbert vetette fel az ún. eldöntés problémát (Entscheidungsproblem): ha adott egy formális nyelv és egy (matematikai) állítás, megadható-e egy olyan eljárás ami megadja igazságtartalmukat (azaz hogy levezethető-e vagy sem). Alonzo Church és Alan Turing egymástól függetlenül válaszolták meg a kérdést, Church verzióját negatív válasznak is szokták nevezni, Turing (amúgy Kleene munkáira alapozott) válaszát pedig pozitívnak (vagy általánosnak) szokták nevezni. Az eszköz ami "képes dönteni" egy elméleti konstruktum, a Turing gép. A pozitív válasz, annyiban pozitív hogy ha eldönthető egy állítás, akkor egy Turing gép képes azt eldönteni.

Turing el is utazott az USA-ba hogy Church mellett töltsön egy kis időd (1936 és 1938 között) ahol a kriptográfiával és a számítástudomány mérnök oldalával is megismerkedett. Nem sokkal visszaérkezése után kitört az második világháború, a lengyel tudósok munkáira és szerencsésen elfogott Engima rejtjelező gépekre alapozva a brit kormány létrehozta Bletchley Parkban a Rejtjelfejtő Iskolát, ahol Turing (és társai) egy nagyon gyakorlati problémával találta szembe magát. A megoldáshoz pedig az eldöntéselmélet megoldásához használt gépét valósította meg, hogy egy ma nagyon divatos algoritmikus gépi tanulási problémát oldjon meg. De akkor még nem volt divat nagy neveket adni mindennek, simán matematika névvel illeték az egészet :D

> [...] in the business of searching through the 26

> <sup><small>3</small></sup>

> possible rotor positions, no improvement was possible on serial trial using the equivalent of moving Enigma rotors, so that improvements rested on having ever faster, more reliable machines produced in larger numbers. For the question of the choice of rotors and their order, however, which was particularly relevant for the Naval Enigma problem, Turing developed a method called 'Banburismus' which, particularly in 1941, much improved upon the simple trial of the possibilities. This method rested on the logical details of the turnover positions of the different rotors, but also on assessing the statistical identification of likely 'depths' — two different stretches of message, both sent on the same Enigma settings. For detecting depths objectively, giving a reliable probability measure to them, Turing developed a theory of Bayesian inference. The most striking feature of his theory was his measurement of the weight of evidence by the logarithm of conditional probabilities. This was essentially the same as Shannon's measure of information, developed at the same time. This theory was developed into sophisticated methodology (Good 1979, 2000). Whilst the logical principle of the Bombe, and its amazingly effective application, was perhaps Turing's most brilliant single idea, his statistical techniques were more general and far-reaching. In particular, they were also applied to the quite different Lorenz cipher system employed by Germany for high-level strategic messages. Thus it was Turing's theory of probability estimation that underlay the methods mechanised by the large electronic 'Colossus' built in 1943-45 to decipher this type of traffic. (Andrew Hodges: [The Military Use of Alan Turing](http://www.turing.org.uk/publications/mathswar1.html))

A háború végeztével a lassan megkezdődött a számítógépek egyre szélesebb, nem csupán katonai alkalmazása. Az ötvenes évekre a mai ismert területek előfutárai is megjelennek, az első mesterséges intelligencia konferenciát is megszervezik, színre lép Chomsky, neurális hálókkal és gépi tanulással kísérletezgetnek sok helyen.

Az egyik első, és máig is aktívan fejlesztett nyelv a Lisp Turing és Churhc ötleteire épült - erről Paul Graham  [The Roots of Lisp](http://www.paulgraham.com/rootsoflisp.html) esszéjéből többet is megtudhat a kedves olvasó - ami később a funkcionális paradigmát alapozta meg. Napjaink "hipster" nyelvei is mint az R, Haskell és Clojure (Incanter) a Lisp hagyományait követik (l. bővebben [Back To The Future: Lisp as a Base for Statistical Computing](http://www.stat.auckland.ac.nz/%7Eihaka/downloads/Compstat-2008.pdf)).

Az elektronika fejlődése és a Szilícium-völgyben kialakult startup kultúra egyszer csak összetalálkozott és a kezdeti próbálkozások felgyorsultak, majd napjainkra átformálták világunkat. Természetesen ez azzal is jár hogy a szakosodás során egyre kevesebb ember látja összefüggőnek a különböző területeket, napjaink adattudomány-őrülete pedig gyakran eredményezi azt hogy sokan elfelejtik hogy alapvetően Turing Colossus-át építjük újra nap mint nap, a statisztikai elemzés nem mellőzheti a matematikai-logikai alapokat, nincs semmi ellentét.

Ennyi a mese dióhéjban. Ahogy időm engedi szeretném jobban kifejteni a következőket:

- a matematika krízise és kiútkeresése

- Frege szerepe és a modern analitikus filozófia megjelenése

- a Bécsi Kör és a Prágai Kör megjelenése, mint ugyanannak a problémának a bölcseleti vonulata

- az eldöntésprobléma és Turing gépek

- az Enigma

- a mesterséges intelligencia megjelenése

- a mesterséges intelligencia krízise

- Charniak és a statisztikai megközelítés megjelenése

- a két kultúra (statisztikai elemzés vs algoritmikus modellezés)

- tudományfilozófia/tudományszociológia avagy miért kell átnevezni a statisztikát, logikát, matematikát, nyelvészetet stb hogy eladható legyen

Akinek megjegyzése, észrevétele van, vagy úgy érzi megírná valamelyik részt helyettem, esetleg írna nekünk valamit ami nincs a listán de ide passzol, az kérem vegye fel velünk a kapcsolatot.
