---
title: "Ezek minden idők leggyakoribb és legfontosabb  szavai a magyar popslágerekben"
date: 2020-08-19T10:11:41Z
publishDate: 2020-08-19T10:11:41Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "wordpress"
forras_cim: "Crow Intelligence blog"
canonical: "https://blog.crowintelligence.org/hu/2020/08/19/hatvan-ev-dalszovegei/"
regi_cimkek:
  - "dalszövegek"
regi_cimkek_mind:
  - "Processing"
  - "adatvizualizáció"
  - "dalszövegek"
  - "natural language processing"
  - "pop"
---

Gondolta volna, hogy az 1980-as évek popslágereinek egyik kulcsszava a túró? És azt, hogy az inka szó az évezred forduló környékén meghatározó szerepet töltött be a magyar popdalokban? A magyar dalok több meglepetést tartogatnak, mint gondolná. Legújabb projektünkben a magyar dalszövegeket szedtük ízekre az 1950-es évektől egészen napjainkig.

Egy napsütéses nyári napon egy nyelvi kincsesbányára bukkantunk, amikor a magyar nyelvű popdalok dalszövegeit gyűjtöttük be zeneszoveg.hu-ról. Tettük ezt azért, hogy megvizsgálhassuk, milyen szavak hagyják el leggyakrabban az énekesek száját és melyek számítanak a legfontosabb kifejezéseknek. Ehhez kizárólag olyan szövegeket vettünk fel a korpuszunkba, melyek magyar nyelvűek és van adat a keletkezésük időpontjáról. Az egyes évtizedekben született slágerek (szövegek) számát az alábbi ábra szemlélteti.

![](/archivum/img/f653f860c538a985.png)

### Szerelmes, csókol, fáj és a többiek

Ha meg kellene tippelnünk, hogy miről szólnak leggayakrabban a popdalok, biztosan sokan a szerelemre szavaznánk. Az adatok tanúsága szerint nem is tévednénk nagyot. Ha évtizedenként végigvesszük a dalszövegek leggyakoribb szavait, azt tapasztaljuk, hogy a szerelemhez kötődők nem kopnak ki az évek során. A *megszeret, szerelmes, csókol, felejt*, *ölel* szavak arra engednek következtetni, hogy menthetetlen romantikusok vagyunk. Úgy tűnik továbbá, hogy a magyar popslágereket hallgatva és énekelve, valóságos érzelmi hullámvasútra ülünk fel. A negatív érzelmek (pl. *sír, fáj,*) és a pozitívak (pl. *boldog, örül*) egyaránt fontos építőelemei a daloknak.

Ha valaki dalszöveg írásra adná a fejét, érdemes átolvasnia a leggyakoribb szavakat tartalmazó listánkat, hogy tudja, mely szavakat kell elkerülnie, ha egyedi alkotást szeretne létrehozni. De természetesen puszta kíváncsiságból is érdemes végiglapozni az alábbi ábrákat, amelyek egy-egy évtized dalszövegeinek leggyakoribb szavait mutatják be.

![](/archivum/img/79217739468af84c.png)

Az 1950-es évek dalainak leggyakoribb szavai

![](/archivum/img/2d9e8a33898885b4.png)

Az 1960-as évek dalainak leggyakoribb szavai

![](/archivum/img/504a2264d6a1dfc0.png)

Az 1970-es évek dalainak leggyakoribb szavai

![](/archivum/img/81adec30f14abccf.png)

Az 1980-as évek dalainak leggyakoribb szavai

![](/archivum/img/41d5e9844eb8bee0.png)

Az 1990-es évek dalainak leggyakoribb szavai

![](/archivum/img/1a019803484ce84c.png)

A 2000-es évek dalainak leggyakoribb szavai

![](/archivum/img/8987c037b948d818.png)

A 2010-es évek dalainak leggyakoribb szavai

![](/archivum/img/a0a5a2657e970b87.png)

A 2020-as évek dalainak leggyakoribb szavai

### Az *érez* mint kulcs ige

Ha évtizedekre lebontva végigpörgetjük a dalok kulcsszavait, a legszembetűnőbb jelenség, amire felfigyelünk, hogy a leggyakoribb 10%-ban 1970-től 2020-ig minden egyes évtizedben szerepel az *érez* szó. Még mielőtt ebből azt a könnyelmű következtetést vonnánk le, hogy a popdalaink sablonosak és nem túl kreatívak, néhány gyöngyszemre szeretnénk felhívni az olvasók figyelmét. Az 1990-es és 2010-es években is kulcsszó rangot tudott kiérdemelni az *inka* szavunk, az 1980-as években bekerült a *túró,* az 1960-asban fontos szerepet kapott a *hajótörött.*

A további csemegék kimazsolázához alább mutatjuk a dalszövegek kulcsszavait évtizedenként.

![](/archivum/img/fa4d118e60297c59.png)

Az 1950-es évek dalainak kulcsszavai

![](/archivum/img/1f15a7bb3d7ed755.png)

Az 1960-as évek dalainak kulcsszavai

![](/archivum/img/1d1ae3e8279a8be6.png)

Az 1970-es évek dalainak kulcsszavai

![](/archivum/img/3644ea738b7b6679.png)

Az 1980-as évek dalainak kulcsszavai

![](/archivum/img/0a06c3939f6afb77.png)

Az 1990-es évek dalainak kulcsszavai

![](/archivum/img/0dd47c299d141b71.png)

A 2000-es évek dalainak kulcsszavai

![](/archivum/img/b83e365b6a8b8678.png)

A 2010-es évek dalainak kulcsszavai

![](/archivum/img/fb00e9282a3177f4.png)

A 2020-as évek dalainak kulcsszavai

### Adatok, kód, szövegfeldolgozás

- Az adatokat a zeneszoveg.hu oldalról scrapeltük.

- [A kapcsolódó repository-ban](https://github.com/crow-intelligence/music_networks) a feldolgozáshoz használt összes kód megtalálható.

A nyers szövegeket az [e-magyar text processing system (emtsv)](https://github.com/dlt-rilmta/emtsv) eszközzel dolgoztuk fel (szótövezés és szófaj alapú szűrés). A dalszövegekből minden évtizednek megfelelően alkorpuszokat készítettünk. Kulcsszókinyeréshez egy úgynevezett [text graph](https://en.wikipedia.org/wiki/Text_graph)-ot készítettünk az egyes alkorpuszokból és a [PageRank](https://en.wikipedia.org/wiki/PageRank) metrika szerinti legmagasabb értékű szavakat tekintjük kulcsszónak. A szófelhőket [Processing](https://processing.org/) használatával generáltuk a [WordCram](https://wordcram.wordpress.com/) könyvtár segítségével.

### Borítókép

A borítókép forrása a **Fortepan / Urbán Tamás**, amely [ezen a linken](https://beta.fortepan.hu/hu/photos/?id=125545) érhető el.
