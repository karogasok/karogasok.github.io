---
title: "Írástudók hajnala IV. - az adatújságírásról"
slug: "irastudok-hajnala-iv-de-mi-az-az"
date: 2011-04-11T17:15:00.001Z
publishDate: 2011-04-11T17:15:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/irastudok-hajnala-iv-de-mi-az-az.html"
regi_cimkek:
  - "adatok"
  - "adatok tudománya"
  - "adatújságírás"
regi_cimkek_mind:
  - "adat vezérelt újságírás"
  - "adatok"
  - "adatok tudománya"
  - "adatújságírás"
---

**Az újságírás is állandóan változik nem csak egy adott kor eseményei, divatjai csapódnak le (nagy érdekes ebből a szempontból a The Economist 1843-ig visszamenő archívuma), hanem alkalmazkodnia kellett a különböző médiumokhoz is (rádió, televízió). Meglepő viszont hogy a sajtó még nem alkalmazkodott teljesen az internet és az adatok kora nyújtotta lehetőségekhez ill. nem reagált még a kihívásokra. Az olvasó joggal kételkedhet, hiszen az internetes hírportálok már torony magasan verik a print médiát, a stílus kalauzokban már külön fejezet foglalkozik az internetes tartalmak készítésének szabályaival, akkor hogy lehet hogy állíthatja valaki hogy nem történt változás? Nos, ez csak részben igaz, már megjelentek az új irány keresői, az adatújságírás (angol terminusokkal data journalism, data-driven journalism, database journalism néven találkozhatunk vele). Írásunk a teljesség igénye nélkül szeretne pár kezdeményezést bemutatni melyek lazán kapcsolódnak, de az adatújságírás hivatkozási pontjai.**

**Az adatújságírás megszületése**

