---
title: "Könyvismertető: Introduction to Linguistic Annotation and Text Analytics"
slug: "konyvismerteto-introduction-to"
date: 2011-06-09T08:24:00.002Z
publishDate: 2011-06-09T08:24:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/06/konyvismerteto-introduction-to.html"
regi_cimkek:
  - "könyvismertető"
regi_cimkek_mind:
  - "GATE"
  - "OpenNLP"
  - "Stanford NLP"
  - "UIMA"
  - "WordFreak"
  - "könyvismertető"
  - "text analytics"
---

**Sokak számára nehéz belépni a számítógépes szövegelemzés világába, legyenek akár nyelvészek (akiknek pl. nem volt alkalmuk programozást és/vagy formális módszereket tanulni) vagy informatikusok (akik pl. nem tanultak specifikusan számítógépes nyelvészetet, nem találkoztak eddig nyelvészeti elemzéssel). A most bemutatásra kerülő könyv nekik nyújt támogatást, és habár nem mentes a hibáktól, jelenleg nem ismerek jobbat a piacon.**

[  
](http://sites.morganclaypool.com/wilcock/)

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-8mnS_R2jDNA/TfCDeZLLwQI/AAAAAAAAAd8/zzSDU3cRyi4/s200/lata.jpg" rel="nofollow noopener">lata.jpg</a></span>](http://3.bp.blogspot.com/-8mnS_R2jDNA/TfCDeZLLwQI/AAAAAAAAAd8/zzSDU3cRyi4/s1600/lata.jpg)

[  
](http://sites.morganclaypool.com/wilcock/)

- [**Graham Wilcock: Introduction to Linguistic Annotation and Text Analytics**](http://sites.morganclaypool.com/wilcock/)

- **Synthese Lectures on Human Languages Technologies #3**

- **Morgan & Claypool Publishers, 2009**

- **160 oldal**

Hogy kiknek ajánlható a könyv azt nagyon nehéz meghatározni tudásszint alapján. Egy felsőbb éves nyelvész vagy informatikus hallgató haszonnal forgathatja, de sokkal fontosabb a hozzáállás. Sokszor hangsúlyozzuk hogy technikai könyveket másképp kell olvasni mint pl. egy nyelvészeti monográfiát. Lehet hogy erőltetett a párhuzam, de itt a lineáris olvasást nem a különböző források összevetésével kell megszakítani amikor feldolgozod a kötetet, hanem a feladatok elvégzésén túl meg kell próbálnod kitatlálni egy olyan mini projektet amire "rá tudod húzni" a tanultakat. Szintén fontos hogy akár a megjelenés után pár hónappal is változhat a technika és lehet hogy az olvasott útmutatások már elavultak, ilyenkor bátran kell kísérletezni és használni a keresőket. Sokkal inkább ezekre a készségekre kell koncentrálnod mint arra hogy mennyi nyelvészetet és informatikát szívtál magadba. Ha elfogadod hogy 160 oldal elolvasása eltarthat egy-két hónapig (bizony!!!), ha elfogadod hogy nem "kész ideákat" kapsz és tudsz így dolgozni, akkor való neked a könyv.

**Szeretném kiemelni hogy semmilyen programozási előismeret nem szükséges ahhoz hogy a kötetet megértsd** - viszont alapvető számítógép-használati jártasság kell (pl. ha adott egy bash szkript akkor futtathatóvá tudod-e tenni és tudod-e futtatni?). Mégis a gyakorló nyelvésznek sokat segíthet hogy automatizálja mindennapi munkájának egy részét, az informatikusok pedig megtanulhatják az alapfogalmakat, hogy mire vagyunk kíváncsiak amikor szöveget elemzünk és milyen eszközök állnak ehhez rendelkezésre (sőt, ha járatos az illető a Java nyelvben, akkor a kötet után kreatívan fel tudja használni a szabad szoftvereket saját projektjeiben!).

A kötet hat, egymásra épülő fejezetből áll. Az első fejezet a nyelvészeti annotációval és az XML markup nyelvvel ismertet meg minket a jEdit szerkesztő segítségével és egy kicsit megismerkedhetünk a GATE rendszerrel is. Ezt követően a mélyebben is megismerkedhetünk a témával és a WordFreak annotátorral. Külön érdekesség hogy nem csak az unalomig ismert POS taggingre tér ki a szerző, hanem a mondat- és szóhatárok beazonosításának és a szemantikai valamit egyéb annotáció problémáira is kitér és foglalkozik a parsing/chunking (ja, erre kérem nincs jó magyar szó...) gyakorlati alkalmazásaival is. Itt kapcsolódik a harmadik fejezethez, ami a Stanford NLP Tools és az OpenNLP használatát mutatja be. Gyakorlati példákkal szemlélteti a szerző hogy a tokenizálás és pos-taggelés rábízható ezekre az eszközökre és futtatásuk tényleg nem igényel három PhD-t. A két eszközt egy gyakorlat keretében össze is vethetjük, a Stanford NLP GUI-ját érdemes használni, ha másért nem akkor hogy szép fákat rajzoljunk vele! A NER (named entity recognition) és a korreferensek feloldásának külön kis alrész foglalkozik, habár ezek nagyon hasznosak és igazán sokat segíthetnek a hétköznapi munkában, sajnos inkább csak említésre kerülnek... A negyedik fejezetben visszatérünk az XML-hez és arra hogy miképp lehet és kell szabványos formátumokat használnunk hogy megoszthassuk munkánk gyümölcsét másokkal, ill. hogy a különböző eszközök dolgozhassanak egymás eredményeivel. Nem valami izgalmas téma, de szükséges a komoly munkához...

Ennyi sok áttekintés és alapozás után az ötödik fejezetben érünk el (végre) a komoly dolgokhoz. Itt részletesebben foglalkozik a szerző a GATE és UIMA rendszerekkel, amik tényleg nagyon jók és a fejezet az alapokban segít is, de túl nagyokat ugrik és gyorsan halad mire elér a címben említett Text Analytics fejezethez egy kicsit elszédülünk. Elvileg a hatodik fejezet mutatná be az egész szövegelemzés területét, amire kicsivel kevesebb mint 30 oldal biztos hogy kevés. Inkább általános útmutatóként tekintsünk a fejezetre ami egy példán keresztül mutatja be miképp segíthetnek nekünk a felvonultatott eszközök.

Azt senki ne várja hogy ebből a rövid könyvből szakértő lesz egy hét alatt. Elindulni azonban megfelel, sőt jelenleg ez a legjobb elérhető cím.
