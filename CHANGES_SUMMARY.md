# Változások összefoglalója

Az oldal elkészült és él: <https://karogasok.github.io/>

Két commit a `main` ágon. A GitHub Pages ebben a repóban `main`-ről épül
(Actions-alapú deploy, a repo létrehozásakor így volt beállítva), ezért nem
feature branch + PR a munkamenet.

---

## Mi készült el

| Lépés | Állapot |
|---|---|
| 1. Hugo váz, konfiguráció, deploy | kész, élesben zöld |
| 2. Layoutok, CSS, betűk | kész |
| 3. Címke-hubok kétmódú sablonja | kész, mindkét irány tesztelve |
| 4. Blogspot import | kész, 306 bejegyzés |
| 5. WordPress import | kész, 58 bejegyzés |
| 6. Feedek, schema.org | kész, buildben ellenőrizve |
| 7. `mashol`, Makefile, README | kész (a `mashol` adat üres, lásd lent) |

**580 oldal**, ebből 364 archív bejegyzés (2010–2013 és 2020–2024),
1 megjelent és 1 ütemezett napi bejegyzés, 5 pillér-címke, 85 régi címke-oldal.

---

## Amiben a specifikáció téves volt

Három ponton nem az volt a helyzet, amit a leírás feltételezett. Mindhármat a
tényleges exportokból mértük.

1. **Az archívum nem 2009–2016.** Blogspot: 2010–2013. WordPress: 2020–2024.
   Van egy valódi, hatéves szünet 2014 és 2019 között. Az archívum bevezetője és
   az évsáv ezt mondja, nem simítja el.
2. **A Blogspot-export a 2018-as Blogger séma**, nem a 2005-ös Atom. Ez jobb: a
   `blogger:filename` megadja a pontos eredeti útvonalat, így a `canonical` nem
   rekonstrukció.
3. **A Blogspot csoportblog volt**, hat szerzővel. Döntés alapján csak Varjú
   Zoltán 306 bejegyzése került át.

---

## Döntések, amelyek a tartalmat érintik

Ezek megváltoztatják, mi kerül ki az oldalra. Egyik sem lett csendben
alapértelmezve.

- **Nyelvfelismerés a WordPress-oldalon.** Nem stopszó-arány dönt, hanem a
  permalink `/hu/` előtagja — ez a blog saját nyelvi besorolása. A stopszavas
  osztályozó ellenőrzésként fut mellette; mind a 178 bejegyzésen egyetértenek.
  Eredmény: 58 magyar bejegyzés.
- **Szerzők megfeleltetése.** `crowintelligenceteam` → Varjú Zoltán,
  `putzorsi` → Putz Orsolya. Ez **feltevés**, nem tény az exportból: a
  `crowintelligenceteam` a cég saját blogján a cég fiókja. A manifeszt
  (`scripts/out/wordpress-manifest.csv`) minden sorban mutatja mindkettőt.
  Ha nem így akarod, a `decision` oszlop átírásával újrafuttatható.
- **Régi címkék küszöbe: 3 bejegyzés.** 452 különböző Blogspot-címkéből 85 kap
  böngészhető oldalt. A többi címke is bekerül a front matterbe
  (`regi_cimkek_mind`), csak nem generál egy-elemű oldalt.
- **A halott Zemanta-képek törlődnek**, nem maradnak törött hivatkozásként.
  Minden törlés naplózva a TODO-fájlban.

---

## Emberi döntést igényel

1. **`data/mashol.yaml` üres.** A séma dokumentált, a sablon kész, az oldal
   őszinte üres állapotot mutat. A megjelenéseket nem lehetett megbízhatóan
   összeszedni (a nyest.hu és a Qubit sem ad szerzői listát), kitalálni pedig
   nem szabad őket. **Csak olyan sor kerüljön bele, aminek az URL-jét valaki
   megnyitotta.**
2. **A pillér-címkék bevezetői.** Öt `_index.md` létezik, üres törzzsel, ezért
   listaként jelennek meg. Az első bekezdéstől kezdve automatikusan átváltanak
   hub-módra. Célhossz 1500–2500 szó.
3. **`sameAs` a schema.org Person csomópontokban.** Jelenleg csak
   `crowintelligence.org`. Ha van LinkedIn / ORCID / Scholar profil, a
   `hugo.toml` `[[params.authors]]` blokkjába kerül.