Az adatújságírás egyik forrásának Adrian Holovaty (programozó/újságíró, a népszerű Django webprogramozási keretrendszer egyik megalkotója) [A fundamental way newspaper site need to change](http://bit.ly/9ScOn8)  esszéjét szokás tekinteni. Holovaty szerint ideje szakítani a „sztori centrikus”, azaz egy-egy történetet középpontba állító közlési formával mivel ez nem teszi lehetővé hogy a különböző platformokhoz tudjuk adaptálni a híreket. Egy hír magját a felhasznált adatok és azok alapvető elemzése alkotja, ezt a központi elemet tudjuk hordozni a print, mobil és webes és egyéb felületek között. Holovaty erről nem csak szépen tud írni, hanem [Every Block](http://bit.ly/elgFXV) oldalával elképzelését bizonyította is ahol helyi híreket gyűjtenek csokorba az érdeklődők számára. Egy helyi hír általában nagyon helyhez kötött és a benne szereplő adatok is egy (viszonylag) szűk univerzumban értelmezhetőek, ez pedig egy számítógép számára nagyban megkönnyíti az automatikus feldolgozást. Azonban a lokális, adatcentrikus hírek csak egy kis szeletét teszik ki a hagyományos médiának is.

**Hogyan lehet egy szövegből adat?**

Sorozatunk második részében ([Az adatok kora](http://bit.ly/e2Qkxq)) már bemutattuk hogy miképp lehet egy adott szövegre technikai értelemben is adatként tekinteni. A strukturált szövegekből már egész jó hatékonysággal tudunk adatokat kinyerni (az egyszerű ún. névvel rendelkező entitásoktól, a minimális szemantikai tartalomig), ez segíti az értő olvasást és az egyes szövegek közötti kapcsolatok feltérképezését (pl. a [sorozat első részében](http://bit.ly/e3tbGy) bemutatott [Wordnik](http://bit.ly/fpxa6c) szótár is mindkét irányban fejleszt, l. továbbá [interjúnkat kutatási igazgatójukkal](http://bit.ly/hpSsEz)).

Hogy mire jó ez? Egy tényfeltáró vagy egy elemző íráshoz általában a szerző áttekinti lapja és a témáról írást közlő más sajtótermékek archívumait. Ezek között keresni néha nem könnyű, minden egyes cikk elolvasása pedig nyilván lehetetlen egyes esetekben. Azonban automatikusan is feldolgozhatjuk a korábbi írásokat és kereshetünk kapcsolatokat egyes adatok (számadatok, nevek, időpontok stb) között.

De nem csak az előzmények felkutatása során segíthetnek ezek módszerek. Johnatan Stray [A full-text visualization of the Iraq War Logs](http://bit.ly/gw6xAA) írása azt mutatja be hogy milyen szövegbányászati módszerekkel dolgozták fel a WikiLeaksen megjelent háborús aktákat.

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-FHvNf6mW61Q/TaM2O9sCLmI/AAAAAAAAAcM/ViTzohpQIcg/s320/abra01.png" rel="nofollow noopener">abra01.png</a></span>](http://3.bp.blogspot.com/-FHvNf6mW61Q/TaM2O9sCLmI/AAAAAAAAAcM/ViTzohpQIcg/s1600/abra01.png)

Szintén érdekes hogy a szerző szerint általános eljárás hogy egy-egy FOIA kérésre (ez tkp. a közérdekű adatok kikérése állami szervektől, általában így nevezik angol nyelvterületen az amerikai [Freedom of Information Act](http://bit.ly/eqP5X3) törvény mintájára, hazánkban is lehetőség van közérdekű adatok kikérésre) gyakran nem pontos adatokat, hanem egy ömlesztett adattengert kapnak a kérők.

Saját elemzésünkben ([Szöveges információk vizualizációja Gephi és az AlchemyAPI segítségével](http://bit.ly/cetrGf)) azt mutattuk be hogy az [AlchemyApi](http://bit.ly/efeLQ8) segítségével miképp nyerhetjük ki automatikusan a kapcsolatot Feyerabend, Lakatos és Popper életében. (Lakatos követte Poppert az LSE katedráján és próbálta megvédeni/kijavítani tudományfejlődési modelljét. Feyerabend Lakatos jó barátja volt, ellenben Popper elképzelését - és egyben Lakatosét is - sokat kritizálta. Az ábrán látható hogy Popper és Lakatos, ill. Lakatos és Feyerabend között több közös pont található, míg Popper és Feyerabend cak lazán kapcsolódik)

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-oXp5_JrNUoo/TOfHjB4LVZI/AAAAAAAAAWw/wr9myry5LDI/s320/tudfil.png" rel="nofollow noopener">tudfil.png</a></span>](http://3.bp.blogspot.com/-oXp5_JrNUoo/TOfHjB4LVZI/AAAAAAAAAWw/wr9myry5LDI/s1600/tudfil.png)

**Hogyan lehet adatokból szöveg?**

Nem csak a szövegekben rejlő adatok kinyerésével került a kezünkbe egy hatalmas adathalmaz. Itt nem csupán arról van szó hogy egyre több adatot generálunk mint az internet használói (erről már [Az adatok tudománya, filozófia és nyelvészet](http://bit.ly/a76k9z) írásunkban már írtunk), hanem az eddig bevett adatgyűjtési módszerek (statisztikai hivatalok pl) és megváltoztak. Egyrészt egyre több kormány nyit abban az irányban hogy nem csak részaadatokat, végelemzéseket, hanem minden adatot publikál és nem csupán letölthetővé teszi az adatokat, hanem olyan nyílt hozzáférést biztosít ami lehetővé teszi hogy más internetes alkalmazások használhassák azokat (úgynevezett API-okat, application programming interface, hoznak létre). Erre az egyik legjobb példa az Egyesült Államok [data.gov](http://1.usa.gov/eZYIfN) portálja.

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-Hw4W2Ag6T24/TaM2y_gqWWI/AAAAAAAAAcQ/DuaOR7PQL6c/s320/Data.gov_1302541998414.png" rel="nofollow noopener">Data.gov_1302541998414.png</a></span>](http://1.bp.blogspot.com/-Hw4W2Ag6T24/TaM2y_gqWWI/AAAAAAAAAcQ/DuaOR7PQL6c/s1600/Data.gov_1302541998414.png)

Az előző szakaszban már említettük hogy gyakran problémát jelent a túl sok adat is. A sztorinak csak az egyik fele hogy vannak publikus adatok, a másik hogy megértsük mi rejlik a számok mögött. Az [Open Knowledge Foundation](http://bit.ly/hOkVKO) [Where Does My Money Go](http://bit.ly/eo2rcc) kezdeményezése remek példája annak hogy a civil összefogás miképp segíthet ebben.

**Adat és szöveg találkozása**

Úgy tűnhet hogy a fürdővízzel együtt kiöntöttük a gyereket is, esetünkben a sztorit és csak az adatok maradtak. Sorozatunk [Digitális mesék](http://bit.ly/hmq0Gy) című részében megpróbáltuk jelezni hogy az új médium lehetővé teszi a régi narrációs technikákon való átlépést. Ez a terület azonban még gyerekcipőben jár és nem tudjuk mi fog kisülni belőle.

Azonban már történtek próbálkozások arra hogy egyfajta formanyelvet (design pattern) találjanak a sikeres vizualizációkról (és a hozzájuk kapcsolódó sztorikról is persze). Ennek legjobb példája a Segel és Heer [Narrative Visualization: Telling Stories with Data](http://bit.ly/fFOOkP) tanulmánya.

A [Journalism in the Age of Data](http://bit.ly/duQweP) riport film a legjobb összefoglalója annak hogy mihez kezd a média az új eszközökkel és hogyan válaszol a kihívásokra. Érdemes rászánni az időt (összesen 54 perc, de nyolc részre tagolták melyek logikusan épülnek egymásra, ha nincs valakinek ideje végig nézni együltőben nyugodtan meg-meg állhat a fejezetek között) és elmélyedni a kapcsolódó információk rengetegében.

**De akkor mi is az az adatújságírás?**

Akik szeretik a szép veretes definíciókat azokat ki kell ábrándítanom, nincs meghatározása a fogalomnak. Láthattuk hogy egyrészt technikai kezdeményezések, másrészt pedig a narrációs technikák korlátai állnak az egyik sarokban, ezeket próbálják itt-ott egybegyúrni. A dolog lényege szerintem hogy együtt kell működnie több oldalnak. A jó újságíró továbbra is újságíró, nem kell informatikussá válnia. Ellenben meg kell tanulnia egy új nyelvet, kommunikálnia kell azokkal a programozókkal, statisztikusokkal és dizájnerekkel akik segíthetnek neki jobban elmondani egy történetet, ill. ő is segíthet nekik egy alkalmazás megalkotásában, egy jelentés elkészítésében és még ki tudja miben. Ha a kedves olvasó érdeklődését sikerült felkeltenünk, akkor [Data-Journalism: Hope for a future in a troubled profession - an interview with Mirko Lorenz](http://bit.ly/dxuwco) posztunkban még további információkat találhat erről az új irányzatról.
