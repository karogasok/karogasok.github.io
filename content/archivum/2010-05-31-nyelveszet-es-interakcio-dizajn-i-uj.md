---
title: "Nyelvészet és interakciódizájn I. - Új irány?"
date: 2010-05-31T17:31:00.001Z
publishDate: 2010-05-31T17:31:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/05/nyelveszet-es-interakcio-dizajn-i-uj.html"
regi_cimkek:
  - "Ubiquity"
  - "firefox"
  - "interakciódizájn"
  - "mozilla"
  - "nyelvészet"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "Ubiquity"
  - "firefox"
  - "interakciódizájn"
  - "mozilla"
  - "nyelvészet"
  - "számítógépes nyelvészet"
---

**Azt hitted hogy a számítógépes nyelvészet gépi fordításra, szövegbányászatra meg keresésre való? Miközben fákat rajzoltál, logikát tanultál, nyelvhierarchiával fárasztottad az agyadat, arra gondoltál milyen szexi dolog a webdizájn? Fáradtan nézted programozó barátodat, aki nagyon örült hogy végre összekötheti művészhajlamait tanult szakmájával a humán-komputer interakció vagy éppen az interakció dizájn területén? Na ennek most vége!**  
  
**1. A számítógépes nyelvészet hagyományos felfogása**  
A nyelv számítógépes kezelése nagyon ígéretesnek tűnt a komputációs őskorban. Üss fel egy bevezető könyvet s azt fogod látni hogy az ötvenes években a gépi fordítást közelinek tartották. Aztán megváltozott a világ, de még mindig reménykedtek a kutatók és geekek hogy lesz egyszer saját HAL-juk. A nyolcvanas években Bill Gates meg volt győződve hogy a következő nagy áttörés a beszédalapú vezérlés lesz a számítástechnikában.  
  
Mostanában pedig az van hogy nem tudjuk hogy mi van. Persze akadnak még szép számmal számítógépes nyelvészeti képzések, ezek nagy részére nyelvész (sőt a liberálisabb angoloknál filozófus, pszichológus) végzettsége is be lehet jutni. De, ha végig böngészed az elsnet vagy a linguist list jobs szekcióját, gyakran találsz "bs/ms/phd in computer science with experience in nlp" hirdetéseket. Persze láttam már olyat hogy valaki bejut ilyen helyekre (számítógépes) nyelvészként, de az ilyen muksók száma csökken.  
  
Ennek igen egyszerű oka van szerintem: a statisztikai megközelítés nyert. Ez nem jelenti azt hogy a logikai megközelítésnek annyi, vagy hogy nem fog még feljönni. Momentán ez van.  
  
