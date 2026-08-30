---
title: "Könyvismertető: Morville - Callender: Search Patterns"
date: 2010-10-18T08:32:00.006Z
publishDate: 2010-10-18T08:32:00.006Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/10/konyvismerteto-morville-callender.html"
regi_cimkek:
  - "interakciódizájn"
  - "keresés"
  - "könyvismertető"
regi_cimkek_mind:
  - "interakciódizájn"
  - "keresés"
  - "könyvismertető"
---

*"The future isn't just unwritten - it's unsearched."*  
  
**Peter Morville és Jeffrey Callender könyve élvezetes olvasmány lehet mindenkinek akit érdekel a keresés témaköre. Itt nem a PageRank algoritmust és társait találod meg, hanem azt hogy milyen kihívásokat jelent egy alkalmazásba integrálni egy keresés funkciót, hogyan keresünk, milyen kereső interfészekkel találkozhatunk a neten és józan ésszel miképp segíthetünk a technikán. Mindezt kellő humorral, gazdagon illusztrálva (elvégre Callender grafikus) érdekes és jó analógiákkal megspékelve teszi a könyv.**  
  
  
  
<span class="lost-media">Hiányzó kép: <a href="http://lh6.ggpht.com/_SM9YHwWrX6M/TLv0D9yvANI/AAAAAAAAAVk/drdHd2NeurY/s144/SearchPatterns.jpg" rel="nofollow noopener">SearchPatterns.jpg</a></span>  
**Peter Morville: Search Patterns Design for Discovery**  
**O'reilly 2010**  
**184 oldal**  
**honlap: [http://searchpatterns.org/](http://bit.ly/d0CflE)**  
  
**Kontextus**  
*"This is a book about tearing down walls. To make search better, we must collaborate across disciplines and we must break through barriers in our minds, so we are open to imagination, innovation and inspiration"*  
  
 A rendszeres olvasók talán észrevették hogy szeretem a kontextus szót. Régi bölcsész hagyomány szerint ez a könyv sem áll magában, szervesen illeszkedik Morville korábbi könyveinek sorába. Habár praktikus okok miatt ki kell emelnem hogy az előzmények olvasása nélkül is érthető és élvezhető a könyv, úgy gondolom nem lehet kikerülni hogy ne szóljunk róluk.  Az [Ambient Findability: What We Find Changes Who We Become](http://amzn.to/drlYit) a keresés problematikájával foglalkozik az információtervezés (Information Architecture - információ építészetnek is nevezik magyarul, csak az nekem nem tetszik) szemszögéből, a Louis Rosenfeld-del (nagy IA, UX guru) közösen jegyzett [Information Architecture for the World Wide Web: Designing Large-Scale Web Sites](http://amzn.to/bX9wOP) pedig magát a szakmát mutatja be, amolyan bevezető tankönyv stílusban. Érdemes tehát felkészülni egy kicsit a divatos rövidítésekből mint pl IA, UX, IdX, UI és a többiek, de még jobb egy kicsit utánuk is olvasni. A lényeg persze az információtervezés, ami egy meglehetősen fluid fogalom még. Ha hasonlítani kell valamihez, akkor a könyvtártudomány a legjobb analógia, aminek célja jobban hozzáférhetőbbé és kereshetővé tenni egy gyűjteményt. Ha a gyűjteményt nem könyvek, periodikák és egyéb nyomtatványok halmazának tekintjük hanem egy honlapnak sok-sok oldallal, akkor beszélünk információtervezésről.  
  
 A könyv "előszavában" (nem tudom hogy egy rövid képregény előszó-e, ezért az idézőjel) szerepel a fenti idézet. Mivel az információtervezés tényleg interdiszciplináris. A könyvtártudományi analógia mellett magában foglalja az információk ergonomikus elrendezést és lekérdezését, ami maga után vonja a felhasználói viselkedés megismerését, de nem mehetünk el a technikai korlátok mellett sem. Persze nem kell megijedni, ezen területeknek megvannak a maguk szakértői, de ahogy az idézet is mutatja rákényszerülünk arra hogy átlépjük a határokat. Hogy ne veszítsük el a fókuszt, azaz az információtervezés célját, nyugodtan fordulhatunk az ún "design pattern"-ekhez, amiket én tervezési mintáknak hívok (de ha te tudod a rendes magyar nevét, írd meg!).  
  
 A szoftvermérnökök körében nagyon divatosak lettek a tervezési minták az objektum-orientált paradigma megjelenésével, hiszen az oo támogatja az "újrafelhasználást" és az enkapszuláció révén egymástól független elemeket illeszthetünk össze modulárisan.  A tervezési minták ebben segítenek, receptként szolgálnak egy-egy tipikus probléma megoldásához. Maga a tervezési minta fogalma [Christopher Alexander](http://bit.ly/aTmV5G) nevéhez fűződik, aki építészként a világ legkülönbözőbb tájain gyűjtött mintázatokat, a számítástudományba pedig a híres Gang of Four (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) [Design Patterns: Elements of Reusable Object-Oriented Software](http://amzn.to/auYnKx) című könyve honosította meg a fogalmat. Az interakciódizájn művelői a szoftvermérnököktől inspirálva, visszatértek az Alexander által is járt útra és elkezdetek különböző design pattern library-ekt publikálni, néha csak egy screenshotot, máskor kódot is közölnek az általuk jónak (vagy éppen rossznak) tartott mintákról. A könyv olvasása előtt érdemes megnézni pár ilyen design pattern library-t (szoftver, interfész és adat tervezési minták is vannak a következő gyűjteményben).

- [Designing Social Interfaces Pattern Library](http://bit.ly/aJt9pm)

- [Welie A Pettern Library for interaction Design](http://bit.ly/9z5HHf)

- [Morville's Search Patterns Collection](http://bit.ly/bY44kc)

- [User Interface Patterns](http://bit.ly/cO5R9B)

- [Endeca User interface Design Pattern Library](http://bit.ly/aPPBRS)

- [Open Source Design Pattern Library](http://bit.ly/aDQFFN)

- [Linked Data Patterns](http://bit.ly/cfKn1M)

- [Patterny User Interface Design Pattern Library](http://bit.ly/csDPTN)

- [Yahoo! Design Pattern Library](http://yhoo.it/agqE9I)

**Térjünk a könyvre!**  
 Az előző szakasz idézetének szellemében a könyv tele van utalásokkal a legkülönbözőbb diszciplínákra. A hat fejezetből azonban csak egy szól tkp. a keresés tervezési mintáiról, az első három (ahogy én szeretem) kontextusba helyezi a problémát, az ötödik összekapcsolja az információtervezéssel az egészet, az utolsó pedig egy sci-fit megszégyenítő képzelőerővel megírt fejezet a jövőről. Az egyes fejezetek címei a következők:

1. Pattern Recognition

1. The Anatomy of Search

1. Behavior

1. Design Patterns

1. Engines of Discovery

1. Tangible Futures

Az első fejezet nem a gépi tanulásban használatos pattern recognition-ről szól, hanem az egyes minták beazonosításáról és magáról a terezési mintázat fogalmáról és szerepéről a keresésben. A második és a harmadik fejezet ugyanazt a problémát járja körbe két oldalról; miképp használják a felhasználók a keresési funkciókat mint adott lehetőségeket és miképp viselkednek keresés közben. A negyedik fejezet bemutatja a különféle mintázatokat, majd az ötödik fejezet azt is megmutatja melyik mintázatot miképp érdemes megtervezni IA szempontból. Az utolsó fejezet amellett hogy érdekes, azért figyelemre méltó mert a szerzők tisztában vannak vele hogy ami ma nem megoldható gépi erővel, az a jövőben triviális feladattá válhat, ugyanakkor minden kérdés megválaszolása újabbakat vet fel és nem kell félni attól hogy hamar kihalnak az IA művelői.  
  
**Összegezve**  
 A könyv az nyújtja amit ígér, egy áttekintést. Aki akar a könyv honlapja alapján tovább indulhat, aki nem, az is tanult valamit. Kikapcsolódásnak sem utolsó, egyedüli negatívuma 39.99 USD ára, biztos hogy aki keres talál olcsóbbat, azonban a szállítási költségek miatt még így is drága lehet egy diák számára. Igaz értéke viszont akkor van a könyvnek ha a szerző más műveit is elolvassuk, vagy az IA témakörében legalább egy bevezető munkát átlapozunk.
