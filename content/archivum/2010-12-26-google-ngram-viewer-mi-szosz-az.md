---
title: "Google Ngram Viewer - Mi a szösz az?"
slug: "google-ngram-viewer-mi-szosz-az"
date: 2010-12-26T19:36:00.002Z
publishDate: 2010-12-26T19:36:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/12/google-ngram-viewer-mi-szosz-az.html"
regi_cimkek:
  - "Google"
  - "digitális bölcsészet"
  - "keresés"
  - "korpusznyelvészet"
  - "lexikológia"
  - "nyelvtechnológia"
  - "nyelvtudomány"
  - "nyelvészet"
  - "számítógépes nyelvészet"
  - "szöveg vizualizáció"
regi_cimkek_mind:
  - "Google"
  - "digitális bölcsészet"
  - "keresés"
  - "korpusznyelvészet"
  - "lexikológia"
  - "nyelvtechnológia"
  - "nyelvtudomány"
  - "nyelvészet"
  - "számítógépes nyelvészet"
  - "szöveg vizualizáció"
---

**A Google Labs mostanában indította el Books Ngram Viewer szolgáltatását és megjelntek a legkülönbözőbb "elemzések" mindenhol - még a print HVG-ben is találtam! Arról viszont kevés szó esik hogy mit is takar tkp. ez a szolgáltatás, miért indította el a Google, mi egyáltalán az az ngram (vagy jobban mondva n-gram) és mire jó ez azon kívül hogy szép grafikont rajzolunk.**  
  
  
  
  
  
 Azok a fránya szerzői jogok nem teszik lehetővé hogy a Google publikálja beszkennelt könyveit. Miközben szidjuk hogy elöli a versenyt stb stb azért szeretnénk ha minden könyv kereshetővé válna (pláne hogy elérhető is legyen!) és lássuk be hogy a szidáson kívül nem sok semmi történt eddig, pedig nem ártana erre is áldoznunk egy kicsit... Gondoljunk bele hogy ha kezünkben van digitális formában az összes eddig publikált könyv akkor milyen távlatok nyílnak. De mi van ha ezek jelentős része ilyen-olyan módon jogvédett? Erre nyújt megoldást a bag-o-words (vagy szépen [bag-of-words](http://bit.ly/exSk2f)) módszer, amit itt is alkalmaznak. Persze a hivatkozott Wikipedia szócikk itt nem segít sokat, hiszen a Google [Harris](http://bit.ly/fBeDz7) (aki Chomsky-ra is nagy hatással volt, no meg a matematikai nyelvészet egyik alapító atyája is egyben) eredeti módszerét használta, azaz szóláncokat alkotott, amik n-gramok. Az 1-gram az ugye egy darab árva szó (pl. vizsla), a 2-gram (vagy bi-gram) két szóból álló lánc (pl. magyar vizsla) és így tovább n-ig (pl. a 'drótszőrű magyar vizsla kölykök ugattak'  egy 5-gram). Miért jó ez? Mert azt senki nem tiltja hogy egy adott műben előforduló szavakat reprodukáljunk! Sajnos nem tudom hogy a magyar jogrendszerben ki lehet-e kerülni a szerzői jogok jelentette korlátokat, de ha igen, az sokat jelentene a hazai korpusznyelvészet számára is... De a lényeg hogy a Google Books projekthez összeszedett 1800 és 2000 között beszkennelt nagy nyelveken (angol, francia, spanyol, német, orosz és a sorból kilógó héber) megjelent kötetek becslések szerint az eddig megjelent könyvek kb 4 százalékát teszik ki (a továbbiakban külön nem hivatkozom a [Quantitative Analysis of Culture Using Millions of Digitalized Books](http://bit.ly/hAkIrW) cikkre, a poszt megírásában olyan nagy mértékben támaszkodom rá, hogy akár minden második mondathoz belinkelhetném, sajnos azonban a link korlátozott hozzáférésű tartalomra mutat).  
  
 De mire jó ez az ngram viewer? Nos még így zanzásítva is a bag-o-words modell értékes információt nyújt számunkra a nyelvről, sőt ha kizárjuk a nem tudományos műveket (fiction), akkor bizony még a tudománytörténetébe is beleláthatunk, vagy a kultúrtörténetünket is jobban megismerhetjük. A Google egy tőzsdei cég és ezt egészen nyilvánvalóan nem profithajhászás céljából teszi, de ettől aki utálja, az csak tegye, nem akarom reklámozni a céget -  viszont aki követné a példáját és felkarolná a digitális bölcsészetet az nagyot nőne olvasóink (és a világ :D) szemében. Ez amolyan érdeklődés - majd csak jó lesz majd valamikor valamire - és [CSR](http://bit.ly/hMtyrm) (társadalmi felelősségvállalás) egyszerre mivel a Google felkarolta a digitális bölcsészet ügyét és bőkezűen támogatja az új diszciplínát (érdemes a bejelentést elolvasni [itt](http://bit.ly/dYN6Tg)).  
  
 A "hagyományos" bölcsészettudományok művelői nem szeretik a kvantitatív elemzést hiszen tudományuk lényegének tekintik a kvalitatív megértést. Azonban egyre kevesebben zárkóznak el attól hogy a megértést "kisegítsék" és egyre többen csatlakoznak a digitális bölcsészet módszertanához (az érdeklődő olvasót itt azonban átirányítom [Mire jó a digitális bölcsészet?](http://bit.ly/ihFEoG) című posztunkhoz). A már említett tanulmány szerzői propaganda gyanánt elvégeztek pár vizsgálatot hogy bemutassák milyen területeken lehet alkalmazni az új eszközt, érdemes ezeket áttekinteni:

- Lexikológia - mekkora egy-egy nyelv lexikona (az angol nyelv esetében 1, 022, 000 szót találtak 2000-ben de csak 544, 000 darabot 1900-ban, továbbá megállapították a szerzők hogy az utolsó ötven évben hetven százalékkal bővült az angol nyelv szótára), a lexikon/szótárkészítők kereshetnek alacsony gyakoriságú új szavak után is

- Grammatikai változás - hogyan változott a rendhagyó igék alakja (pl a learnt/learned változatok gyakorisága hogyan változott az idővel)

- Miképp jelenik meg a történelmi tudat a művekben? - hányszor jelenik meg egy jelentősebb évszám (pl. 1789), milyen korokban válik fontossá egy esemény, mely történelmi alakok nevei fordulnak elő gyakran egy adott korban ill. mikor kerülnek ismét elő

- Cenzúra és egyéb nyomásgyakorlás - a cenzúra nyomot hagy a művekben, pl. a nácik által nem éppen kedvel Marc Chagall nevének gyakorisága az angol munkákban emelkedik az 1936 és 1944 között miközben a német nyelvű könyvekből eltűnik

Magát a kvantitatív elemzést a szerzők [culturomics](http://bit.ly/hsD7RR)-nak nevezték el ami jól hangzik, de nem jelent más mint nagy mennyiségű adat elemzése a digitális bölcsészet és a komputációs társadalomtudományok területén. Az Ngram Viewer nem tesz mást mint a nagy rakás bag-o-words-öt kereshetővé teszi és a szépen megjeleníti az eredményt egy grafikonon.  Ez csak arra jó hogy apró, relatív trendeket keressünk. Vegyük például a filozófia nyelvi fordulatát (ez az ún. [linguistic turn](http://bit.ly/eWaX9s)) amely a múlt század hatvanas éveiben kapott nevet és vált elterjedtté, azonban az 1880-as évektől datálhatjuk létrejöttét. Vessük ezt össze a tudományfilozófia "népszerűségével".

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/_SM9YHwWrX6M/TReaGVn_YKI/AAAAAAAAAX8/7MEMrzT6ZF4/s640/Google+Ngram+Viewer_1293391542902.png" rel="nofollow noopener">Google+Ngram+Viewer_1293391542902.png</a></span>](http://2.bp.blogspot.com/_SM9YHwWrX6M/TReaGVn_YKI/AAAAAAAAAX8/7MEMrzT6ZF4/s1600/Google+Ngram+Viewer_1293391542902.png)

Az ábra szép és láthatjuk hogy a tudományfilozófia gyakoribb terminus (vagy n-gram), de a hatvanas évektől mindkettő emelkedik mégpedig tendenciózusan. Amit az ábra nem árul el az az a tény hogy a tudományfilozófiában is fordulat következett be a hatvanas években, mégpedig a nyelvi fordulattól inspirálva. Az ábrával még nem mondunk semmit, csak akkor ér valamit az elemzés ha kontextus tudunk mellé állítani. Így habár érdekes és értékes eszközt adott kezünkbe a kereső óriás, mielőtt használatba vesszük vegyük figyelembe korlátait és céljait és ne illesszünk n-grammokat minden megnyilatkozásunkhoz.
