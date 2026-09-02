---
title: "Valószínűség, statisztika és nyelv"
slug: "valoszinuseg-statisztika-es-nyelv"
date: 2010-05-17T14:32:00.001Z
publishDate: 2010-05-17T14:32:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/05/valoszinuseg-statisztika-es-nyelv.html"
regi_cimkek:
  - "R"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "valószínűségszámítás"
regi_cimkek_mind:
  - "R"
  - "nyelvészet"
  - "statisztika"
  - "számítógépes nyelvészet"
  - "valószínűségszámítás"
---

**Ha már túl vagy a statisztika alapjain, vagy élénken él benned a középiskolai matek, esetleg igazi matek zseni vagy, akkor itt az ideje egy kicsit a nyelv statisztikai tulajdonságaival is foglalkoznod. Ha nem, talán egy [régebbi posztom](http://szamitogepesnyelveszet.blogspot.com/2010/04/statisztikai-tulelokeszlet.html) segít neked felturbózni tudásodat.**  
  
A statisztikai/valószínűségi megközelítést sokan a nyelvtől idegennek tartják, maximum hallottak [Zipf törvényéről](http://en.wikipedia.org/wiki/Zipf%27s_law), de alapvetően idegenkednek ezen módszerek alkalmazásától. Hagyományosan a nyelvészet szabályokat keres, ha-akkor formában megfogalmazott szabályokat. Ahol kivételek vannak, ott is szabályokat keresünk. Persze a nyelv nem éppen olyan mint amilyennek látni szeretnénk, de hát erre is van egy szép elméletünk, a [kompetencia - performancia](http://www.unm.edu/%7Edevalenz/handouts/competence.html) megkülönböztetés Chomskytól. Nagyon röviden, egy kicsit félreértelmezve, ez annyit tesz hogy vannak a szabályok (kompetencia), de hát mi véges lények vagyunk akik ezen szabályokat felépítésük folytán nem képesek 100%-ra hozni, azaz hibázunk.  
  
Habár én hiszek ebben a megközelítésben, a helyzet az hogy egyre többen kérdőjelezik ezt meg. Ők már nem a szobában ülve találnak ki példamondatokat, hanem "kimennek az emberek közé", adatot gyűjtenek a nyelvhasználatról és azt elemzik ami van. Magyarán nem egy elmélethez gyártanak példákat, hanem az adatokból akarják kihámozni a mögöttük rejlő rendezőelvet (ezt ők mondják a szabálygyárosokról, nem én!). Egy nagyon jó, olvasmányos és átfogó kötet [Probabilistic Linguistics](http://www.amazon.com/Probabilistic-Linguistics-Bradford-Books-Rens/dp/0262523388/ref=sr_1_1?ie=UTF8&s=books&qid=1274103814&sr=8-1) mutatja be hogyan alkalmazzák a kutatók ezt a megközelítést a nyelvészet különböző területein. Ha nem is borítótól hátlapig, de a téged érdeklő részeket legalább érdemes elolvasni.  
  
Személyes véleményem hogy a statisztikai megközelítés sokat segíthet nekünk, de önmagában nem képes megmagyarázni mindent. Viszont egyre népszerűbb, hiszen sok konkrét eredményt ért el és gyakorlati alkalmazásai sem elhanyagolhatóak. Gyakorlati alkalmazásai miatt a számítógépes nyelvészet ma legfelkapottabb megközelítése épp a statisztikai módszer, s ezért szivárog át a nyelvészetbe is. Ha nem kerülhetjük meg, akkor olvassunk olyan könyveket amik megszerettetik velünk!  
  
Előzetes megjegyzések  
Ha valaki meg akar tanulni valamit, akkor nem csak az elméletet kell bebifláznia, hanem valahogy kontextusba kell hoznia azt. Mire jó X elmélet és miben más mint Y, Z? Mire használjuk? De ezek mellett nem árt tudni hogy hogyan használjuk! Gondolj arra hogy ma Magyarországon mindenki ért a focihoz és a gazdasághoz elméletben, de mi van a gyakorlattal!  
  
A nyelvészet terén olyan szerencsénk van hogy nyugodtan kibicelhetünk és végig követhetjük mások munkáját. Megismételhetjük és magunk is kísérletezhetünk, mégpedig otthon a fotelból. Ehhez viszont szükségünk van egy-két dologra.  
  
A legfontosabb dolgunk az [R statisztikai programozási](http://www.r-project.org/) nyelv. Itt nem részletezem hogyan töltsd le és telepítsd, ezt az R oldalán megtalálod. Kövesd az operációs rendszerednek megfelelő utasításokat és nem lesz gond. Szükséged lesz még egy programozó szövegszerkesztőre, ha linuxon vagy OSX-en nyomulsz én a Vim-et és az Emacs-et ajánlom, de a Google a barátod és a "programmers editor" kifejezésre keresve rátalálhatsz a saját kedvencedre, amely oprendszereden futni is tud.  
  
Az itt következő könyvek az R használata során tanítanak neked hasznos módszereket és nem mellékesen programozni is megtanulhatsz (nem leszel egy guru, de jó alapod lesz velük). Mindegyik könyv tartalmaz technikai útmutatást az R letöltéséhez valamit a könyvben használt csomagok telepítéséhez. Kezd azzal hogy a csomagokat telepíted!!!  
  
**Ingyenesen hozzáférhető könyvek**  
Baayen: [Analyzing Linguistic Data](http://www.google.com/#hl=en&source=hp&q=baayen+analyzing+linguistic+data&aq=0&aqi=g1&aql=&oq=baayen+ana&gs_rfai=&fp=d4b0803f5f994e53)  
Kicsit nehéz követni ha még nem  programoztál és nincs semmi fogalmad a statisztikáról, de nagyon jó könyv és egy igen kidolgozott vázlata ingyenesen letölthető. Majdnem megegyezik a hivatalos kiadással és nagyon hasznos útmutató.  
  
Shravan Vasishth - Michael Broe : [The foundations of statistics: A simulation-based approach](http://www.ling.uni-potsdam.de/%7Evasishth/SFLS.html)  
Baayen könyvénél nehezebb és egy kicsit nehézkesebb a nyelvezete is, de ingyenes és alapos könyv. Személyes élményem hogy elsőre untam és abba is hagytam az olvasását, de másodszorra nem tudtam letenni. (Pont a fenti könyv után jött ez)  
  
**Pénzes, de kiváló könyvek**  
Stefan Th. Gries: [Quantitative Corpus Linguistics with R](http://www.amazon.com/Quantitative-Corpus-Linguistics-Practical-Introduction/dp/0415962706/ref=sr_1_1?ie=UTF8&s=books&qid=1274105828&sr=8-1)  
Ha meg akarsz veni egy könyvet, ez az amire érdemes költened. Nagyon alaposan és érthetően magyarázza el a korpusz nyelvészet alapjait, a statisztika használatát ezen a területen és az R alapjait. Ez az amire azt mondom hogy a KÖNYV. Kontextus, gyakorlat és elmélet egy helyen.  
  
Baayen: [Analyzing Linguistics Data](http://www.amazon.com/Analyzing-Linguistic-Data-Introduction-Statistics/dp/0521709180/ref=pd_bxgy_b_text_b)  
Nos ezt fent már említettem az ingyenesen elérhető anyagok között, de itt is helyen van. A CUP által kiadott változat néhol eltér a vázlattól és azt kell mondjam jobb is. A különbségek nem eget verőek, de ebből a verzióból szerintem jobban lehet tanulni.  
  
Keit Johnson: [Quantitative Methods in Linguistics](http://www.amazon.com/Quantitative-Methods-Linguistics-Keith-Johnson/dp/1405144254/ref=pd_bxgy_b_text_c)  
Ez a könyv pár éve még szabadon elérhető volt a szerző honlapján, sajnos amióta megjelent nyomtatott formában is már nem tölthetjük le. Ez előbbi könyveknél sokkal nehezebb és a nyelvezete is nehezebben követhető (legalábbis nekem). Én mégis nagyon ajánlom, különösen nyelvészeknek, mivel igazi "nyelvészeti problémákat" vizsgál.  
  
**Összegezve**  
A fenti könyvek nagyon sokat segíthetnek annak aki a nyelvészet felől közelít a számítógépes nyelvészet felé. Biztos alapokat nyújtanak és az R nyelv ismerete hasznos, mivel egyre több álláshirdetésben találkozhatunk vele. Úgy érzem azonban, hogy nem lehet eléggé hangsúlyozni hogy a tárgyalt könyveket nem lehet egyszerűen olvasni. Aktív hozzáállást követelnek meg. Nem elég a példákon végig dolgozni, saját projekteket is kell készítened (gyakorlásnak és örömforrásnak is remek dolog ám ez).
