---
title: "Tudatkutatás és AI"
slug: "ai-consciousness"
date: 2026-09-28T07:00:00+02:00
publishDate: 2026-09-28T07:00:00+02:00
author: "Varjú Zoltán"
forras_url: "https://www.anthropic.com/research/global-workspace"
forras_cim: "A global workspace in language models"
tags: ["tudat", "AI", "kognitív tudomány", "neurális hálók", "elmefilozófia", "bázis kogníció"]
draft: false
temak:
  - Mesterséges intelligencia
  - Tudományfilozófia
  - Megismerés és idegtudomány
kulcsszavak:
  - tudatosság
  - J-space
  - Hoel
  - tudat
  - munkaterület
---

Mostanában a tudat kérdése ismét divatos; pár hónapja [Richard Dawkins arra jutott, hogy Claude bizony öntudattal rendelkezik](https://unherd.com/2026/05/is-ai-the-next-phase-of-evolution/), majd Carlo Rovelli bejelentette, hogy a tudat nehéz problémája ([hard problem of consciousness](https://en.wikipedia.org/wiki/Hard_problem_of_consciousness)) tudománytalan. Nekem ez azért vicces, mert Dawkins úgy érzi, hogy Claude tudattal rendelkezik, mert azt érzi. Rovelli pedig pont tudománytalannak tartja a nehéz problémát, mert nem igazán lehet operacionalizálni, azaz pont ezt az érzetet, kválét szeretné végleg kiiktatni. 

{{< kep src="ai-consciousness/Gemini_Generated_Image_3vhauu3vhauu3vha.jpeg"
        alt="Absztrakt, csurgatásos festmény: egymásba gabalyodó fekete, kék, piros, sárga és fehér festékvonalak és -foltok"
        szerzo="Gemini által generált kép" >}}

Mindeközben két nagyon izgalmas fejleménnyel érdemes még foglalkozni. Az első az Anthropic J-space “felfedezése”, ami tkp. nem más, mint egy globális munkaterület. A [globális munkaterület elmélete](https://en.wikipedia.org/wiki/Global_workspace_theory) szerint az észlelés, memória, figyelem, stb. egy központi munkaterületre szállítják az információt. Az elmélet szerint ennek a munkaterületnek a megléte a tudatosság szükségszerű feltétele, mivel globálisan hozzáférhetővé teszi az információt (ezért hozzáférési tudatosságnak is szokás nevezni), azaz általa tudunk reflektálni a minket érő ingerekre, tudjuk előkeresni az emlékeinket, stb. Az Anthropic által azonosított J-space hasonlóan működik a Claude-ban: egy olyan belső központ, ahol a modell a végső kimenettől függetlenül dolgozza fel az aktív koncepciókat. Sikeresen teljesíti a "hozzáférési tudatosság" öt fő feltételét:

+ Jelenthetőség: A modell képes pontosan beszámolni a J-space aktuális tartalmáról.

+ Irányított moduláció: Képes belső, "csendes" gondolkodásra egy fogalomról anélkül, hogy az a kimeneti szövegben megjelenne.

+ Belső érvelés: Itt hajtja végre a több lépésből álló feladatok köztes logikai és matematikai lépéseit.

+ Rugalmas általánosítás: Egy információ célzott megváltoztatása a J-space-ben automatikusan és strukturáltan frissíti az összes ahhoz kapcsolódó válaszát.

+ Szelektivitás: A J-space kikapcsolása tönkreteszi a komplex, célirányos problémamegoldást, miközben az automatikus nyelvtani és folyékony beszédkészséget teljesen érintetlenül hagyja.

"Nem rossz!" - mondhatnánk. "Na és akkor mi van?" - tehetjük fel a kérdést. Egyrészt tényleg érdekes ez az eredmény, másrészt a tanulmányban felvetett esetleges biztonsági kérdések is relevánsak. De attól, hogy ez a terület úgy tűnik, a Claude-on kívül más LLM-ekben is azonosítható, még nem mondhatjuk, hogy megjelent a tudatosság.

De egyáltalán, mi a fene az a tudatosság? Hogyan definiáljuk? A rossz hír, hogy nem lehet mindent definiálni, hiszen valahol meg kell állni, különben definícióink körkörösek lesznek. [Erik Hoel arra hívja fel a figyelmet](https://arxiv.org/pdf/2512.12802), hogy a tudatosságelméleteknek egyszerre kell falszifikálhatónak és nem-triviálisnak lenniük. Hoel szerint egy elmélet akkor falszifikálható, ha ütközhet egymással az, amit a rendszer belső működéséből jósol, és az, amit a rendszer beszámolóiból és viselkedéséből következtetünk. Triviális pedig akkor, ha a jóslatai ugyanarra a bemenet–kimenet adatra épülnek, mint a beszámolók, így sosem tévedhet. A nem-trivialitás kérdése nagyon izgalmas az LLM-ek esetében. Hoel levezeti, hogy egy LLM bemenet–kimenet viselkedése elvileg reprodukálható egyetlen rejtett réteggel rendelkező, statikus hálóval, az pedig egy lookup táblával. Egy sima lookup pedig nem igazán tekinthető tudatosnak.

De igazából a nehéz problémával nem tud se Hoel, se az Anthropic J-space mit kezdeni. Bármennyire ellenzi Rovelli, a tudatosságnak igenis van egy szubjektív része. Frank Jackson klasszikus epifenomenális [kválék](https://hu.wikipedia.org/wiki/Kv%C3%A1l%C3%A9)ról szóló [esszéjében](https://www.sfu.ca/~jillmc/JacksonfromJStore.pdf) van egy remek gondolatkísérlet. Képzeljük el Maryt, a kiváló idegtudóst, aki valamilyen oknál fogva egy fekete-fehér szobából, fekete-fehér képernyőt használva kutatja a látást. Tudja, milyen agyi területek aktiválódnak és milyen hullámhosszú fény érkezik a retinához, amikor egy piros paradicsomot, vagy egy piros almát lát valaki, tudja, milyen mintázatot mutat a fehér lap, vagy a hó észlelése. Minden külső információ rendelkezésére áll a megértéshez, amikor valaki azt mondja “Az ég kék”, vagy “A fű zöld”. Tegyük fel, egy napon Mary kijön a szobájából vagy csak kap egy színes monitort. Elmondhatjuk, hogy bármi újat megtudhat a látásról? Ha igen, akkor el kell fogadnunk, hogy a látás nem csak az összes rendelkezésre álló fizikai információ összessége, hanem valami más, valami je ne sais quoi.

A másik kérdés, hogy mi lehet tudatos. Csak neurális aktivitás járhat együtt tudattal, vagy esetleg más is? Csak szerves anyagok kellő komplexitása, vagy más is rendelkezhet vele? A neurocentrikus elméletek lassan, de biztosan bomlanak lefelé. Egyrészt Chalmers és Clark [kiterjesztett elme](https://crowintelligence.org/aporia/epistemic-arcade/) (figyelem, a hivatkozás önpromó) elmélete szerint az elme nem áll meg a koponyánknál, különféle eszközöknek szervezzük ki a feladatait. Illetve az elme befelé sem áll meg a koponyánknál: [egyesek a bélmikrobiomot is kognitív rendszerünk részének tekintik](https://link.springer.com/article/10.1007/s10539-021-09790-6) illetve [a mikrobiom–bél–agy tengely fontosságára hívják fel a figyelmet](https://pmc.ncbi.nlm.nih.gov/articles/PMC6282467/). Másrészt [Michael Levin](https://aeon.co/essays/how-to-understand-cells-tissues-and-organisms-as-agents-with-agendas) munkássága is azt mutatja, hogy alsóbb szinteken is megjelenik a célorientált viselkedés (pl. sejt, szövet). Mennyire jár együtt a kognitív képességek komplexitása a tudatossággal? 

Ha elfogadjuk, hogy van kvále, akkor el kell fogadnunk, hogy nem vagyunk képesek pusztán fizikai magyarázatot adni a tudatra. Ha abból indulunk ki, hogy márpedig van valamilyen fajta tudati élmény, hívják azt bárhogyan is, akkor könnyen pánpszichistává válhatunk. Az [integrált információ elmélete](https://en.wikipedia.org/wiki/Integrated_information_theory) is evvel kacérkodik, amikor mindennek tulajdonít valamennyi tudatosságot. Egy kavicsnak nyilván nullához közelít ez az érték, egy békánál magasabb, míg egy ember esetében egész magas. Hogy miért? Mert más a kauzalitási komplexitásuk. A kauzális komplexitás befelé az önfenntartást jelenti, ahogy az egyes részek együttesen és külön-külön törekednek fennmaradásra. Ez mérhető avval is, hogy mennyire bontható egy adott rendszer önállóan is működőképes alrendszerekre. Pl. az emberi agy nagyon integrált, egyben nagyon specializált részekből áll, melyek egymásra folyamatosan hatnak. Hoel viszont máshol ragadja meg a legnagyobb különbséget az ember és az LLM-ek között: a folyamatos tanulásban. Az emberi agy minden élménnyel változik, az LLM viszont a tanítás után statikus. Ugyanarra a bemenetre, a teljes addigi beszélgetéssel együtt, mindig ugyanazt adja; az ún. in-context learning csak visszatáplált kontextus, nem valódi tanulás. Lehet, szuper cikket ír az LLM, mindenkinél jobban kódol és úgy általában nagyon intelligens, de “senki sincs otthon”, hogy minderre reflektáljon.

Lehet, itt nem is a válaszok fontosak, hanem a kérdések!
