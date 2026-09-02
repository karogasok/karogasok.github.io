---
title: "Logika mindenkinek II - automaták, formális nyelvek és kiszámíthatóság"
slug: "logika-mindenkinek-ii-automatak"
date: 2010-05-09T12:37:00.001Z
publishDate: 2010-05-09T12:37:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/05/logika-mindenkinek-ii-automatak.html"
regi_cimkek:
  - "logika"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "automata elmélet"
  - "formális nyelvek"
  - "logika"
  - "számítógépes nyelvészet"
---

**Sorozatom [első darabjában](http://szamitogepesnyelveszet.blogspot.com/2010/05/logika-mindenkinek-i-bevezetes.html) bevezető könyveket ajánlottam a különféle hátterű embereknek. Ebben a részben a logikával szorosan összefüggő, és történeti okok miatt is nehezen elválasztható, ún automata elmélettel foglalkozom. Olyan könyveket igyekeztem összeszedni amelyek segítenek egyfajta minimum tudás elsajátítását. A hangsúly most is azon van hogy a filozófia/logika és a nyelvészet felől érkezők találjanak olyan könyveket melyek segíthetnek nekik. Persze nem szabad elfeledkeznem arról hogy akadnak programozó/programtervező informatikus olvasóim is, így röviden nekik is ajánlok egy könyvet majd.**  
  
**Boolos et all.: [Computability and Logic](http://www.amazon.com/Computability-Logic-George-S-Boolos/dp/0521701465/ref=sr_1_1?ie=UTF8&s=books&qid=1273405413&sr=8-1)**  
Ha már van egy alapvető logikai műveltséged, ez a könyv nem okozhat meglepetést. Ugyanis nem elég tudni hogy mire képes a logika, jó tudni a határait is (Wittgenstein Tractátusa is erről szól, hol húzhatjuk meg a logika határait). Miért érdekes ez? Nos ha a nyelvvel foglalkozunk, és számítógépes feldolgozásról beszélünk, akkor tudnunk kell hogy mire képes a formális rendszerünk. Nyilván valamilyen szabályrendszert állítunk fel és bízunk benne hogy használható eredményünk lesz, de tudnunk kell hogy meddig mehetünk el. Ezért ez a könyv nem csak a kiszámíthatóság fogalmát tálalja a filoszoknak szépen, de előkészíti a talajt hogy az algoritmusok nehezebb világát is megismerhesd majd. A könyv feladatai kötelezőek! Megoldásuk/végig gondolásuk nélkül szerintem nem lehet megérteni a témát. Fontos! A korábbi kiadások sok nyomdahibát, pontatlanságot tartalmaztak, ezért a hivatkozott kiadást vagy későbbit használj!  
  
**[Smith: An Introduction to Gödel's Theorems](http://www.amazon.com/Introduction-Theorems-Cambridge-Introductions-Philosophy/dp/0521674530/ref=pd_bxgy_b_text_b)  
[Nagel et all.: Godel's Proof](http://www.amazon.com/Godels-Proof-Ernest-Nagel/dp/0814758371/ref=pd_bxgy_b_text_c)**  
Gödel tételei központi helyet foglalnak el a logika elméletében. Megértésük nem csak ezért fontos, sokkal inkább egy gyakorlati oldalát emelném ki ennek: az alapok biztos ismerete elengedhetetlen hozzá. Nem beszélve a személyes "aha" élményre, amiben sokaknak volt része ezen könyveket olvasgatva (persze ez csak az én szűk baráti köröm).  
  
**[Partee et all. Mathematical Methods in Lignuistics](http://www.amazon.com/Mathematical-Methods-Linguistics-Studies-Philosophy/dp/9027722455/ref=sr_1_1?ie=UTF8&s=books&qid=1273406556&sr=1-1)**  
Az előző posztban már írtam erről a könyvről és az egekig magasztaltam. Nincs más ennyire átfogó könyv a piacon. Nyelvészeknek az első laptól az utolsóig kötelező! Filoszok, ha már olvasták a BML-t vagy a GAMUT-ot, lapozzanak a formális nyelvek és az automata elmélet részhez! Sajnos nem tudok olyan könyvről, amely filoszoknak tálalná a formális nyelvek elméletét. Szerencsére a nyelvészek és filoszok logikához való viszonya hasonló, ezért könyveik is nagy átfedést mutatnak. Ezért bátran olvashatja ezt a könyvet egy filozófia felől érkező is, de matekosok és számítás tudorok is haszonnal forgathatják.  
  
Itt egy kicsit elkanyarodok. "Miért is kell nekem ezeket is tudnom?" "OK, Gödel kell nekem hogy lássam hol a határ, de ez nagyon nem logika." Ilyen kérdéseket hallottam már párszor, még olyantól is aki profi számítógépes nyelvész lett (azaz ebből él). Persze nem kell profinak lenned, hiszen nem logikusnak készülsz. De formális nyelveket használunk, abban reménykedve hogy ezek legalább valamennyire leírják a "támadott" természetes nyelvet. A számítógép buta, világos szabályokat követel meg. Sajnos a természetes nyelvek nem ilyenek. Így a nyelvek és automaták elmélete ad alapot arra hogy tisztában legyünk mennyire lehetünk sikeresek. Megint a határok problémájánál vagyunk, és ennyiben (is) összefügg az automata elmélet és a formális nyelvek elmélete a logikával.  
  
**[Hopcroft et all.: Introduction to Automata Theory, Languages, and Computation](http://www.amazon.com/Introduction-Automata-Theory-Languages-Computation/dp/0321462254/ref=sr_1_1?ie=UTF8&s=books&qid=1273407709&sr=1-1)  
[Sipser: Introduction to the Theory of Computation](http://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/0534950973/ref=pd_bxgy_b_text_b)**  
Ezeket a könyveket azoknak ajánlom akik a szigorúan formális tálalást szeretik, azaz matekosoknak és számítás tudoroknak. Az érdeklődő bölcsészek szerintem csak akkor képesek megemészteni ezeket, ha előtte már átrágták magukat a fenti könyveken (vagy azok egy részén). Itt már nem csak szimplán tálalják a szükséges ismereteket egy kis magyarázattal, hanem az egyes tételek bizonyításait is olvashatjuk. Habár nem árt tudni ezeket, és nagyon hasznos pár tétel formálisabb átnézése, nyugodt lelkiismerettel ki lehet hagyni a nehezebb részeket.  
  
  
**Összegezve**  
Habár ez a terület elhanyagolt, nem szabad megfeledkezni róla. Már csak azért sem, mert a logikán kívül, az algoritmusok területével is érintkezik, és remek terep hogy ennek befogadására is felkészülj.  
  
Nem győzőm hangsúlyozni azonban hogy itt csak támpontot találsz. A döntés rajtad múlik. Ismerned kell önmagad, és időt kell szánnod a megfelelő könyv kiválasztására.
