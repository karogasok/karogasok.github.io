---
title: "Bátran legyünk nyíltak - megéri"
date: 2011-08-20T13:47:00Z
publishDate: 2011-08-20T13:47:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/08/batran-legyunk-nyiltak-megeri.html"
regi_cimkek_mind:
  - "FSF"
  - "Open Knowledge Foundation"
  - "creative commons"
  - "licencek"
  - "linux"
  - "nyílt szoftver"
  - "open data"
  - "open definition"
  - "open source"
  - "szabad szoftver"
  - "szerzői jog"
---

**Sokak számára a nyílt egyet jelent a nyílt szoftverrel az IT világában. Sokan esküsznek a nyíltságra míg mások viszolyognak tőle. Egyesek szerint az egyetlen út a tökéletesség felé, mások szerint nem lehet minőségi eszközöket elérni egy nyílt környezetben. Azonban a furi flanelinges csókák mozgalmából akik egy saját ingyenes oprendszert szerettek volna, eljutottunk odáig hogy már nem csak a szoftverek szabadságát hirdetik egyre többen, hanem az adatokhoz való hozzáférést is. Nem mellesleg ezzel kapcsolatban felmerült egy halom (szerzői)jogi kérdés is. Milyen távlatai vannak a szabad szoftvernek, nyílt adatoknak és megengedő licenceknek?**

**1 Egy kis terminológia/etimológia**

Ahhoz hogy megértsük mit is jelentenek a nyílt és szabad szavak ebben a kontextusban, szükséges egy kicsit foglalkoznunk avval is hogy miképp alakultak ki körülöttük mozgalmak. Lépésről lépésre haladva először a szabad szoftverrel ismerkedünk meg, majd a creative commons szerzőjogi licencel vesszük górcső alá, végül pedig az Open Knowledge Foundation adatokra vonatkozó alapelveit tekintjük át. Természetesen egy poszt nem törekedhet átfogó elemzésre, de a lényeget igyekeztem mondandómnak megfelelően sűríteni, aki többre kíváncsi a linkek mentén induljon felfedezőútra.

**1.1 Szabad szoftver (free software)**

