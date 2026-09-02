---
title: "Gondolkodó gépek 1."
slug: "gondolkodo-gepek-1"
date: 2011-06-14T10:11:00Z
publishDate: 2011-06-14T10:11:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/06/gondolkodo-gepek-1.html"
regi_cimkek:
  - "Turing"
  - "filozófia"
regi_cimkek_mind:
  - "ELIZA"
  - "Turing"
  - "Turing teszt"
  - "Weizenbaum"
  - "filozófia"
  - "intelligencia"
  - "kognitív tudomány"
  - "mesteséges intelligencia"
---

**A népszerű Jeopardy vetélkedőn aratott sikere után Watson bekerült a médiába és lassan mindenkinek van róla véleménye. Előkerültek ismét a gépek képességeit firtató kérdések, tényleg lehetnek-e annyira intelligensek mint az ember, vagy túlszárnyalhatják-e és a cyberpunk alkotásokban megjövendölt poszthumán jövő már itt jár a keretek alatt. A dolog pikantériáját az adja hogy az MIT nagyágyúi egy nem rég megrendezett szimpóziumon éppen azon keseregtek hogy valahol letértek az aranykorban kijelölt útról és újra kell indítani a mesterséges intelligencia kutatásokat. Akkor hogyan is állunk ezzel? Miért kesergünk, ha Watson nyert, a jövő pedig már itt is van.**

**A számítógép megszületése és az intelligencia kérdése**

