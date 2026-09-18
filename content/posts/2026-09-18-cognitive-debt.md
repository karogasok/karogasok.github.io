---
title: "Kognitív és egyéb adósságok felhalmozása a vibe coding során"
slug: "cognitive-debt"
date: 2026-09-18T07:00:00+02:00
publishDate: 2026-09-18T07:00:00+02:00
author: "Varjú Zoltán"
forras_url: "https://arxiv.org/abs/2603.22106"
forras_cim: "From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI"
tags: []
draft: false
temak:
  - Statisztika és R
kulcsszavak:
  - coding
  - vi
  - halmoz
  - tartozás
  - pair
---

A vibe coding hihetetlenül felgyorsította a fejlesztési folyamatokat. Ugyanakkor egyre több helyről hallani hogy a fejlesztők kezdenek kimerülté válni, a projektek pedig egyre átláthatatlanabbak és egy-egy változtatás egyre körülményesebb és egyre több nemszándékolt következménnyel jár. Storey nagyon meggyőzően szól arról, hogy ennek legfőbb okai 1) a vibe  coding technical debt-tel is jár - habár ez viszonylag könnyen orvosolható 2) kognitív tartozást halmozunk fel miközben egyre több mindent bízunk az AI-ra 3) mindeközben a projekt szándékaival szemben is tartozást halmozunk fel.

{{< kep src="cognitive-debt/Screenshot_2026-09-18_14-20-30.png"
        alt="ábra a hivatkozott tanulmányból"
        szerzo="Margaret-Anne Storey"
        forras="https://arxiv.org/pdf/2603.22106" >}}


Egy barátom ajánlotta ezt a tanulmányt, mert rögtön az egyik számomra legkedvesebb programozásról szóló esszére hivatkozik a szerző. Peter Naur (Programming As Theory Building)[https://pages.cs.wisc.edu/~remzi/Naur.pdf] című írását azért szeretem, mert hihetetlenül jól fogalmazza meg a programozás lényegét; egy adott probléma közös megértésenek externalizálása, "kódba öntése". Mivel egy közös megértésről van szó, egy bonyolult rendszer esetében ez azt jelenti, hogy a csapat közösen érti a rendszert. Nincs olyan ember aki mindent tud és ért. A vibe coding itt zavar be a képbe, ezt a közös megértést erodálja erősen. A projekt intencióival, szándékával kapcsolatban kérdések merülnek fel, ha azt a közös tervezés helyett különböző kódolási asszisztensek teljesen, vagy félig automatikus döntései veszik át.

Hogy mi a megoldás? Sosem gondoltam volna, hogy egy szoftverfejlesztésről szóló tanulmányban McLuhan-re találok hivatkozást, de már ezen is túl vagyok! A megoldás régi technikák újbóli használata (technological retrieval), mint pl specifikáció, tesztek, stb írása, frissen tartása, pair programming, walkthrough stb. Nyilván nem a régi megszokott formában. Én pl az aider-rel imádok pair programmingban dolgozni, de elképzelhetetlennek tartom hogy egy teljes kódbázis minden során végig tudjon menni az ember. Persze lehet technológiával segíteni a több dolgon is.  Viszont ezek már nem technikai készségeket igényelnek, hanem inkább fejlett kritikai gondolkodást és a jó kommunikációs- és íráskészséget.
