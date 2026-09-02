---
title: "R, de miért is használjam? - I."
slug: "r-de-miert-is-hasznaljam-i"
date: 2010-07-29T06:21:00.001Z
publishDate: 2010-07-29T06:21:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/07/r-de-miert-is-hasznaljam-i.html"
regi_cimkek:
  - "R"
  - "nltk"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "R"
  - "nltk"
  - "számítógépes nyelvészet"
---

**Sok olvasó kérdezte miért is használjon R-t, hiszen a Python nyelv ideális nyelvészek számára, nem beszélve az nltk-ról. Senkit sem szeretnék lebeszélni megszokott eszközeinek használatáról, de vannak esetek amikor az R használata egyszerűbb, természetesebb és hatékonyabb. Most azt szeretném bemutatni miért érdemes elgondolkodni más eszközök használatáról is.**  
  
**Az nltk dizájn hátrányai**  
Eddig a legjobb cikk amivel találkoztam az nltk mögötti dizájn filozófiáról Edward Loper NLTK: [Building a Pedagogical Toolkit in Python](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.805&rep=rep1&type=pdf) című írása. Érdekes milyen követelményeket vettek figyelembe a rendszer tervezése során:

- könnyű használhatóság

- konzisztencia

- bővíthetőség

- dokumentáció

- egyszerűség

- modularitás

Nyilván ezeket minden rendszernél szeretjük látni. De ne feledjük hogy gyakran kell kompromisszumokat kötnünk hogy az elkészült rendszer pl gyors legyen, vagy "állja a sarat" nagy igénybevétel esetén is. Azonban az nltk egy pedagógiai céllal készült eszköz. Loper éppen ezért emeli ki írásában hogy **milyen követelményeknek nem kell megfelelnie** az nltk-nak. Nézzük mik is ezek:

- nem kell mindenre kiterjedő, átfogó rendszert alkotni

- a teljesítményt épp annyira kell optimalizálni hogy diák projekteket lehessen kivitelezni vele

- okoskodás, a fenti ponthoz kapcsolódva nem trükkös hack-kek sorával kell tuningolni a programokat, hanem tiszta átlátható implementációt kell készíteni (hogy a diákok láthassák a forráskódban miképp valósítottak meg egy-egy elképzelést)

Szerencsére az nltk annyira jól sikerült hogy nem igazán vesszük észre "hiányosságait", sőt egyes moduljait az iparban is felhasználják (habár itt figyelembe kell venni hogy a nyílt forráskódot módosítják néha a jobb teljesítmény elérése érdekében).  
  
**Milyen követelményeknek kell megfelelnie egy számítógépes nyelvészetben használt programozási nyelvnek?**  
Erre a kérdésre mindenki máshogy válaszolna nyilván, sőt úgy tűnik az ipar letette a voksát a Java mellett (követve az IT egész világát). Természetesen akadnak kivételek és sok számítógépes nyelvészeti feladatot egyszerűen túl bonyolult Java-ban elvégezni. Ha a mesterséges intelligencia felől közelítjük meg a kérdést (hiszen tekinthetjük kedvenc tudományunkat az AI egy részterületének is), akkor sokaknak rögtön eszébe jutnak az olyan egzotikus nyelvek mint a LISP, Scheme, Prolog. Nem véletlenül, a mesterséges intelligencia programozás klasszikusa, [Norvig PAIP](http://norvig.com/paip.html)-ja kora ellenére még ma is kötelező olvasmány ezen a területen, még ma is hatással van a kezdőkre és profikra egyaránt. Ebben nagy érdekes követelményeket fogalmaz meg a szerző egy AI programozásban hasznos nyelvvel szemben:

1. built-in support for lists

1. automatic storage management

1. dynamic typing

1. first-class functions

1. uniform syntax

1. interactive environment

1. extensibility

1. history

A listára ma is rábólintunk, talán két dolgot tennénk hozzá. Egyrészt nem szégyenkezzünk, számít a gyorsaság. Másrészt már a könyv publikálásakor is feljövőben volt a sztochasztikus megközelítés amely mára az uralkodó paradigmává vált, így joggal kérhetjük ideális nyelvünktől hogy tegye könnyűvé életünk és támogassa a különböző statisztikai függvényeket (ne kelljen már annyit gépelnünk) és adatstruktúrákat.  
  
A Python nyelv az eredeti nyolc pontból hét és félnek megfelel (lehet hogy egy csak az én személyes véleményem, de a 4. pontnak csak részben felel meg a pythonos lambdázás). A további két kritériumnak is megfeleltethetjük a kígyós nyelvet, de ehhez ki kell használnunk bővíthetőségét. A statisztikai elemzéshez és bonyolultabb adatstruktúrák létrehozásához szükségünk lehet a numpy/scipy csomagra, ezek használata kezdő kezekben bizony nagy teljesítmény csökkenéshez vezethet, nem beszélve hogy a nyelv "magján kívül" egy új csomagot kell elsajátítanunk.  
  
**Összegzés**  
Mind a Python, mind az nltk hasznos és sokoldalú eszközök, de dizájnjukból fakadóan nem felelnek meg az általunk felállított kritériumoknak. A következő részben végre rátérünk arra hogy az R miért is ideális nyelvészeti elemzésekre, de persze semmi sem tökéletes, az R-nek is vannak hátrányai!
