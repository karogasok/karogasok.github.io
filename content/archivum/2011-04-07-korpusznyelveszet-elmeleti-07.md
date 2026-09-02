---
title: "Korpusznyelvészet – elméleti megfontolások"
slug: "korpusznyelveszet-elmeleti-07"
date: 2011-04-07T15:05:00.004Z
publishDate: 2011-04-07T15:05:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/korpusznyelveszet-elmeleti_07.html"
---

**Mi is az a korpusznyelvészet? Sokan úgy tekintenek a korpuszokra mint a nyelvi adatok egyetlen lehetséges forrásaira, mások azt hiszik hogy ez valami nagyon új irányzat, de szeretnénk lehűteni a kedélyeket – a korpusznyelvészet ugyanis egy módszertani irányzat, se nem több, se nem kevesebb. Sajnos azonban ezt az irányzatot is „megfertőzte” a szokásos irány és szeretik a korpusznyelvészek is Chomskyval szemben meghatározni magukat. Vizsgáljuk meg egy kicsit közelebbről a két legelterjedtebb ködképet a korpusznyelvészetről.**

**A korpusznyelvészet egy új dolog**

Sokan azt hiszik hogy a korpusznyelvészet új, hiszen manapság korpuszon számítógépekkel olvasható elektronikus korpuszokat értünk. A nyelvi adatok elemzéséhez kapcsolódik a statisztika és sokan el sem tudják képzelni hogy a modern eszközök és elméleti háttér nélkül is lehetett korpuszt vizsgálni. Mielőtt bárki azt hinné hogy visszamegyünk a régi görögökhöz, megnyugtatok mindenkit hogy ettől nem kell félni. Az adatok természetesen a nyelvészeti munka részét képezik, így amióta létezik a nyelv módszeres tanulmányozása, születnek különböző szótárak, szószedetek stb. Tehát a változást ott kell keresnünk amikor az adatokkal nem egy-egy elméletet vagy nyelvtani szabályt akartak alátámasztani visszamenőlegesen hanem pont fordítva az adatokból szerettek volna nyelvi törvényszerűségeket megállapítani.

-

