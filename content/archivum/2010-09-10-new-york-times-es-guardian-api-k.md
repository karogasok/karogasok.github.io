---
title: "A New York Times és a Guardian API-k használata"
slug: "new-york-times-es-guardian-api-k"
date: 2010-09-10T14:45:00.004Z
publishDate: 2010-09-10T14:45:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/09/new-york-times-es-guardian-api-k.html"
regi_cimkek:
  - "R"
  - "adatok tudománya"
  - "data science"
  - "digitális bölcsészet"
  - "korpusznyelvészet"
  - "vizualizáció"
regi_cimkek_mind:
  - "R"
  - "adat vezérelt újságírás"
  - "adatok tudománya"
  - "data driven journalism"
  - "data journalism"
  - "data science"
  - "digitális bölcsészet"
  - "korpusznyelvészet"
  - "processing"
  - "vizualizáció"
---

**Ahogy az előző posztokban említettem sokan reménykednek abban hogy a neten összegyűlt hatalmas adat mennyiség betekintést nyújthat abba hogyan is működik a nyelv. Habár sokat segíthet ha rengeteg adattal rendelkezünk, ennek vannak határai - ahogy erre pl [Kilgariff](http://www.kilgarriff.co.uk/publications.htm) is rámutatott. Nem is beszélve a technikai és jogi korlátokról.**  
  
  
  
**A nyílt kormányzás eszméje**  
 Gondoljuk egy kicsit tovább a dolgokat. Nem csak roppan mennyiségű nyelvi adat generálódik ám nap mint nap, hanem mindenféle más is. Minden országnak megvan a maga KSH-ja, nekünk európaiaknak meg még van egy Eurostatunk is, benne vagyunk egy halom nemzetközi szervezetben (pl ENSZ és annak szatellit szervezetei WHO stb) amik szintén szépen gyártják a maguk statisztikáit. Ezekről ki-ki kiadja a maga kis összefoglalóját, vagy éppen pénzt kér a bővebb adatokért. De miért nem nyilvánosan hozzáférhetők ezek az adatok? Miért nem készítheti el maga az adófizető állampolgár az adatok elemzését? Ahogy a nyílt/szabad szoftver megteremtette az "érdek nélküli" együttműködést és tényleg minőségi termékeket képes produkálni, ugyanúgy nagy lehetőségek rejlenek abban ha szabaddá tesszük az adatokhoz való hozzáférést . Ez nem csak afféle hippi ideológia! Az angolszász világban mindenhol születtek már kormányzati kezdeményezések az adatok felszabadítására, összekapcsolva a gov2.0 (kb. webkettes eszközök beemelése a kormányzat eszköztárába). Akit érdekel a sztorinak ez az oldala is, ajánlom a wikipedia [open government](http://bit.ly/bqlwE6) szócikkét, az O'Reilly Media [Gov 2.0 Summit ](http://bit.ly/aIXK2g)oldalát, illetve a Lathrop és Ruma [Open Government](http://oreil.ly/bIwPqy) könyvét. És már arra is akad példa hogy emberek tényleg kódolnak a közösségükért, megéri megnézni a [Code for America](http://bit.ly/b7Z6Ct) oldalát (és elgondolkodni hogy miért nincs ilyen hazánkban és az EU-ban).  
  
**Nyílt adatok**  
 Nos nem csak a kormányzati szervek gyűjtenek adatokat. Manapság minden cég elkerülhetetlenül adatokat generál működése során, ezek feldolgozása az [üzleti intelligencia ](http://bit.ly/9ih9oe)területe. De van egy olyan terület ami szintén adatokkal dolgozik; az újságírás. A zsurnaliszták adatokkal dolgoznak (persze itt nem a bulvár médiára gondolok), alapesetben a gazdasági újságíró lételeme a gazdasági statisztika, de a sportújságíró sem lehet meg adatok nélkül, és hát egy társadalmi riport is jó ha adatokkal van megtámogatva. Szerencsére a klasszikus újságírók nem azok a profithajhász, bezárkózó emberek és felismerték hogy a negyedi hatalmi ág is sokat tehet azzal a demokráciáért ha közzéteszi az általa összeszedett anyagokat. Ezt pedig a [New York Times](http://bit.ly/9NWMx9) és a [Guardian](http://bit.ly/damPpK) lapok profi módon tették meg. Nem csak egyszerűen letölthetők az adatok össze-vissza, hanem jól megtervezett API-kat hoztak létre erre. Ez pedig egy új újságírói módszertan kialakulását hozta magával, az adat újságírást (data journalism/data-driven journalism). Sajnos ennek bemutatása szétfeszítené egy poszt kereteit, az érdeklődő olvasónak ajánlom hogy olvassa el és nézze meg [hogyan készült a Guardian API](http://bit.ly/ds5scS), és egy kis posztot arról hogy [hogyan áll a helyzet a kontinentális Európában](http://bit.ly/9uUBlB) és megéri az augusztusban lezajlott [data driven journalism](http://bit.ly/d3s2T0) konferencia anyagait és nézegetni.  
  
**Hogy kerül ide a nyelvészet?**  
 Végre! Ideértünk! Nos, a legtöbb szépen megtervezett korpusz részét képezi egy "hírlap" minta. Nos, mindkét API lehetővé teszi a tartalom keresését, méghozzá nem csak egyszerűen kulcsszavakra kereshetünk, hanem a publikálás dátuma, tagek stb szerint. Tehát nem csak a klasszikus adatok (GDP, munkanélküliség, stb) hanem maguk a cikkek is hozzáférhetőek. Így egyaránt használhatjuk az újságok tartalmát klasszikus nyelvészeti kutatáshoz, vagy épp számítógépes nyelvészeti rendszerekben (én eddig 'sentiment analysis'-ről, tőzsdei hírekkel kapcsolatos szakértői vélemények kinyeréséről és választási hírek elemzéséről hallottam, de tutira van ezer és egy más felhasználásuk is).  
  
**Egyszerű tartalom keresés R segítségével**  
 Mi most megnézzük hogyan is indulhatunk el. Nem fogunk itt nagy dolgot véghez vinni. Gyakorlott programozók pedig takarják el a szemüket! Felteszem hogy az olvasó beszerezte már az API kulcsait, ha nem most itt az idő hogy a [New York Times](http://bit.ly/9NWMx9) és a [Guardian](http://bit.ly/damPpK)  oldalain ezt megtedd. Szükséged lesz még az R legújabb verziójára (Ubuntusoknak ajánlom [ezt a rövid írást](http://bit.ly/9y74Bg)) és installálnod kell a [stringr](http://bit.ly/cv3KS6) és az[ RJSONIO](http://bit.ly/bQZKod) csomagokat is.  
  
 Ha ez megvan, akkor kezdjük a Guardian-nel. Milyen gyakran említik kis hazánkat a britek? Nézzük!  
  
 library(stringr)  
 query = 'hungary'  
 u = 'http://content.guardianapis.com/search?q='  
 u_end = '&order-by=newest&format=json&api-key=ide-jön-a-te-api-kulcsod&tag=tone/news,politics/politics'  
 address = paste(u, query, u_end, sep="")  
 raw.data = readLines(address, warn="F")  
 regexp <- "([[:digit:]]{4})-([[:digit:]]{2})-([[:digit:]]{2})"  
 d <- str_extract(raw.data,regexp)  
 dates.frame <- as.data.frame(d)  
 plot(dates.frame)  
  
 Mit csináltunk itt? A query változóba tároljuk hogy mire keresnénk a tartalomban, ha más kifejezése akarunk rákeresni, egyszerűen kicseréljük. Az u és az u_end változók közé kerül be a keresett szó, mivel és a paste() függvénnyel tkp összefűzzük egy url címmé. Így nem teszünk mást mint a böngészőnk egy oldal betöltésekor. Érdemes beütni az R konzolba a raw.data kifejezést és egy entert hogy lássuk hogy néz ki amit letöltöttünk. Én úgy gondoltam a legegyszerűbb ha megnézzük mikor is publikálták azokat a cikkeket. Erre az ún "szabályos kifejezéseket" (regular expressions/regex) használjuk, itt a ÉÉÉÉ-HH-NN formátumot keressük segítségükkel. Az str_extract() függvény megkeresi az összes előfordulást, ezt pedig az as.data.frame() függvénnyel tkp egy táblázattá alakítjuk, amiből pedig egyszerűen készíthetünk grafikont a plot() függvénnyel (ahogy a táblázatkezelők is táblákból készítenek ábrát). Én ezt kaptam:  
<span class="lost-media">Hiányzó kép: <a href="http://lh5.ggpht.com/_SM9YHwWrX6M/TIpg_WMVQNI/AAAAAAAAAT0/EwlBHtDQ-yc/%5BUNSET%5D.png" rel="nofollow noopener">Guardian Content API results for "Hungary"</a></span>  
 Ha érdekel mi mindent lehet "kibányászni" az API által küldött adatokból, a [Wikibooks R könyve](http://bit.ly/925u43) sokat segíthet neked (kiváltképp a [Text Processing](http://bit.ly/dqdO9A) része). A NY Times API használatáról R-ben pedig [itt](http://bit.ly/aoINPt) olvashatsz. A poszt sokkal szofisztikáltabb példa programot mutat be, de ez persze azzal jár hogy bonyolultabb a fent bemutatott példánál. Remélem kedvet kaptál a felfedezéshez, és bonyolultabb kereséseket és grafikonokat is fogsz készíteni!  
  
 Az API-k és a Processing  
 Sokan nem szeretik az R grafikáját. Nos ebben van is igazság, annyiban hogy szép és színes-szagos grafikát nehéz R-ben készíteni. Nagyon érteni kell a nyelvhez, és ugye az interakció hiányzik. De ugye ott a Processing, csak valahogy használni kellene! Nos mint mindig itt a legfőbb gond az hogyan kapcsolódjunk az API-hoz. Persze öreg róka programozóknak ez nyilvánvaló, de a kezdőknek bele törik ám a bicskája rendesen!  
  
 Nos a lényeg hogy a kapott adatokat valahogy értelmezni kell. Az adatokat vagy xml vagy JSON formátumban kapjuk az API-tól. Szerintem egyszerűbb a JSON (bővebben[ itt ](http://bit.ly/dnn11V)olvashatsz erről) és egy alapos kis útmutató megmutatja neked [itt](http://bit.ly/aeaKyU) hogyan teheted képessé processing vázlataidat kezelésére.  
 Nos nézzünk egy nagyon egyszerű példát. Hogyan tudjuk egy-egy keresés összes előfordulását megtalálni és szépen összevetni.

```
import org.json.*;

String baseURL = "http://api.nytimes.com/svc/search/v1/article";

String apiKey = "ide-jön-az-api-kulcsod";

void setup() {
size(600,300);

String[] words = {
"Hungary", "Slovakia", "Romania", "Poland", "Austria"
}
 color[] colors = {
#FF0000, #00FF00, #0000FF, #FF3300, #FF9900
}
int barSize = 25;
int startY = 80;

String start = "20050101";
String end = "20100101";

for (int i = 0; i < words.length; i++) {
int freq = getArticleKeywordCount( words[i], start, end);
fill(colors[i]);
rect(0, startY + (barSize * i), freq/5, barSize);
}
}

void draw() {
}
int getArticleKeywordCount(String word, String beginDate, String endDate) {
String request = baseURL + "?query=" + word + "&begin_date=" + beginDate + "&end_date=" + endDate + "&api-key=" + apiKey;
String result = join( loadStrings( request ), "");

int total = 0;

try {
JSONObject nytData = new JSONObject(join(loadStrings(request), ""));
JSONArray results = nytData.getJSONArray("results");
total = nytData.getInt("total");
println ("There were " + total + " occurences of the term " + word + " between " + beginDate + " and " + endDate);
}
catch (JSONException e) {
println ("There was an error parsing the JSONObject.");
}
return(total);
}
```

Nos ez valami ilyet produkált nálam:  
<span class="lost-media">Hiányzó kép: <a href="http://lh5.ggpht.com/_SM9YHwWrX6M/TIpoMAhSquI/AAAAAAAAAT4/X19DHKWulJ0/%5BUNSET%5D.png" rel="nofollow noopener">%5BUNSET%5D.png</a></span>  
 Az apiKey változóba értelemszerűen írd be a saját api kulcsodat. A start és end date változókkal kijelölheted milyen időintervallumban keressen a tartalomban a programod. Remélem ennyi elég hogy ráérezz a dologra és legalább a példa programokat módosítgatod majd. Itt nincs jó vagy rossz megoldás. A cél itt szentesíti az eszközt! Ha van egy kérdésed amire a Guardian vagy az NY Times korpusza válaszolhat, akkor egy kis barkácsolással megtalálhatod azt!
