---
title: "Könyvismertető: Getting Started with Processing"
date: 2010-08-06T17:13:00.001Z
publishDate: 2010-08-06T17:13:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/08/konyvismerteto-getting-started-with.html"
regi_cimkek:
  - "kezdő"
  - "könyv"
regi_cimkek_mind:
  - "kezdő"
  - "könyv"
  - "processing"
  - "programozás"
---

**Sokan kérték hogy egy egyszerű, mindenki számára érthető bevezető könyvet ajánljak. Dióhéjban: a Processing nyelvet egyszerűen, példákon keresztül el lehet sajátítani akár egyedül is, hiszen alapvetően vizualizációkat készít vele az ember és "látásra"[![getting-started-with-processing](http://farm5.static.flickr.com/4082/4865363103_c263cb7894.jpg)](http://www.flickr.com/photos/szgny/4865363103/) el tudjuk dönteni hogy azt érte-e el a kódunk amit akartunk. A Processing-et tekinthetjük speciális Javanak, elsajátítása után könnyen áttérhetünk a nagy testvér használatára is. Ne feledjük azt sem hogy nagyon szórakoztató bütykölni egy ilyen nyelvet!**

- **O'Reilly/Make**,  2010

- **Angol nyelvű**

- **ISBN-10:** 144937980X

- **Szerzők:** Casey Reas, Ben Fry

**Mi is az a Processing?**  
Saját ön meghatározása szerint a [Processing](http://processing.org/) " is an open source programming language and environment for  
 people who want to create images, animations, and interactions" azaz egy nyílt forráskódú programozási nyelv és környezet azok számára akik képeket, animációkat és interakciókat akarnak készíteni.  
  
Ezt a meghatározást nem árt kiegészíteni. A szokványos komparatív programnyelv tanulmányokban két táborra oszlanak a szakik a Processing kapcsán. Mivel a Processing sokkal inkább egy környezet (egy IDE és pár hasznos cucc) és egy Java könyvtár, hiszen majdnem 100%-ban standard Java szintaxist használ, Java byte code-ot produkál és a JVM-en fut. Ugyanakkor nem tiszta Java, mind a strukturált, mind az objektum orientált paradigmát támogatja. Ha ehhez még hozzá vesszül hogy akadnak egyéb JVM-en futó nyelvek (Groovy, Scala, Clojure) akkor csak nagyobb a homály. Maradjunk annyiban hogy a Processinget itt nyelvnek nevezzük és észben tartjuk szoros kapcsolatát a Javahoz.  
  
**Minek nekünk egy újabb nyelv?**  
Szerintem gyakran ennek nincs más oka mint hogy a készítő szeretett volna egy saját nyelvet, ami neki megfelel. A Processing alapvetően [Casey Reas](http://en.wikipedia.org/wiki/Casey_Reas) és [Ben Fry](http://benfry.com/) fejéből pattant ki, akik híres [MIT Media Lab](http://media.mit.edu/)-ben [John Maeda](http://en.wikipedia.org/wiki/John_Maeda) doktoranduszai voltak. Maeda a kilencvenes években érdeklődött hogy miképp lehetne a digitális művészek, dizájnerek és nem-programozók számára megkönnyíteni a belépést a programozás világába, ennek eredménye lett a Design by Numbers nyelv lett, ami habár már nem egy aktív projekt, inspirálta a Processing alkotóit.  
  
Reas és Fry koncepciója szerint a nem technikai háttérrel rendelkező (de kellően motivált) alkotó emberek nem egy játékot akarnak. Egy eszközre van szükségük, amivel elintézhetik amit akarnak. Többek között ezért nem áldozhatták fel a gyorsaságot (ne feledjük egy grafikus program bizony számításigényes) és választották a Java-t kiindulási alapul. Ugyanakkor törekedniük kellett a használhatóságra, amit szerintem az egyszerű programozási környezettel el is értek.  Habár a Processing megengedi hogy a feladat nehézsége és tudásunk szintje szerint megválasszuk milyen paradigmát használunk (szimpla parancsokat adunk, procedurális modorban függvényeket definiálunk vagy objektum orientáltan alkotunk) a használó nagyon gyorsan el fog jutni az OO módhoz ha naponta pár kis programot megír. Így habár egy kontinuumot képzelhetünk el az első Processing sketch és az első Java programunk között, sokan megmaradnak a rugalmas környezetben.  
  
Fontos kiemelni hogy pedagógiai szempontból is jó ötlet egy grafikus programozási nyelvvel kezdeni. Hasonló elveken (csak más korosztálynak) épült fel a [Scratch](http://scratch.mit.edu/) is. Ha a kód manipulálását direkt vizuális visszajelzés követi egyszerűbben és gyorsabban halad a programozás elsajátítása is.  
  
**Nézzük a könyvet**  
A könyv vékony és nem is olyan drága, sok ábrával és példa programmal van megspékelve, vizuálisan kifejezetten hívogató. Nem is beszélve hogy a Processing két atyja mint szerző meggyőzőnek hangzik. Egy ilyen vékony kötettől persze ne várja senki hogy hacker lesz mire a végére ér, de ha valaki szépen végig csinálja a példa programokat és veszi a fáradságot hogy egy kicsit módosítgassa őket, akkor képes elsajátítani mind a Processing nyelv, mind pedig a programozás alapjait (mi egy változó, mi az hogy iteráció, kondicionális, mi a különbség egy osztály és egy objektum között stb). Ennél nem is ígérnek többet a szerzők az előszóban.  
  
Grafikus nyelvként az alapokkal indul a könyv (pont, vonal, kör koordinátákkal való képernyőre rajzolása), majd szépen halad az alapvető kontroll struktúráktól az osztályokig. Minden fejezet végén egy nagyobb projekt várja az olvasót; egy robotot készíthetünk ami egyre szebb és több képességgel rendelkezik. Ez nem csak mókás, de meg is mutatja hogyan használhatjuk egy hosszabb kódban (vagy mini projektben) megszerzett tudásunkat.  
  
Az utolsó fejezet inkább arról szól hogy merre tovább, alapvetően az [Arduino](http://www.arduino.cc/) és a processing honlapja ajánlható ha tényleg jobban el akarsz mélyedni ezen a területen, de nem árt persze elolvasni azt a néhány oldalt.  
  
**Pro és kontra**  
Ami nekem kifejezetten tetszett az egyrészt hogy tele van a könyv jó tanácsokkal, apró trükkökkel hogyan kell programozni (kommenteld ki a kód egy részét, használd a println() függvényt hogy lásd a koordinátákat stb) és egy külön függeléket szentelnek a további, általános praktikáknak. Mivel a a változók hatóköre sokszor okoz problémát a kezdők számára, ennek is külön függeléket szántak, továbbá a különböző beépített típusoknak is, érdemes ezt a részt elővenni ha valami nem világos. Ez már csak azért is fontos, mert a könyvben gyakran találkozunk olyan változó deklarációkkal amikor nincs érték rendelve a változóhoz explicite (sőt ez tovább van bonyolítva egy autoincrement operátorral is).  
  
**Összevetve más könyvekkel**  
Természetesen nem ez az egyetlen jó könyv amiből megtanulhatsz programozni és a Processinget használni. A Processing honlapján találsz egy [komplett listát](http://processing.org/learning/books/) a megjelent (és hamarosan megjelenő) könyvekről, érdemes megnézni hogy a számodra legmegfelelőbbet kiválaszthasd. Itt most csak az általam ismert, főleg kezdőknek szánt könyvekre szorítkozom.  
  
[Processing: A Programming Handbook for Visual Designers and Artists](http://www.amazon.com/gp/product/0262182629?ie=UTF8&tag=processing09-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0262182629), Reas and Fry, MIT Press, 2007  
Címéből adódóan ez egy kézikönyv. Rengeteg hasznos példát találsz benne, ha van egy kis programozási gyakorlatod akkor pusztán ezzel a könyvvel is elindulhatsz. Viszont az ára egy magyar átlag ember/diák számára nem barátságos.  
  
[Learning Processing: A Beginner's Guide to Programming Images, Animation, and Interaction](http://www.amazon.com/gp/product/0123736021?ie=UTF8&tag=processing09-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0123736021), Daniel Shiffman, Morgan Kaufmann, 2008  
Ez a KÖNYV minden kezdőnek, kiváló támogató oldallal és sok-sok feladattal. Viszont az ára húzós (nekem legalábbis az) és ha tényleg gyorsan akarsz valami használhatót, akkor ez talán kicsit hosszú. Ha nem követed teljes figyelemmel könnyen elveszhetsz.  
  
[Processing: Creative Coding and Computational Art (Foundation](http://www.amazon.com/gp/product/159059617X?ie=UTF8&tag=processing09-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=159059617X)), Ira Greenberg, Friends of Ed., 2007  
Nekem nagyon vegyes benyomásaim vannak ezzel kapcsolatban. Nyilván nem tartozom a célcsoportjába (művészlelkek). A stílusa nem a szokványos technikai, száraz, tömör leírás, hanem szép elbeszélés.  
  
[Visualizing Data](http://www.amazon.com/gp/product/0596514557?ie=UTF8&tag=processing09-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0596514557), Ben Fry, O'Reilly, 2007  
Nem kezdőknek való, de mindenképpen hasznos. Amolyan tutorialba öntött ötlettár hogy hogyan prezentáld adataidat.  
  
**Összegezve**  
A Getting Started with Processing azt teszi amit ígér, elindít a kódolás világába mindezt magas színvonalon és még nekünk is elérhető áron.
