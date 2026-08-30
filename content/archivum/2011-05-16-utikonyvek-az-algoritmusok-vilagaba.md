---
title: "Útikönyvek az algoritmusok világába - ahogy megígértük"
date: 2011-05-16T07:59:00.004Z
publishDate: 2011-05-16T07:59:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/05/utikonyvek-az-algoritmusok-vilagaba.html"
regi_cimkek:
  - "logikai programozás"
  - "prolog"
  - "python"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "algoritmusok"
  - "logikai programozás"
  - "prolog"
  - "python"
  - "számítógépes nyelvészet"
---

**A [Legyél te is számítógépes nyelvész](http://szamitogepesnyelveszet.blogspot.com/2011/05/legyel-te-is-szamitogepes-nyelvesz-tiz.html) posztban megígértük hogy megpróbálunk olyan anyagokat is ajánlani melyek segítenek belépni az algoritmusok gyönyörű világába. Azonban figyelmeztetni kell az olvasót hogy ha hátizsákos turistaként maga szervezi meg az utazást nagyon sok kellemetlenséggel találkozhat, gyakran el fog akadni és néha idegen, fura nyelven beszélő emberek jóindulatára lesz utalva, és soha nem fogja tudni hol éri az este. Ellenben rengeteg élményben lesz része, és ahogy egyre több tapasztalata halmozódik fel, egyre jobban fogja érteni magát és az őt körülvevő világot. Mielőtt azonban elindulnál győződj meg arról hogy minden benne van-e a hátizsákodban (a fent említett poszt ebben segíthet neked)!**

**Felkészülésnek könnyű túrák**

Ha már van némi tapasztalatod a programozás terén, akkor ideje egy kicsit rendszerezni és módszeresen átismételni mindent. Hátteredtől függően, az MIT Open Courseware nagyszerű anyagai segíthetnek. A [Structure and Interpretation of Computer Programs (6.001)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/) és az [Introduction to Computer Science and Programming (6.00)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm) előadásai szabadon letölthetők, az órákra kiadott problémákkal, és a vizsgakérdésekkel együtt. Továbbá mindkét kurzus szabadon hozzáférhető könyveket használt, minden a MIT OCW-n elérhető anyag CC licenc alatt van, így nyugodtan letöltheted, odaadhatod a haveroknak stb. Hogy melyiket választod, az a tőled függ, ha ismered egy kicsit a Python-t, akkor a 6.00 való neked, ha a funkcionális (és/vagy logikai) paradigmában vagy jártasabb, esetleg a Lisp vagy a Scheme nyelvekkel is jóban vagy valamennyire, akkor a 6.001 a te kurzusod. Ez a felkészülés azt szolgálja hogy biztos alapokra tegyél szert! Sokkal inkább szól a két kurzus az algoritmikus problémamegoldásról, a számítástudomány alapjairól és a programozásról, mint az algoritmusokról, de ezekre az alapokra szükséged lesz!

**Lépjünk tovább - nyelvészeti algoritmusok**

A legjobb anyag, ami nem mellesleg ingyenesen elérhető, az [Algorithms for Computational Linguistics](http://www.coli.uni-saarland.de/projects/milca/courses/coal/html/) és a [Natural Language Processing Techniques in Prolog](http://cs.union.edu/%7Estriegnk/courses/nlp-with-prolog/html/) könyvek. A kettő tkp. ugyanaz! A második az első kicsit átdolgozott és bővített változata. Ahogy a második címe mutatja, Prolog nyelven mutatja be a legalapvetőbb algoritmusokat, éppen csak annyi elméletet tartalmaz amennyi feltétlenül szükséges, de máshol még ennyit se találhatsz, ezért is érdemes egy kicsit foglalkozni a nyelvel.

Van egy eléggé elhanyagolt területe a számítógépes nyelvészeti algoritmusoknak, amit viszonylag kevés előismerettel felfedezhetsz, ez az ún string algoritmusok világa. A [Jewels of Stringology](http://igm.univ-mlv.fr/%7Emac/JOS/JOS.html) kötet nagyon érthetően mutatja be a legalapvetőbb eljárásokat, a formalizmusokat és az elméleti hátteret a minimumra szorítva. Ezzel ellehetsz egy ideig és ha a fent említett anyagokat végig vetted ideje a matekkal is foglalkozni!

**Kalandra fel!**

Ha a fentiek mellett rendelkezel diszkrét matek és valószínűségszámítási alapokkal (nyugi, nem kell matematikusnak, vagy informatikusnak lenni, csak a legszükségesebbeket kell tudni a területről). Akkor indulhat a nagy kaland! Most már nem elmélet vagy gyakorlat a kérdés, kössük össze a kettőt. Hetland [Python Algorithms: Mastering Basic Algorithms in the Python Language](http://www.amazon.com/Python-Algorithms-Mastering-Language-Experts/dp/1430232374/ref=sr_1_1?ie=UTF8&s=books&qid=1305531485&sr=1-1) könyve alig fél éve jelent meg, de hatalmas népszerűségre tett szert, mivel praktikus szempontok alapján, sok-sok példán keresztül mutatja be az alapokat. Az elméleti részekhez pedig az MIT OCW [Introduction to Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/index.htm) kurzusát hívjuk segítségül, remek előadás videókkal! Cormen at all. [Introduction to Algorithms](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=8570) könyve klasszikus, érdemes beszerezni, később referencia könyvnek is jó!

**Csúcstámadás**

Ennyi kaland után jöhetnek  a nagy csúcsok! Két, alapvetően elméleti könyvet ajánlok. A bemelgítőben már említett Jewels of Stringology szerzői megírták a kötet nagy testvérét, [Algorithms on Strings](http://www.amazon.com/Algorithms-Strings-Maxime-Crochemore/dp/0521848997/ref=sr_1_2?s=books&ie=UTF8&qid=1305531972&sr=1-2). Igen, egy számítógépes nyelvész sokat foglalkozik stringekkel, nem árt ismerni a hozzájuk kapcsolódó algoritmusokat. A másik nagyon fontos terület a parsing (szintaktikai elemzés). Ebbe a [Parsing Techniques: A Practical Guide](http://www.amazon.com/Parsing-Techniques-Practical-Monographs-Computer/dp/1441919015/ref=sr_1_1?s=books&ie=UTF8&qid=1305532221&sr=1-1) nyújt bevezetést.

**Jó utat!**

Ahogy láthatod, nagy kaland elé nézel. Nem szabad menetelésnek felfogni ezt! Sokkal inkább túraként tekints az algoritmusok megismerésére. Vagy ha jobban tetszik, fogd fel úgy hogy külföldön fogsz tanulni és el kell sajátítanod a fogadó ország nyelvét! Nyilván nem fogsz úgy beszélni mint egy ott felnőtt és iskolázott ember, de sok gyakorlással elérheted azt hogy elfogadjanak és megérts másokat, kifejezd magad másoknak. Ha ezt elérted, akkor képes leszel tanulni, és a tanultakat alkalmazni!
