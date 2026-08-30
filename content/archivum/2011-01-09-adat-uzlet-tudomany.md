---
title: "Adat, üzlet, tudomány (frissítve)"
date: 2011-01-09T17:49:00.004Z
publishDate: 2011-01-09T17:49:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/01/adat-uzlet-tudomany.html"
regi_cimkek:
  - "adatok tudománya"
  - "nltk"
regi_cimkek_mind:
  - "adatok tudománya"
  - "factual"
  - "freebase"
  - "google prediction api"
  - "google refine"
  - "nltk"
---

**Ahogyan arról már korábbi posztunkban beszámoltunk, kialakulóban van egy új alkalmazott tudomány mely megpróbálja komplex módon kezelni és elemezni a megnövekedett adatmennyiséget. A hangsúly az alkalmazott jelzőn van, hiszen már napjainkban is vannak olyan cégek melyek adattudományi módszereken alapuló megoldásokat kínálnak, ezek közül próbálunk meg párat bemutatni.**  
  
  
  
  
**Google Prediciton API**  
 A legjobb példa arra hogy miképp lehet a gépi tanulás és a komputációs statisztika eredményeit mindenki számára hozzáférhetővé tenni a [Google Prediction API](http://bit.ly/e6wxfB)-ja. Akinek van adata és hozzáférése az API-hoz, az rengeteg elemzési módszer közül választhat. Persze nem árt tudni programozni, de a belépés szintje folyamatosan csökken. A Google Spreadsheets-ben elérhető [Google Apps Script](http://bit.ly/ibs9ul)-en keresztül is elérhető a szolgáltatás, így egy "mezei" táblázatkezelő elemző is igénybe veheti. Ez nagy szó, hiszen az átlagos szociológus, politológus vagy éppen közgazdász az SPSS, SAS vagy hasonló, egyszerű szkript nyelvet már ismeri valamennyire. Így ha nem is tömegtermékké, de eléggé széles réteg számára hozzáférhetővé válik a statisztikai előrejelzés. Nem beszélve arról hogy a Google saját rendszere is sokat tanul a feltöltött adatok alapján, így nem csak a használati díjjal gyarapodik. (Bővebben a Prediction API fizetős rendszeréről [itt](http://rww.to/f9Ji6b) olvashat a kedves olvasó)  
  
**Az adat önmagában is aranyat ér**  
 Ha végig gondoljuk hogy milyen adatokra lehet szüksége egy vállalatnak vagy éppen egy kormányzati szervnek akkor könnyű belátnunk hogy önmagában ezek beszerzése is nagy üzlet lehet. Pláne ha nem nyersen, hanem szépen kitisztítva, az elemzésekre előkészítve adjuk el az adatot.  
  
 Az [Infochimps](http://bit.ly/fZUulZ) egy adat piac. Lehet keresni ingyenes és fizetős adatokért, egy viszonylag egyszerű API-t is kínál és saját adatainkat akár el is adhatjuk itt. A [Data marketplace](http://bit.ly/ff5Ibi) (az Infochimps akvizíciója immár) is hasonló modellt követ, ám itt nem csak eladásra ajánlani lehet adatokat, hanem kérni is lehet.  
  
 A Prediction API fizetős verziója után érthető hogy a Google miért kebelezte be a Metaweb-et és annak Freebase nyílt, szemantikus metadatokat tartalmazó tudás adatbázisát és Freebase Gridwork adattisztító eszközét. A [Freebase](http://bit.ly/gIhUY8) remek kiegészítője az automatikus adattisztításnak, hiszen segítségével könnyedén felturbózhatjuk adathalmazunkat értékes információkkal, ez pedig különösen fontos az ún. nem strukturált adatok esetében. A mostmár [Google Refine](http://bit.ly/dSaEid) néven futó Gridworks tkp. ezt a strukturálási folyamatot végzi el, több-kevesebb sikerrel. Lehet hogy nem az volt a Google célja a kezdetektől hogy megágyazzon fizetős előjelzés szolgáltatásának, de remekül sikerült ezt megtennie így utólag visszatekintve... [Kedves vécsé nevű, amúgy legszorgalmasabb, olvasónk hívta fel figyelmemet arra hogy itt érdemes megemlíteni a [Google Visualization API](http://bit.ly/hLIdPv)-t is, hiszen remekül illeszkedik a képbe. Ha figyelembe vesszük hogy a Google-nél immár sok közgazdász, statisztikus és hci szakember dolgozik és a legújabb akvizíciók és Labs ötletek mind ezzel a területtel foglalkoznak, arra következtethetünk hogy a Google új piacok felé kacsingat, talán át is pozicionálja magát - legalábbis olvasónk szerint]  
  
 A [Factual](http://bit.ly/e2j9sE) strukturált adatokat ad (nagy részt ingyen) a felhasználók kezébe, melyeket könnyen illeszthetnek alkalmazásaikba. A Facebook Places szolgáltatás is a Factual adatbázisán alapul ami remek példája annak hogy akár adatvezérelt vállalatok is együttműködhetnek. Azonban ez a cég nem csak adatokat kínál, hanem sémát is amiben érdemes gyűjteni adatainkat, egy nagyobb adathalmazt amibe illeszkednek adataink. Egy kis, vagy akár egy közepes vállalkozás számára is értelmetlen dolognak tűnhet saját sémával és adatbázissal bajlódni, a Factual sokak számára kínál előre csomagolt megoldást. Itt a nyereség főleg abból származik hogy ha a felhasználó bővíti az adatbázist, az a Factual szerverein is megjelenik ami még pontosabbá teszi az adatbázist és a további ügyfelek számára még nagyobb és pontosabb portékát lehet ajánlani. Hogy ez működni fog-e az a jövő zenéje, hiszen még nincs hivatalos árazási modell bevezetve a cégnél. Aki szeretne megismerkedni a Factual API-val, regisztráljon gyorsan, amíg ingyenes a dolog!  
  
**Számítógépes nyelvészeti elemzés mint szolgáltatás**  
 Kedvenc bloggerem [Jacob Perkins](http://bit.ly/fkE8lr) ([streamhacker.com](http://bit.ly/ew2ZgK)), aki egyben a [Python Text Processing with NLTK 2.0 Cookbook](http://amzn.to/hBQXag) könyv szerzője egy érdekes kísérletbe fogott mivel szeretné a számítógépes nyelvészetet tömegtermékké tenni. Ezért jelenleg négy API-t tett elérhetővé, érzelmi viszony elemzés, stemming, pos tagging frázis kinyerés és entitás felismerés területén. Ezek ingyenesek és persze limitáltak, de reméljük hogy Jacob kísérlete életképes lesz, az érdeklődő olvasó pedig kipróbálhatja a demokat, ill az API-t ha meglátogatja a [text-processing.com](http://bit.ly/i0wknQ) oldalt.  
  
 Érdemes megjegyezni hogy egy természetes nyelvi elemző szolgáltatás nem légből kapott ötlet. A népszerű elemző csomagok, mint pl az SPSS és a SAS is rendelkeznek ilyenekkel (text analytics néven futnak). Az érzelmi viszonyulás elemzése (sentiment analysis) is egyre inkább bevett módszer a marketing és a társadalomkutatás területén, ez is vastagon számítógépes nyelvészet, így piaca biztos hogy van az ilyen megoldásoknak, csak az a kérdés hogy miképp lehet azt elérni.  
  
**Összegzés**  
 Az adatoknak van piaca, főleg az adatelemzésnek. Hogy milyen ez a piac az a jövő zenéje, de mindenképpen érdekes és szép dolgok állnak előttünk. A tudomány számára kész felüdülés, egy kegyelmi állapot következik, amikor ténylegesen együttműködhet az üzlet világával és az elméleti problémák megoldása pozitívan hathat életünkre. Ez legalább ennyire fontos az üzleti világnak is, hiszen nem csak profitot szerezhetnek a területen vállalkozók, hanem hatással lehetnek az emberekre, jobbá tehetik egy kicsit világunkat. A nagy szavak néha pedig fontosak...
