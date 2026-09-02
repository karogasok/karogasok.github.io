---
title: "Az adatok megmagyarázhatatlan természete"
slug: "az-adatok-megmagyarazhatatlan"
date: 2010-09-14T11:27:00.003Z
publishDate: 2010-09-14T11:27:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/09/az-adatok-megmagyarazhatatlan.html"
regi_cimkek:
  - "adatok tudománya"
  - "data science"
  - "elvek és paraméterek"
  - "filozófia"
  - "korpusznyelvészet"
  - "minimalista program"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "valószínűségszámítás"
regi_cimkek_mind:
  - "adatok tudománya"
  - "data science"
  - "elvek és paraméterek"
  - "filozófia"
  - "korpusznyelvészet"
  - "minimalista program"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "valószínűségszámítás"
---

**"For those who were hoping that a small number of general rules could explain language, it is worth noting that language is inherently complex, with hundreds of thousands of vocabulary words and a vast variety of grammatical constructions. Every day, new words are coined and old usages are modified. This suggests that we can’t reduce what we want to say to the free combination of a few abstract primitives."** Halevy, Norvig, Pereira: [The unreasonable Effectiveness of Data](http://bit.ly/9T4wKI)  
  
 Előző posztjaimban az[ adatok tudományával foglalkoztam](http://bit.ly/a76k9z) és a visszajelzések alapján sokak érdeklődését felkeltettem. Mielőtt azonban a szögre akasztanánk megszokott eszköztárunkat, egy kicsit gondolkozzunk el az adatok természetéről.  
  
  
  
**Matematizáltság és logika**  
 Érdekes hogy a Google nagyágyú mesterséges intelligencia kutatói mind a logikai/szabályalapú megközelítés felől indultak. Norvig híres PAIP könyvében vagy Pereira [Prolog and Natural Language Analysis](http://bit.ly/9wpgN2)-e még nem nagyon találkozunk statisztikai megközelítéssel. Az idézett cikk pedig bevallottan utal Wigner Jenő [The Unreasonable Effectiveness of Mathematics in the Natural Sciences](http://bit.ly/bS0Hxj) című előadására, aminek szerzője azon elmélkedik hogy milyen hatékonyan képes pár (számára) egyszerű matematikai formula leírni a természetet. Norvig és társai megjegyzik hogy ami működőképesnek tűnik a természettudományok területén, nem megy a társadalom- és humán tudományok esetében. Habár végkövetkeztetésükkel nem kell feltétlenül egyetértenünk. Vendégposztolónk [már elmélkedett arról](http://bit.ly/aOl8re) hogy a nyelvészet számára is kívánatos lenni ha jobban eluralná a fizika irigység (physics envy) és ez valóban nem lenne rossz dolog, de gondoljunk egy kicsit a matematikafilozófiára.  
  
 A filozófia már a kezdetektől fogva összekapcsolódik a matematikával (ahogy azt a kiváló magyar tudós Szabó Árpád könyvei is szemléltetik azt). A matematika természete máig is nagy talány számunkra, hiszen annyi minden amit tudunk azon áll vagy bukik hogy a matematikánk tényleg biztos lábakon áll. Olyannyira izgatta ez a matematikusokat és filozófusokat hogy Hilbert, Frege, Cantor, Carnap, Russel és társaik egész életüket ennek vizsgálatára tették fel. Mit sikerült elérniük? Ennek interpretálásába most nem megyünk bele, akit érdekel utána olvas, de műveikben a logika központi szerepet kap, mivel a különböző matematikai struktúrákról általa tudunk beszélni. Az hogy velük tartunk-e és kitüntetjük a logikát mint a matematika alapját, vagy Quine érveit fogadjuk el miszerint a logika praktikusan a legegyszerűbb eszközünk momentán hogy egyáltalán beszélhessünk a matematikáról és a tudományos érvelésről számunkra édes mindegy most. A logika kitüntetett helye abban áll, hogy segítségével érvelhetünk a különböző matematikai struktúrákról, így a valószínűségszámításról és a statisztikáról is.  
  
**Mérnöki tudományok versus tiszta tudományok**  
 Az alkalmazott és elméleti tudományok szembeállítása persze erőltetett, de nem ördögtől való ötlet. Nyilván vannak határesetek amikor nem tudjuk hogy egy alapkutatással van dolgunk, vagy éppen egy probléma elegáns gyakorlati megoldását keresi valaki, de vannak olyan esetek amikor szépen elkülöníthetőek ezek a területek. Vegyük például a newtoni fizikát és a relativitáselméletet. A fizikusok körében senki nem gondolja hogy a newtoni fizika írja le a világot, elismerik hogy bizonyos léptékben használva alkalmazhatónak tartják. Egy építész amikor házat tervez nem veszi figyelembe a részecskék természetét, a gépész nem törődik a relativitáselmélet nüanszaival, hanem a jó öreg, bevált newtoni elveket alkalmazza.  
  
**Tudományfilozófia és az empirikus aluldetermináltság**  
 Az hogy rengeteg adat áll rendelkezésünkre még nem jelenti azt hogy az adatok maguk tartalmazzák az őket generáló szabályokat. Attól hogy nincsenek meg ezek a szabályok még nem kell elfogadnunk azt hogy azok nem is léteznek. Az adatok maguk ugyanis nem fedhetik le (még elvben sem) a lehetséges mondatok halmazát (mivel azok száma végtelen). Tegyük fel hogy elméletben sikerül valahogy egy végtelen adathalmazt összeszednünk! Ha ezt nem generatív szabályok alakították, akkor ugye nem tudjuk hogy mi definiálja magát a halmazt. Ha mégis valamilyen szabályok alakították, akkor viszont nem tudjuk milyen szabályok is lehetnek ezek. Gondoljunk a [Quine Duhem tézisre](http://bit.ly/aDlYPd)! Egy adott jelenségnek több magyarázata is lehetséges, amik mindig túllépnek azon amit az adatok sugallnak. Hogy melyiket fogadjuk el, azt nem csak belső faktorok (mennyire igaz, mennyire képes előrejelezni bizonyos jelenségeket stb), hanem külső tényezők is befolyásolják (a tudományos közösség szociológiája, a tudománypolitika alakítóinak kedve stb).  
  
**A nyelvészet és az adatok ismét**  
 Sokan azt hiszik hogy a "bevett nézet" a Chomsky-féle minimalista program a nyelvészetben. Ez nem így van! Ha egy kicsit kutakodik az ember, hamar kiderül hogy a minimalista program nem egyenlő a generatív megközelítéssel és a generatív megközelítés egyáltalán nem egyeduralkodó. Szinte divattá vált Chomsky elméletének fényében meghatároznia magát minden valamire való nyelvészeti irányzatnak. A leggyakoribb önmeghatározás az adatokhoz való viszony szokott lenni. Sokan szeretik azt állítani hogy a generatív nyelvészek csak ülnek a kényelmes karosszékeikben és különböző grammatikai konstrukciókat ötlenek ki. Azonban ez nem teljesen igaz! Az elvek és paraméterek elmélete megköveteli a kísérleti adatgyűjtést és a pszicholingvisztika irodalma tele van ilyen típusú adatokkal, de a blogon bemutatott [korpusznyelvészeti bevezető](http://bit.ly/biokFe) is tele van példákkal arra hogy a generatív megközelítés is adatokra alapozott.  
  
 Sokkal súlyosabb ellenérvet fogalmaz meg [Wilks](http://bit.ly/cokmuW) miszerint Chomsky és követői Carnap nyomdokain haladva túlságosan is a "középre" koncentrálnak. Persze erre is vannak érvek (a biológiai limitek lehatárolják a komputációk kivitelezhetőségét, azaz a kompetencia behatárolt a performancia által), de valahogy érezzük hogy ezek inkább kifogások. A szabályalapú megközelítések egészen addig jól működtek amíg meghatározott, viszonylag kis feladatra alkalmazták őket, azaz a középre hegyezték ki használatukat. Azonban ha csak egy kis teret is engedünk annak hogy a nyelv valódi változatosságában jelenjen meg, gyönyörű szabályaink nem állják ki a használhatóság próbáját. Norvig és társai épp arra mutatnak rá hogy a statisztikai megközelítések kicsiben nem túl jók, viszont nagyon sok adatot használva már elfogadható eredményeket produkálnak.  
  
 Ezek az elfogadható eredmények azonban csak bizonyos szinten elfogadhatóak. A Google Translate segíthet nekünk hogy képet kapjunk egy általunk ismeretlen nyelven íródott dokumentum tartalmáról. Különböző módszerekkel kezelni lehet hogy a sajtóban milyen visszhangja van egy adott cégnek, egy dokumentum tartalmáról elfogadható összegzést lehet készíteni és még ezernyi alkalmazása van a nagy adathalmazokon végzett statisztikai elemzések használhatóságának. Azt senki nem gondolja hogy a szépirodalom fordítása bármikor is gépekre bízhatók, de mindenki reménykedik benne hogy egyszer talán a híreket automatikusan és megbízhatóan lefordítják nekünk a gépek. Lehet hogy egy számítástudós bízik abban hogy kellő mennyiségű adatot kell csak találnia (azt esetleg kezelnie valahogy) és megfelelő stratégiát annak elemzéséhez, de egy nyelvész kételkedik ebben, hiszen éppen arra lenne szükség hogy az elszórt "kivételek", a középtől való eltérések miértjeire választ találjunk. Miért? Mert a nyelv nem állandó valami, de a nyelvi képesség (már ha van olyan) igen (legalábbis evolúciós értelemben még annyira új, hogy mostanában nem fog változni) és leírásába beletartozik ezen "anomáliák" rendszerezése is. A mérnöki munka (az adatok kezelése - pl. a mapreduce megközelítéssel) és a statisztikai elemzés új távlatokat nyit. Itt egy kicsit szétválik az elméleti munka, hiszen az eredményeket más szemszögből próbáljuk rendszerezni, míg a gyakorlati alkalmazások "problémát" oldanak meg praktikus szempontok szerint. De valahol, mint a tudomány történetében már annyiszor, a két megközelítés összetart. Addig pedig maradnak nekünk az adatok, és az ő megmagyarázhatatlan természetük...
