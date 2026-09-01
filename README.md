# Varjú Károgások

Magyar nyelvű olvasónapló a mesterséges intelligenciáról, a megismerésről és a
következményeikről. Naponta egy forrás, három bekezdés. Mellette egy évtizednyi
régebbi írás két korábbi felületről.

Élesben: <https://karogasok.github.io/>

Ez az oldal nem ügyfélszerzésre való. A kereskedelmi profil a
[crowintelligence.org](https://crowintelligence.org/) oldalon van.

---

## Bejegyzést írni

```sh
make new t="Az LLM-ek nem tudnak zárójelet számolni"
```

Létrehozza a `content/posts/ÉÉÉÉ-HH-NN-slug.md` fájlt a mai dátummal, kitöltött
címmel. Utána már csak a `forras`, a `forras_cim` és a `tags` kell.

A cím **állítás legyen, ne téma.** „Az LLM-ek nem tudnak zárójelet számolni",
nem „Az LLM-ek és a zárójelek".

A törzs bevett tagolása — ez konvenció, a kód nem kényszeríti ki:

1. **Mi ez.** Miről szól a forrás.
2. **Mit gondolok róla.** Az álláspont.
3. **Mihez kapcsolódik.** Hová illeszkedik.

Nagyjából 150–300 szó.

Az `inbox.md` a nyersanyag: napközben oda kerül egy link meg két mondat. Nincs
köré épített eszköz, és ne is legyen.

## Ütemezés

A `publishDate` lehet jövőbeli. A Hugo alapból kihagyja a jövőbeli dátumú
bejegyzéseket, és **a `buildFuture` szándékosan nincs bekapcsolva** — ez az egész
mechanizmus alapja. Egy bejegyzés akkor jelenik meg, amikor a dátuma után
legközelebb lefut egy build.

Ezt a `.github/workflows/deploy.yml` cronja intézi:

```yaml
schedule:
  - cron: '0 5 * * 1-4'   # hétfő–csütörtök
```

**A cron UTC szerint jár.** 05:00 UTC nyári időszámításkor 07:00 Budapesten,
télen 06:00. Az óraváltáskor tehát egy órát csúszik a megjelenés. Ezt így
hagytuk: a másik lehetőség két cron és egy szabály arról, melyik él, egy
blogbejegyzés egyórás mozgatásáért.

Kézzel bármikor indítható: Actions → Deploy Hugo site to GitHub Pages → Run
workflow.

## Pillér-címke felvétele

1. `content/tags/<slug>/_index.md`, benne `title` és `osszefoglalo`.
2. A törzs egyelőre maradhat üres.

Amíg a törzs üres, a címke **sima listaként** jelenik meg. Amint próza kerül
bele, a sablon átvált a **hub-változatra**: a bevezető felül, a bejegyzések
alatta. Nincs kapcsoló a front matterben — a szöveg jelenléte maga a kapcsoló.
A kezdőlapon a pillérek attól látszanak, hogy van `_index.md`-jük, nem attól,
hogy megírtad a bevezetőt.

Célhossz egy érett bevezetőnek 1500–2500 szó.

## Az archívum újraimportálása

A nyers exportok a `scripts/raw/` alatt vannak (gitignore-olva, mert nagyok).
Az importereknek nincs függőségük: sima `python3` elég hozzájuk.

```sh
make import-blogspot     # 306 bejegyzés, 2010–2013
make import-wordpress    # osztályozás + manifeszt, NEM ír fájlt
make import-kereses      # Kereső Világ: csak lead + hivatkozás
```

**A WordPress-import szándékosan nem ír semmit az első futásra.** Osztályoz,
kiírja a manifesztet, és megáll. Átnézed, majd:

```sh
python3 scripts/import_wordpress.py --review scripts/out/wordpress-manifest.csv --write
```

Amit tudni érdemes róluk:

- A Blogspot-export a **2018-as** Blogger séma (`blogger:type`,
  `blogger:filename`), nem a régi 2005-ös Atom. A `blogger:filename` adja a
  pontos eredeti útvonalat, így a `canonical` nem tippelés.
- A Blogspot csoportblog volt, hat szerzővel. Csak Varjú Zoltán 306 bejegyzése
  kerül át; a többi szerzőé nem a mi közlésünk.
- A WordPress-blog kétnyelvű. A magyar bejegyzések permalinkjében ott a `/hu/`
  előtag — ez a blog saját nyelvi besorolása, és ez dönt. A stopszó-alapú
  osztályozó mellette fut ellenőrzésként; ha a kettő nem ért egyet, a manifeszt
  külön jelzi. Jelenleg mind a 178 bejegyzésen egyetértenek.
- **A Jetpack adománygyűjtő blokkja kikerül** a WordPress-bejegyzésekből (31-et
  érintett). Ez nem szerkesztés: a platform tette a szöveg alá, nem a szerző írta
  — ugyanaz a kategória, mint a megszűnt Zemanta widget képei. Az importer a
  WordPress saját blokk-határolóira (`wp:jetpack/donations`) illeszt, nem az
  angol szövegre, és nem nyúl hozzá, ha a nyitó és záró jelölés nem stimmel.
- **Csak kép kerül a `static/archivum/img/` alá.** Az importer a szerver
  `Content-Type` válasza alapján dönt, nem az URL végződéséből: korábban HTML
  oldalakat és PDF-eket is letöltött `.jpg` néven, amitől azok a hivatkozások
  eltörtek. Ami nem kép, az marad az eredeti URL-jén.
- **Az archívumot nem szerkesztjük.** Se javítás, se rövidítés, se válogatás.

### Kereső Világ — ami nem a miénk

A `make import-kereses` **nem importál**. A szerző 2011 és 2018 között a
[Kereső Világ](https://kereses.blog.hu/) blogra írt, a Precognox
alkalmazottjaként; **azok a szövegek a céghez tartoznak.** A script ezért csak
egy listát állít elő `data/kereses.yaml` néven: cím, dátum, a blog saját ajánlója
(lead) és a hivatkozás. Teljes szöveg nem kerül át, és **saját oldalt sem
kapnak** — az archívum listájában és az évsávban jelennek meg, a címük pedig
egyenesen a blogra mutat.

Miért nincs saját oldaluk: több száz vékony oldal jönne létre valaki más
ajánlójával, mindegyik a saját eredetijével versenyezve a találati listán, és
mindegyiknek magától elfelé mutató canonical kellene. Egy listasor semmit nem
tárol, és minden olvasót az eredetihez küld.

A szűrés a szerző blog.hu **user ID-je** (555969) alapján történik, nem név vagy
évszám alapján: a blog csoportblog volt, a szerzőség a tényleges szempont, egy
azonosítót pedig nem lehet elgépelni. A leadeket 300 karakternél elvágjuk — egy
nagyon rövid bejegyzésnél az `og:description` maga a teljes szöveg lenne.

A letöltött oldalak a `scripts/raw/kereses/` alatt cache-elődnek, így az
újrafuttatás nem terheli a blogot.

**A teljesség ellenőrizve, és az ellenőrzés be van építve.** A sitemap egy
udvariassági fájl: ha valaha megcsonkulna, az import csendben kevesebb
bejegyzést hozna, és semmi nem látszana rosszul. Ezért a script lekéri a blog
`/archive` oldalát is, ami hetenként egy hivatkozást sorol fel — ez a blog saját
állítása arról, mi létezik —, és megnézi, hogy minden meghirdetett héthez
tartozik-e begyűjtött bejegyzés. Jelenleg **479 hét, mind lefedve**.

Az összevetés dátum alapján megy, nem hétsorszám alapján: a blog.hu másképp
számozza a heteket, mint az ISO 8601 (van `w0`-ja, és egy december 31-i
bejegyzés a következő év első ISO hetébe esik). Egy hiányzó hét figyelmeztetést
ad a hét kattintható URL-jével, de nem állítja meg a futást — több hét egyszerre
viszont valódi csonkulást jelez.

### Ami elveszett

A Blogger képalbumait a Google kiürítette: a Takeout egyetlen képfájlt sem
tartalmaz, az album `totalItems: 0`, és az élő blog is 404-et ad ugyanazokra az
URL-ekre. Körülbelül 130 kép 2010–2013-ból már sehol nem létezik.

Ezek helyén nem törött kép jelenik meg, hanem egy látható jelzés azzal az
URL-lel, ahol a kép volt. A teljes lista a `scripts/out/blogspot-TODO.txt`
fájlban. A Zemanta widget képei (a szolgáltatás megszűnt) törlődnek, szintén
naplózva.

A YouTube-, Vimeo-, Gist- és SlideShare-beágyazásokból sima hivatkozás lesz: az
oldalon nincs JavaScript és nincs iframe.

### A konverzió határa

A HTML→Markdown átalakítás nem tökéletes, és nem is lehet az: a Blogger
szerkesztője olyan jelöléseket is előállított, amiket a Markdown nem tud
kifejezni — egymásba ágyazott félkövér, vagy záró `**` közvetlenül írásjel és
betű között. A 443 archív oldalból **2 oldalon marad összesen 4 darab** látható
`**` a szövegben.

Ez a szám mérve van, nem becsülve: a `scripts/` alatti importerek minden
átalakítás után ellenőrzik a saját kimenetüket (lezáratlan kódblokk, páratlan
félkövér-jelölés), és a talált eseteket a TODO-fájlba írják.

Egyetlen dolgot **nem** javítunk: a magányos `*` karaktert. Ez nyelvészeti
jelölés — `*Ez mondat lenni helytelen` —, és az átírása elrontaná azt, amit a
bejegyzés állít.

### Méret

A `static/archivum/img/` mintegy 35 MB, 136 fájl. A képeket **nem tömörítjük
újra**: az újrakódolás is szerkesztés, az archívumot pedig nem szerkesztjük. Egy
kilóg a sorból, a *Magyarország demográfiai változásai* bejegyzés 11 MB-os
animált GIF-je — ez a bejegyzés tartalma, nem díszítés, ezért marad.

Ehelyett minden kép `loading="lazy"` attribútummal jelenik meg
(`layouts/_default/_markup/render-image.html`), így akkor töltődik, amikor az
olvasó odaér. A bájtok ugyanazok, csak nem egyszerre érkeznek.

## Feedek

Két feed van, és ez nem véletlen:

- `/index.xml` — **csak a napi bejegyzések.**
- `/archivum/` — nincs feedje.

A Hugo alap kezdőlap-feedje minden oldalt beletenne, vagyis a 364 archív
bejegyzés egyszerre landolna minden feliratkozónál. Ezt a
`layouts/index.rss.xml` szűrése akadályozza meg, és a `scripts/check_build.sh`
ellenőrzi minden buildnél — ha valaki elrontja, a build bukik, nem a feed.

```sh
make check    # build + feed-ellenőrzés
```

## Fejlesztés

```sh
./scripts/install_hugo.sh   # ugyanaz a Hugo, mint a CI-ban
make serve                  # helyi szerver, piszkozatokkal
make build                  # éles build a public/ könyvtárba
```

A Hugo verziója egyetlen helyen van rögzítve: `HUGO_VERSION` a
`.github/workflows/deploy.yml` fájlban. Az `install_hugo.sh` onnan olvassa ki,
így a helyi build nem csúszhat el a CI-tól. Extended Hugo nem kell — sima CSS
van, nincs SCSS.

### Betűk

Két önhosztolt betűkészlet: **Archivo** (címsorok, margó) és **Spectral**
(kenyérszöveg). Nincs betűkészlet-CDN.

```sh
make fonts    # scripts/fetch_fonts.py
```

Mindkettőt ellenőriztük, hogy **valódi kettős éles ékezetet** rajzol (`ő ű Ő Ű`),
nem pedig átcímkézett trémát. Ez nem magától értetődő: több népszerű
betűkészlet elhasal ezen. Betűcsere előtt ezt kell először megnézni.

A `-ext` fájlok viszik a Latin Extended blokkot, amiben az `ő` és az `ű` van —
egy magyar oldalon ezek nem opcionálisak, ezért ezek is előre töltődnek.

## Amit szándékosan nem építettünk

Komment, kereső, hírlevél, analitika, sötét mód, címkefelhő, kapcsolódó
bejegyzések, megosztógombok, admin felület. Nincs JavaScript. Ha valamelyikre
tényleg szükség lesz, akkor lehet hozzátenni — a legtöbbre nem lesz.

## Licenc

Szöveg: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.hu).
Betűkészletek: SIL Open Font License 1.1 (a licencszövegek a `static/fonts/`
mellett).

Kapcsolat: <hello@crowintelligence.org>