Történetünk visszavezet minket 1936-ba, amikor a fiatal Alan Turing megírta [On Computable Numbers with an Application to the Entscheidungsproblem](http://www.thocp.net/biographies/papers/turing_oncomputablenumbers_1936.pdf) című tanulmányát. Az [Entscheidungproblem](http://en.wikipedia.org/wiki/Entscheidungsproblem) (vagy eldöntésprobléma) lényege ha adott egy formális nyelv és egy matematikai állítás az adott nyelven, konstruálható-e egy mechanikus módszer (a mechanikus szón itt nem fogaskerekeket és ötletes szerkezeteket, hanem egy procedúrát kell értenünk) amely képes ledönteni az állítás igazságértékét. Hibert ezt a kérdést 1928-ban fogalmazta meg, Turing általánosan bebizonyította hogy ilyen eljárás nem létezik (Church egy sokkal szűkebb bizonyítását adta ennek, Turingtól függetlenül 1937-ben).

De a negatív eredmény is eredmény, ugyanis a vizsgálódások feltárták hogy mely függvények eldönthetőek, azaz kiszámíthatóak (computable) és megszületett az első elvi számítógép, a Turing gép ([Turing machine](http://en.wikipedia.org/wiki/Turing_machine)). Hogyan lehet egy gép elvi? Nos, egy Turing gép csakis elvi lehet, mivel feltételezi hogy végtelen sok memória áll rendelkezésre a műveletek elvégzésére, és a műveletek lépései megszámlálhatóak (de nem feltétlenül végesek). Ha elvesszük a végtelen lehetőségét, akkor megkapjuk a konkrét számítógépek architektúráját. Turing miután elolvasta Church cikkét, el is utazott hogy a Princeton-on együtt dolgozzanak a gép fizikai megvalósításán, azonban a világháború közbeszólt. Hazatérése után nem sokkal bekapcsolódott a német Engima rejtelek feltörését végző Gonvernment Code and Cypher School munkájába és egymás után építhette csodálatos masináit. A háború után, 1948-tól a University of Manchester matematika tanszékén kapott állást, itt készítette el munkatársaival a világ első, kereskedelmi forgalomban kapható elektronikus számítógépét.

Turing érdeklődése széles körű volt, az elméleti megközelítés mellett érdekelték a gyakorlati problémák is és egészen beleásta magát a villamosmérnöki tudományokba is, azonban nem szabad elfelejtenünk hogy alapvetően mindig a matematika nagy problémái érdekelték. Maga az eldöntésprobléma azért érdekes, mert egy alapvetően emberi tevékenység formalizálására törekszik, hiszen egy matematikai sejtés bebizonyítása nagyon intuitív folyamat (l. Lakatos [Proofs and refutations](http://en.wikipedia.org/wiki/Proofs_and_Refutations) könyvét!). A számításelmélet tudománya arról szól miképp tudjuk formalizálni az egyik legmagasabb szintű kognitív folyamatot!

**A híres Turing teszt**

A Turing gépeknek, és fizikai utánzataiknak van egy nagyon érdekes tulajdonságuk: szimulálhatnak más gépeket! Ezt nagyon fontos megértenünk és elfogadnunk! A legegyszerűbb analógia a személyi számítógép! Egy viszonylag egyszerű utasításkészletet tartalmaz minden gép lelke, ez a ALU (arithmetic logic unit) ami a legalapvetőbb aritmetikai műveleteket tartalmazza. Erre épülve futatthatunk egy szövegszerkesztőt, de akár egy kalkulátort is a gépünkön, vagy böngészhetünk a neten. A programozás lényege hogy az apró építőkövekből valami mást rakunk össze!

Ahogy Turing híres tanulmányában bebizonyította, bizonyos függvények kiszámíthatóak egy adott "géppel". Mivel azonban egy gép szimulálhat bármely másik gépet, így ha már van egy gépünk, akkor az az összes kiszámítható függvényt képes megoldani, ergo azon problémákat amiket képesek vagyunk megoldani, egy gép is képes megoldani!

Tudjuk hogy a számítógépek a sok számolással és ismétlődéssel járó munkában nagyon jók, sőt túltesznek rajtunk mivel nem fáradnak el. Egy táblázat összeadása és az átlag kiszámítása pillanatok alatt megvan egy gépnek, nekünk órákig is eltarthat vagy akár évtizedekig is! Néha fitymálódva szoktuk mondani hogy ez nem intelligencia, hanem monotónia tűrés és szabálykövetés... De mikor mondhatjuk akkor hogy egy gép intelligens?

Turing az ún. imitációs játékok vezeti be ennek eldöntésére [Computing Machinery and Intelligence](http://blog.santafe.edu/wp-content/uploads/2009/05/turing1950.pdf) című tanulmányában. Az imitációs játékban egy nő, egy férfi és egy kérdező vesz részt. A játék célja hogy a kérdező a végén megállapítsa hogy melyik játékos a férfi és melyik a nő (ezt lehet bonyolítani azzal hogy a kérdező csak egy szöveges konzolon kommunikálhat a játékosokkal). Turing szerint egy gép akkor tekinthető intelligensnek ha egy ilyen játék során nem lepleződik le, azaz a kérdezőt sikerül meggyőznie arról hogy ő nő, vagy férfi. (Manapság a Turing teszt név elterjedtebb mint az imitációs játék, azonban gyakran nem az eredeti problémát értik rajta. A Stanford Encyclopedia of Philosophy r[emek összefogalólját](http://plato.stanford.edu/entries/turing-test/) ajánlom az érdeklődő olvasónak ami nem csak az eredeti cikket mutatja be, hanem későbbi fejleményeket is)

Vegyük észre hogy ez a teszt semmit sem mond arról hogy egy ilyen gépnek milyennek kell lennie! Külső kritériumok alapján határozza meg mit tekintünk intelligens viselkedésnek és ebben központi szerepet szán a nyelvnek!

**ELIZA, a megértő társ**

[Joseph Weizenbaum](http://en.wikipedia.org/wiki/Joseph_Weizenbaum) 1966-ban megalkotott ELIZA programja úgy tűnik átment a Turing teszten! A hangsúly azon van hogy "úgy tűnik", ugyanis sokak szerint semmilyen intelligenciát nem tulajdoníthatunk ELIZA-nak!

ELIZA a [Carl Rogers](http://en.wikipedia.org/wiki/Carl_Rogers) nevével fémjelzett rogeraiánus (vagy kliensközpontú) terápiában alkalmazott módszert alkalmazza, azaz a "pácienst" beszélteti. Lássuk hogyan is néz ki egy ilyen beszélgetés (kis betűvel a páciens, nagy betűvel ELIZA):

Men are all alike.

IN WHAT WAY?

They're always bugging us about something or other.

CAN YOU THINK OF A SPECIFIC EXAMPLE?

Well, my boyfriend made me come here.

YOUR BOYFRIEND MADE YOU COME HERE

He says I'm depressed much of the time.

I AM SORRY TO HEAR YOU ARE DEPRESSED

It's true. I am unhappy

DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY

I need some help, that much seems certain.

WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP

Perhaps I could learn to get along with my mother.

TELL ME MORE ABOUT YOUR FAMILY

My mother takes care of me.

WHO ELSE IN YOUR FAMILY TAKES CARE OF YOU

My father.

YOUR FATHER

You are like my father in some ways.

WHAT RESEMBLANCE DO YOU SEE

You are not very aggressive but I think you don't want me to notice that.

WHAT MAKES YOU THINK I AM NOT VERY AGGRESSIVE

You don't argue with me.

WHY DO YOU THINK I DON'T ARGUE WITH YOU

You are afraid of me.

DOES IT PLEASE YOU TO BELIEVE I AM AFRAID OF YOU

My father is afraid of everybody.

WHAT ELSE COMES TO YOUR MIND WHEN YOU THINK OF YOUR FATHER

Bullies.

DOES THAT HAVE ANYTHING TO DO WITH THE FACT THAT YOUR BOYFRIEND MADE YOU COME HERE

A fenti beszélgetést Weizenbaum [ELIZA - A Computer Program For the Study of Natural Language Communication Between Man and Machine](https://www.fbi.h-da.de/fileadmin/personal/b.harriehausen/NLP/ELIZA_reading__assignment_1_.doc) cikkéből vettem át. A program lényegét ebben az írásban a szerző nagyon egyszerűen foglalja össze:

The gross procedure of the program is quite simple; the input is read and inspected for the presence of a *keyword*. When such a word is found, the sentence is transformed according to a *rule* associated with the keyword, if not a content-free remark or, undercertain conditions, an earlier transformation is retrieved. The text so computed or retrieved is then printed out.

Hogy mit is jelent ez a gyakorlatban, azt a következő részben vizsgáljuk meg!
