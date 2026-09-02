---
title: "Facebook Graph Search"
slug: "facebook-graph-search"
date: 2013-01-18T12:38:00.001Z
publishDate: 2013-01-18T12:38:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/01/facebook-graph-search.html"
regi_cimkek_mind:
  - "Facebook Graph Search"
  - "hülyeség"
---

**A héten jelentették be a Facebook Graph Search elindulását. A béta szolgáltatás csak kevés kiválasztott és gyorsan jelentkező felhasználóknak érhető el. Sőt - a Facebook oldalán is olvasható - kizárólag az Egyesült Államok területén, a US English felületet használók válhatnak béta tesztelőkké. Persze ez nem zavar senki abban, hogy véleménye legyen.**

Kezdjük az amúgy általam nagyon kedvelt [Webisztán "elemzésével"](http://webisztan.blog.hu/2013/01/15/facebook_graph_search_reszkess_google).

*A Facebook lényegi ereje, a felhasználók közötti ezerféle kapcsolódás a lájkok és egyéb információk révén nagyon jó támpont ahhoz, hogy szemantikusabb keresőt tudjanak építeni, mint ma a Google. Vagy legalábbis megpróbáljanak.*

Ez akár igaz is lehetne. Ne bonyolódjunk a szemantika szó kapcsán szemantikai vitákba, koncentráljunk a lényegre! A Facebook nem szemantikusabb a Google-nél még ebben az értelemben sem. A[ Google 2010-ben vásárolta meg a Metawebet](http://en.wikipedia.org/wiki/Metaweb), azóta van egy nagyon tuti, tényleg szemantikus adatbázisa, a [Freebase](http://www.freebase.com/). Ezen is alapul a [Google Knowledge Graph](http://www.google.com/insidesearch/features/search/knowledge.html), aminek az eredményeit mindenki látta már, a pici kis dobozokban amik jobb oldalt keretben jelennek meg bizonyos esetekben a találati oldalon.

Persze valahogy a big data és/vagy az analitika is bele kell hogy kerüljön egy rendes tech posztba!

*Ha idén még nem is kell feltétlenül azzal számolnunk, hogy a Facebook alapvetően megváltoztatja például a keresőoptimalizálásról alkotott képünket. De mindenesetre új horizontokat mutathat az analitikának, mely a nem olyan távoli jövőben már nem csak arctalan emberek által generált aktivitásokkal tud majd számolni, hanem nagyon is emberi jellemzőkkel. Úgyis mint a személyes ízléshez, preferenciákhoz, szakértelemhez, aktivitáshoz kapcsolódó információkkal.*

Ne legyünk igazságtalanok, a Facebook biztos elő fog jönni majd valami olyannal mint a Google Analytics meg a Trends - az az analitika. Amire a szerző gondolt, az az lenne, ami már a nagyoknak meg is van - a társadalomtudományi elemzők hada. Aki hosszú olvasmányra vágyik, annak ajánlom a Technology Review-n még a nyáron megjelent [What Facebook Knows](http://www.technologyreview.com/featuredstory/428150/what-facebook-knows/) c. cikket. Lelövöm a poént, a Facebook a fenti szempontok szerint elemzi saját "kis" adatbázisát és igen, szeretne valahogy pénzt csinálni belőle. Vegyük észre, maga az idézett cikk a Graph Search előtt keletkezett, ez setetni engedi hogy az ilyen irányú kutatások már 2012 nyara előtt elindultak. Ez összecseng avval a ténnyel hogy mind a Microsoft, mind a Google (és még a Yahoo! is) tart pár társadalomtudóst. (L. Microsoft Research  a "Research Areas" és a "Research Groups" alatt találunk ilyeneket, a Google esetében meg [Hal Varian](http://en.wikipedia.org/wiki/Hal_Varian) a hasonló csapat sztárja)

Nézzük a következőt, az Onlinemarketing blogot. A [Graph Serch-ről írt poszt](http://onlinemarketing.blog.hu/2013/01/15/hova_raktam_kulcsom) kapcsán itt is találkozhatunk pár nagyon érdekes dologgal.

A természetes nyelvi keresésről.

*Voltak, vannak kísérletek persze az ilyen típusú keresések feldolgozására, ott van ugye a [Wolfram Alpha](http://www.wolframalpha.com/) vagy éppen az Apple Siri-je, de ezek nem igazán terjedtek el a mindennapi használatban, hiszen bár demonstrálni tudták a megoldást, de nincs elég nagy adatbázis a háttérben.*

[A TR ugyanerről a témában](http://www.technologyreview.com/news/509986/facebooks-graph-search-wont-hurt-google-without-your-help/).

*[Greg Ver Steeg](http://www.isi.edu/people/gregv/about), a computer scientist who studies social networks at the University of Southern California’s Computer Sciences Institute, is skeptical that users will want to spend much time feeding complex queries into Graph Search. “The really successful additions to social media are things that reduce your cognitive load, not add to it—things that make it easier and more automatic to find what you like,” he says.*

Igen, attól hogy autoritásokra hivatkozunk, még éppen lehet a szerzőnek igaza. De gondoljunk bele, a Microsoft felvásárolta a [Powerset ](http://en.wikipedia.org/wiki/Powerset_(company))keresőt, a lényeges megoldásokat integrálta a Bing-be és hagyta a fenébe a természetes nyelvi keresést. Ma az iparban bevett nézet, hogy az aki természetes nyelvi "question answering" témában mozog, az beszédtechnológia felé kacsingat. Ez pedig egyenlő a mobil iránnyal, mivel ott ez egy természetesebb interakciót tesz lehetővé és a technikai feltételek ha nem is tökéletesek, de már adottak. (Bővebben erről l. a [Kereső Világon megjelent írásomat](http://kereses.blog.hu/2012/08/28/nuance_beszedtechnologia_mint_szolgaltatas).)

Szakmázzunk tovább! A question answering általában tényanyagokon működik a legjobban, ez kb. köztudott tény a szakmában. És ebből ki is lehet találni, mindenki a Wikipedia feldolgozásával kezd ilyen rendszer kifejlesztésébe ([bővebben a témáról a Kereső Világon](http://kereses.blog.hu/2011/11/02/kerdezz_felelek_957)). További tény, hogy gyakran csalás áldozata az aki természetes nyelven keres, hiszen ilyenkor gyakran kiszűrjük a tölteléket és csak a kulcsszavak maradnak a tényleges query-ben. Ezzel ellenben a vizsgált írás szerint:

*A Google pedig egy érdekes helyzetbe került: az erősségük a meglévő, nyilvános weboldalak feldolgozása, azt tudják adni találatra, amit a weben meg lehet mutatni. És a weben nem nagyon van olyan szöveg, ami a fenti hosszú kérdésemet értené, hiszen a kritikák vagy éppen a filmleírások nem ilyen gondolkodásmóddal és tartalommal bírnak*

Nem tudom kinek is hihetek... Talán maradok [a kedvenc könyvemnél](http://www.amazon.com/Speech-Language-Processing-Daniel-Jurafsky/dp/0131873210) és elvetem a fenti állítást. Félve teszem még ehhez, a Google bizonyos esetekben "érti" mit kérdezünk tőle. A már említett Google Knowledge Graph-ról érdemes olvasgatni ([igen, a Kerső Világon](http://kereses.blog.hu/2012/03/20/google_knowledge_graph)), továbbá érdemes egy kicsit a [Google Now-val is ismerkedni](http://kereses.blog.hu/2012/07/10/google_now_a_gondolatolvaso) ha már a témánál vagyunk!

De akkor mi van a Graph Search-el, hogyan működik, mit tudhatunk róla? A tény, hogy [a Kereső Világon erre is megtalálható a válasz](http://kereses.blog.hu/2013/01/16/facebook_graph_search) azt mutatja, az információ elérhető erről. Úgy látszik, a számítógépes nyelvészet és a keresés osztozik a nyelvészet sorsában; mindenkinek van véleménye róla. De a két tárgyalt posztról nekem egyik kedvenc témám, a "tudománytalan rokonítási kísérletek"  jutottak eszembe. A hobbi nyelvészek valamit hallottak arról, hogy hogyan hasonlítunk össze két nyelvet és egy-egy szóba, kifejezésbe csimpaszkodva kihozzák a sumér-magyar rokonságot. Általában ezek az alakok az önjelölt számítástechnikai zsenik is...
