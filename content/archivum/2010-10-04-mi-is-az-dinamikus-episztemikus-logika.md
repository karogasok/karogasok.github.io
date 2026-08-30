---
title: "Mi is az a dinamikus episztemikus logika és mihez is kezdjünk vele?"
date: 2010-10-04T11:48:00.004Z
publishDate: 2010-10-04T11:48:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/10/mi-is-az-dinamikus-episztemikus-logika.html"
regi_cimkek:
  - "logika"
  - "nyelvészet"
  - "szemantikus web"
regi_cimkek_mind:
  - "dinamikus episztemikus logika"
  - "játékelmélet"
  - "logika"
  - "nyelvészet"
  - "szemantikus web"
---

Szépfalussy Enikő vendégposztja  
  
**A dinamikus episztemikus logika (röviden DEL) az évtized "buzz word"-je a logikusok körében és mint ilyen megosztja a szakmát. Mi itt és most nem vállalkozunk másra mint egy képet adni az olvasóknak arról miért van ez így. Ezért itt nem mutatjuk be a különböző rendszerek formális definicióit, csak jelezzük merre érdemes elindulni és miért érdemes megismerkedni ezzel az irányzattal.**  
  
  
  
**Miért logika?**  
 A laikusok számára nem kézenfekvő kérdés, de kezdjük itt; mi is az a logika. A magyar wikipédia egy frappáns [megfogalmazást](http://bit.ly/dwKqnJ) ad; "*A **logika** az érvényes következtetések és bizonyítások illetve az ezzel összefüggő filozófiai, matematikai, nyelvészeti és tudománymetodológiai kérdések tudománya*." Ebben az értelemben a del logika, de van egy nagyon érdekes tulajdonsága. A hagyományos logikai rendszerek (klasszikus elsőrendű logika, modális logika, stb) általánosak. Ez annyit jelent hogy univerzális szabályokat írnak le, gondoljunk pl Wittgenstein Tractatus-ára, ahol a logika a világ nyelve, a fennálló tények szerkezetének leírása (azaz nem a tények mögötti dolgok leírása, hanem az hogy milyen relációkban beszélhetünk ezen tényekről és hogyan érvelhetünk róluk). A nyelvészetben ezt használjuk ki, hiszen habár a nyelvet egyes beszélők használják és a jelentés e használat során érhető tetten, a logika segít leírni a NYELV működését. Tehát az általános találkozik az egyedivel, egy adott beszélő nézőpontjából műveljük a nyelvészeti szemantikát (jobban mondva annak logikai ágát). A dinamikus episztemikus logika ebben tér el a hagyományos logikai rendszerektől; nézőpontot vált, nem egy adott beszélő vagy egy univerzális leírás szempontjából közelíti meg tárgyát, hanem adottnak veszi hogy több ágens interakciója alakítja ki azt hogy mit tudunk. Épp ez az a tulajdonsága ami miatt sokan megkérdőjelezik hogy a del tekinthető-e egyáltalán logikának, de most mi megelégszünk ennyi információval. Akit bővebben érdekel hogy miért és jó kilépni a hagyományos nézőpontból, olvass el a terület egyik legnagyobb kutatójának, J. van Benthem-nek [On is a Lonely Number](http://bit.ly/atIwhD) c. írását.  
  
**Miért episztemikus?**  
 Térjünk egy kicsit vissza a logika definíciójára;  *az érvényes következtetések és bizonyítások* tudománya nyilvánvalóan nem az olyan episztemológiai kérdések iránt érdeklődik hogy mit jelent tudni valamit, mikor tudhatunk valamit, hanem az érdekli hogy ha tudunk valamit, akkor abból mi következik ezért a hagyományos logikai megközelítés nem igazán foglalkozott azzal miképp konstruálódik a tudás annak tartalmától függetlenül (hiszen az az ő szempontjukból egyszerű levezetés). [Jaakko Hintikka](http://bit.ly/cWufPX) fordult először a hétköznapi nyelv filozófiája felé és próbálta meg formalizálni hogyan 'alakul' a tudás egy vagy több ágens esetében, miképp tudjuk formalizálni a különbséget egy állítás és annak állítása között hogy valaki tudja hogy egy állítás igaz, hogyan tudunk érvelni egy ágens meggyőződéseiről stb. Ez az irányzat az ún [episztemikus logika](http://bit.ly/a6mL2E).  
  
**Miért dinamikus?**  
 Elérkeztünk a legérdekesebb kérdéshez, miért dinamikus a del? Nagyon röviden; a del lényege hogy egy olyan eszközt ad a kezünkben amivel modellezhetjük miképp alakul több ágens tudása. Persze ezzel még nem mondtunk sokat, de talán segít ha segítségül hívjuk [Robert Aumann](http://bit.ly/anxffF) közgazdasági Nobel-díjas játékelméleti kutatót. Interactive Epistemology[ I ](http://bit.ly/advrok)és [II](http://bit.ly/a9H4Vp) cikkeiben tulajdonképpen egy érme két oldalát mutatja be nekünk. Az olvasó számára talán ismertebb a játékelmélet fogalma. Induljunk ki ismét a [Wikipédia meghatározásából](http://bit.ly/9pMywj) mely szerint ez a tudomány "*azzal a kérdéssel foglalkozik, hogy mi a racionális (ésszerű) viselkedés olyan helyzetekben, ahol minden résztvevő döntéseinek eredményét befolyásolja a többiek lehetséges választása, vagyis a játékelmélet a stratégiai problémák elmélete*". Ennek matematikai leírása megmutatja miképp válasszunk stratégiát különböző helyzetekben, a del pedig segít nekünk leírni milyen episztemológiai változások zajlanak le egy ilyen szituációban. Ha valaki bejelent egy információt (public announcement) ezzel az információról értesült csoport episztemológiai állapota is megváltozik, erre kíváncsi a del.  
  
**Mire használható?**  
 A játékelmélet filozófiai problémáinak elemzésén túl a del alkalmas episztemológiai és tudományfilozófiai modellezésre is. Nyelvészeti szempontból pedig egyrészt új utakat nyithat a diskurzuselemzésben és a játékelméleti pragmatika kiegészítője is lehet. Legérdekesebb alkalmazása a blog olvasói számára talán a szemantikus web területe. Ahogy egyre több tudás válik szemantikus formában elérhetővé a neten, a del lehetővé teszi hogy annak terjedését modellezzük és a különböző forrásokat összevessük (egy-egy ontológia hitelességét nem tudjuk ellenőrizni, de összevethetjük a különböző hiteket). Ezen a téren Pietarinen írásait ajánlom az olvasók figyelmébe, különösen a [Possible-Words Ontology for the Semantic Web](http://bit.ly/94zixM) rövid kis írást.