[Zipf 	szógyakorisági megfigyelései ](http://en.wikipedia.org/wiki/Zipf%27s_law)a legismertebbek, ezeket a múlt 	század harmincas, negyvenes éveiben publikálta, szorgos kétkezi 	munkával gyűjtve az adatokat

-

[Roberto 	Busa](http://en.wikipedia.org/wiki/Roberto_Busa), akit minden rendes digitális bölcsész mint alapító 	atyát tisztel, a skolasztikus szerzők szövegein végzett 	kutatásokat, amikor összehozta a sors az IBM egyik igazgatójával, 	[Thomas J. 	Watson](http://en.wikipedia.org/wiki/Thomas_J._Watson)-nal (biza, a Watson neve rá is utal!) és 	(lyukkártyákon!) elkészült az első nagy korpusz, 	konkordanciákkal és minden szépséggel, 10,600,000 szóval! Busa 	és csapata emellett még egy ötmillió szavas többnyelvű 	korpuszt is összedobott, mindezt az 1950-es években!

-

Mosteller és Wallace 1964-ben 	végzett bayesiánus elemzést többek között szöveg 	kategorizálás, szerző megállapítás és stilometria területén. 	Mindezt pedig kézzel, öt éven keresztül 80 diák segítségével! 	[Könyvük](http://www.amazon.com/Applied-Bayesian-Classical-Inference-Federalist/dp/0387909915) a mai napig a terület klasszikusa!

A hatvanas években szerencsésen összeért a két irányzat, a számítógépek fejlődésével búcsút inthettünk a lyukkártyáknak, a kézzel végzett számlálást (és számításokat!) felváltották a gépek és megszülettek az ismert korpuszok, mint pl a [Brown korpusz](http://en.wikipedia.org/wiki/Brown_Corpus) vagy a BYU [Corpus of Contemporary American English](http://en.wikipedia.org/wiki/BYU_Corpus_of_American_English) és a [British National Corpus](http://en.wikipedia.org/wiki/British_National_Corpus).

**A generatív nyelvészet korpuszellenes**

Chomskyt és általában a generatív nyelvészeket szeretik megvádolni mindennel amivel csak egy nyelvészeti elméletet meg lehet vádolni. [Arról már beszámoltunk](http://szamitogepesnyelveszet.blogspot.com/2011/05/vissza-jovobe-avagy-miert-veszitett.html) hogy Chomsky szerint a sztochasztikus modellek magyarázati ereje korlátozott (de ez nem jelenti azt hogy gyakorlati alkalmazásukat kerülni kell!), de egyéb érveket is tulajdonítanak neki. Ezek röviden:

-

a korpusz a performancia 	megnyilvánulása, nem szolgálhat a kompetencia modelljéül

-

adott nyelvben a lehetséges 	jólformált mondatok száma megszámlálhatóan végtelen, ergo egy 	korpusz nem modellezheti le

-

nincs olyan hogy kiegyensúlyozott 	korpusz

Vegyük sorra ezeket! Chomsky megkülönbözteti a komptenciát (a nyelv tudásának belső képességét, egy internalizált szabályrendszert a fejünkben) és a performanciát (azt amikor használjuk a nyelvet). A kompetencia általános elveken alapul, mint pl a rekurzió (önmagát meghívó szabály). Így ha pl. egy szabály szerint ha kiegészíthetem egy az

„Egész nap csak esik”

mondatot azzal hogy és esik. Akkor az alábbi mondatok mind helyesek:

„Egész nap csak esik és esik.”

„Egész nap csak esik és esik és esik”

„Egész nap csak esik és esik és esik és esik”

És így tovább a végtelenségig! Nyilván nem élünk végtelen ideig és valamikor abba kell hagyni egy ilyen mondatot, de elvileg (és ez nagyon fontos!) akár meddig folytathatjuk, ahogy a természetes számok sorát (hiszen minden mondathoz hozzárendelhetjük annak hosszát, és ahogy minden természetes egész számnál tudunk eggyel nagyobbat mondani, úgy tudunk egy elemmel hosszabb mondatot generálni). Hogyan lehet így a nyelv egy modelljét megadni? A kulcs a generálási szabályok megtalálása. A lexikon, azaz az építőkövek, nem érdekes ebből a szempontból!

Technikai értelemben valóban nem tudunk olyan korpuszt találni ami modellje lehet a nyelvnek. Azonban nem szabad elfeledkeznünk a lexikon egy érdekes tulajdonságáról. Vannak ugyanis olyan elemei melyek nem változnak nagyon az idővel, azaz zárt osztályt alkotnak. Ezek általában valamilyen grammatikai funkciót töltenek be (gondoljunk a kötőszavakra pl.) és akadnak olyanok melyek sokkal változékonyabbak. Azonban a zárt osztályt alkotó szavak száma nagyon alacsony, legalábbis a többihez képest. Azonban a generatív elméleteket is tesztelni kell valahogy, erre pedig kiválóan alkalmas egy korpusz, azonban a korpuszba vetett hit mértéke Chomsky hívei körében alacsony. Ez alatt nem azt kell érteni hogy vitatják a nyilvánvalót, csupán annyit tesz hogy nem fogadják el hogy ha valami nincs a korpuszban, az nem is létezik.

Ezzel pedig el is jutottunk az egyik kedvenc témámhoz! Lehet-e olyan korpuszt készíteni ami reprezentatív? Reprezentativitáson, ahogy megszoktuk pl a közvélemény-kutatások esetében, azt értjük hogy jó megközelítéssel leírja a minta az egész sokaságot. Vannak akik szerint ahogy egyre jobban fejlődik a technika és egyre több adatot generálunk úgy tkp. elérjük hogy lényegében egy végtelen, állandóan növekvő korpuszunk van ami gyakorlatilag lefedi a teljes sokaságot (l. Norvig et all. [The Unreasonable effectiveness of data](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en//pubs/archive/35179.pdf) tanulmányt).

Ha elfogadjuk hogy a nyelv rekurzív és ezáltal minden egyes nyelv lehetséges mondatainak száma megszámlálhatóan végtelen, akkor bele kell törődünk hogy nincs olyan korpusz ami modellje lehetne. Azonban ahogy a fizikusokat sem zavarja hogy nem vizsgálhatnak meg minden egyes apró részecskét, úgy minket sem kell hogy zavarjon hogy véges lények vagyunk és csak véges adatokkal dolgozhatunk. Viszont figyelembe kell vennünk azt a tényt hogy az adatokkal nagyon óvatosan kell bánnunk! Pl. ha a mai beszélt magyar nyelv korpuszát szeretnénk elkészíteni cenzusos alapon (azaz minden beszélőtől vennénk adatot) egy sztenderd irányított beszélgetés keretében amiben pl személyi adatokat kérdezünk, akkor a „Budapest” szó felülreprezentált lenne a korpuszban, hiszen a legnépesebb városban laknak a legtöbben, de kiugrana pl „Debrecen” vagy „Miskolc”, és könnyen megeshetne hogy a szórványmagyarság körében végzett kutakodásunk eredménye egy sor településnevet (vagy foglalkozást) eredményezne ami nagyon alacsony számban fordul elő, ezek jó eséllyel ki is esnének a végleges korpuszból mint [hapax legomenák](http://en.wikipedia.org/wiki/Hapax_legomenon)...

Ideális esetben mindenkinek vagy mindennek egyenlő eséllyel kell beleesnie a mintába. Vannak ugye nagyon rövid, meg nagyon hosszú szavak, de a legtöbbjük se nem túl hosszú, se nem túl rövid. Ezt nevezik normál eloszlásnak, és a legtöbb dolog ezt a mintát követi. Vessünk egy példát a grafikonjára

[normal distribution]

s láthatjuk hogy a legtöbb érték az [átlag ](http://hu.wikipedia.org/wiki/Sz%C3%A1mtani_k%C3%B6z%C3%A9p)körül csoportosul és a leggyakoribb érték azaz a [módusz](http://hu.wikipedia.org/wiki/M%C3%B3dusz) is itt található, ahogy haladunk a szélek felé, úgy csökken az átlagtól eltérő értékek gyakorisága. Azonban előfordulhat hogy az ugyanazon átlag nagyon eltérő görbét eredményez. Ugyanazon átlag mellett a módusz és a [medián](http://hu.wikipedia.org/wiki/Medi%C3%A1n) (a sorba rendezett értékek közepe) eltérhet jobbra és balra.

[skewed]

Egy kiegyensúlyozott korpusznak figyelembe kell vennie a mintavételezésnél hogy vannak csángó beszélők, nagyváradiak, encsiek és győriek, nekik mind egyenlő eséllyel kell a mintába kerülniük. Ugyanakkor azt is figyelembe kell vennünk hogy a nyelvnek területi változatai is vannak, de ez mind nem elég, mert a társadalmi helyzet, iskolázottság stb mind hat a nyelvhasználatra, érdemes ezekre is tekintettel lenni. És a végén ott a [megfigyelő paradoxona](http://en.wikipedia.org/wiki/Observer%27s_paradox), felmerül a kérdés hogy mennyire hat az adatgyűjtő jelenléte a beszélőre (a kedves olvasó eleresztene egy „bazd meg”-et ilyen helyzetben? És otthon vagy baráti körben kicsúszik egy-egy káromkodás a szádon?). Szinte biztos hogy valamerre kitér a mintánk, de nem tudjuk merre!

**Mégis akkor mire jó ez az egész?**

Nem kell elfordulnunk a korpusznyelvészettől, csak tisztába kell lenni azzal hogy nem tudjuk egyetlen korpusszal lefedni a nyelvet és el kell fogadnunk hogy nem a nyelv egy modelljét rejti egy korpusz, hanem egy forrást amivel tesztelhetjük elméleteinket. Ebben az értelemben a korpusznyelvészet nem a nyelvtudomány egyik ága, hanem a lehetséges kutatásmódszertanok egyike.
