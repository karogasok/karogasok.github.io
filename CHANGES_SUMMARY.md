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

1. **A pillér-címkék bevezetői.** Öt `_index.md` létezik, üres törzzsel, ezért
   listaként jelennek meg. Az első bekezdéstől kezdve automatikusan átváltanak
   hub-módra. Célhossz 1500–2500 szó.
2. **A 11 MB-os animált GIF** a *Magyarország demográfiai változásai*
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

## A bemutatkozás a cím alá került

A kezdőlap egy általános mondattal indult, a „Ki írja" szakasz pedig hét
képernyővel lejjebb magyarázta el, kié az oldal. Ez fordítva volt jó: egy
személyes oldalon az első, amit egy hidegen érkező olvasó — szerkesztő,
konferenciaszervező — keres, az az, hogy kicsoda ez.

A bemutatkozás most közvetlenül a cím alatt van, a „Ki írja" szakasz és a
`content/rolam.md` pedig törölve (semmi más nem hivatkozott rá).

A mondat **egyetlen helyen** él: a `partials/site-description.html` rakja össze
a szerző nevéből és a `home.bio` szövegből, és ezt használja a látható lede, a
meta description, az OpenGraph kártya, az RSS csatorna és a schema.org `Blog`
csomópont is. A `params.description` törölve, hogy ne legyen belőle második
példány, ami elcsúszhat.

Két apróság: a `nyelvész - filozófus` **nagykötőjelre** javítva
(`nyelvész – filozófus`), és a LinkedIn-profil bekerült a schema.org `Person`
csomópont `sameAs` mezőjébe is — ez volt a fenti nyitott kérdések egyike. A
`jobTitle` is frissült, hogy ne mondjon mást, mint a látható bemutatkozás.

---

## A fejléc és a „Máshol" lista

A fejléc eredetileg a Crow Intelligence öt menüpontját vitte tovább (Portfolio /
Services / About / Blog / Contact). Ez félrevezető volt: ettől úgy nézett ki,
mintha a cégoldal egyik aloldala lenne, holott ez egy személyes olvasónapló.
A navigáció most a saját három pontja: **Archívum, Máshol, Kapcsolat**.

A Kapcsolat `mailto:zoltan.varju@crowintelligence.org`, és ez az e-mail váltja a
láblécben a Crow közös `hello@` címét is — egy cím van az oldalon, és az a
szerzőé. (A kérésben `.com` szerepelt; a valódi domain a `.org`, a `.com` egy
üres, parkoltatott domain.)

A Crow két helyen marad: a cím alatti „Powered by Crow Intelligence" soron és a
lábléc első hivatkozásán. Ennyi elég egy oldalon, ami szándékosan nem
ügyfélszerző csatorna.

Az angol nyelvű Crow-blog hivatkozása **törölve** a láblécből. Ezt a
specifikáció §9 még kérte; a szerző utólag máshogy döntött, és az ő oldala.
A lábléc most: Crow Intelligence · e-mail · CC BY-NC-SA 4.0 · RSS.

A `data/mashol.yaml` már nem üres: **14 tétel**, ebből 13 nyest.hu-cikk
2011 és 2019 között, plusz egy 2012-es Clojure-tanulmány. Minden URL ellenőrizve;
mind él, kivéve a ResearchGate-et, ami böngészőn kívül mindenre 403-at ad.

---

## Kereső Világ (kereses.blog.hu) — 401 bejegyzés, hivatkozásként

A szerző 2011 és 2018 között a Kereső Világ blogra írt, a Precognox
alkalmazottjaként. **Az a tartalom nem az övé**, ezért ebből semmi nem került át:
`data/kereses.yaml` csak címet, dátumot, a blog saját ajánlóját (lead, 300
karakterben maximálva) és a hivatkozást tárol. **401 bejegyzés**, 2011–2018.

Ezek **nem kapnak saját oldalt.** Az archívum listájában és az évsávban
jelennek meg, a címük egyenesen a blogra mutat. Több száz vékony oldal jönne
létre valaki más ajánlójával, mindegyik a saját eredetijével versenyezve a
találati listán, és mindegyiknek magától elfelé mutató canonical kellene. Egy
listasor semmit nem tárol, és minden olvasót az eredetihez küld.

A szűrés a szerző blog.hu **user ID-je** (555969) alapján megy, nem név vagy
dátum alapján — a blog csoportblog volt (8 szerző), és egy azonosítót nem lehet
elgépelni. Ellenőrizve: nincs másik Varjú-fiók.

