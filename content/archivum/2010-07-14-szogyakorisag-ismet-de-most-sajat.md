---
title: "Szógyakoriság ismét (de most saját fájlból, R használatával elemezve)"
date: 2010-07-14T19:53:00.001Z
publishDate: 2010-07-14T19:53:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/07/szogyakorisag-ismet-de-most-sajat.html"
regi_cimkek:
  - "R"
  - "korpusznyelvészet"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "R"
  - "gnuplot"
  - "korpusznyelvészet"
  - "számítógépes nyelvészet"
  - "szógyakoriság"
---

**Az előző technikai jellegű [posztomban](http://bit.ly/9H52qu) a Magyar Webkorpusz alapján vetettünk egy pillantást a szógyakoriságra. Most egy saját szöveges fájlból készítünk szógyakorisági témát.**  
  
**Eszközök**  
**Egy szövegfájl** Keressünk egy szövegfájlt az [OSZK MEK](http://bit.ly/d9Gibg%20) honlapján. Válaszd a html formátumot.  
**HTML "kitisztító"** html2text, ha Ubuntu, vagy Linux alapú oprendszered van akkor a szokásos módon telepítheted. Vagy választhatod a python alatt bármikor bárhol futtatható [verziót](http://bit.ly/bQs0Ui) is. Házi feladat, készíts a html fájlból egy "plain text" fájlt. A program [man page](http://bit.ly/9VtKLD)-e talán segít.  
**Egy kész szövegfájl letölthető[ itt](http://zolizoli.webs.com/files/rejto06.txt), ha lusta vagy (vagy valamiért nem tudod magad megcsinálni).**  
**R** Ha még nincs fent a gépeden, akkor telepítsd fel az [R statisztikai programozási nyelvet](http://bit.ly/cr5PYi).  
  
**A feladat**  
Arra vagyunk kíváncsiak hogy egy adott szó hányszor fordul elő a fájlban. Gondolkozz egy kicsit milyen problémákat vet ez fel. Mi az hogy szó? Mi neked egy szó és mi a számítógépnek? Mi nagyon egyszerű definíciót adunk itt, *szónak egy olyan karaktersort tekintünk amit két nem-karakter között összefüggően fordul elő*. Jó mi? (Kicsit gondolkozz el azon hogy ez mennyire jó meghatározás, hogyan kellene finomítani hogy megfeleljen a szó intuitív fogalmának) Elgondolkodtál? Akkor egy kicsit még maradjunk a témánál. Nyilván így egy halandzsa, vagy félreütött karaktersor is szó (pl asAnza), felmerül a kérdés hogy a "tó" "tavak" egy vagy két szó-e (nálunk kettő, mivel technikailag nagyon nehéz lenne morfológiailag elemezni). Mi van a mondat elején nagybetűvel kezdett "Asztal" és a csupa kisbetűs "asztal" esetében? Ezt könnyű megoldani, nem okoz gondot átalakítani a karaktereket. Nyilván figyelembe kell venni ezeket a kérdéseket. De ha eltekintünk ezektől, attól még egy becslést tehetünk.  
  
Vágjunk bele!  
Indítsd el az R-t abban a könyvtárban ahol a szövegfájlod található. Először olvassuk be a fájlt hogy tudjunk vele dolgozni.  
  
> textfile<-scan(file.choose(), what="char", sep="\n", quote="", comment.char="")  
**Figyelem!** Mac és Windows használók a file.choose() függvényt cseréljék ki choose,files() -ra.  
  
Alakítsuk át a fájlt csupa kisbetűs karakterek sorává. (Ugye mondtam hogy egyszerű lesz, "Asztal"-ból, "asztal" lesz így)  
> textfile<-tolower(textfile)  
  
Abban maradtunk hogy "*szónak egy olyan karaktersort tekintünk amit két nem-karakter között összefüggően fordul elő*" . Ez R-ben:  
> words.list<-strsplit(textfile, "\\W+")  
  
Fent semmi mást nem tettünk mint a fájl tartalmát "feldaraboltuk" a "nem szó-karakterek" mentén. Ezt a \W+ reguláris kifejezéssel értük el [(szabályos kifejezéseknek](http://bit.ly/a7U820) is hívják őket, ha angolul keresed regular expressions).  
  
Egy kicsit bonyolítsuk a dolgot. Tudjuk az előző posztból hogy bizonyos szavak nagyon gyakoriak. Ezeket gyakran töltelékszavaknak hívjuk, vagy angolos szakzsargonnal [stop words](http://bit.ly/cmNTla). Ha kiszűrjük ezeket a szavakat, akkor egy kicsit jobb képet kaphatunk hogy a normális szavak milyen gyakoriak (kontentívumok maradnak, mivel a legtöbb töltelékszó funktor). Tegyük ezt akkor! Először is egy listát készítünk ezekről a faramuci szavakról:  
  
> stop.list<-c("a", "egy", "be", "ki", "le", "fel", "meg", "el", "át", "rá", "ide", "oda", "szét", "össze", "vissza", "de", "hát", "és", "vagy", "hogy", "van", "lesz", "volt", "csak", "nem", "igen", "mint", "én", "te", "ő", "mi", "ti", "ők", "ön", "ez", "az", "ha")  
  
Alakítsuk egy kicsit át a beolvasott szövegfájlt:  
> words.vector.h<-unlist(words.list)  
  
Most már egy adat típusba tartozik a beolvasott szöveg és a töltelékszavak listája is, ki is szűrhetjük őket.  
> words.vector<-words.vector.h[!(words.vector.h %in% stop.list)]  
  
A következő lépésekben pedig elmentjük a gyakorisági táblázatot egy kimeneti fájlba.  
> freq.list<-table(words.vector)  
> sorted.freq.list<-sort(freq.list, decreasing=T)  
> sorted.freq.list<-sorted.freq.list[sorted.freq.list>1]  
> sorted.table<-paste(names(sorted.freq.list), sorted.freq.list, sep="\t")  
> cat("WORD\tFREQ", sorted.table, file=file.choose(), sep="\n")  
  
**Bónusz gnuplot bütykölés**  
A gyakorisági adatokat csökkenő sorrendbe tettük és a csak egyszer előforduló elemeket is kiszűrtük (hogy nagyon okos legyél olvasd el mi az a [hapax legomenon](http://bit.ly/b9LhVA), na azé' szűrjük ki!). Most hogy elmentettük, gnuplot-tal az előző [posztomban](http://bit.ly/9H52qu) leírtak szerint készíthetsz egy szép ábrát hogy lásd arányaiban hányszor fordul elő egy-egy elem. Az enyém így néz ki.

![](http://zolizoli.webs.com/files/abra.png)

Ha összeveted az előző ábrával láthatod hogy nincsenek kiugró vonalak (hapax legomena!). Nem is kezd olyan magas értéknél, de hát kisebb is a mintánk. A lényeg hogy szebb (lehet hogy csak nekem).  
  
**Ha érdekel akkor ezt olvasd**  
A poszt megírásához [Stefan Th. Gries](http://bit.ly/b8z7t8) [Quantitative Corpus Linguistics with R](http://amzn.to/bB9VVl) könyve adott inspirációt, a kódrészleteket pedig minimális változtatással vettem át.