No nem kell a kardunkba dőlni. Egyrészt ahogy már [arról posztoltam](http://szamitogepesnyelveszet.blogspot.com/2010/05/valoszinuseg-statisztika-es-nyelv.html), nekünk is fejlődni kell, a statisztikai módszerek megtanulhatóak. Habár nagyon szeretem Peter Norvigot, bizonyára nem értünk egyet legutóbbi [esszéjével](http://oreilly.com/catalog/9780596157128) (segéd anyag [itt](http://norvig.com/ngrams/)), melyben nagyon leegyszerűsítve amellett érvel hogy igazán nagy adathalmazzal pusztán egyszerű, a nyelvi strukturát tkp figyelmen kívül hagyó, valószínűségi módszerekkel szofisztikált gépi fordítás is elérhető akár.  
  
Szintén jó hír: a beszédfelismerés terén is kezd visszatérni a nyelvészeti tudás. Miért? Mert a hirdetések 99%-os pontossága bizony csak bizonyos speciális estekben igaz, és csak eléggé speciális területekre szűkítve. Ezen a területen, a jelfeldolgozás hagyománya miatt is, úgy gondolták minden megoldható egy "kis trükközéssel". Ennek ékes bizonysága egy névtelenség homályába burkolódzó IBM-es kutató elhíresült mondása: "Every time I fire a linguist my system improves." [Olvasni egy [blogban](http://robertfortner.posterous.com/the-unrecognized-death-of-speech-recognition) olvastam először, de ha jól emlékszem fonetika órán hallottam először - jajj 2002-ben]. Persze ez így nagyon sarkos, de nyelvészeti tudás nélkül is lehet beszédfelismerő rendszereket építeni. Ami igazán érdekes hogy a gyakorlatban ez a hozzáállás 90% feletti eredményességet hozott. De elég ennyi? Miért nem lehet HMM módszerekkel sokkal tovább jutni? Azért mert nem egy sima bottom-up rendszerrel van dolgunk, hanem az alulról építkező feldolgozás kiegészíti egy top-down rendszer is. Itt jönnek képbe újra a nyelvészek, pszichológusok, fiziológusok és egyéb csodabogarak.  
  
**2. Számítógépes nyelvészet ma**  
Hol van akkor a helye egy számítógépes nyelvésznek ebben a katyvaszban? Egyrészt nem kell lemondanunk arról hogy a mesterséges intelligencia mellett mi is kivegyük a részünket korunk "buzz words" tengeréből. Text mining, data mining, computational intelligence, information retrieval, érezük hogy lenne itt keresni valónk. Korpusz nyelvészek szíve dobban ha belegondolnak mekkora adattömeggel dolgozhatnának ha nekik is lenne egy felhőben futó hatalmas adatbázisuk, vagy egyszerűbben fogalmazva a yahoo vagy a google hatalmas szöveges adataira gondolnak, "web as a corpus" mormolják lefekvés előtt. Van remény! (Nekik pl [itt](http://www.umiacs.umd.edu/%7Ejimmylin/book.html)). Nem kell computer scientist átképzésre menni és a diplomát kidobni az ablakon! A nyelvész, még ha számítógépes is, elsősorban nyelvész. Viszont meg lehet, és meg is kell tanulni az alapokat, el kell sajátítani egy új nyelvet amit nevezzünk statisztikának (de értsük bele a valószínűségszámítást is). Ahogy angolból is van alap- közép- és felsőfok, úgy itt is. Lassan, de biztosan el lehet jutni egy erős középfokra, ami már elegendő munkánk elvégzéséhez. (Viszont ha nem tudsz diszkrét matekul, akkor azt is meg kell tanulnod).  
  
Ma nyitva áll a pálya (no nem itthon, ezt tapasztalatból mondom), ha értelmesen koncentrálod erőidet. Szerintem ma egy nyelvész eszköztárába tartozik hogy ismerje a python és az R nyelveket, valamit pár adatbázissal képben legyen. Ezt lehet bővíteni egy kis web ismerettel (html, javascript alapok), prolog-ot és/vagy haskell-t sokan ismerik általában. Nagyon nagy előny a Java (esetleg egy SCJP certification) és alaposabb OOP ismeretek.  
  
**3. Számítógépes nyelvészet holnap**  
A holnap az interakció! Bill Gates álma még messze van, de a nyelv egy remek eszköz az interakcióra (meg arra hogy ne akarj interakcióba kerülni másokkal, de ez itt nem játszik). Igen, lassan elérünk a címben ígért interakció dizájnhoz.  
  
Már most itt közlöm, hogy olvastam Hume-ot, és a jövőre nem tudok biztosat mondani, az sem tuti hogy holnap fel fog kelni a Nap. Ebből levezethető hogy amit itt mondani fogok az spekuláció, de van alapja, ma is láttam a Napot felkelni, és használtam a Ubiquity-t.  
  
Hozzászoktunk a grafikus interfészekhez, de nagyon. Egy konzol olyan fapados. De kerestél már valamit mélyen egy menüben? Dolgoztál már egyszerre több alkalmazáson, amelyek mindegyik más struktúrát képzelt el a legjobb GUI alatt. És persze az egyikben van egyféle helyesírási progi, a másikban egy másik, esetleg egy kalkulátor, de mind más, más funkciókkal. Ellenben a konzolok élő őskövülete, a bash (és testvérei) más filozófián alapulnak. Minden kis részfeladatra egy-egy spéci kis program áll rendelkezésedre, alapvetően közös alapokon (pl. közös regex könyvtár) és alapból úgy tervezték hogy együtt dolgozhassanak (és az egyik ne a másik melóját végezze) a IO átirányítás és a csatornák(pipes) ha ismerősen hangzanak, erre valók.  
  
Vissza akkor a konzolhoz? Ezt még a megrögzött bash-fanok sem akarják. Sokkal inkább egy közös interfészre van szükség. A [Ubiquity](http://mozillalabs.com/ubiquity/) project őse ezt célozta meg. A menük böngészése helyet, egy egyszerű, természetes nyelvszerű szöveges paranccsal meghívni a kívánt funkciót sokkal kézenfekvőbb mint végig sakkozni a menüket és control-c control-v nyomkodással tölteni az időt. Pl. "ezt a képed másold be ebbe a doksiba és küld el Ferinek". Na jó, ez jól hangzik, de ennyire flottul még nem megy.  
  
Egy másik fontos tényező a lokalizálás (i18 mostanában menőbb nevén). Minden alkalmazás minden pontját lefordítani biza nagy munka, de elvben ha van egy fent leírt alkalmazásod, akkor csak a megadott parancsokhoz kell kapcsolódni a programnak. Pölö egy szövegszerkesztő értse a "szúrd be a képet" parancsot, oszt jó napot...  
  
Kedvenc, sajnos most éppen egy kicsit a fősodorból kiesett Mozilla projectem ezt próbálja meg elérni. És figyelem! Megszállott generatívok, szintakták és egyéb fura alakok. A lokalizálás (elvben, gyakorlatban még nem teljesen) a mi szeretett "principels and parameters" elméletünkön alapul! Magyarán lokalizálni annyi, mint megírni az adott nyelv egy töredékének grammatikáját. Ez a grammatika pedig a paraméterek beállítása (elvben, gyakorlatban még nem).  
  
A kör bezárult, vissza az eredethez. A (számítógépes) nyelvész tudását felhasználva segíti a polgárokat jobban boldogulni, azaz jobban uralni, kezelni, használni gépüket, túllépve a nyelvi korlátokon is. Csoda szép!  
  
**4. Folyt.köv.**  
A továbbiakban körbejárjuk a Ubiquity projectet. Kezdjük azzal milyen alapelvek mentén szerveződött, mit sikerült elérni, miért jegelték. Ezután egy kicsit megnézzük hogyan lehet szabályokat írni hozzá és majd egy kicsit arról is szólok hogy milyen szerepe lehet a nyelvnek/nyelvészetnek az interakciódizájn területén.