**A sitemap teljessége ellenőrizve, és az ellenőrzés beépítve** az importerbe:
a `/archive` 479 hetet hirdet meg, és mind a 479-hez tartozik begyűjtött
bejegyzés. Kézzel is ellenőrizve 32 hét / 62 bejegyzés — egy sem hiányzott.

Ezzel a 2014–2018 közötti rés eltűnt az évsávról. 2019 továbbra is üres, mert
abban az évben tényleg nem született bejegyzés. Az archívum bevezetője kimondja,
hogy **ez nem a szerző írásainak teljes archívuma**: ami az övé, teljes egészében
megvan; ami nem az övé, arra csak mutatunk.

Két új build-ellenőrzés: nem kerülhet `kereses.blog.hu` URL a feedbe, és nem
épülhet oldal olyan tartalomhoz, ami nem a szerzőé.

---

## Az archívum oldal

A hosszú, ötbekezdéses bevezető helyett két mondat áll az oldal élén; a
tulajdonjogi részletek (Precognox, a 300 karakteres lead-korlát, miért nincs
saját oldaluk) a `README.md`-ben és itt maradnak — az egy build-döntés
magyarázata, nem az olvasóé.

**Minden sor alatt ott a forrás**, nem csak a Kereső Világ soroké:
`SZÁMÍTÓGÉPES NYELVÉSZET` (306), `CROW INTELLIGENCE` (58), `KERESŐ VILÁG` (401).
Az archívum három blogot kever, és korábban csak az egyik volt jelölve.

A felirat mindháromnál ugyanaz a halvány szürke: azt mondja meg, *honnan való*.
Hogy a kattintás elhagyja-e az oldalt, az másik kérdés — arra a `↗` és a lead
válaszol. Ha a külsők maroon színt kapnának, az 765-ből 401 soron jelenne meg,
és ott már nem kiemelés.

A feliratok a `forras_platform` mezőből jönnek az `i18n/hu.toml`-on keresztül,
nem a bejegyzésekben tárolt `forras_cim`-ből: így egy forrás átnevezése egy
soros javítás, nem 364 fájl újraimportálása.

`scripts/check_build.sh` — a deploy elbukik, ha bármelyik sérül:

1. **A napi feed nem tartalmazhat archív bejegyzést.** 364 archív fájl egyszerre
   landolna minden feliratkozónál, és csendben tenné.
2. **Jövőbeli `publishDate` nem kerülhet ki.** Ez maga az ütemezés; ha elromlik,
   az összes betárazott bejegyzés egyszerre jelenik meg, más tünet nélkül.

---

## Témamodell, kulcsszavak, `tema` taxonómia

Új, különálló Python-projekt az `analysis/` mappában (uv, saját `pyproject.toml`
és lockfile). A `scripts/` szándékosan stdlib-only marad, hogy az importálók
évek múlva is elinduljanak egy csupasz `python3`-mal; az ML-stack nem szivárog
bele.

**A folyamat:** emtsv (Docker) lemmatizálás → huBERT beágyazás (chunkolva,
átlagolva, L2-normalizálva) → BERTopic → keyflux kulcsszavak → `temak`
taxonómia és `data/temak.yaml`.

### A modell, mérve

818 dokumentum, ebből **318 teljes szövegű**, amire a modell illeszkedik; a
maradék 496 rövid tétel (Kereső Világ-felvezetők, média- és máshol-leírások)
utólag kerül rá a kész témákra, 0,25-ös valószínűségi küszöb felett. Fordítva
nem lett volna értelme: a korpusz darabszám szerinti többsége 37 szavas
felvezető, és ha azokra illesztünk, azok határozzák meg a témákat.

- **19 téma**, 21,1% kívülálló, a legnagyobb téma a korpusz 9,1%-a.
- Két futás azonos maggal **814/814 azonos** besorolást ad.
- Előre rögzített küszöb: ha a kívülállók 40% fölé mennek, vagy egy téma a
  korpusz harmadánál többet visz, azt rossz modellként jelentem, nem szállítom.
  Mindkettő teljesült.

### Döntések, amelyek a számokat érintik

