---
title: "Scheme - királyi út a funkcionális programozás felé"
slug: "scheme-kiralyi-ut-funkcionalis"
date: 2012-11-19T16:33:00.001Z
publishDate: 2012-11-19T16:33:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/11/scheme-kiralyi-ut-funkcionalis.html"
regi_cimkek:
  - "funkcionális programozás"
regi_cimkek_mind:
  - "funkcionális programozás"
  - "scheme"
---

**Szerencsére egyre többen érdeklődnek a funkcionális nyelvek iránt. Sokkal sajnálatosabb hogy sokan eltántorodnak a kezdeti lelkesedés után. Sok nyelvész és logikus számára életük első programozási nyelve a Haskell manapság, nekik nem okoz gondot a régi szokások levetkőzése, ellenben a komolyabb feladatok (vagy az egész egyszerű I/O) estén sokan elakadnak. Szoftverfejlesztők általában az Erlang vagy a Clojure mellett teszik le a garast, de gyakran szembesülnek azzal hogy ezen közösségekben divat régi Lisp és Prolog könyveket ajánlgatni. Sokkal egyszerűbb ha nem rögtön a divatos nyelvekkel ismerkedünk meg, hanem a Scheme nyelvvel töltünk el egy kis időt. A nyelvek változnak, a mögöttes elvek azonban nem, érdemesebb először ezeket megtanulni.**

**1. Az alapok**

- [Simply Scheme: Introducing Computer Science](http://www.eecs.berkeley.edu/~bh/ss-toc2.html) - A legjobb könyv amivel elkezdheti valaki a programozás és/vagy a funkcionális programozás tanulását. Remekül szemlélteti az alapfogalmakat és sok-sok érdekes feladattal foglalkoztatja az olvasót. Nem csak a programozás terén kezdőknek ajánlom, hanem mindenkinek aki nem rendelkezik több éves tapasztalattal.

- [The Little Schemer](http://www.ccs.neu.edu/home/matthias/BTLS/) -Zseniális könyv, amely példákon keresztül mutatja be a funkcionális programozás főbb technikáit. Továbbá megtudhatja belőle az olvasó hogy az Y-combinator nem csak egy startup program :D Nagyon kezdőbarát, érdemes többször elolvasni! Figyelem, a szerzők már az előszóban leszögezik, hogy attól senki sem válik programozóvá hogy elolvassa a könyvet!

- [The Seasoned Schemer ](http://www.ccs.neu.edu/home/matthias/BTSS/)-A fenti könyv folytatása, szépen tovább építi az alapokat.

- [How to Design Programs](http://www.htdp.org/) - ingyenesen elérhető könyv, mely nagyon gyakorlat orientált. Célja a programfejlesztés logikájának bemutatása nem műszaki/tudományos érdeklődésű olvasók számára. A kötethez készül speciális Scheme implementáció nőtte ki magát a [Racket ](http://www.racket-lang.org/)nyelvvé, mely annak ellenére hogy nem szabvány Scheme, a legelterjedtebb ma a Schemerek körében.

**2. A klasszikusok**

- [Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/) - A "köznyelvben" csak SICP. Ez a számítástudomány leghíresebb bevezető könyve. Annak ellenére hogy bevezető, nem ajánlható kezdőknek! Minden tisztességes funkcionális programozással foglalkozó embernek egyszer el kell olvasnia, aki ezt nem teszi meg, legalább ismerje a címét és tegyen úgy mintha olvasta volna. Ingyenes, ezért nem lehet azt mondani hogy nem volt rá pénzed :D Érdemes az [OCW kapcsolódó kurzusával](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/) - vagy legalább az előadás videokkal - kiegészíteni a feldolgozását. 

- [The Reasoned Schemer ](http://mitpress.mit.edu/books/reasoned-schemer)- a Little Schemer stílusában íródott kicsi könyvecske, mely a funkcionális-logikai programozásba vezet be minket

**3. Hard core computer science**

- [Essentials of Programming Languages](http://www.eopl3.com/) - a programozási nyelvek (és paradigmák) alapjaiba vezet be ez a remek könyv, csak a SICP ismeretét feltételezi ehhez csupán.

- [Types and Programming Languages](http://www.amazon.com/Types-Programming-Languages-Benjamin-Pierce/dp/0262162091/ref=pd_sim_b_53) - Habár nem kell a típusokkal bajlódni a Scheme esetében, nem árt tisztában lenni velük, ha Haskell vagy Scala felé kacsingatunk, akkor nincs más választásunk!

**4. Bónusz**

- [Andvanced Topics in Types and Programming Languages](http://www.amazon.com/Advanced-Topics-Types-Programming-Languages/dp/0262162288/ref=pd_bxgy_b_text_y) - az előző kötet folytatása

- [Paradigms of Artificial Intelligence Programming ](http://norvig.com/paip.html)- Norvig könyve még ma is alapmű. Nem csak a Scheme, hanem a CommonLisp és a Prolog is terítékre kerül benne, no meg hogy hogyan használjuk AI területen ezeket.

- [Scheme NLTK](http://www.snltk.org/) - érdemes egy kicsit foglalkozni a SNLTK-val, habár nem jól dokumentált, a kódjából sokat tanulhatunk arról hogyan működik az nlp funkcionális nyelven