4. **A 11 MB-os animált GIF** a *Magyarország demográfiai változásai*
   bejegyzésben. A bejegyzés tartalma, ezért maradt. Nem tömörítettük újra —
   az újrakódolás is szerkesztés.

---

## Amit szándékosan nem nyúltunk hozzá

- **Az archívum szövegéhez.** Se javítás, se rövidítés, se válogatás. A hibás
  hivatkozások, az elavult állítások és az elgépelések bennmaradtak.
- **A magányos `*` karakterhez** az archív szövegben. Ez nyelvészeti jelölés
  (`*Ez mondat lenni helytelen`), nem elrontott Markdown.
- **Az eredeti blogokhoz.** Mindkettő él, minden importált bejegyzés `canonical`
  hivatkozással az eredetire mutat.
- **A képek méretéhez.** Helyette `loading="lazy"` minden képen.

---

## Ismert korlátok, mérve

- **~130 kép véglegesen elveszett** (Google kiürítette a Blogger-albumokat).
  Helyükön látható jelzés az eredeti URL-lel. Lista:
  `scripts/out/blogspot-TODO.txt`.
- **4 darab látható `**` maradt** 443 archív oldalból 2-n. Olyan egymásba
  ágyazott félkövér, amit a Markdown nem tud kifejezni. Az importerek minden
  futáskor ellenőrzik a saját kimenetüket, így ez a szám mérve van.
- **A cron UTC szerint jár**, ezért az óraátállításkor egy órát csúszik a
  megjelenés. Elfogadva, nem kerülgetve.

---

## Utólagos javítás: a Jetpack adománygyűjtő blokkja

Az 58 importált WordPress-bejegyzésből **31 a szerző utolsó bekezdése után**
hordozta a Jetpack adománygyűjtő widgetjét („Make a one-time donation / Your
contribution is appreciated. / Donate", három változatban). Ez kikerült.

Ez nem szerkesztés: a platform tette a szöveg alá. Ugyanaz a kategória, mint a
megszűnt Zemanta widget képei, amiket az importer eddig is eldobott. Az illesztés
a WordPress saját blokk-határolóira megy (`wp:jetpack/donations`), nem az angol
szövegre, és nem fut le, ha a nyitó és záró jelölés nem stimmel.

**A widget egy súlyosabb hibát is felszínre hozott.** Minden „Donate" gomb a
bejegyzés saját permalinkjére mutatott, a médialetöltő pedig minden
saját-tárhelyes URL-t letöltött, függetlenül attól, mi jött vissza, és `.jpg`
néven mentette. A képkönyvtárban **42 fájl volt, ami nem kép**: 39 HTML oldal és
3 PDF, ~6 MB. Ebből **11 élő törött hivatkozás** volt — nyolc blogoldal és három
tanulmány, köztük Norvig *Unreasonable Effectiveness of Data* cikke.

Javítva: a letöltés csak akkor marad meg, ha a `Content-Type` `image/*`, és a
kiterjesztés is ebből jön, nem az URL-ből; minden más az eredeti URL-jén marad.
A `SELF_HOSTED` lista már nem illeszkedik a csupasz `googleusercontent.com` és
`files.wordpress.com` hostokra, mert azok nem képtárhelyek, hanem mindenki
fájljait kiszolgáló CDN-ek.

Új: `scripts/prune_media.py` (`make prune-media`) — az import eddig csak
hozzáadott; ez törli azt, amire már egyetlen bejegyzés sem hivatkozik.

Mérve: 364 bejegyzés változatlan (306 + 58). A törzsszöveg 1066 szóval lett
kevesebb, ami pontosan a 31 widget. Képkönyvtár 138 fájl / 38 MB → **96 / 32 MB,
mind kép**. Mindhárom PDF-hivatkozás az eredeti URL-jén, mindhárom él.

---

## Ellenőrzések, amiket a build futtat

`scripts/check_build.sh` — a deploy elbukik, ha bármelyik sérül:

1. **A napi feed nem tartalmazhat archív bejegyzést.** 364 archív fájl egyszerre
   landolna minden feliratkozónál, és csendben tenné.
2. **Jövőbeli `publishDate` nem kerülhet ki.** Ez maga az ütemezés; ha elromlik,
   az összes betárazott bejegyzés egyszerre jelenik meg, más tünet nélkül.