| paraméter | érték | miért |
|---|---|---|
| `min_cluster_size` | 7 | 318 dokumentum; a BERTopic 10-es alapértéke ennyiből túl keveset hagy |
| `cluster_selection_method` | `leaf` | a huBERT-vektorok szűk kúpban ülnek, az `eom` egyetlen témába dönt mindent |
| `min_df` | 2 | egyszer előforduló lemma ne legyen témakifejezés |
| valószínűségi küszöb | 0,25 | ez alatt a rövid tétel kívülálló marad, nem erőltetjük témába |
| `MIN_FIT_WORDS` | 80 | ez alatt nincs témajelzés a szövegben |
| keyflux `min_focus_freq` | 2 | a könyvtár 5-ös alapértéke korpusz-korpusz összevetésre való, nem egyetlen posztra |
| kulcsszavak / írás | 8 | ebből 6 kerül a front matterbe |

### Emberi döntést igényel

**A 19 témanév gépi javaslat.** Mind a 19 `checked_by_human: false`
állapotban van az `analysis/out/topic_names.json`-ban, és mindegyik mellett ott
a téma kifejezéslistája, öt jellemző írás címe, és egy **szó szerinti idézet**,
amit a szkript visszaellenőrzött a forrásban — így a név ellenőrzése
sztringkeresés, nem újraolvasás. Mind a 19 idézet visszakereshető.

A témaoldalak ezért egyelőre kiírják, hogy a név gépi javaslat. Az
`export_temak.py` alapból meg is tagadja a publikálást, amíg a név nincs
átnézve; a mostani futás a `--allow-unchecked` kapcsolóval készült, hogy legyen
mit átnézni.

**A 3-as téma („A blog életéből") a leggyengébb.** A 17 írás közös vonása a
hangnem, nem a tárgy: évfordulók, tervek, köszönetek. Vagy kap egy őszintébb
nevet, vagy érdemes kívülállóként hagyni.

**Angol kulcsszavak magyar posztokon.** Az emtsv az angol szövegre is magyarként
néz, így egy angolul idéző poszton az angol tartalmas szavak (`dance`,
`behavior`) kulcsszóként jönnek ki. Az angol funkciószavakat kiszűrjük, a
tartalmasakat nem — azok tényleg megkülönböztetik az adott írást.

### Két hiba, amit a modell hozott felszínre

1. **Egy poszt címkéi elvesztek.** A „Chomsky és a statisztika" öt címkéje egyetlen
   sztringgé olvadt, U+FFFD karakterekkel elválasztva — a rontás a Blogger
   exportjában van, nem az importálóban. Mivel így minden címke egyszer
   fordult elő, egyik sem érte el a hubküszöböt: a poszt öt címkeoldalról
   hiányzott. Az importáló mostantól szétvágja ezeket, a poszt pedig
   visszakerült a Chomsky, statisztika és számítógépes nyelvészet oldalakra.
2. **Egy régi bekezdésben megmaradt szemét.** Egy 2011-es poszt linkszövegében
   `bitxəšï-史` áll, még az eredeti blogból. Az emtsv a CJK-karakterre U+FFFD-t
   ad vissza, ezért lett belőle témakifejezés. Nem javítottam a szöveget, csak
   a nem-szó lemmákat szűröm ki.

### Amit szándékosan nem nyúltunk hozzá

- **Az öt pillércímke (`tags`) érintetlen.** A `tema` külön taxonómia; egy
  klaszterezés eredménye nem keveredhet észrevétlenül a kézzel gondozott
  szerkesztői állításokkal. A címlap továbbra is csak a pillérekre hivatkozik.
- **A `temak` taxonómiának nincs feedje.** A `taxonomy`/`term` kimenet
  továbbra is csak HTML, tehát a 19 új oldal nem hozott vissza 19 hirdetetlen
  feedet. A build most is pontosan két feedet ad.
- **A Kereső Világ-tételek nem kaptak oldalt.** A témájuk a
  `data/temak.yaml`-ban van, a hub onnan listázza őket, hivatkozásként.

## A Trianon- és metafora-bejegyzések szerzősége

A *Koronavírus és metaforák* sorozat és a *Trianon 100* interjúk **Putz Orsolya**
megjelenései, ezért nem szerepelnek a Média oldalon.

A hozzájuk tartozó **blogbejegyzések viszont Varjú Zoltáné**: ő írta őket, hogy
beharangozza az elkészült anyagokat. A Crow Intelligence a közös vállalkozásuk,
így a `crowintelligenceteam` fiók alatt megjelent bejegyzések helyesen szerepelnek
az ő neve alatt. **A bylinek maradnak, ahogy vannak** — ez a korábbi importnál
jelölt feltevés ezzel megerősítést nyert.

Ami a Média oldalra kerül, az ettől külön kérdés: ott a megjelenés szerzője
számít, nem a beharangozó bejegyzésé.
