---
title: "Könyvismertető: Clojure in Action"
date: 2011-12-30T20:36:00.003Z
publishDate: 2011-12-30T20:36:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/12/konyvismerteto-clojure-in-action.html"
regi_cimkek:
  - "Clojure"
  - "könyvismertető"
  - "lisp"
regi_cimkek_mind:
  - "Clojure"
  - "Java"
  - "könyvismertető"
  - "lisp"
  - "programozás"
---

**Az elmúlt pár évben egyértelműen megnőtt az érdeklődés a funkcionális programozási nyelvek iránt és ez összekapcsolódott a JVM nyelvek körüli felhajtással is. Míg a Marin Odersky vezetésével az EPFL-en kifejlesztett Scala egy alapvetően objektum orientált nyelv ami magába olvasztja a funkcionális paradigma javát, a Clojure visszatért a második legöregebb nyelv, a Lisp, által követett nem tisztán funkcionális stílushoz. Habár a Scala olyan nagy ágyúknál van használatban mint a Twitter, a Wordnik vagy az Uberblic, a [FlightCaster](http://flightcaster.com/) (és Bradford Cross legendás, már megszűnt Measuring Measures blogja) és a [Factual](http://www.factual.com/) sikerei bebizonyították hogy a Clojure kifejezetten alkalmas a napjainkban meghatározó vonalat képviselő ún. research driven data startupok problémáinak megoldására. A kiadók persze próbálják meglovagolni a fokozódó érdeklődést több-kevesebb sikerrel, azonban ez nem könnyű egy JVM nyelv esetében sem. A Clojure közelébe kétféle ember kerül általában, Java vagy Lisp (vagy más funkcionális nyelv iránt érdeklődő) programozó. Vitathatatlan tény hogy a Java háttérrel rendelkezők vannak többségben, őket remekül ki is szolgálják az eddig megjelent könyvek, ellenben Rathore olyan könyvvel ajándékozta meg a közönséget amit a Lisperek is haszonnal forgathatnak.**

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-wAo-OWPhY3Q/Tv4hkAJ84wI/AAAAAAAAAow/0MmjWBTJw8Y/s200/clinaction.jpeg" rel="nofollow noopener">clinaction.jpeg</a></span>](http://1.bp.blogspot.com/-wAo-OWPhY3Q/Tv4hkAJ84wI/AAAAAAAAAow/0MmjWBTJw8Y/s1600/clinaction.jpeg)

- **Amit Rathore: Clojure in Action**

- **Manning Publications, 2011**

- **432 oldal**

- **[a kiadó oldala a könyvhöz](http://www.manning.com/rathore/)**

Nehéz belőni kik forgathatják haszonnal a könyvet. A Clojure nem kezdőknek való, a fejlesztői környezet tisztességes beállítása is kemény feladat elsőre. Továbbá általános probléma hogy a programozási könyvek előszeretettel elfeledkeznek a dolog gyakorlati oldaláról ti. a nyelv apró nüanszainak ismertetésére koncentrálnak ahelyett hogy átfogó képet adnának az adott nyelven folyó munkafolyamatnak (tesztelés, projekt automatizálás, IDE integráció stb.). Így nem elég hogy a funkcionális paradigmával és/vagy a JVM-mel kell egyszerre ismerkedni, valahogy össze kell szedegetni a morzsákat arról is hogy hogyan dolgozunk Clojure-rel (pl. az emacs, slime, leiningen hármas). Így én első sorban azoknak ajánlom a könyvet akik már valamennyire kiismerik magukat ezen a téren, ismerik valamennyire a Java-t (minimális tapasztalat elengedhetetlen, én pl. kb. értem valamennyire, de a generics és collections témáknál feladtam) van némi programozási tapasztalatuk (akár Javaban, vagy más OO nyelvben) és foglalkoztak már funkcionális programozással (a Common Lisp ismerete előny, a Scheme/Racket majdnem annyira jó, a Haskell elmegy). Továbbá kellő érdeklődés és nagy adag kitartás kell még - senki ne várja hogy hamar végez a könyvvel, vagy hogy nem kell Google-t használnia, kiegészítő információkat beszereznie. Szintén kellő elszántság szükségeltetik saját mini projektek kiötléséhez, mivel feladatok nincsenek a kötetben.

Akik erős Java háttérrel rendelkeznek, azoknak ajánlom Stuart Halloway (a nyelv atyja) [Programming Clojure](http://www.amazon.com/Programming-Clojure-Pragmatic-Programmers-Halloway/dp/1934356336/ref=sr_1_4?ie=UTF8&qid=1325272800&sr=8-4) könyvét inkább. VanderHart és Sierra [Practical Clojure](http://www.amazon.com/Practical-Clojure-Experts-Voice-Source/dp/1430272317/ref=sr_1_6?ie=UTF8&qid=1325272800&sr=8-6) kötete nagyon jó és alapos, de nem annyira mély mint a Clojure in Action (tipp; ha nagyon nem érti az olvasó Rathore-t, akkor előtanulmánynak ez a legjobb). Aki már ismeri a Clojure-t, az Fogus és Houser [The Joy of Clojure](http://www.amazon.com/Joy-Clojure-Thinking-Way/dp/1935182641/ref=sr_1_1?ie=UTF8&qid=1325272800&sr=8-1)-ét jobban kamatoztathatja.

Ennyi felvezetés után nézzük hogyan is épül fel a kötet. A két rész, Getting Started és Getting Real, tizenöt fejezetet tartalmaz. Az első megpróbálja a kettős eredetet körüljárni, ami nem könnyű feladat, de kb. megoldotta szerző. A második fejezet egy Clojure gyorstalpaló, nem hiszem hogy sokat mond annak aki még nem találkozott Lisp-el. A buli ezek után viszont elkezdődik. A harmadik fejezet (Building blocks of Clojure) a függvények, namespaces, scope jegyében telik, a negyedik az ún. multimethodsok világába vezet minket be (ami a polimorfizmus egyik válfaja). Az ötödik fejezet a Java interoperabilitással foglalkozik, ami a nyelv igazi előnye - minden rendes Java könyvtárat használhatunk Clojure-ben! A hatodik fejezet a konkurens programozásról szól számomra meglepően rövid, különösen annak tükrében hogy a Clojure-ben megvalósított verziót sokan dicsérik. A hetedik fejezettel zárul az első rész, nem csoda hogy ez amolyan felvezető a makrókról amik elengedhetetlenek a terület specifikus nyelvekhez.

A második részben gyakorlati és haladóbb témákkal találkozhatunk. Rögtön teszt vezérelt fejlesztéssel indít a nyolcadik fejezet, majd az SQL és noSQL adatbázisokkal való együttműködésről kapunk hasznos információkat. A tizedik fejezet a weprogramozás alapjaival, a tizenegyedik pedig a skálázhatósággal foglalkozik. Talán nem véletlen hogy az adatfeldolgozás külön fejezetbe került. Számomra meglepő hogy a tizenharmadik fejezetig nem kerülnek elő a haladóbb funkcionális fogalmak, mint a magasabb rendű és curry-zett függvények. Ezután egy kis típuselmélet következik, hiszen a Java-val ellentétben a Clojure dinamikus típusokkal dolgozik (de "bekapcsolható" a típus rendszer). Zárásképpen a makrók és a domain specifikus nyelvek kerülnek elő ismét.

A könyv nagyon informatív - néhol talán túlságosan is - de a nyelvezete néha szerintem dagályos. Amennyire örültem hogy helyet kaptak benne gyakorlati kérdések, annyira hiányoltam hogy valamennyire bemutassa a Clojure workflow-t végre valaki. Kezdő lépésnek remek, különösen azoknak akik nem Java guruk.
