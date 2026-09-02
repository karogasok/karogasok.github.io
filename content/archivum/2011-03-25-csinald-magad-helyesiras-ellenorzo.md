---
title: "Csináld magad helyesírás-ellenőrző program á la Google"
slug: "csinald-magad-helyesiras-ellenorzo"
date: 2011-03-25T09:45:00.003Z
publishDate: 2011-03-25T09:45:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/03/csinald-magad-helyesiras-ellenorzo.html"
regi_cimkek:
  - "python"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "helyesírás"
  - "helyesírás-ellenőrző"
  - "python"
  - "számítógépes nyelvészet"
---

**[Peter Norvig](http://bit.ly/eWKvK3) nagy sikerű esszéjét követve most saját helyesírás ellenőrzőt fogunk készíteni, mégpedig a Google megszokott javaslatainak mintájára. Ehhez viszont mi nem használjuk fel A magyar helyesírás szabályait, sőt semmilyen szabályt nem fogunk követni! Az adatok fognak minket vezetni utunkon. Itt nem törünk a kereskedelmi forgalomban és ingyenesen elérhető szoftverek babérjaira, csak az alapelveket szeretnénk bemutatni és egy kicsit bátorítani szeretnénk az olvasót hogy vágjon bele a programozás világába akkor is ha csak kevés előismerettel rendelkezik a területen.**

**Eszközök**

Ahhoz hogy követni tud a posztot szükséged van:

- a [Python programozási nyelvre](http://www.python.org/) (2.5 vagy magasabb verzió, de Python 3.x nem jó) és az általam elkészített github repo-ban megtalálható fájlokra

- egy [programozóknak készített szövegszerkesztőre](http://bit.ly/fydPND), IDE-ra vagy ha Windows felhasználó vagy, akkor a Python installációdban megtalálható IDLE-re

- és erre a [github repo](http://bit.ly/fTNdMt)-ra (A fájlokat a böngésződdel is letöltheted a megszokott módon, de ajánlom hogy a legalapvetőbb git és github eszközök használatát tanuld meg mihamarabb)

- nem szükséges egyáltalán, de jó ha tudsz angolul olvasni (nem Shakespeare-t, hanem pl egyszerű szakszöveget)

**Barkácsolás 101**

Ha nem tudsz programozni még, nem baj! Azzal a pedagógiai szándékkal is írtam ezt a posztot hogy bemutassam azt a megközelítést amit sokan csak barkácsolásnak nevezünk. Ma a programozás már nem abból áll hogy mindent magának ír meg az ember, a fájlok kezelésétől a grafikus interfészig. Ha meg tudod fogalmazni a problémát amit szeretnél megoldani, akkor már félig meg is oldottad minden gondodat!  Valaki valószínűleg már valami nagyon hasonlóval foglalkozott már és jók az esélyek hogy szabadszoftver hívő az illető! Ha megtaláltad azt ami nagyon hasonlít a te problémádra, meg kell ismerned az adott megoldást. A következő lépés hogy módosítanod kell azt a te problémád szempontjai szerint. Egy nagy szoftverprojekt is így épül fel, megannyi kész vagy hasonló dolog módosításából és összecsiszolásából születnek ma a programok. Ez nem jelenti azt hogy az alapok elsajátítását megspórolhatod, hiszen akkor tudsz jól keresni, ha igazán érted a probléma mindkét oldalát (mind a nyelvészeti, mind pedig a számítástudományi oldalról). De az egyik elősegíti a másikat. (Ajánlom Peter Seibel [Coders at Work](http://bit.ly/fVJTyW) című interjú kötetét, különösen a Norviggal készített interjút - ha másért nem hogy ne csak tőlem halljon ilyen dolgokat :D)

**A probléma**

Hogyan készíthetünk egy helyesírás ellenőrző programot? Ennek egyik megoldása lehet hogy az adott nyelv nyelvtani és helyesírási szabályait a lehető legpontosabb szabályok szerint leírjuk, ha kellően formalizáltuk ezeket, akkor egy jó programozó számára a feladat triviális. Morfológus olvasók itt elővehetnek egy spirálfüzetet, egy tollat és pl Az Új magyar nyelvtant. Mi többiek vakarjuk a fejünket... Na jó, remélem hogy azért egy elfogadható szabályhalmazt össze tudnánk hozni. De tényleg erre kell fordítanunk az időnket? És mi van ha hirtelen kell egy másik nyelvvel is foglalkoznunk? Mennyire független az egyes nyelvek szerkezetétől ez a megközelítés?

**Egy alternatív megközelítés**

Egy másik megközelítés az adatokból indul ki. Az emberek nyilván követnek el helyesírási hibákat, de egyben legtöbbjük az írás elsajátítása mellet az azt vezérlő szabályokat is megtanulta. Így valószínűleg az írott nyelvi adatokban, ha jól választjuk azokat meg, felülreprezentáltak a helyes alakok (pl. mivel az emberek jobban odafigyelnek ha írnak, pláne ha nyilvános helyre, újságba, blogba, szakmai periodikába stb).

Erre már építhetünk! Itt indulhat a keresés! Nem kell hogy feltétlenül magyar nyelvre találjunk megoldást, viszont fontos hogy magyar adatokat be tudjunk szerezni! Kezdődhet a móka! A megfelelő fogalmak (pl spell correcetor, statistical, probabilistic stb) jó alapot adnak. Első körben érdemes a standard bevezető könyvek vonatkozó részeit is átolvasni hogy legyen egy rálátásunk a területre.

**Egy megoldás**

Nem kell sokat keresnünk hogy rátaláljunk Peter Norvig már említett [How to Write a Spelling Corrector](http://bit.ly/cjxvn2) esszéjére (Kérlek ha nem ismered az írást, tölts el pár percet vele!). Láthatjuk hogy maga a kód nem hosszú és alapvetően egy fájlt igényel amit

```
NWORDS = train(words(file('big.txt').read()))
```

kifejezésben nyit meg a program. Élhetünk a gyanúval hogy ha sikerül hasonló magyar nyelvű adatokat találnunk, akkor nagyobb módosítások nélkül megúszhatjuk a dolgot.

**Nagyon röviden az elméleti háttérről**

Most szerencsénk van, hiszen az esszé lényege az elméleti háttér. Ebből kiderül hogy alapvetően a szógyakoriságon alapul a megközelítés (épp ahogy vártuk). A gyakorisági tábla adja a nyelvünk egy modelljét, mely alapján megadjuk hogy egy adott szó (na, jó, lehet hogy helyesebb egy elgépelést karaktersornak nevezni csupán), mekkora valószínűséggel reprezentál egy elemet. Örülünk, hiszen így tényleg csak az adatoktól függ ez a megközelítés, munkánk nagyban leegyszerűsödött arra hogy a big.txt fájlhoz hasonló magyar adatot találjunk.

**Mit és hogyan kell módosítani?**

Szükségünk van tehát egy olyan fájlra melyben két oszlop található, az elsőben az egyes szavak, a másodikban pedig a hozzájuk tartozó gyakorisági értékek tartoznak. Szerencsére valami nagyon hasonló akad a magyar nyelvre, ez a magyar webkorpusz (sajnos a projekt honlapja a poszt írása során nem volt elérhető, de[ az ftp szájton](http://bit.ly/g6McgM) is érdekes információka és értékes adatokat találhat az olvasó). A repo-ban megtalálható a leggyakoribb százezer magyar szót tartalmazó fájl. Ha vetünk egy pillantást rá, láthatjuk hogy valahogy így néz ki:

a    91905116    89013997    65868724    43050309  
 az    32836302    32483167    24383179    16189184  
 s    26216677    26038935    19288013    12398358  
 A*    18411067    18160755    13490177    8867291  
 hogy    16291361    16118673    11902102    7654795  
 is    15782647    14271378    10097022    6285293  
 nem    14228895    14018094    9918516    6151477  
 egy    9574168    9446422    6440405    3746912

Ellenben a big.txt ettől eltérően valahogy így

a    21160  
 aah    1  
 aaron    5  
 ab    2  
 aback    3  
 abacus    1  
 abandon    32  
 abandoned    72  
 abandoning    27  
 abandonment    15

Mielőtt kétségbe esnénk vagy órákat töltenénk azzal hogy kézzel átszerkesszük a fájlt, több lehetőségünk van. Vagy egy táblázatkezelőben töröljük a harmadik és negyedik oszlopot, vagy egy kicsit programozunk. Az awk szkript nyelv pont ilyen feladatokra lett létrehozva, az alábbi kis parancssorból futtatható szkript kiválasztja az első két oszlopot a webkorpuszból és átmásolja tartalmukat a wordcount.txt fájlba.

[GitHub Gist](https://gist.github.com/886523)

Most már tényleg nincs más dolgunk mint hogy kicseréljük a  a kérdéses sorban a big.txt fájl nevét a saját gyakorisági táblánkat tartalmazó wordcount.txt nevére.

[GitHub Gist](https://gist.github.com/886619)

**Teszteljük munkánkat**

Ha valakinek olyan csapnivaló a helyesírása mint nekem, akkor könnyen tesztelheti az eredményeket. Ha nem, akkor keresni kell pl. gyakori hibákat. A magyar [Wikipedia szerkesztői szerencsére vezetnek egy oldalt](http://bit.ly/hMT7kW) a náluk előforduló hibákról, így van adatunk tuti hibára és annak javítására.

Indítsuk el a Python-t a fájlokat tartalmazó könyvtárban. Majd importáljuk a programunkat:

Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56)  
 [GCC 4.4.3] on linux2  
 Type "help", "copyright", "credits" or "license" for more information.  
 >>> from hun_spell_corrector import *  
 >>>

(A '>>>' karaktersort nem kell begépelni, ezzel jelzi a python interpreter hogy inputot vár a felhasználótól. Amikor "válaszol" nekünk a gép, akkor nem látjuk ezt a jelsort.)

Keressünk pár szót a teszteléshez! Én lusta vagyok, ezért most csak pár a betűs szót tesztelek.

>>> correct("aminósav")  
 'aminosav'

Remek! Na nézzünk még egyet!

>>> correct("antena")  
 'antenna'

És akkor egy olyat is ami nem egyértelmű hogy minek az elírása:

>>> correct("aszt")  
 'aszt'

No itt elvéreztünk, de hát nem lehet minden tökéletes. Viszont már tudjuk hogy működik a rendszer, van mit piszkálgatni, lehet a kóddal játszadozni, vagy több és/vagy jobb adatot gyűjteni.
