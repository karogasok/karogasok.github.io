---
title: "Nyelvészet és interakciódizájn II. - elvek, paraméterek, minimlaizmus és Ubiquity"
slug: "nyelveszet-es-interakciodizajn-ii-elvek"
date: 2010-06-09T16:07:00.001Z
publishDate: 2010-06-09T16:07:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/06/nyelveszet-es-interakciodizajn-ii-elvek.html"
regi_cimkek:
  - "Ubiquity"
  - "elvek és paraméterek"
  - "firefox"
  - "interakciódizájn"
  - "minimalista program"
  - "mozilla"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "Ubiquity"
  - "elvek és paraméterek"
  - "firefox"
  - "interakciódizájn"
  - "minimalista program"
  - "mozilla"
  - "számítógépes nyelvészet"
---

**[Ahogy arról már posztoltam](http://szamitogepesnyelveszet.blogspot.com/2010/05/nyelveszet-es-interakcio-dizajn-i-uj.html) a Ubiquity projekt teljesen új irányt jelent a számítógépes nyelvészet és az interakciódizájn területén. De milyen elvek rejlenek mögötte?**  
  
**Az örök kérdés: szabályok vagy statisztika?**  
A számítógépes nyelvészet, nevéhez híven egyre inkább elmozdul a számítástudomány megoldásai felé. Ez azt jelenti hogy előtérbe kerültek az adatbányászat, a statisztikai és a nosql mozgalom kellékei. Hogy jó irány-e ez (ahogy egy kedves olvasó kérdezte) nem tudom megmondani. Nyilvánvaló hogy egy probléma megoldása ilyen eszközökkel lehetséges és értelmes, ezért az ilyen módszerek léte nem megkérdőjelezhető. A nyelvészetben is teret nyert a statisztikai megközelítés, és szerintem ez is rendben van.  
  
Azonban ezen megközelítéseknek van egy amolyan "buherálós fílingje". Ezzel nem nézem le az snlp művelőit, sőt! Az ilyen buherálás szüli a legtöbb jó dolgot az életben, ezt hívjuk mérnöki munkának. Egy adott problémát megoldani (persze a rendelkezésre álló eszközökkel) nagy dolog. A tudományos ismeretek bizonyos értelemben művészetté válnak a jó szakemberek kezében. Igen ám, de mennyire lehetnek ezek a megoldások hordozhatóak? Vannak bizonyos mintázatok, az egyes problémák osztályokba sorolhatóak, de nem tudunk előre adott módszerekkel ráugrani egyre. A kedves olvasó végezhet egy kis gyakorlatot is. Keressen egy szöveget angolul. A GoogleTranslate segítségével fordítsa le magyarra és franciára/németre vagy egy másik nyelvre amit ismer (ok, lehetőleg indoeurópai nyelvre). Melyik fordítás jobb? [Igaz ez csak személyes élmény, de én ezt franciával és spanyollal szoktam eljátszani, de kértem már erre hollandul és németül beszélőket és tudománytalan felmérésem eredménye hogy ezen nyelvekre értelmesebb fordítások születnek.]  
  
A  fenti kísérlet eredménye elvileg az hogy valamelyiket (hacsak kicsit is) jobbnak találjuk. Minnél közelebb van a két nyelv egymáshoz, annál jobb lesz a fordítás eredménye. A rendszer finomhangolása során nem tudjuk az általános elméleti hátteret felhasználni, hanem bütykölnünk kell. A nyelvészettel foglalkozók most hátradőlnek és vagy azt mondják "Na ugye! Nincs univerzális grammatika", vagy pedig mosolyognak "Nem tudják hogy vannak univerzális szabályok?".  
  
És valóban ha a minimalista program működik egy-egy nyelvi rendszer leírása univerzális kell hogy legyen. Az elvek és paraméterek elmélete szerint az egyes nyelvek közötti különbségek csupán a paraméterek bináris értékeiben rejlenek. Ha ez igaz és ezen paraméterek formálisan is leírhatóak a nyelvi elemeken végzett műveletekkel együtt, akkor alapjaiban változtathatjuk meg az ember-gép interakciót és a számítógépes nyelvészetet. De hogyan is?  
  
**A Ubiquity projekt születése**  
Minden a régi görögöknél kezdődött! Oké ez csak vicc, de visszamehetnénk akár hozzájuk is. Egyszer egy srác, [Aza Raskin](http://en.wikipedia.org/wiki/Aza_Raskin), [apja nyomdokaiba lépve](http://en.wikipedia.org/wiki/The_Humane_Interface) elgondolkodott milyen is egy jó interfész és mi a baj a mostaniakkal. [A hivatkozott wikipedia oldalon találhatók linkek Raskin írásaihoz, érdemes őket elolvasni, ha nem akkor olvass tovább egy kis összefogalóért]  
  
Raskin szerint a grafikus felhasználói interfészek forradalmiak voltak a maguk korában, azonban a technika fejlődése kihívások elé állítja ezt a technológiát is:

1. A mai GUI alapú rendszereken futó programok redundáns funkciókat tartalmaznak, a sztenderdek hiánya miatt a funkciók helye nehezen található meg

1. Nem veszik figyelembe hogy manapság egy felhasználó egyszerre több programot használ munkára/szórakozásra

1. A GUI bogarászása a bonyolult menük esetében nem természetes, gyakran hosszadalmas

Ezzel szemben a régi, jól bevált unix alapú rendszerek rendelkeznek az interakciódizájn szempontjából is érdekes tulajdonságokkal

1. Az operációs rendszerbe integrált apró, feladatspecifikus programok kerülik a redundanciát

1. A különböző programok között az I/O átirányítás sztenderd módozatai könnyűvé együttműködésüket

1. A szövegbevitel gyorsabb mint a grafikus navigáció

Ellenben a unix típusú rendszerek nem véletlenül nem lettek felkapottak az átlagfelhasználók körében, mivel

1. A különböző kapcsolók, parancsnevek teljesen esetlegesek

1. A bash és egyéb shell-ek szintaxisa eléggé távol áll a természetes nyelvtől

1. Parancssorban nem élvezhetjük a modern multimédiás tartalmakat

Raskin alapötlete az Enso projekt, ami később a Mozilla Foundation Ubiquity-je lett elegánsan oldja meg ezt a problémát. A széttagolt alkalmazásokat, legyenek azok a gépen vagy a neten egy közös interfésszel köti össze. Ez az interfész egy egyszerű szövegbeviteli felületet mutat a felhasználónak aki természetes nyelvi parancsokat adhat ki. Így megmarad a szép GUI, és megkapjuk a shell előnyeit is.  
  
Persze ez nagyon szépen hangzik, de a gyakorlatban az Enso projekt jégre került, helyét a Ubiquity vette át. Ez a projekt annyit visszavett az eredeti elképzelésből hogy nem törekszik a desktop alkalmazások integrálására, viszont annyiban előre mutat hogy lehetővé teszi a különböző netes felületek összekötését (nem csak gyári parancsokkal, hanem lehetőséget biztosít bővítésre is).  
  
**Lokalizáció újratöltve**  
A Ubiquity lokalizációja nem hagyományos módon történik. Amíg egy alkalmazás/honlap honosítása egyszerű fordítás, a Ubiquity-nél teljesen más a helyzet. Itt a parancsok természetes nyelvi (általában felszólító módú) mondatok. A program tkp. megérti hogy felhasználó mire utasítja, azaz interpretálja a parancsot.  
  
Persze az egyik út az hogy az "e-mail this map to John" parancsot simán lefordítjuk és magyarul "küld el ezt Jánosnak" parancsot várunk. De akkor hogyan írhat valaki egyedi parancsokat? Ha van egy parancskészletünk angolul, akkor annak minden elemét le kell fordítanunk a célnyelvre?  
  
[Michael (mitcho) Erlewine](http://mitcho.com/) MIT-s PhD hallgató erre egy nagyon okos ötlettel állt elő. [Írásait (nem csak a Ubiquity projektről) érdemes elolvasni] Válasszuk szét a parancsok írását és azok megértését! A saját nyelvén bárki írhat parancsokat, minden különösebb szakértelem nélkül. A parancsok megértését bízzuk egy külön rendszerre s lokalizáljuk azt!  
  
Habár jómagam is csak pár hete ismerkedem a rendszerrel, teljesen magával ragadott. Viszont nagyon nehéz elmagyarázni másoknak. A parancs írás és értelmezés szétválasztása után sokan visszakérdeznek "Hogyan?". [Itt csak röviden térek ki erre, a következő részben próbálom ezt felvázolni bővebben.] Adott egy parancs "e-mailezd ezt el Katinak " és a hozzá tartozó akció ("vágd ki ezt a képet, nyisd meg a gmail fiókomat, nyiss egy üres levelet Katinak címezve és másold be a képet az üzenetbe") és az ennek megfelelő természetes nyelvi mondat "e-mail this to Kate". A szintaktikai viszonyok elemzése kapcsolja hozzá a parancsot és az annak megfelelő akciót a természetes nyelvi parancshoz.  
  
"Na ez ugyanaz, csak hosszabban!" - szokták nekem mondani mostanában. OK! Megvan az elvek és paraméterek elmélet? Ha nincs akkor nagyon röviden összefoglalva: A nyelv univerzális emberi képesség, ezen alapul minden természetes nyelv. A nyelvek közötti különbségek arra vezethetők vissza hogy ez nem egy "kemény" képesség, csak elveket tartalmaz arra nézve hogy milyen lehet egy-egy nyelv. Amikor elsajátítjuk anyanyelvünket, akkor ezen képesség segít nekünk. Azaz nem tudjuk előre anyanyelvünket, azt meg kell tanulnunk. Viszont kulcsokat ad nekünk amikre figyelünk (elvek amiket a nyelv használ és paraméterek amik a nyelv jellemzői). Egyszerűbben kötött-e a szórend, agglutináló nyelvet akarunk-e elsajátítani, a főnévhez viszonyítva hol vannak a melléknevek stb. Elvileg a mélyben a nyelv az nyelv, a paraméterek határozzák meg milyennek halljuk (angol, dán, kantoni, malájállam, stb). Legyenek a parancsok a mélyben meghúzódó univerzális grammatika nyelvén megírva, így elvileg egy általános parancsot kapunk. Ha meg tudjuk adni egy-egy nyelv paramétereit, akkor a parancsok lokalizálása tkp. annyi hogy eldöntjük milyen nyelven fogalmazódott az meg.  
  
Ha nem érted kedves olvasóm nem a te hibád, én is ismerkedem ezzel a megközelítéssel!  
  
**Miért nagy dolog ez?**  
Egyrészt a lokalizáció új dimenzióba kerül. Nem kerülnek utcára az alkalmazások fordítói, de megváltozhat az interakció gép és ember között, és a nyelvi akadályokat is eltüntetheti (vagy legalábbis csökkentheti). Gondolj bele egy kicsit ma mennyien használják a netet? Milyen nyelveken? Hol növekszik legjobban  felhasználók száma? Hol fog növekedni a felhasználók száma? Mennyire tudnak angolul az emberek? Mit szeretnek jobban, anyanyelvükön vagy egy idegen nyelven interakcióba lépni?  
  
A szép az hogy a gyakorlatban is tesztelhetjük a minimalista program elveit. Ez az elmélet elegáns és szép, nem is beszélve arról hogy gazdaságos. Ahelyett hogy hatalmas adatmennyiséget szednénk össze lelassítunk! Csak az érdekel bennünket a nyelvi adatokból amik paraméterekre utalnak. De hisz ezt már a nyelvészek elvégezték! OK vannak még fehér foltok, de kb megvan ami kell. Van egy elméleted egy paraméterről, teszteld le, van már hol! Persze a Ubiquity-ben használt Parser2 nem tökéletes, de akár erre is használható. Mit nyerünk? Nem kell adatokkal bajlódni folyton, nem kell próba-hiba módszerekkel toldozgatni a rendszer amikor új nyelvre alkalmazzuk.  Ha minden jól megy, a távoli jövőben a repülő autók idejében, a lokalizáció annyit tesz majd hogy beállítjuk a paramétereket és kész!
