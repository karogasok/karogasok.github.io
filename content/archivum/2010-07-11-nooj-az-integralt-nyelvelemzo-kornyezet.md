---
title: "NooJ, az Integrált Nyelvelemző Környezet I."
slug: "nooj-az-integralt-nyelvelemzo-kornyezet"
date: 2010-07-11T19:59:00.001Z
publishDate: 2010-07-11T19:59:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/07/nooj-az-integralt-nyelvelemzo-kornyezet.html"
regi_cimkek:
  - "nltk"
  - "számítógépes nyelvészet"
  - "vendégposzt"
regi_cimkek_mind:
  - "NooJ"
  - "korpusz nyelvészet"
  - "nltk"
  - "nyelvelemző"
  - "számítógépes nyelvészet"
  - "vendégposzt"
---

VENDÉGPOSZT!

**Előzetesnek szánom ezt a cikket. Bemutatni, hogy mennyi és milyen minőségű nyelvelemző programok állnak már jelenleg is a rendelkezésünkre. De előzetes abban az értelemben is, hogy az eszközökről szeretnék majd több hosszabb-rövidebb leírást is adni. És nem utolsó sorban előzetes abból a szempontból is, hogy a későbbre tervezett Natural Language Toolkit használatát fogjuk a most bemutatott NooJ eszközzel megalapozni.**

A NooJ, és elődje az INTEX egy integrált nyelvelemző környezet. Egy francia nyelvész készítette, aki ráébredt arra, hogy rengeteg szakterület tudná alkalmazni, használni a saját céljaira egy nyelvelemző rendszert. A többi nyelvelemző ellen mindig az első ellenérv a kezelhetőség volt. Még a jelenleg a PTE-n fejlesztett (prolog nyelven fejlesztett) szövegelemzőről is (bár csak néhány bemutatót sikerült erről a fejlesztésről megszereznem...) első hátrányként említik, hogy nehezen kezelhető, olvasható az eredmény. Ez azért könnyedén orvosolható lenne. Mindenesetre megértem azokat, akik csak egy-egy ötletért nem hajlandóak ennyire belemerülni a témában. Pont a számukra lehet a legideálisabb eszköz a NooJ.

Szerencsére a témának van magyar honlapja. [http://corpus.nytud.hu/nooj/ ](http://corpus.nytud.hu/nooj/%20)címen tudjátok elérni. Itt található meg hozzá továbbá a magyar modul is, amivel el tudjuk végezni az elemzéseinket. Illetve a kipróbáláshoz ajánlom mindenki figyelmébe Vajda Péter bemutatását: [http://corpus.nytud.hu/manye/vp_nooj.ppt](http://corpus.nytud.hu/manye/vp_nooj.ppt)

Hogy van magyar honlapja, ez sajnos nem egyenlő azzal, hogy fejlesztik is. 2006-ban indult, és azóta csak a magyar modul került fel. De a még akkoriban tervezett grammatika nem jelent meg azóta sem.

A NooJ a morphdb.hu-t használja. Akik használták már külön, azoknak nem lesz meglepetés a szavak elemzésének eredménye vagy a típushibái, de ezeket könnyedén javíthatjuk az aktuális szövegnél. Viszont a NooJ nem csak erre képes. Lehetséges vele szógyakoriságot vizsgálni, ahogyan lehet csak simán szegmentálni. Saját nyelvtannal kiegészítve pedig határ a csillagos ég. És akkor még nem is beszültünk arról, hogy képes az elemzett szöveget xml-formátumban visszaadni, tehát az eredményen tovább dolgozhatunk például az NLTK-val... de erről majd csak később.

Egy-két javaslatot azért tennék a program használatához. A Huntoken mondatszegmentálót használja. Ezért a legjobb eredmény érdekében minden sorban csak egyetlen mondat szerepeljen! Továbbá mivel a szavak elemzéséhez a Hunmorph-ot használja, így nem számítsunk eredményre a tulajdonnevek és a szóösszetételek esetén. Ezeket nem tudja kezelni.

Továbbá álljon itt egy minta is. Példaként és a várható eredmények előrejelzése végett. Ezt a cikket elemeztettem le vele, egészen eddig a bekezdésig:

-

Összesen 	26 mondat

-

242 	különböző szóalak

-

30 	olyan szó, aminek nem tudta meghatározni a szófajtát, 	felépítését (tulajdonnevek, formátumtípusok, webcímek és 	szóösszetételek)

-

426 	különböző felismert és elemzett szóalak (a kettő szám azért 	nem egyezik, az összes szóalak és az elemzett szóalakok száma, 	mert sok olyan szóalak van, ahol elképzelhető több elemzési 	eredmény a szövegkörnyezetnek megfelelően, de a program jelzi 	számunkra a lehetséges elemzéseket. Például a „szánom” két 	elemzési módja a következő: szánom,szán (szótő): 	N+nom+1+sg+pssg+ps vagy V+1+def+sg. Itt az emberi értelem meg tudja 	határozni, hogy az igei a helyes, de ezt csak jelentéstanilag 	tehetjük meg. Egy másik szövegkörnyezetben már főnévként 	szerepelhet.)

**Szerző:**

**Gerő Dávid: Magyar és nyelvtechnológus hallgató,** kezdő programozó és webfejlesztő, aki érdeklődik a nyelvészet és az informatika iránt. A határterületekért különösen rajongok, de sajnos mindkettőben csak kezdő, érdeklődő laikus vagyok.