A számítógépek hőskorában az operációs rendszereket együtt adták a gépekkel. Ez azonban nem olyan előre installált oprendszereket jelentett mint manapság, hanem az operációs rendszer egészét, azaz annak forráskódját is. Mivel akkoriban a gépek általában nagyobb cégek és egyetemi kutató laborokban voltak, így nagyon felkészült emberek kapták meg ezeket a kódokat. A fejlesztők birtokában voltak az operációs rendszernek, szükség esetén módosították is egyes részeit és ezeket egymás között kicserélték - hát igen a kutató/fejlesztő társadalom már csak ilyen. Így alakult ki a BSD ([Berkeley Software Distribution](http://en.wikipedia.org/wiki/Berkeley_Software_Distribution)) is, ami a Berkeley Egyetem kutatóinak vezetésével terjesztette a unix típusú oprendszerét. Egy napon azonban az MIT-n [Richard Stallman](http://en.wikipedia.org/wiki/Richard_Stallman) feladta kutatóállását, mivel szeretett programjainak forráskódját zártá tették. Ez annyit jelentett hogy tilos volt immár megosztania másokkal és nem módosíthatta kedvére a forráskódot.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-fbzxZJPqey0/Tk-2vhLExtI/AAAAAAAAAjU/XMJlpxc6KQA/s1600/stallman.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="212" src="http://4.bp.blogspot.com/-fbzxZJPqey0/Tk-2vhLExtI/AAAAAAAAAjU/XMJlpxc6KQA/s320/stallman.jpg" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Stallman előad, forrás http://en.wikipedia.org/wiki/File:Rms_at_pitt.jpg</td></tr>
</tbody></table>

Stallman megalapította a [Free Software Foundation](http://www.fsf.org/)-t melynek célja az lett hogy egy unix típusú, ám szabad szoftvert alkosson meg. Ezzel közel egy időben [Linus Torvalds](http://en.wikipedia.org/wiki/Linus_Torvalds) szerette volna felfedezni az oprendszerek világát és megszületett a Linux. A két dolog tkp. egy, sokak szerint [GNU/Linux](http://en.wikipedia.org/wiki/GNU/Linux#GNU.2FLinux)ról kellene beszélnünk, hiszen a Linux adja a rendszer lelkét (a kernelt) az FSF GNU programjai pedig a funkcionalitást. Számunkra azonban az a lényeg hogy az FSF erőfeszítéseinek érdekében meghatározták mi számít szabad szoftvernek. A szabad magyar fordítás jobban visszaadja mire gondoltak az FSF-nél amikor a free szót használták, hiszen ez nem kell hogy "ingyenes" legyen, de meg kell hogy feleljen a szabadság négy fokának:

> 0 - a programot szabadon lehet futtatni, bármilyen szándékkal

> 1 - szabadon lehet vizsgálni hogy miképp működik a program és igény esetén szabadon lehessen módosítani

> 2 - szabadon terjesztheted a programot, odaadhatod bárkinek

> 3 - szabadon fejlesztheted a programot és szabadon terjesztheted a továbbfejlesztett verziót hogy az egész közösség profitálhasonn belőle

Ezt a nyíltságot a GPL ([General Public License](http://en.wikipedia.org/wiki/General_Public_License)) biztosítja. Ennek lényege hogy a 3 pontnak megfelelően minden származtatott projekt is szabad marad, mégpedig ebben az eredeti értelemben (nevezzük ezt erős szabad szoftvernek). Az FSF amellett hogy a GNU ezsközök fejlesztésére koncentrál a GPL licence alatt álló projekteknek biztosít jogi kérdésekben konzultációt, segítséget és bizonyos fokig védelmet az esetlegesen felmerülő vitákban.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-1-NyPZTEntk/Tk-3CyOL9VI/AAAAAAAAAjY/uBkehNKGi34/s1600/pingvin.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-1-NyPZTEntk/Tk-3CyOL9VI/AAAAAAAAAjY/uBkehNKGi34/s320/pingvin.png" width="272" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Az elengedhetetlen Linux pingvin, forrás: http://en.wikipedia.org/wiki/File:Tux.svg</td></tr>
</tbody></table>

**1.2 Nyílt forráskód (open source)**

Minden szabadszoftver nyílt forráskódú, azonban a nyílt forráskód nem feltétlenül jelenti azt hogy GPL licenc alatt áll az adott projekt. Sokszor semmilyen licencet nem jelölnek meg az alkotók, máskor egy már futó szabad projekt módosítása a cél, vagy kivállnak és viszik magukkal az eredeti licencet a hackerek. Sok esetben azonban egy kis cég, startup, vagy éppen egy multi fejleszt nyílt forráskódú programot és szeretné ha azt "dobozos" formában, üzletet csinálva értékesíthetné vagy olyan verziókat készíthetne melyek zártak. De az is gyakran megesik hogy a projekten dolgozók szeretnék ha bárki bármire - azaz nyugodtan akár üzleti célra is - használhassa az elkészült progit. Erre találtak ki sok, megengedőbb, vagy gyengébb licencet mint pl. [LGPL](http://en.wikipedia.org/wiki/LGPL), [MIT](http://en.wikipedia.org/wiki/MIT_License), [BSD](http://en.wikipedia.org/wiki/BSD_licenses)

**1.3. Creative Commons (CC)**

Az internet megjelenése és a szabad szoftverek elterjedésével egyre többen váltak alkotóvá is és megjelent az igény a kreatív munkák egyszerű és szabad licencelésére. A [Creative Commons](http://creativecommons.org/) erre ad megoldást. Egy nagyon egyszerű netes felületen pár lépésben generálhatunk igényeinknek megfelő licencet.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-rGMR4VLTOso/Tk-3egYoyrI/AAAAAAAAAjc/4Zy1VQXpN5U/s1600/cc_licensing.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://4.bp.blogspot.com/-rGMR4VLTOso/Tk-3egYoyrI/AAAAAAAAAjc/4Zy1VQXpN5U/s320/cc_licensing.png" width="189" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC licenc generálás egyszerűen, forrás: http://creativecommons.org/choose/</td></tr>
</tbody></table>

Négy alaptulajdonság kombinációiból jön ki a "végtermék":

> 1 Nevezd meg! (by)

> A szerző vagy a jogosult által meghatározott módon fel kell tüntetni a műhöz kapcsolódó információkat (pl. a szerző nevét vagy álnevét, a mű címét).

> 2. Ne add el! (nc)

> A mű nem használható fel kereskedelmi célokra.

> 3. Ne változtasd! (nd)

> A mű nem módosítható és nem készíthető belőle átdolgozás, származékos mű.

> 4. Így add tovább! (sa)

> A mű a jelenlegivel megegyező, vagy azzal csereszabatos licenc alatt terjeszthető.

> [forrás: [Wikipedia](http://hu.wikipedia.org/wiki/Creative_Commons)]

Ezek alapján az alábbi kombinációk lehetségesek (CC a creative commons-ra utal, a kétbetűs rövidítések pedig a fenti alaptulajdonságokra):

- CC-BY

- CC-BY-ND

- CC-BY-NC-ND

- CC-BY-NC

- CC-BY-NC-SA

- CC-BY-SA

- CC0 (közkincs)

**1.4. Az OKFN nyíltság definiciói**

Az [Open Knowledge Foundation](http://okfn.org/) célja hogy egységesen határozza meg a nyíltságot, az adatok, tartalom és szoftver szolgáltatások viszonylatában. A [definíciók alapján](http://www.opendefinition.org/) beszélhetünk nyílt tudásról (open knowledge), nyílt adatról (open data), nyílt tartalomról (open content) és nyílt szolgáltatásról (open service). A definíciók egyfajta egyszerűsítés szolgálnak, segítik a felhasználókat eligazodni,  az alapítvány listát vezet a meghatározásoknak megfelelő licencekről. A legátfogóbban az OKFN a nyílt tudást definiálta, ehhez kapcsolódik az összes többi:

> **"A piece of content or data is open if anyone is free to use, reuse, and redistribute it — subject only, at most, to the requirement to attribute and share-alike"**

> [forrás: [Open definitions](http://www.opendefinition.org/)]

**2. De miért legyünk nyíltak?**

Ahelyett hogy rögtön válaszolnánk a fő kérdésre, vegyük sorra a nyíltság pár tipikus alkalmazási területét. Itt sem törekszünk teljes áttekintésre, sokkal inkább a legfontosabb elemekre koncentrálunk, bemutatva hogy mit nyerhetünk a nyíltság különböző alkalmazásaival.

**2.1. Nyílt szoftver**

A megszámlálhatatlan [Linux disztribúción](http://en.wikipedia.org/wiki/Linux_distrobutions) túl más nyílt forráskódú projektek is vannak természetesen. Az [OpenOffice](http://www.openoffice.org/), vagy manapság inkább a [LibreOffice](http://www.libreoffice.org/) ingyenes irodai programcsomag, vagy az [Apache alapítvány](http://apache.org/) népszerű szerver csomagjai mind mind jó példák arra hogy a nyílt forráskód stabil szoftvereket eredményez. Nincs program hiba nélkül, azonban a lelkes programozók ezeket hamar észreveszik és a hibák javítása általában nagyon rövid időn belül megszokott jelenni. Nem is beszélve arról az előnyről hogy a közösség tagja munkájukkal nem csak a projektet, hanem személyes névjegyüket is építik, gyakran egy-egy állásra a legjobb ajánlólevél a nyílt projektekben végzett szorgos munka.

A legjobb példa arra hogy nem csak a szoftver fejlesztéséről szól egy nyílt projekt a [Mozilla Foundation](http://www.mozilla.org/foundation/) működése. A Firefox böngésző köré épített önkéntes közösség nem csak a szoftvert fejleszti, hanem a dizájntól kezdve a felhasználóktól begyűjtött adatok vizsgálatán át a marketingig bezárólak mindent végez. A modell annyira sikeresnek bizonyult hogy az utóbbi időben az Ubuntu fejlesztői is hasonló modell alapján kezdték átszervezni közösségüket.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-aRHnK7IoxRc/Tk-4PMVMf2I/AAAAAAAAAjk/DkF0NmDjjWI/s1600/testpilot.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="195" src="http://1.bp.blogspot.com/-aRHnK7IoxRc/Tk-4PMVMf2I/AAAAAAAAAjk/DkF0NmDjjWI/s320/testpilot.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Mozilla Labs Test Pilot, a felhasználói vizsgálatokat is "kiszervezik", forrás: http://mozillalabs.com/testpilot/</td></tr>
</tbody></table>

**2.2. Nyílt tudomány - állampolgári tudomány**

2.2.1. Nyílt tudomány

A kreatív munkák egy külön "alfaja" a tudományos munkák köre. Miért kellene még pluszban fizetnünk azért hogy megkapjunk egy tudományos publikációt? Gondoljuk csak végig, a kutatók közpénzeket használnak fel, többségük közalkalmazott, tegyük egy kicsit nemzetközi perspektívába és azt látjuk hogy egy-egy nagy kutatás finanszírozásába sok-sok különböző nemzeti és nemzetközi szervezet száll be. Miért lesz ezeknek az eredménye egy zárt, nagyon drága publikáció? Egyáltalán értelmes csak a publikációra koncentrálnunk? Egy kutatáshoz hozzátartozik a kutatás menetének megtervezése, a kísérletek megszervezése, a kutatási adatok és az adatokon végzet elemzés, az elemzés eredménye és annak csak legvégsőbb állomása a publikáció.

A tudományos kutatások fent részletezett praktikáit nevezik "workflow"-nak. A kutatás menetének leírása és megosztása lehetővé teszi hogy megismételhető, ellenőrizhető legyen egy-egy kutatás. A módszerek megosztása pedig könnyebbé teszi az új kutatások tervezését, lehetővé teszi a legjobb módszerek (best practices) átvételét. A [Kepler project](https://kepler-project.org/) lehetővé teszi mindezt és megjelenése óta sok hasonló kezdeményezés született már.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-It43fir25n4/Tk-4mALyyVI/AAAAAAAAAjo/a36QOFkY-j4/s1600/predator.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="311" src="http://3.bp.blogspot.com/-It43fir25n4/Tk-4mALyyVI/AAAAAAAAAjo/a36QOFkY-j4/s320/predator.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Így néz ki egy Kepler workflow - ragadozók és prédáik, forrás: https://kepler-project.org/users/sample-workflows</td></tr>
</tbody></table>

2.2.2. Állampolgári tudomány - citizen science

Sokan ismerik a [SETI@home](http://setiathome.berkeley.edu/) projektet, melynek keretében személyi számítógépünk feles kapacitásait felajánlhatjuk a földön kívüli intelligenciák kutatására. Azóta egyre több hasonló projekt indult és ma már egy PC vagy laptop és internetkapcsolat segítségével bárki bakapcsolódhat egy neki tetsztő kutatásba. Az ilyen számítási kapacitást felajánló projekteket tekintik az állampolgári tudomány előfutárainak. Ez tulajdonképpen okos [crowdsourcing](http://en.wikipedia.org/wiki/Crowdsourcing), annak felismerése hogy a laikusok is érdeklődnek a tudomány iránt és segíthetnek a kutatóknak.

Azonban nem csak arra nőtt meg az igény hogy az emberek segíthessenek a kutatóknak, a csináld magad mozgalmakhoz hasonlatosan egyre többen fordultak az otthon végezhető kísérletek felé. A hacker magatartás habár első sorban a programok és a számítógépes hardverek bütykölését jelentette, hamar áttevődött más területekre is. Elterjedtek az olyan magazinok mint a Make és megjelent egy olyan réteg ami nem csak passzívan akart résztvenni a tudományban. Az [Arduino](http://www.arduino.cc/) pl visszahozta a hardveres hackkelés élményét, elérhetővé tette ismét az interaktív felfedezés és nagyon megkönnyítette a belépést erre a területre, hiszen nagyon olcsó egy "lap" mivel maga a kapcsolási rajz CC licenc alatt van, azaz ingyenes.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-AlIoyzV5jz8/Tk-403nQftI/AAAAAAAAAjs/AzmYUi6fuPs/s1600/arduino.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-AlIoyzV5jz8/Tk-403nQftI/AAAAAAAAAjs/AzmYUi6fuPs/s320/arduino.jpg" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Arduino lap - ezt lehet hackellni!, forrás: http://en.wikipedia.org/wiki/File:Arduino_Duemilanove_2009b.jpg</td></tr>
</tbody></table>

A hacker mentalitás azonban napjainkban új területekre is betört, az élettudományok területén megjelent a biopunk mozgalom. Az olyan eszközök mint az [OpenPCR](http://openpcr.org/) megjelenésével drasztikusan csökkent a területre lépés költsége, gyakorlatilag egy komolyabb számítógép áráért beléphetünk a szintetikus biológia és a bioinformatika csodás világába.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-lMRZcXjo0JM/Tk-5IxrNeCI/AAAAAAAAAjw/dCs1-6wm_YU/s1600/OpenPCR_Front_Corner.gif" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://2.bp.blogspot.com/-lMRZcXjo0JM/Tk-5IxrNeCI/AAAAAAAAAjw/dCs1-6wm_YU/s320/OpenPCR_Front_Corner.gif" width="280" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">[OpenPCR, kb 600 USD és otthon lehet meghackelni a DNS-t, forrás: http://openpcr.org/features/</td></tr>
</tbody></table>

**2.3. Gov2.0 és adatújságírás**

A Gov2.0 (Government 2.0 - azaz kormányzat 2.0) neve egy gyűjtőfogalmat takar, tkp. a webkettes és hármas technológia alkalmazását fedi a kormányzat különböző szintjein. Egyrészt a közösségi szájtokhoz hasonló elvek mentén a részvételi demokrácia erősítése a mozgalom célja, azonban számunkra sokkal fontosabb most az információ szabadság biztosítása. A különböző kormányzati szinteken rengeteg adat keletkezik, ezek nagy része közérdekű és az internet kiválló platform arra hogy ezeket a polgárok számára hozzáférhetővé tegyük. Az adatok elérhetősége azonban csak az első lépés.

Az adatújságírás tkp. párhuzamba állítható a Gov2.0 megjelenésével. Ahogy egyre több nyers adat jelenik meg, úgy az igény is megjelent arra hogy ezeket valamiképpen értelmezzük. Az újságírók - vagy legalábbis egy csoportjuk - feladata éppen ez már réges-régen. Az új időkre adott válaszként megjelentek az információtechnológia eszközei az újságírásban is, ezt nevezzük adatújságírásnak. Ez nem csak a "hagyományos" szerkesztőségekben jelent meg, hanem a civil mozgalmak is elkezdtek érdeklődni ezen eszközök iránt (jó példája ennek az OKFN [Where Does My Money Go](http://wheredoesmymoneygo.org/) oldala).

**2.4. Szemantikus web**

Az eddigiek alapján nem meglepő hogy a nyílt szoftver és a nyílt adat a két "kulcsfogalom". A szoftverek esetében adott az egységes alap, az adott programozási nyelv amiben írták és pált eszköz ami segít portolni a különböző platformaokra. De mi a helyzet az adatokkal?

Önmagukban a nyers adatok nem sokat érnek, feldolgozásukhoz bizony sok munka szükséges. Vannak esetek amikor ésszerűbb az adatokat olyan meta-adatokkal ellátni melyek megkönnyítik értelmezésüket és feltárják az adatok közötti összefüggéseket. Nem is beszélve arról hogy ha ezen adatok elérhetőek, akkor egy dokumentum nem csupán egy szöveges fájl, hanem hordozza önmaga interpretációját is. Ha adott az interpretáció, akkor az internetes alkalmazások ezeket kicserélhetik egymás között. Pl. ha tudom hogy orvoshoz kell mennem, a határidőnaplóm tudja mely elfoglaltságaim átütemezhetőek, melyek nem, megkeresheti a hozzám legközelebbi specialistát és időpontot egyeztethet nekem a doki határidőnaplójával, ehhez átrendezheti egyéb találkozóimat szükség esetén, további egyeztetéseket folytatva és így tovább. Ez lenne a szemantikus web ideája.

A fent felvázolt szcenárió még nem valósult meg, de nem is állunk olyan távol tőle. Sok részterületen már egyre többen publikálnak a weben szemantikus adatokat is. Azonban gyakran ez egyszerűen nem életszerű, kinek lenne megtaggelni sok sok oldalt szemantikusan is? A linked data ötlete figyelembe veszi ezeket a helyzeteket és egy kicsit lazább megközelítést ajánl. Bizonyos adathalmazokon végezzzük el a meta-adatok és az adatok közötti relációk hozzáadását. Az elérhető adatoknak így öt típusa létezik:

1. a weben elérhető nyílt adat

2. gépileg olvasható adat

3. nem védett fromátumú

4. megfelel az RDF standardnak

5. linkelt adat

A linkelt adatok meghatározása egy kicsit bonyolultabb, a lényeg hogy minden elem rendelkezzen egy saját azonosítóval és tartalmazzon adatokat hogy milyen relációkban áll más elemekkel (ezek lennének a linkek). Szép lenne ha mindent le tudnánk írni így, de ez nem lehetséges, hiszen minden pillanatban változik hogy mit is írjunk le, de még ha elvileg meg is oldató ez, gyakorlatilag többe kerülne egy ilyen rendszer fenntartása mint amennyi hasznot hajtana. Ezért kényelmesebb több linked data tárat létrehozni, és szükség esetén az egyes halmazok közötti relációkat felfedezni/megalkotni. Azonban hogy ezt megtehessük az adatoknak nyíltaknak kell lenniük!

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-_lAFKsQgIXE/Tk-56_v1OnI/AAAAAAAAAj4/MmCwNT_etCQ/s1600/linkeddata.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="208" src="http://1.bp.blogspot.com/-_lAFKsQgIXE/Tk-56_v1OnI/AAAAAAAAAj4/MmCwNT_etCQ/s320/linkeddata.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Sok sok linked data összekapcsolva, forrás:  http://upload.wikimedia.org/wikipedia/commons/2/23/Lod-datasets_2010-09-22_colored.png</td></tr>
</tbody></table>

**3. Mivel jár a nyíltság?**

A szerzői jogok a 15-16 században jelentek meg a nyomtatás elterjedésével. A nyomdák nyilván védeni kívánták termékeiket a kalózkiadásoktól. Ugyanekkor jelentek meg a szabadalmak is. A reneszánsz ember egyszerre fordult vissza az antikvitáshoz és vágott bele új kalandokba a világ megismerése felé. A tudományok és a művészetek nem váltak szét, sokkal inkább kiegészítették egymást mint a megismerés különböző formái. A reneszánsz ember szerette volna megérteni a világot melyben él, ezért aktívan viszonyult hozzá, nem csak megfigyelt, hanem kísérletezett is. A felvilágosodás nagy gondolkodói már nem egyetemeken tanítottak, hanem úriemberek voltak akik idejüket a tudománynak és a kísérletezésnek szánták, kiterjedt levelezést folytattak egymással.  A gondolatok eredetiségét nagyra tartották, de eredményeiket megosztották egymással,  különböző társaságokba tömörültek és egyre aktívabb közösségé formálódtak. Ez az intézményesülés később segített a tudományoknak visszatalálni az egyetemekre is.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-arxpD6OLkV0/Tk-6OVs36VI/AAAAAAAAAj8/HYy3R8l9TPw/s1600/copyright.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://2.bp.blogspot.com/-arxpD6OLkV0/Tk-6OVs36VI/AAAAAAAAAj8/HYy3R8l9TPw/s320/copyright.jpg" width="199" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">VI. Sándor pápa elsők között büntette a kalózkiadásokat,  forrás:  http://en.wikipedia.org/wiki/File:Index_Librorum_Prohibitorum_1.jpg</td></tr>
</tbody></table>

A 18-19 században kibontakozó ipari forradalom megteremtette az ipari innovációt és a szabadalmak elterjedését is magával hozta. Azonban a szabadalmak sokáig egyrészt nem jelentettek túl sok védelmet (gondoljunk pl. Kínára ahol a mai napig eléggé lazán kezelik ezt) másrészt nehezen volt nemzetközi keretek között értelmezhető (egy Britanniából hazánkban tévedő mérnököt miért kötött volna hazája szabadalmi jogrendszere? ki ellenőrizhette hogy sérti-e bárki jogát itteni munkájával?). A huszadik századra azonban kialakult a szerzői jogok és szabadalmak rendszere, mely a magántulajdon mintájára alkotta meg a szellemi javak védelmét.

Ha történelmi léptéket alkalmazunk azonban a huszadik század közepére, a nyugati világban kialakult és megszilárdult állapot sokkal inkább egy kivétel mint maga a szabály. Ahogy [Lessing](http://en.wikipedia.org/wiki/Lawrence_Lessig) [Code 2.0](http://codev2.cc/) és [Remix](http://remix.lessig.org/) köteteiben nagyszerűen leírta, a kreatív alkotások velejárója hogy "óriások vállán állunk", azaz az új egyben a régi átvétele és továbbgondolása. Amennyiben korlátozzuk a hozzáférést a régi dolgokhoz, annyiban egyben le is fékezzük az innovációt.

Mivel társadalmunk egyik alappillére a magántulajdon, ezért nem helyezkedhetünk a minden mehet elvére, valamilyen módon természetesen védenünk kell a szellemi javakat. Azonban ebbe bele kell hogy tartozzon a nyílt hozzáférés biztosítása a közjavakhoz, azaz a közérdekű adatokhoz, a szellemi-kulturális örökségünkhöz. Meg kell adnunk a jogot mindenkinek hogy ehhez szabadon csatlakozzon és nyílt licencek használatával publikálja munkáit. A nyílt adatok és nyílt eszközök használat nem csak sokat spórol meg a felhasználóknak, hanem együttműködésre tanít és új lehetőségeket teremt. A nyílt innováció csökkentette a belépési költségeket az IT iparban, jelenleg hasonló forradalom játszódik le az élettudományok területén is, egyre több alkotó ember (tudósok, művészek, hobbisták) használja ki az internet nyújtotta lehetőségeket új üzleti lehetőségeket teremtve és új adatokat, projekteket adva vissza a közösségnek.
