---
title: "Korpusznyelvészet - a korpuszkészítés alapjai 1."
date: 2011-06-27T09:30:00Z
publishDate: 2011-06-27T09:30:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/06/korpusznyelveszet-korpuszkeszites.html"
regi_cimkek:
  - "korpusznyelvészet"
regi_cimkek_mind:
  - "ces"
  - "eagles"
  - "korpusznyelvészet"
  - "tei"
  - "tei-xml"
  - "unicode"
  - "xml"
---

**Az[ előző korpusznyelvészeti posztban](http://szamitogepesnyelveszet.blogspot.com/2011/06/korpusznyelveszet-elmeleti.html) láthattuk hogy milyen elméleti megfontolásokat kell figyelembe vennünk mielőtt korpuszt használunk. Ezeket figyelembe véve érdemes tudnunk hogy milyen elvek mellett épül fel egy jó korpusz. Most a legalapvetőbb vezérelevekt és ajánlásokat vesszük sorra.**

**Leech maximái**

A korpusznyelvészek körében Leech maximáit nagy tisztelet övezi, mivel betartásuk maximalizálja az adott korpusz használhatóságát és megoszthatóságát. Vegyük sorra ezeket:

1. az annotáció legyen eltávolítható úgy hogy visszakaphassuk a nyers szöveget

1. az annotáció legyen kinyerhető és külön tárolható a szövegtől

1. az annotáció alapelvei legyenek hozzáférhetőek

1. legyen világos hogy kik és hogyan végezték az annotációt

1. a felhasználó számára legyen világos hogy az adott annotáció nem megfellebbezhetetlen hanem gyakorlati szempontokat követ hogy egy használható korpuszt kapjon

1. az annotáció alapelvei legyenek elmélet semlegesek amennyire ez csak lehetséges

1. nincs kitüntetett, standard annotáció

Ezek az alapelvek nem meglepőek, a legtöbb tapasztalati tudomány kívánatosnak tartja hogy az adatok begyűjtésének és rendszerezésének elvei nyilvánosak legyenek, hogy a kísérletek megismételhetőek legyenek mások által is. Ehhez kapcsolódik a lehető legsemlegesebb annotációs séma választásának maximája, hiszen eleve zavart okozhat ha valamely elmélet befolyása alatt rendszerezzük adatainkat. Egy semleges séma a különböző iskolák képviselőinek egyaránt megfelel. Az adatok megoszthatóságának elve sajnos gyakran csak el, de szép dolog, hiszen milyen jó lenne ha mindenki akár otthon is elemezhetne egy-egy korpuszt, azonban a szerzői jogok és a tudományos vaskalaposság gyakran közbeszól. (A [Science Commons](http://sciencecommons.org/about/) egy nagyon jó lehetséges megoldása lehet a problémának)

**A legfontosabb standardok és alapelvek**

Jelenleg a három nagy standard alakult ki, melyek betartása szinte kötelező minden új korpusz esetében. Ezek egymásra épülnek és kölcsönösen kiegészítik egymást. Megegyeznek abban hogy az XML ([Extensible Markup Language](http://en.wikipedia.org/wiki/XML)) szabványra épülnek. Dióhéjban az XML lehetővé teszi hogy "mini-nyelveket" határozzunk meg a segítségével, így az annotációs sémánkat is leírhatjuk segítségével. Ennek nagy előnye hogy a tartalom (azaz a nyers szöveg) és az annotáció (vagy markup/jelölés) egyértelműen elkülönül mégpedig szabályosan így a Leech-i maximákat teljesen betarthatjuk. A három legfontosabb standard nem más mint annak meghatározása hogy miképp építsük fel "mini-nyelveinket". Ezek közül a legfontosabbak:

- TEI - [Text Endocing Initiative](http://www.tei-c.org/index.xml), a legátfogóbb standardok és ajánlások gyűjteménye, az oldalon található tutorialt mindenkinek ajánlom

- EAGLES - [Expert Advisory Groups on Language Engineering Standards](http://www.ilc.cnr.it/EAGLES/home.html), egy EUs projekt, a korpuszok, lexikonok, formális grammatikák és nyelvtechnológiai eszközök kiértékelésének alapelveit határozza meg. A dokumentumok átbogarászása alap ha EUs projektben veszel részt vagy olyan adatot használsz amit EUs projekt keretében fejlesztettek ki.

- CES - [Corpus Encoding Standard](http://www.cs.vassar.edu/CES/). A TEI és az EAGLES ajánlásain alapuló standard.

A jó hír az hogy minden EAGLES és/vagy CES alapú formátum megfelel a TEI ajánlásoknak (de fordítva nem feltétlenül áll fent a megfeleltetés!!!).

**Karakterkódolás**

Habár manapság a Unicode szabvány kezd elterjedni sokszor futhatunk bele olyan adatokba melyek nem szabványos karakterkódolással készültek. Érdemes áttekinteni a Wikipedia [Character encoding](http://en.wikipedia.org/wiki/Character_encoding) szócikkét hogy megismerkedjünk a különböző kódolásokkal.

A Unicode alapjait a[ vontakozó Wikipedia szócikk](http://en.wikipedia.org/wiki/Unicode) nagyon jól bemutatja, a részletekért érdemes a [The Unicode Consortium](http://unicode.org/) honlapján böngészni. Habár már nyolc éve írodott Joel Spolosky T[he Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!) ](http://www.joelonsoftware.com/articles/Unicode.html)posztja mindenkinek kötelező aki egy kicsit programozgatna is korpusz piszkálás közben (magyarán megkerülhetetlen).

**Folyt.köv.**

Az XML és a Unicode magában is megérdemel egy-egy posztot, így a sorozatban valamikor bővebben s fogunk foglalkozni a témával.
