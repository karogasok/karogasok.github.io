---
title: "Korpusznyelvészet - Unicode; a korpuszkészítés alapjai 2"
date: 2011-08-03T12:19:00Z
publishDate: 2011-08-03T12:19:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/08/korpusznyelveszet-unicode.html"
regi_cimkek:
  - "korpusz"
  - "korpusznyelvészet"
regi_cimkek_mind:
  - "karakterkódolás"
  - "korpusz"
  - "korpusznyelvészet"
  - "unicode"
---

**Az[ előző posztban](http://szamitogepesnyelveszet.blogspot.com/2011/06/korpusznyelveszet-korpuszkeszites.html) végig vettük Leech maximáit, melyek segítenek minket abban hogy használható korpuszt készítsünk. Mivel egy korpusz általában szöveges (de nem szükségszerűen, hiszen már vannak audio korpuszok is) szükségünk van arra hogy a szöveget alkotó karaktereket is egységesen kezeljük, ez teszi lehetővé hogy igény szerinti formában jelenítsük meg, vagy hasonlítsuk össze az egyes korpuszokat. Ez nem csak az eredmények és adatok megosztását, de feldolgozását is megkönnyíti. Sajnos azonban ez nem mindig volt magától értetődő elv, szerencsénkre azonban a dolog változik és a Unicode szabvány terjedőben van. A posztban nem törekszünk arra hogy bemutassuk teljesen magát a szabvány, csupán a mögötte rejlő elveket vesszük sorra és egy kis eligazítást adunk hol tanulhat többet az érdeklődő olvasó (aki kényes a pontos megfogalmazásra és szeretne komolyabban elmerülni a témában, az inkább csak az ajánlott irodalmat fussa át).**

Az egyszerű felhasználónak a karakterek a képernyőn megjelenő betűket jelentik. Aki több gépet és/vagy operációs rendszert használ, bizonyára észrevette már hogy kicsit vagy nagyon másképp jelenik meg ugyanaz a szöveg. Ez azért van mert a "betű" mint szimbólum és annak "megvalósítása" gyakorlati okok miatt különbözik.

Kedvenc szövegszerkesztőnkben (pl. OpenOffice Writer, vagy MS Word) írhatunk egy dokumentumot az alap betűtípussal (ez általában Times New Roman), majd ha valamiért meggondoljuk magunkat egyszerűen váltogathatunk a betűtípusok között. Ilyenkor habár a megjelenítés változik, maga a leírt információ és az azt hordozó karakterek nem. Van valami ami összefogja a betűtípusokat, ahogyan a kézzel írt betűk és a nyomtatott írás között is van valami összefüggés. Ezt a kapcsolatot nevezzük most karakternek, ami nem más mint egy olyan minimális leírás ami változatlan marad a különböző transzformációk során.

A Unicode szabvány igyekszik praktikus kereteken belül minden karaktert felsorolni. A szabványban megtalálható karakterek leírása ezért a következőket kell hogy tartalmazza:

- karakterkép (glyph)

- szám/kód

- egyedi név

- tulajdonságok

- annotációk

Azaz minden karakterhez tartozik egy lehetőleg egyszerű kép (egy jellemző kép, ami a különböző betűtípusok közül a lehető legsemlegesebb), egy azonosító kód, egy egyedi név, a legalapvetőbb (tipográfiai) tulajdonságok és annotációk (megjegyzések, gondoljunk pl. a francia e változataira, **e**, **é,**  **è, ê** és    **ë** alakokban fordulnak elő, jelenleg mindegyik külön karakternek van elismerve, de régebben az e változatai voltak és az annotációban voltak felsorolva hogy milyen kiegészítő jelekkel fordulhat elő ).

Mivel karakterkódolásról beszélünk, az olvasó joggal gyanakodhat arra hogy a legfontosabb dolog az a bizonyos szám/kód. Ez jelenleg egy 16 bites azonosító, azaz potenciálisan kettő a tizenhatodikon azaz 65536 karakter azonosítását teszi lehetővé. De a szemfüles olvasó bizonyára észrevette hogy csak arról volt eddig szó hogy egy karakterhez egy számot rendelünk (a karakterkét, annotáció stb. csak körítés). A lényeg éppen ez: válasszuk szét a karakter megvalósítását magától a karaktertől. Bármennyire is hihetetlen ez egy nagyon jó dolog. Miért? Egy dokumentumnak semmit nem kell tudnia a unicode szabványról, nem kell törődnie azzal hogy miképp fog ez megjelenni a képernyőn, sőt igazából azzal sem hogy az adott gép ismeri-e az adott karaktereket.

Vegyünk egy egyszerű példát és indítsuk el a Python interpretert. Az én nevemben van két olyan betű is ami nincs benne a megszokott ASCII kódkészletben, azaz problémás lehet olyan helyeken ahol nincs unicode támogatás. Tegyük el egy változóba a nevemet:

>>> a = "Varjú Zoltán"

Figyeljük meg hogy ha meg akarjuk jeleníteni a változó tartalmát, akkor a print a paranccsal visszakapjuk az eredeti stringet, de ha csak meg szeretnénk vizsgálni a változó tartalmát és simán beütjük hogy á, akkor azt kapjuk vissza ahogy a Python tárolja a karaktereket.

>>> print a

.....    Varjú Zoltán

>>> a

....     'Varj\xc3\xba Zolt\xc3\xa1n'

Mennyivel egyszerűbb ez így! A print parancs lehet hogy balul sül el, de a változó tartalma nem okozhat gondot akkor se ha gépünk nem képes megjeleníteni a "különös" betűket. Ez lehetővé teszi pl hogy japán szövegeket tömör formában tároljunk, akár úgy is dolgozhatunk egzotikus nyelvekkel hogy gépünk tkp. nem képes megjeleníteni a kódok mögötti karaktereket!

Ha szöveges fájlokkal dolgozunk érdemes a unicode szabványt használnunk - kivételt csak azok a nagyon, de nagyon egzotikus nyelvek képezhetik melyeknek vagy még nincs bevett írásuk, vagy még nem kerültek be karaktereik a szabványba. Ennek valószínűsége azonban csekély. Azonban sok jó minőségű korpusz még a szabvány bevezetése előtt készült és sajnos nem tértek át a szabványra. Itt nagyon vigyáznunk kell arra hogy miképp használjuk a karakterkódolást, szerencsére azonban viszonylag könnyű egyértelmű megfeleltetést találni a régi jelölés a megfelelő unicode karakterek között.

Ha "csak" feldolgozunk egy szöveget, akkor érdemes kideríteni a kódolását és a feldolgozó eszközök nyújtotta lehetőségeket. A legtöbb modern programozási nyelv valamilyen formában támogatja a unicode szabványt, ezzel nem lehet gond. Komolyabb munkához azonban érdemes elmélyedni az irodalomban, amihez egy kis segítséget nyújtunk az alábbiakban.

**Magyar irodalom**

- *[Prószéky Gábor - Kis Balázs: Számítógéppel emberi nyelven](http://www.szak.hu/konyvek_htm/szamitogeppel_emberi_nyelven.html)*, SZAK Kiadó, 1999

Habár néhol már eljárt a könyv felett az idő, a külföldi irodalommal összevetve is megállja a helyét a könyv. Az első fejezet foglalkozik a karakterkódolás témakörével, de nem árt az egész kötetet elolvasni egy esős hétvégén és mindent megtudhatunk az intelligens szövegkezelésről.

- *[Virágvölgyi Péter: A tipográfia mestersége számítógéppel](http://www.libri.hu/konyv/a-tipografia-mestersege-szamitogeppel.html),* Osiris Kiadó, 2004

Ahogy a címe is mutatja, ez a könyv a tipográfiával foglalkozik, de az első harmada nagyon hasznos mindenkinek aki szöveggel foglalkozik, a többi pedig szimplán érdekes.

**Angol irodalom**

- *[Jukka K. Korpela: Unicode Explained](http://www.amazon.com/Unicode-Explained-Jukka-K-Korpela/dp/059610121X/ref=pd_bxgy_b_text_b)*, O'Reilly, 2006

Kicsit talán túl terjedelems, de nagyon alapos útmutató a Unicode-hoz. Nem igényel különösebb technikai előismeretek.

- *[Yannis Haralambous: Fonst and Encodings](http://www.amazon.com/Fonts-Encodings-Yannis-Haralambous/dp/0596102429/ref=pd_bxgy_b_text_c)*, O'Reilly, 2007

A kötet alcíme nagyon sokat elárul: From Unicode to Advanced Typography and Everything in Between - azaz a unicode-tól a haladó tipográfiáig és minden a kettő között. Több mint ezer oldalon részletesen olvashatunk mindenről a témakörben és nekem spéci nagyon bejött.

- *[Ken Lunde: CJKV Information Processing: Chinese, Japanese, Korean and Vietnamese Computing](http://www.amazon.com/gp/product/0596514476/ref=pd_lpo_k2_dp_sr_1?pf_rd_p=1278548962&pf_rd_s=lpo-top-stripe-1&pf_rd_t=201&pf_rd_i=1565922247&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0VZ3CB3AVQD5YF1NTR3T),* O'Reilly, 2009

Akit érdekelnek a nem-latin karakterek, vagy dolgozniuk kell ilyen egzotikus cuccokkal, azoknak kötelező ez a kötet - azonban vigyázat, nagyon technikai nyelvezetet ölt a bevezető részek után!

- *[Steven Roger Fischer: History of Writing](http://www.amazon.com/History-Writing-Reaktion-Books-Globalities/dp/1861891016)*, Reaktion Books, 2004

Hamár karakterkódolás, akkor érdemes egy kicsit az írásról is olvasgatni - ez a rövid könyv követhető, élvezetes és rövid (350 oldal).

- *[Peter T. Daniels - William Bright: The World's Writing Systems](http://www.amazon.com/Worlds-Writing-Systems-Peter-Daniels/dp/0195079930/ref=sr_1_1?s=books&ie=UTF8&qid=1311759359&sr=1-1)*, Oxford University Press, 1996

Akit komolyabban érdekel az írás, annak ez a könyv az igazi. Vigyázat, ez már nem ismeretterjesztő munka, hanem egy tanulmánygyűjtemény.
