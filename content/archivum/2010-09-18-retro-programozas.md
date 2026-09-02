---
title: "Retro programozás"
slug: "retro-programozas"
date: 2010-09-18T19:35:00.003Z
publishDate: 2010-09-18T19:35:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/09/retro-programozas.html"
regi_cimkek:
  - "kezdő"
  - "lisp"
regi_cimkek_mind:
  - "kezdő"
  - "lisp"
---

**A funkcionális programozás napjainkban egyre nagyobb teret nyer, habár már nagyon régen velünk van. Az egyik legöregebb programozási nyelv a LISP, ami bizonyos körökben éppen reneszánszát éli. Számunkra azért fontos ez a remek nyelv, mert a korai mesterséges intelligencia és számítógépes nyelvészeti kutatások paradigmatikus alkalmazásait LISP-ben írták, és területünk klasszikus műve, Norvig [Paradigms of Artificial Programming](http://bit.ly/dA4Shf) könyve, (nagyrészt) erről a nyelvről szól.**  
  
  
  
 Miért Common LISP?  
 Röviden: egyszerű elsajátítani. Hosszabban; biztos alapokat nyújt. Egy analógiával élve, egy klasszikus nyelven érteni annyit tesz, hozzáférhetsz a kulturális örökség alapjaihoz. De nem csak ennyit jelent, ha tudsz latinul, már tudsz egy nyelvet, tudod hogy kell nyelvet tanulni ezért gyorsabban haladsz. De ez nem csak ezt jelenti, az újlatin nyelveket még ennél is gyorsabban sajátíthatod el. Nos a LISP nem csak ezt adja neked, hiszen nem halott nyelv! De mindent megad neked amire szükséged lehet. Nem csak arra gondolok hogy kedvenc könyvemet te is értve elolvashatod segítségével, hanem betekintést nyerhetsz egy kultúrába. Ez a kultúra nagyon izgalmas. Ennek egy része az ún. "hacker culture",  a legjobb ha ezt magad kezded el felfedezni [Paul Graham](http://bit.ly/cNu4hJ) esszéin keresztül. A kultúra másik része, Norvigot plagizálva, a terület emblematikus könyveinek tanulmányozása, de minimum Abelson-Sussman-Sussman Structure and Interpretation of Computer Programs című klasszikusa kötelező annak aki komolyan veszi magát ezen a területen. Sajnos nem lehet kifogás hogy nem férsz hozzá, ugyanis a könyv (és sok kiegészítő anyag, pl retro videó egy kurzusról) elérhető [online](http://bit.ly/cNpBVc) ingyen!  
  
 Sokkal hosszabban: a funkcionális nyelvek egyre több teret nyernek. Haskell, Clojure, Erlang és R, mind mind a LISP programozók hagyományaiból táplálkozik és területünkön egyre többen használják ezek valamelyikét. Ezek nem könnyű nyelvek, szépek, hasznosak, de "forr körülöttük a levegő", állandóan alakulnak, kevés jó és kezdőbarát könyvet találsz róluk. Nem beszélve arról hogy a funkcionális programozás egyik előnye egyben a hátránya is; emacs függő. Nézzük hogy tudunk betörni ebbe a világba a lehető legkevesebb fejfájást okozva magunknak!  
  
**1. [Common Lisp: A Gentle Introduction to Symbolic Computation](http://bit.ly/cnRrNb)**  
 Szabadon hozzáférhető, nem hagyományos (programozó, matematikus) hátterű emberkék számára íródott bevezető könyv.  
**2. Egy LISP implementáció**  
 Lisp-ből több van. Nincs a LISP, a Common Lisp egy szabvány, bárki implementálhatja, akinek van kedve és mersze hozzá. Én a [Steel Bank Common Lisp](http://bit.ly/9yKkO0) híve vagy, mert szabad szoftver, jól hangzik a neve és megbízható. Ha neked neem jön be, egy kis kutakodással biztos találsz egy neked való implementációt.  
**3. Emacs és SLIME**  
 A legtöbb Linux disztribúció vagy tartalmazza eleve, vagy csomagkezelővel egyszerűen telepíthető az emacs ide (vagy valami ide-szerű valami). Hogy mi az emacs, nehéz elmagyarázni. A lényeg, hogy egy interfészként viselkedik az oprendszer felé, azaz bash parancsokat futtathatsz benne, egy kicsit szövegszerkesztő is, de ezen tulajdonságai összekeveredtek. A kezdők számára nehéz, de mivel maga az emacs is egy lisp dialektusban íródott természetesen összenőtt a Common (és egyéb) lisp-pel. Használatát [itt](http://bit.ly/a3VIuG) sajátíthatod el, kell egy kis idő megszokni, de mindenképpen megéri.  
 Ha már megismerted az emacs alapjait, fent van az sbcl (vagy más lisp implementáció) itt az ideje a [SLIME](http://bit.ly/a7g4uK) telepítésének. Ha eddig nem értetted mi a fenének van interaktív python, ruby stb felület. Mire jó bepötyögni a parancsot, visszakapni az eredményt, aztán amikor rájöttél valamire, pötyögheted be az egészet, vagy "kontrolcé-kontrolvéztél" akkor most le fog esni az állad. A slime segítségével adott neked a repl (read-eval-print-loop), azaz az interaktív felfedező cucc, megnyitsz egy forrást fájlt, szerkesztgeted és a fájlból szépen kijelölheted mit értelmezzen neked a repl. Egyszerűen bele fogsz szeretni. Gyorsan, görcsölés nélkül dolgozhatsz és az emacs betanulásába fektetett egy-két napod (órád, heted, stb) nagyon hamar megtérül.  
**4. Ha tetszett amit eddig láttál, lépj tovább**  
 Érdekel mit lehet kezdeni a Lisp-pel a "való világban"? Szabadon olvashatod Peter Seibel [Practical Common Lisp](http://bit.ly/ad9Dye) könyvét, hajrá!
