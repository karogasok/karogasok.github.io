---
title: "Hogyan kezdtem szófajelemzőt írni?"
date: 2011-04-05T08:04:00.002Z
publishDate: 2011-04-05T08:04:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/hogyan-kezdtem-szofajelemzot-irni.html"
regi_cimkek:
  - "korpusznyelvészet"
  - "nltk"
  - "python"
  - "vendégposzt"
regi_cimkek_mind:
  - "korpusznyelvészet"
  - "nltk"
  - "python"
  - "trainer"
  - "vendégposzt"
---

Tempfli Péter vendégposztja

**A probléma**

**Ahhoz, hogy lehessen valamit mondani egy mondatról, jó tudni, miféle cselekvést vagy történést ír le; egy vagy több alany csinálja-e, megtörtént, történni fog, esetleg csak vágyunk arra, hogy megtörténjen. Egyszóval, az ige és a kapcsolódó elemek számos hasznos információt hordoznak. Ha géppel akarom megkeresni ezeket az adatokat, egy olyan eszközre van szükség, ami felismeri az igéket egy adott szövegben és kinyeri a fenti információkat. Erre való a szófajelemző(felismerő), angolul part-of-speech tagger (POS-tagger). Az NLTK-ról szóló könyv [ötödik fejezete](http://nltk.googlecode.com/svn/trunk/doc/book/ch05.html) ismertet néhány, az NLTK-be beépített eszközt, de ezeket sajnos csak angol nyelvű szövegeken lehet használni. Magyar nyelvű morfológiai elemző is létezik (a HUNMORPH ill. a HUNSPELL), azonban ezek azon túl, hogy nagyon nehezen konfigurálhatók, azt az örömet is elveszik, hogy magam gondolkozzam el a problémán;) (természetesen ezek nagyon jó eszközök, de professzionális felhasználásra készültek, ezért nem nagyon veszik figyelembe a "barkács-programozók" igényeit)**

Azt a célt tűztem ki magam elé, hogy programom az [Esti Kornél](http://mek.niif.hu/00700/00744/00744.htm) (a Magyar Elektronikus Könyvtár állománya) első néhány bekezdéséből válogassa ki az igéket, és lehetőleg próbálja meg minnél pontosabban megmondani, milyen időben, számban és személyben állnak.

**Előzetes megjegyzések:**

Ahhoz hogy követni tudd a posztot, szükséged van a [Python](http://www.python.org/) programozási nyelvre (2.5 vagy régebbi, de 3.x alatti verzió), az [nltk csomagra](http://www.nltk.org/) és az alábbi [github repo](https://github.com/zolizoli/tempfli)-ban található fájlokra.

**A lehetséges megoldások**

A legjobb az lenne, ha lenne egy óriási szótárunk, ami minden szónak tartalmazza a szófaját. Ez angol nyelven még csak-csak megoldható, ám az erősen ragozó magyar nyelven elég reménytelennek tűnik. Lehetne azt csinálni, hogy minden szóról levágjuk egy "stemmerrel" (szótevezővel) a ragokat, és az így kapott tövet keressük meg az elképzelt szótárban, de sajnos szótár továbbra sincs, és a tövező sem mindig megbízható. A végződésekből azonban mégis kitalálható rengeteg dolog, például ha egy szó 'k'-re végződik, az jó eséllyel többes számú főnév (vagy: melléknév, névmás, ige...). Pontosan ez alapján osztályoz az NLTK regexp-taggere is, vagyis az előre megadott minták alapján határozza meg egy szóalak szófaját. Ez remek ötlet, de sajnos én lusta vagyok felkutatni az összes lehetséges igevégződést és írni belőlük egy vélhetőleg több száz soros szabálylistát. A negyedik, lustáknak való megoldás: mindent a számítógépre bízni -- kicsit "tanítani a nyelvre", aztán meg hagyni, hadd találja ki, milyen szóval áll szemben.

**A tanítás**

Itt kell előrebocsátanom, hogy sem a statisztikához, sem a programozáshoz nem értek, így az itt következőket úgy kell olvasni, mint a saját, leegyszerűsített értelmezésemet, a programot pedig mint dilettáns barkácsolást.

A NLTK rendelkezik több nagyon hasznos és egyszerűen használható gépi tanuló algoritmussal, én a naív Bayes osztályozót fogom használni. Ez az algoritmus a tanuló adatok alapján felállít magának egy szabályszerűségeket leíró szabályhalmazt, majd az "éles" adatokat ezek alapján értékeli ki. Például: ha megmondjuk neki, hogy a "venni" és a "hülyéskedni" infinitív alakok, a "sétálok" és "ugráltak" pedig nem, akkor jó eséllyel a "majomkodni" igét az infinitívek közé fogja besorolni. Ennek megvalósítása pythonban:

[GitHub Gist](https://gist.github.com/901368)

A *classifier*-t az *fs1* nevű tömbbel tanítjuk be, ami párokat tartalmaz. A párok egy szó *bizonyos* tulajdonságát tartalmazzák, illetve az ehhez a tulajdonsághoz tartozó szófajt. A tulajdonságot egy függvény generálja magából a szóból. Tehát az fs1 tömb így néz ki:

[GitHub Gist](https://gist.github.com/901374)

Az INF jelöli a főnévi igenevet, az X pedig minden mást. A legfontosabb az, hogy mit csinál a szóval a *tulajdonsag* nevű függvény:

[GitHub Gist](https://gist.github.com/901377)

A függvény a megadott szó utolsó két betűjét adja vissza. Tehát, a tanuló algoritmus valójában nem is látja a szavakat, csupán a végződéseket. Ezek alapján tanulja meg, hogy a 'ni' általában azt jelenti, hogy 'INF', hiszen leggyakrabban azzal együtt fordul elő. A X-szófajhoz (ami a "minden mást" jelenti) nem képes rendelni semmit, mert ennyi adatban nincs semmiféle szabályszerűség. (mindez sokkal részletesebben az NLTK könyv [6. fejezetében](http://nltk.googlecode.com/svn/trunk/doc/book/ch06.html) olvasható)

**A program**

Ezzel gyakorlatilag készen is van a program lényegi része, a feladatom csupán annyi volt, hogy létrehozzak egy olyan szó-listát, amiből a program képes tanulni. Így néz ki:

tanulni[INF]

tanulok[j-e1]

köszönöm[j-e1]

tanulsz[j-e2]

izzadsz[j-e2]

virít[j-e3]

ellenzi[j-e3]

szeretünk[j-t1]

sejtjük[j-t1]

.

.

átkozták[m-t3]

tudták[m-t3]

akarták[m-t3]

Látható, hogy az igéket 3x2x2, vagyis 12 kategóriába osztottam, idő(j/m), személy(e/t) és szám(1/2/3) szerint. Az alanyi és tárgyas ragozástól eltekintettem, sem a felszólító móddal, sem a műveltető alakkal, sem semmi egyébbel nem foglalkoztam. A program beolvassa az adatbázist, létrehozza a tanuló-mintákat (a szavak és a hozzájuk tartozó kategóriák párjait) és lefuttatja a tanuló algoritmust. A tulajdonság-elemző függvény egy kicsit bonyolultabb lett:

[GitHub Gist](https://gist.github.com/901379)

Látható, hogy nem csak az utolsó két betűt, de az utolsó három, négy, ill. az utolsó előtti 2 és 3 betűt is vizsgálom. Ebben sincsen túl sok morfológiai megfontolás, a próbálgatás alapjám ezek a tulajdonságok váltak be a legjobban. Ennek felmérésében a *classifier.show_most_informative_features()* nevű parancs segít, ami megmutatja, mely tulajdonságok esnek leginkább a latba az értékelés során:

Most Informative Features

ut_2_betu = 'bb' Xfok : X = 10.6 : 1.0

ut_2_betu = 'nk' j-t1 : X = 7.7 : 1.0

ut_2_betu = 'ek' Xpl : X = 6.7 : 1.0

ut_2_betu = 'ik' Xsor : X = 6.5 : 1.0

ut_2_betu = 'el' Xval : X = 6.1 : 1.0

ut_3_betu = 'tem' m-e1 : X = 5.6 : 1.0

ut_2_betu = 'et' Xt : X = 5.5 : 1.0

ut_2_betu = '\xfck' j-t1 : X = 4.9 : 1.0

ut_2_betu = 'ul' j-e3 : X = 4.5 : 1.0

ut_2_betu = 'ta' m-e3 : X = 4.4 : 1.0

ute_2_betu = 'to' j-t2 : X = 4.4 : 1.0

ute_2_betu = 'na' Xnak : X = 4.3 : 1.0

ute_2_betu = 'ne' Xnak : X = 4.3 : 1.0

.

.

**Az egyensúly kérdése**

A fent bemutatott elven felépített adatbázis már viszonylag jó hatékonysággal keresi ki az igéket, azonban van egy komoly hibája: olyan szavakat is igének vesz, amelyek nem azok. Ennek a a magyarázata, hogy az igék leírása túlreprezentált volt a tanuló-adatbázisban, és a Bayes osztályozó abból indul ki, hogy amiből a legtöbb van a tanuló-korpuszban, abból lesz a legtöbb az "éles" adatok közt is. Így nem volt más hátra, mint teleszórni az tanuló-adatbázist "nem-ige" szófajú szavakkal. Az osztályozó ezek után már nem hitte feltétlenül minden, igére picit is hasonlító szóról, hogy az ige, de az eredmény így sem volt kielégítő. Ennek az oka az volt, hogy az igékben sokkal több szabályszerűség fedezhető fel, mint az "nem-igékben", így továbbra is elsősorban az előbbiek tulajdonságai alapján osztályozott a program. A megoldás: differenciálni a nem-igék osztályát is, hogy ott is minnél több szabályszerűség legyen felfedezhető a program számára, és így hatékonyan tudja különválasztani őket az igéktől. Kénytelen voltam hát bevezetni olyan kategóriákat, mint pd. az [Xpl], [Xt], [Xval] (többes szám, tárgyragos főnév, -val/vel végződés). A fenti tulajdonság-kimutatásból látható, hogy az osztályozó csodálatos könnyedséggel találja meg a fokozott mellékneveket (Xfok), a sorszámneveket (Xik), vagy a -val/vel ragot (Xval). A különválasztás valóban sokat segített, a jelenlegi adatbázisban az igéken kívül 12 másik szóosztály található.

Lássuk tehát, mit tud kezdeni a fenti elvek alapján felépített program az Esti Kornél első néhány bekezdésével

(az tanuló-adatbázis mérete 5 kilobájt, kb. 420 szót tartalmaz):

túljártam[m-e1]

**életem[m-e1]**

jutott[m-e3]

Elhatároztam[m-e1]

meglátogatom[j-e1]

fölújítom[j-e1]

érintkeztünk[j-t1]

történt[m-e3]

**közöttünk[j-t1]**

tudja[j-e3]

**Nem[m-e1]**

haragudtunk[m-t1]

elmúltam[m-e1]

kezdett[m-e3]

lenni[INF]

Sértett[m-e3]

Untam[m-e1]

**magas-nyitott[m-e3]**

Fárasztott[m-e3]

kevert[m-e3]

haladtunk[m-t1]

kirántott[m-e3]

élesíteni[INF]

**embert[m-e3]**

szólított[m-e3]

**venné[INF]**

**imént[m-e3]**

hullott[m-e3]

**embert[m-e3]**

vártam[m-e1]

függött[m-e3]

volt[m-e3]

befûttetett[m-e3]

félrevonta[m-e3]

adta[m-e3]

védelmezte[m-e3]

tiszteltek[m-t2]

fürödtek[m-t2]

ültek[m-t2]

történt[m-e3]

**volna[INF]**

Látható, hogy számos hibát ejt a program, azonban ezek jó része megmagyarázható. Egy részük talán orvosolható (a "volna" félreosztályozása bizonyára), a "magas-nyitott" vagy az "embert" esete azonban már elgondolkodtató. Ezek kiküszöbölésére valószínűleg más, a fentitől eltérő osztályozási technikákat is igénybe kell majd venni.

(amennyiben valaki szeretné látni a teljes adatbázist és a programot, kérem írjon a szerzőnek: tempflip-kukac-gmail-pont-com)

**A szerzőről**

Tempfli Péter az MTA Irodalomtudományi Intézet Közép- és kelet-európai osztályának segédmunkatársa, ahol összehasonlító irodalomtudománnyal foglalkozik; szabad idejében blogot ír, amin az orosz nyelv tanulását népszerűsíti. (link: [orosz-blog.blogspot.com](http://orosz-blog.blogspot.com/))
