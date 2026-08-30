---
title: "Mire jó a funkcionális programozás"
date: 2012-12-06T10:39:00.001Z
publishDate: 2012-12-06T10:39:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/12/mire-jo-funkcionalis-programozas.html"
regi_cimkek:
  - "funkcionális programozás"
regi_cimkek_mind:
  - "funkcionális programozás"
---

**Sokan úgy vannak a funkcionális programozással mint a big data-val; ízlelgetik, próbálgatják és foglalkoznak vele, mert mindenki más is ezt teszi. Alapvetően három dolog fokozta fel a paradigma iránti érdeklődést 1) a MapReduce-t a funkcionális paradigma ihlette 2) a statisztikai programozás és a gépi tanulás terén népszerű R nyelv és a mostanában különösen startupok körében elterjedt Clojure sikere 3) a párhuzamos feldolgozás elterjedése. A posztban megpróbálom körüljárni hogy tényleg jobb-e a funkcionális paradigma és hogy milyen feladatokra érdemes funkcionális nyelvet választani.**

Az első kérdésre - ti. hogy jobbak-e a funkcionális nyelvek - a válasz egész egyszerűen az hogy nem. Bővebben; se nem jobbak, se nem rosszabbak mint pl. az OO nyelvek. Ennek oka, hogy a jelenlegi Neumann-architektúrán **[Turing-ekvivalensek](http://en.wikipedia.org/wiki/Turing_completeness)**. Ezen nincs értelme vitatkozni, mivel bizonyított tény, hogy amit az egyik paradigmában meg tudunk oldani, azt a másikban is elérhetjük. Más lapra tartozik, hogy Backus híres **[Can Programming Be Liberated from the Neumann Style?](http://www.thocp.net/biographies/papers/backus_turingaward_lecture.pdf)** esszéjében megmutatta, hogy a jövőben más lesz a helyzet, de erre már harminc éve várunk és még jó ideig várnunk kell.

Peter Naur **[Programming as Theory Building](http://www.itu.dk/courses/SASU/F2010/files/Naur%20from%20Cockburn.pdf)** esszéje más oldalról közelíti meg a dolgot. Naur szerint a programozó munkája során externalizálja (külsővé teszi) és mások által használhatóvá teszi tudását. De miből áll ez a tudás? Egyrészt a programozó jártas kell hogy legyen a számítástudományban, másrészt jó adag általános intelligenciával is rendelkeznie kell hogy megértse a kapott feladatait. Elvben egy jó programozó mindent meg tud oldani, gyakorlatban specializálódás ment végbe a szakmában, ami továbbra is tart és csak fokozódni fog.

Aria Haghighi **[nem rég írt az ACM blogján](http://cacm.acm.org/blogs/blog-cacm/157645-a-funny-thing-happened-on-the-way-to-academia/fulltext)** arról, hogy miért hagyta ott rendkívül ígéretes akadémiai karrierjét és lett a Prismatic társalapítója. Haghighi saját bevallása szerint nem akarta életét egy egy részterület apró kis problémájának szentelni. Habár az NLP-ben szeretjük azt hinni hogy majd egyszer eljutunk a teljességhez, vagy a közelébe kerülünk, igazából a tudomány logikáját követve részterületek alakultak ki, mely kutatói elvannak a saját kis problémáikkal. Ez hatással van arra, hogy miképp jelenik meg az NLP az alkalmazott területeken. Egy termék fejlesztése során ha felmerülnek számítógépes nyelvészeti kérdések, akkor a fejlesztők egy palettáról válogatják össze a megoldásokat. Így az NLP a mellékes featur-ökbe szivárog be. Haghighi **[O'Reilly Radar-on megjelent írásában](http://strata.oreilly.com/2012/04/great-machine-learning-products.html)** megjegyzi, hogy az igazán érdekes problémákra nincs ilyen "leemelhető" válasz. Ha tényleg szeretnénk megoldani egy kérdést és a termékünket erre szánjuk, akkor holisztikusan kell gondolkodnunk!

Naur tézisét szerintem a legtöbben elfogadják. Adjuk ehhez hozzá Haghighi gondolatait is. Az NLP (és a gépi tanulás, továbbá valamennyi kutatás-vezérelt terület) esetében is azon van a hangsúly hogy a fejlesztő tudását szoftverbe tudja "önteni", s ha jó terméket akarunk, akkor a lehető legjobb szerszámot kell megtalálnuk ehhez. Az erősen formalizált tudományok esetében a legjobb szerszám egy funkcionális programozási nyelv, mivel ezek segítségével egy ismerős nyelven lehet kifejezni a formális elméleteket.

A párhuzamos feldolgozás terén valóban izgalmas dolgok történnek a funkcionális paradigmában. De itt is sokkal inkább arról van szó, hogy megfelelő absztrakciós eszköz áll egyes fejlesztők rendelkezésére. **[Pankratius és tsai](http://www.neverworkintheory.org/?p=375)** alapos összehasonlító kísérlet során arra jutottak hogy

> *Contrary to popular belief, the functional style does not lead to bad performance. Average Scala run-times are comparable to Java, lowest run-times are sometimes better, but Java scales better on parallel hardware. We confirm with statistical significance Scala’s claim that Scala code is more compact than Java code, but clearly refute other claims of Scala on lower programming effort and lower debugging effort.*

A megállapítás sokkal inkább az ún. generalista programozókra vonatkozik, akik egy software shopban készítenek a "beeső" ügyfeleknek különféle alkalmazásokat. Ilyenkor egy jó szaki dolga, hogy ügyfelével konzultálva a lehető legjobb szolgáltatást tudja nyújtani. Ilyen környezetben nem jár előnyökkel egy funkcionális nyelv használata.

A kutatás-intenzív termékfejlesztés során azonban a funkcionális nyelvek használata megkönnyíti a kutatók és a fejlesztők dolgát. A kutatóknak nem kell ún. throw away prototípusokkal bíbelődniük kedvenc nyelvükben, a fejlesztők nem kapnak agyvérzést amikor a prototípusok alapján kell valódi termékké formálniuk az ötleteket. Rövidül a fejlesztés idő, olcsóbbá válik a hibázás (ami a kutatás része) és csökken a kockázat (érdemes Paul deGrendis **[Clojure-powered Startups](http://www.infoq.com/presentations/Clojure-powered-Startups)** előadását megnézni a témában erről).
