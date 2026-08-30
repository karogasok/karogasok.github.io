---
title: "Nyelvi értelmező, házilag"
date: 2011-08-10T10:10:00.001Z
publishDate: 2011-08-10T10:10:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/08/nyelvi-ertelmezo-hazilag.html"
regi_cimkek:
  - "nyelvtechnológia"
  - "szemantika"
  - "vendégposzt"
regi_cimkek_mind:
  - "grammatika"
  - "lex"
  - "nyelvi értelmező"
  - "nyelvtechnológia"
  - "sql"
  - "szemantika"
  - "vendégposzt"
  - "yacc"
---

*r0ller vendégposztja*

**„A programok bemenetének általában van valamilyen szerkezete. Tulajdonképpen, minden program, amely valamilyen bemenetet vár, definiál egy saját nyelvet amelyen a bemenetet meg kell fogalmazni. A bemenet lehet akár olyan összetett mint egy programnyelv vagy egyszerű mint egy számsor.” Ahogyan az egyik legismertebb nyelvtani elemző, a Yacc rövid ismertetőjéből is kitűnik, az emberek többségének a problémája a számítógépeken futó programokkal az, hogy mindegyikhez meg kell tanulni azok sajátos nyelvét. Ahelyett azonban, hogy az emberek tanuljanak meg több tíz vagy akár száz programmal hatékonyan kommunikálni, az egyszerűbb feladatok esetén a számítógépet is felruházhatnánk az adott feladat megoldásához szükséges természetes nyelvi töredék megértésének képességével.**

**A fenti célkitűzés jelen szerző egy nemrég indult magánakciójának sajátja. A projekt az Alice nevet kapta és a [githubon](http://github.com/r0ller/alice/wiki) bárki tanulmányozhatja vagy akár kísérletezhet vele. A program jelenleg az alapvető fájlkezeléshez kapcsolódó szavakból összeállított szótár alapján megfogalmazott angol nyelvű utasításokat fogad el. Ilyenek például a ‘list all executable files in directory abc’ vagy a ‘delete all files’. A szótár jelenleg igen kicsi, legfőképp mert a projekt egyelőre még inkább csak egy megvalósíthatósági tanulmány, így nem a használhatóság kiterjesztése áll a középpontban. Az alábbiakban megpróbálom bemutatni, hogyan is lehet felépíteni egy ilyen természetes nyelvi értelmezőt, mind nyelvészeti mind technikai oldalról.**

**Mindenek előtt**

Meg kell tudnunk fogalmazni mi az alapprobléma, mi a feladat: természetes nyelven megfogalmazott mondatok fordítása egy a számítógép által értelmezhető nyelvre. Ráadásul, mivel a gépeknek többnyire utasításokat adunk, kézenfekvőnek tűnik a természetes nyelvek felszólító mondatai felől közelíteni. (Valamivel emberközelibb lenne, ha a kérdőmondatokat is ide vennénk, de azzal egyelőre nem foglalkozunk.) Ez a feladat elég összetett, ezért nem árt ha részfeladatokra bontjuk:

1.  Modellalkotás.

1.  Az értelmezendő nyelv ábécéjének meghatározása.

1.  Az értelmezendő nyelv lexémáinak meghatározása.

1.  A modellben fennálló viszonyok, tulajdonságok leírása.

1.  Az értelmezendő nyelv nyelvtanának meghatározása.

1.  A szemantikai elemzés meghatározása.

**Nyelvészet**

Vegyük sorra a meghatározott részfeladatokat:

1. A modellezendő világ szereplőinek (főnevek) és azok lehetséges viszonyainak (igék) valamint a szereplők tulajdonságainak (melléknevek) összegyűjtése, modellalkotás:  
 Szükségünk van tehát egy univerzumra, mely tulajdonképpen a modellezett világban szereplő dolgok halmaza. Valamint értelmeznünk kell az univerzum elemein néhány műveletet, melyek a szereplők között elképzelhető viszonyokat, relációkat tükrözik. De mi kerüljön bele a modellbe? Képtelenség és meglehetősen sokáig is tart az általunk ismert világot teljes egészében lemodellezni. Elégedjünk meg csak egy olyan szűkebb környezettel, ami még átlátható de már elegendő információt tartalmaz ahhoz, hogy dolgozni lehessen vele, ugyanakkor nem árt ha mind a forrás- illetve a célnyelven könnyű leírni. Ez utóbbi kritérium a gépek esetén úgy teljesíthető, ha számukra is jól definiált dolgokat veszünk bele a modellbe. Ilyenek például a fájlok, az időjárás viszont nem. Tehát ha a célunk az, hogy mondjuk a számítógép által értelmezhető fájlkezelő utasításokra fordítsuk a természetes nyelvi mondatokat, akkor a modellt úgy alkotjuk meg, hogy az univerzumba ezen környezet által meghatározott dolgok kerülnek. Legyenek esetünkben ezek épp a legalapvetőbbek vagyis a file és directory, tulajdonságaik közül pedig ezek futtatható (executable) illetve nem futtatható (non-executable) voltát vegyük figyelembe. Az univerzumba ezen túlmenően az adott fájlrendszeren létező konkrét fájlok és könyvtárak is beletartoznak. Ezeket konstansokként kezeljük és az értelmezés során nem rendelünk hozzájuk egyedi azonosítót. A halmaz többi eleme esetén azonban az egyértelműség biztosítása érdekében egyedi azonosítókat kell rendelnünk a szereplőkhöz, tulajdonságaikhoz és a relációkhoz, melyet a lexémák meghatározásakor teszünk meg (1. táblázat). A fájlműveletek közül pedig értelmezzük a másolás, törlés, könyvtárváltás, listázás, áthelyezés és könyvtár létrehozása műveleteket.

1. Az értelmezendő nyelv ábécéjének meghatározása:  
 A modellalkotáshoz hasonló problémával szembesülünk most is: nehéz lenne az összes létező nyelv ábécéjét számba venni, jobb hát ha kezdésképp választunk egyet. Az angol nem tűnik rossz választásnak, legfőképp azért mert a legtöbb program is ezen a nyelven kommunikál velünk. A nyelvválasztásból fakadóan tehát, az angol nyelv ábécéjére mindenképp szükségünk van. A természetes nyelvekben megszokott írásjeleket viszont most figyelmen kívül hagyjuk. Ezen túlmenően viszont, a fájl- és könyvtárnevek tartalmazhatnak speciális karaktereket, így ezeket hozzá kell vegyük a saját ábécénkhez, de szorítkozzunk csak a leggyakoribbakra mint pl. a ., -, _, / karakterek és persze a számok.

1. Az értelmezendő nyelv lexémáinak meghatározása a főnevek, melléknevek és igék tekintetében valamint a meghatározott lexémákhoz tartozó, megengedett szóalakok meghatározása:  
 A természetes nyelvekben egy szónak több különböző alakját használjuk, amelynek megvan a maga jelentősége akár nyelvtani akár jelentéstani szempontból azonban az általunk létrehozandó nyelvben a természetes nyelvbeli szavak különböző alakjai által hordozott nyelvtani információkból igen kevésre van szükség. Így például, felszólító mondataink esetében az egyes illetve többes szám megkülönböztetésére szükség lehet, de a szám/személy egyeztetések, igeidők jelzésére szolgáló információk egyike sem fordul bennük elő. Esetünkben a nyelvben, amellyel az általunk modellezett világot leírjuk, az 1. táblázatban látható szavak szerepelnek.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-jr6ZezeFOys/TkDsLDaw4SI/AAAAAAAAAhI/N2FeJvdnjyE/s1600/t%25C3%25A1bla01.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://1.bp.blogspot.com/-jr6ZezeFOys/TkDsLDaw4SI/AAAAAAAAAhI/N2FeJvdnjyE/s640/t%25C3%25A1bla01.png" width="524" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">1. Táblázat</td><td class="tr-caption" style="text-align: center;"><br /></br>
</td></tr>
</tbody></table>

1. A szereplők és tulajdonságaik, illetve a szereplők és köztük elképzelhető relációk leírása:  
 Egy mondat állítmánya határozza meg az alany és a tárgy valamint egyes határozók (pl. részeshatározó) viszonyát azaz, hogy milyen relációban állnak egymással. Jelen esetben az alany mindig a számítógép, mivel a felszólítás implicite annak szól egyes szám második személyben: ’You list all files!’ vagy segédigével ’You do list all files!’ A mondat állítmányát mint relációt értelmezzük, a reláció argumentuma pedig a mondat tárgya vagy valamely határozója. Az angolban a vonzatos igék jelentését nagyban módosítja prepozíciójuk, így a relációkat azokkal együtt kell számontartani. Megállapodunk ugyanakkor abban, hogy a relációk argumentuma vonzat híján tárgyként értelmezendő. A relációk esetében jelenleg nem értelmezzük a határozószókat, mint pl. ’List all files recursively!’ esetében. Ezen információ tárolását azonban egy későbbi fejlesztés során egy újabb adatszerkezet bevezetésével meg lehet oldani. Az univerzumban fennálló viszonyokat az 2. táblázatban található reklációkkal fejezzük ki.  
  
 Ahhoz, hogy az univerzumban a fennálló viszonyok ismeretén túl a benne létező dolgok tulajdonságaira is legyen rálátásunk, szükségünk van egy szemantikus hálóra. Ezeket a tulajdonságokat általában melléknevekkel írjuk le. Az 1. ábrán vázolt szemantikus háló korántsem teljes, de a vizsgálódás tárgya ezt nem is követeli meg.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-R9VNEd2BS8A/TkJHFrx9LeI/AAAAAAAAAhQ/Y-Phq4B87B4/s1600/t%25C3%25A1bla02.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://1.bp.blogspot.com/-R9VNEd2BS8A/TkJHFrx9LeI/AAAAAAAAAhQ/Y-Phq4B87B4/s640/t%25C3%25A1bla02.png" width="400" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">2. táblázat</td><td class="tr-caption" style="text-align: center;"><br /></br>
</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-qtEAy5dY1ac/TkJHSRF3LyI/AAAAAAAAAhU/3feAcFpf--A/s1600/%25C3%25A1bra01.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="248" src="http://4.bp.blogspot.com/-qtEAy5dY1ac/TkJHSRF3LyI/AAAAAAAAAhU/3feAcFpf--A/s320/%25C3%25A1bra01.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">1. ábra</td></tr>
</tbody></table>

1. Az értelmezendő nyelv nyelvtanának meghatározása:  
 Most, hogy meg tudjuk nevezni az univerzumban létező dolgokat, ismerjük a köztük fennálló viszonyokat és tulajdonságaikat, már csak egy nyelvtanra van szükség, mellyel a szótárban szereplő szavakból nyelvtanilag helyes mondatokat tudunk előállítani. A nyelvtani szabályokat a 3. táblázat mutatja be. A terminálisok a hozzájuk rendelt szabály bal oldalán álló nyelvtani kategóriával egyező nyelvtani kategóriájú szavak halmazából veszik fel értéküket (ld. 1. táblázat). Az általunk megalkotott nyelvtan a [Transformational Grammar](http://en.wikipedia.org/wiki/Transformational_grammar) szempontjait követi annyi módosítással, hogy az ún. ’binarity principle’ ne sérüljön. Vagyis, hogy a szintaktikai elemző fának bináris fának kell lennie. Ez a követelmény egyben utat mutat a későbbi fejlesztéseknek, a Noam Chomsky által felvetett ún. [Universal Grammar](http://en.wikipedia.org/wiki/Universal_Grammar) irányába a [Minimalist Program](http://en.wikipedia.org/wiki/Minimalist_Program) keretein belül. Ez épp azt feltételezi, hogy bármely természetes nyelv nyelvtana elemezhető bináris fával. Az angol nyelv esetében ezt Andrew Radford a Minimalist Syntax c. könyvében meg is mutatta. Mindazonáltal, a probléma megoldása során kizárólag az angol nyelv nyelvtanának jellegzetességeire építő és ezen nyelvtan elemzésére alkalmas módszereket használtam fel, elsősorban Ronnie Cann: Formal Semantics és Andrew Radford: Transformational Grammar c. könyvei alapján. Ilyen pl. a ’head-first’ tulajdonság vagy a szórend kihasználása azaz az értelmező jelen formájában nem alkalmas egyetlen más nyelven írt mondat elemzésére sem.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-jAN7QmE5bWw/TkJHtOOpFzI/AAAAAAAAAhY/gIHFYuQE6EY/s1600/t%25C3%25A1bla03.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://4.bp.blogspot.com/-jAN7QmE5bWw/TkJHtOOpFzI/AAAAAAAAAhY/gIHFYuQE6EY/s640/t%25C3%25A1bla03.png" width="272" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">3.táblázat</td><td class="tr-caption" style="text-align: center;"></td></tr>
</tbody></table>

1.  A szemantikai elemzés meghatározása:  
 A szemantikai elemzés során formális szemantikai eszközöket használunk, melyek alapjait Ronnie Cann: Formal Semantics c. könyvéből könnyedén el lehet sajátítani. A formális szemantika leegyszerűsítve javarészt arra törekszik, hogy igaz/hamis értékekre tudjon kiértékelni egy adott állítást. Ugyanakkor felmerül a kérdés: hogyan lehet kiértékelni egy felszólító mondatot? Hogyan lehet pl. a töröld le az összes könyvtárat felszólítás igaz vagy hamis? Természetesen ebben a formában sehogy. Viszont vizsgálhatjuk a végrehajthatóságát azaz egy olyan állítást, hogy pl. az összes könyvtár letörölhető. Amennyiben az állítás igaz, az utasítás végrehajtható. Azonban átalakítani egy felszólító mondatot kijelentővé meglehetősen bonyolult eljárás egy gépnek. Ehelyett, a következőképp járunk el: szemantikai elemzés akkor megy végbe, amikor olyan nyelvtani szabályhoz érünk, amely két csúcs fölé helyez egy szülő csúcsot (alulról fölfelé történő elemzés szemszögéből nézve). Az értelmező ekkor megkeresi az újonnan létrehozandó szülő csúcs bal gyerekében a kifejezés fejét, a jobb gyerekében pedig a direct vagy indirect objectet. Ezt követően pedig a szülő csúcs nyelvtani kategóriájától függően, vagy a szemantikus hálóban vagy pedig a relációk között ellenőrzi, hogy a kifejezés feje és a direct/indirect object között fennállhat-e a leírt kapcsolat. Igei kifejezések (Vt, Vdt) esetén a jobbgyerekben található direct/indirect objecttel egyezteti a fejelemben tárolt relációt, főnévi kifejezések (NP) esetén pedig a szemantikus hálóban keres egy olyan utat melynek bármely két csúcsában megtalálhatók a fejelemben illetve a tárgyban szereplő lexémák. A jelenlegi megvalósítás nem ütközteti a jelzős szerkezetekben található valamennyi jelzőt az elemzett jelzős szerkezet fejével azaz a ’list executable non-executable files’ mondatot helyesnek értékeli. Ez azonban egy későbbi fejlesztés során könnyen pótolható.

**Technológia**

Az alábbiakban a felhasznált módszereket mutatnám be. Ezek működésének megértéséhez személy szerint egyrészt Hunyadvári László-ManhertzTamás: Formális nyelvek és automaták előkészületben lévő könyvét ajánlom, amely nem mellesleg a megjelenésig ingyen letölthető [innen](http://aszt.inf.elte.hu/%7Ehunlaci/book.pdf). Másrészt pedig Csörnyei Zoltán: Fordítóprogramok c. könyve szintén kihagyhatatlan e téren.

**A Lex**

A Lex egy program generátor, melyet olyan programok előállítására hoztak létre, amiket a bemenetként megadott karaktersorozatok lexikális elemzésére terveztek. Tulajdonképpen karaktersorozatok felismerésére adott magas szintű problémaorientált specifikációból képes előállítani egy általános felhasználási célú nyelven írt programot, amely felismeri a reguláris kifejezéseket. A reguláris kifejezéseket a felhasználó adja meg a specifikációban, amely a Lex forrása egyben. A Lex által előállított program felismeri ezeket a kifejezéseket a bemenetben és feldarabolja a kifejezéseknek megfelelő részekre. Az egyes részeknél a kifejezéshez rendelt felhasználói rutin hajtódik végre. Ezeket a felhasználói rutinokat a Lex forrásában lehet a reguláris kifejezésekhez rendelni bármely, a Lex által támogatott nyelven.

A kifejezések felismerésére generált programot a felhasználó által a rutinok megírására használt nyelven állítja elő a Lex, amennyiben az támogatott. Így nem kell külön egy a karaktersorozatok feldolgozására kidolgozott nyelven megírni a lexikális elemzőt és egy általános célú nyelven a program többi részét, mert a Lex egy általános célú nyelven generált programmal teszi lehetővé a karaktersorozatok lexikális elemzését.

A Lex által generált -általában yylex névre keresztelt- program felismeri a bemeneten előforduló kifejezéseket és végrehajtja a hozzárendelt felhasználói rutint. A reguláris kifejezésekhez rendelt felhasználói rutinok egy switch utasítás ágaiként jelennek meg. A futás folyamát pedig az automata interpretere irányítja.

Dióhéjban ennyit a Lexről, ha valaki többre kíváncsi [ezen](http://dinosaur.compilertools.net/lex/index.html) a linken tovább kutakodhat. Az értelmező esetében tulajdonképpen csak az engedélyezett karakterek szűrésére használom, hiszen a szavakat az adatbázisban található szótárban tárolom, nem pedig a Lex forrásban vannak rögzítve.

**A Yacc**

A Yacc a programok bementének adott struktúrába történő tördelésére alkalmas általános célú eszköz. A felhasználó elkészíti a bemeneti folyamat specifikációját, mely akár LALR(1)-es nyelvtant is leírhat az egyértelműséget biztosító szabályok megadásával. A specifikáció ezen túl tartalmazza a bemenet struktúráját leíró szabályokat, a felhasználói rutinokat, melyek a szabályok alkalmazásakor hívódnak meg, és a lexikális elemzőt, amely a bemenet beolvasását és előkészítését végzi. A Yacc ezt követően előállítja a bementi folyamat vezérlését ellátó yyparse függvényt. Ez a függvény az ún. elemző (parser), meghívja a felhasználó által írt lexikális elemzőt, hogy az a bemenetet feldolgozva visszaadja a terminális szimbólumokat ún. tokeneket. A tokenek a bemenet struktúrájának megfelelően létrehozott szabályok, az ún. nyelvtani szabályok szerint kell legyenek szervezve. Egy-egy ilyen szabály alkalmazásakor a hozzárendelt felhasználói rutin hajtódik végre. Az alkalmazott szabály során végrehajtott felhasználói rutin eredménye eltárolható, így más szabályok alkalmazásakor a korábbi szabályoknál született eredmények felhasználhatók. A Yacc C nyelven írt program és maga is C nyelvű elemzőt generál. Ebből következően a felhasználói rutinokat is C nyelven várja.

További ismerkedésre a Yacccal [itt](http://dinosaur.compilertools.net/yacc/index.html) van lehetőség. Azt hiszem, mindenkinek aki kicsit is érdeklődik a transzformációs grammatika és a számítógépes nyelvészet iránt, majdhogynem kihagyhatatlan eszköz. Az értelmező esetében a korábban bemutatott nyelvtani szabályok a Yacc forrásban vannak rögzítve. A projekt rövid távú céljai között szerepel azonban, hogy az adatbázisban tároljam őket. Ezzel elkerülhető a Yacc forrás állandó újrafordítása, a nyelvtani szabályok változtatása esetén.

**Az SQLite**

Azt hiszem erről nemrégiben született egy poszt épp ezen a blogon, így inkább csak [arra](http://szamitogepesnyelveszet.blogspot.com/2011/06/python-es-az-sqlite-adatbazis-lajtosan.html) hivatkoznék.

**Az elemzés menete**

Példaként lássuk, hogyan elemzi az értelmező a ‘list executable files to file abc’ mondatot:

1. A nyelvtani elemző megnézi, hogy van-e a bemenetként megadott szövegre –előreolvasás nélkül– alkalmazható szabály.

1. A nyelvtani szerkezet helyessége kedvéért, a nyelvtani szabályok között megtalálhatók a mondat alanyát elemző szabályok is, bár az angol felszólító mondatok esetében ez rejtett alany. Ennek megfelelően a nyelvtani elemző megtalálja az első szabályt: Pro→ͼ.

1. A hozzá tartozó levelet beilleszti az értelmező fába:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-YAGkcF87b-Y/TkJP_vCstzI/AAAAAAAAAhg/futwj1HRjlM/s1600/%25C3%25A1bra02.png" rel="nofollow noopener">%25C3%25A1bra02.png</a></span>](http://1.bp.blogspot.com/-YAGkcF87b-Y/TkJP_vCstzI/AAAAAAAAAhg/futwj1HRjlM/s1600/%25C3%25A1bra02.png)

1. A következő, előreolvasás nélkül alkalmazható szabály pedig az: NP→Pro.

1. Az értelmező fában létrehozza az ennek megfelelő csúcsot:

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/-Krbd2X3Wp8Q/TkJQOhOBQrI/AAAAAAAAAhk/o0FUZzQuOJk/s1600/%25C3%25A1bra03.png" rel="nofollow noopener">%25C3%25A1bra03.png</a></span>](http://2.bp.blogspot.com/-Krbd2X3Wp8Q/TkJQOhOBQrI/AAAAAAAAAhk/o0FUZzQuOJk/s1600/%25C3%25A1bra03.png)

1. Nincs több előreolvasás nélkül alkalmazható szabály, így a lexikális elemző beolvassa az első szót: list. Mindeközben ellenőrzi, hogy az az általunk definiált nyelv ábécéjének betűiből áll-e.

1. Megállapítja az elsőként megtalált szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

1. A nyelvtani elemző megkeresi a kapott tokenhez tartozó szabályt: V→LIST.

1. A nyelvtani szabályhoz nem tartozik szemantikai elemzés mert az egyetlen szón nem hajtható végre. Így első lépésként az értelmező fában létrehoz egy levelet, melynek címkéje a nyelvtani szabály bal oldalán álló nemterminális szimbólum, de tartalmazza a tokenhez tartozó lexémát is.

1. További előreolvasás nélkül nincs alkalmazható szabály, ezért beolvassa a következő szót: executable.

1. Megállapítja a szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-P2_tqy8w6_U/TkJQzGMHoHI/AAAAAAAAAho/S5Ig9n3rLgw/s1600/%25C3%25A1bra04.png" rel="nofollow noopener">%25C3%25A1bra04.png</a></span>](http://3.bp.blogspot.com/-P2_tqy8w6_U/TkJQzGMHoHI/AAAAAAAAAho/S5Ig9n3rLgw/s1600/%25C3%25A1bra04.png)

1. A nyelvtani elemző megkeresi a kapott tokenhez tartozó szabályt: A→EXECUTABLE.

1. Önálló szóról és nem kifejezésről lévén szó, ismét csak létrehoz egy levelet az értelmező fában.

[<span class="lost-media">Hiányzó kép: <a href="http://4.bp.blogspot.com/-fNE7NCs_lNY/TkJRPlGahqI/AAAAAAAAAhw/AqAvSc7f3jI/s400/%25C3%25A1bra05.png" rel="nofollow noopener">%25C3%25A1bra05.png</a></span>](http://4.bp.blogspot.com/-fNE7NCs_lNY/TkJRPlGahqI/AAAAAAAAAhw/AqAvSc7f3jI/s1600/%25C3%25A1bra05.png)

1. További előreolvasás nélkül viszont nincs alkalmazható szabály, ezért beolvassa a következő szót: files.

1. Megállapítja a szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

1. A nyelvtani elemző megkeresi a kapott tokenhez tartozó szabályt: N→FILE.

1. Megint csak egy levelet hoz létre az értelmező fában.

[<span class="lost-media">Hiányzó kép: <a href="http://4.bp.blogspot.com/-8cA1LznJL7U/TkJRghl2W1I/AAAAAAAAAh0/y8MrhzBxzVM/s320/%25C3%25A1bra06.png" rel="nofollow noopener">%25C3%25A1bra06.png</a></span>](http://4.bp.blogspot.com/-8cA1LznJL7U/TkJRghl2W1I/AAAAAAAAAh0/y8MrhzBxzVM/s1600/%25C3%25A1bra06.png)

1.  A nyelvtani elemző megtalálja a következő alkalmazható szabályt előreolvasás nélkül: CNP→N.

1. Létrehozza az ennek megfelelő csúcsot az értelmező fában.

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/-b4DerWMHhfY/TkJR7dbyVTI/AAAAAAAAAh4/yJTbKb-miL4/s400/%25C3%25A1bra07.png" rel="nofollow noopener">%25C3%25A1bra07.png</a></span>](http://2.bp.blogspot.com/-b4DerWMHhfY/TkJR7dbyVTI/AAAAAAAAAh4/yJTbKb-miL4/s1600/%25C3%25A1bra07.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: CNP→A CNP.

1. Elérkezett az első kifejezéshez: executable file. Elvégzi a szemantikai elemzést: veszi a kifejezés fejét (EXECUTABLE) és a tárgyát (FILE). Ezekkel keres a szemantikus hálóban egy olyan utat, melynek bármely két csúcsában ez a két lexéma megtalálható.

1. Ha nem találhatók, az elemzés leáll. Ellenkező esetben létrehozza az új csúcsot az értelmező fában.

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-oN5OR6nLSgY/TkJSCZ-TxVI/AAAAAAAAAh8/6l5245Ej6aE/s400/%25C3%25A1bra08.png" rel="nofollow noopener">%25C3%25A1bra08.png</a></span>](http://3.bp.blogspot.com/-oN5OR6nLSgY/TkJSCZ-TxVI/AAAAAAAAAh8/6l5245Ej6aE/s1600/%25C3%25A1bra08.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: NP→CNP.

1. Az értelmező fa ekkor a következőképp alakul:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-YMTHzrtSi6Q/TkJSbCzbUmI/AAAAAAAAAiA/DXIplQm6JsA/s640/%25C3%25A1bra09.png" rel="nofollow noopener">%25C3%25A1bra09.png</a></span>](http://1.bp.blogspot.com/-YMTHzrtSi6Q/TkJSbCzbUmI/AAAAAAAAAiA/DXIplQm6JsA/s1600/%25C3%25A1bra09.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: Vt→V NP.

1. Ez egy újabb kifejezés, amely szemantikai elemzésre szorul. Veszi a kifejezés fejelemét (LIST) és a tárgyát (FILE). Ellenőrzi, hogy a LIST reláció tárgya valóban lehet-e FILE.

1. Ha nem, az elemzés leáll. Ellenkező esetben egy újabb csúcsot illeszt az értelmező fába:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-WIwUYqIw92I/TkJS91jHkoI/AAAAAAAAAiE/DWJLxyFFsTg/s640/%25C3%25A1bra10.png" rel="nofollow noopener">%25C3%25A1bra10.png</a></span>](http://1.bp.blogspot.com/-WIwUYqIw92I/TkJS91jHkoI/AAAAAAAAAiE/DWJLxyFFsTg/s1600/%25C3%25A1bra10.png)

1. Előreolvasás nélkül nincs több alkalmazható szabály, így a lexikális elemző beolvassa a következő szót: to.

1. Megállapítja a szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

1. A nyelvtani elemző megkeresi a kapott tokenhez tartozó szabályt: Prep→TO.

1. Ennek megfelelően létrehoz egy újabb levelet a fában:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-N63kpA2lc-U/TkJTO1eAV1I/AAAAAAAAAiI/EpVaDJNJQrg/s640/%25C3%25A1bra11.png" rel="nofollow noopener">%25C3%25A1bra11.png</a></span>](http://1.bp.blogspot.com/-N63kpA2lc-U/TkJTO1eAV1I/AAAAAAAAAiI/EpVaDJNJQrg/s1600/%25C3%25A1bra11.png)

1. Előreolvasás nélkül nincs több alkalmazható szabály, így a lexikális elemző beolvassa a következő szót: file.

1. Megállapítja a szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

1. Előreolvasás nélkül nincs több alkalmazható szabály, így a lexikális elemző beolvassa a következő szót: abc.

1. Megállapítja a szóhoz tartozó terminális szimbólumot (tokent) és átadja a nyelvtani elemzőnek.

1. Az utoljára kapott tokenre alkalmazható szabály: Con→abc.

1. Az értelmező fába egy újabb levelet illeszt:

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/-8CkQbMuYZxs/TkJTgnnSoMI/AAAAAAAAAiM/TpwfxqKx76c/s640/%25C3%25A1bra12.png" rel="nofollow noopener">%25C3%25A1bra12.png</a></span>](http://2.bp.blogspot.com/-8CkQbMuYZxs/TkJTgnnSoMI/AAAAAAAAAiM/TpwfxqKx76c/s1600/%25C3%25A1bra12.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: N→FILE.

1. Beillesztve az újabb csúcsot, az értelmező fa a következőképp alakul:

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-gnBKVkj_lpo/TkJUCAYmecI/AAAAAAAAAiQ/aEicvOHEW_4/s640/%25C3%25A1bra13.png" rel="nofollow noopener">%25C3%25A1bra13.png</a></span>](http://3.bp.blogspot.com/-gnBKVkj_lpo/TkJUCAYmecI/AAAAAAAAAiQ/aEicvOHEW_4/s1600/%25C3%25A1bra13.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: CNP→N.

1. Létrehozza az ennek megfelelő csúcsot az értelmező fában:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-hFr-pkUnRzY/TkJUSzUXGdI/AAAAAAAAAiU/OL8MHRuQtbs/s640/%25C3%25A1bra14.png" rel="nofollow noopener">%25C3%25A1bra14.png</a></span>](http://1.bp.blogspot.com/-hFr-pkUnRzY/TkJUSzUXGdI/AAAAAAAAAiU/OL8MHRuQtbs/s1600/%25C3%25A1bra14.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: NP→CNP.

1. Létrehozza az ennek megfelelő csúcsot az értelmező fában:

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-FJUcnjvrXmU/TkJVXoyECOI/AAAAAAAAAic/i3uzs66wXWo/s640/%25C3%25A1bra15.png" rel="nofollow noopener">%25C3%25A1bra15.png</a></span>](http://1.bp.blogspot.com/-FJUcnjvrXmU/TkJVXoyECOI/AAAAAAAAAic/i3uzs66wXWo/s1600/%25C3%25A1bra15.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: PP→Prep NP.

1. Az értelmező fa ekkor a következőképp alakul:

[<span class="lost-media">Hiányzó kép: <a href="http://4.bp.blogspot.com/-NM1cMC7pPzM/TkJVrmM0fnI/AAAAAAAAAig/lul3KLsnri0/s640/%25C3%25A1bra16.png" rel="nofollow noopener">%25C3%25A1bra16.png</a></span>](http://4.bp.blogspot.com/-NM1cMC7pPzM/TkJVrmM0fnI/AAAAAAAAAig/lul3KLsnri0/s1600/%25C3%25A1bra16.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: Vdt→Vt PP.

1. Ez egy újabb kifejezés, amely szemantikai elemzésre szorul. Veszi a kifejezés fejelemét (LIST) és a tárgyát (FILE). Ellenőrzi, hogy a LIST reláció és a hozzá tartozó elöljárós kifejezésben található TO prepozíció vonzata lehet-e FILE.

1. Ha nem, az elemzés leáll. Ellenkező esetben beilleszti az új csúcsot az értelmező fába:

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-O9Y0RjLCqSo/TkJV9q8gudI/AAAAAAAAAik/CIc_0joM1qg/s640/%25C3%25A1bra17.png" rel="nofollow noopener">%25C3%25A1bra17.png</a></span>](http://3.bp.blogspot.com/-O9Y0RjLCqSo/TkJV9q8gudI/AAAAAAAAAik/CIc_0joM1qg/s1600/%25C3%25A1bra17.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: VP→Vdt.

1. Beillesztve az újabb csúcsot, az értelmező fa a következőképp alakul:

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/-ZiwWwXt8nBo/TkJWT57zVsI/AAAAAAAAAio/izhAJ45VGRU/s640/%25C3%25A1bra18.png" rel="nofollow noopener">%25C3%25A1bra18.png</a></span>](http://2.bp.blogspot.com/-ZiwWwXt8nBo/TkJWT57zVsI/AAAAAAAAAio/izhAJ45VGRU/s1600/%25C3%25A1bra18.png)

1. Előreolvasás nélkül a következőként alkalmazható szabály: S→NP VP.

1. Miután elérte a Start szimbólumot, az elemzés sikeresen zárul. A fa végső alakja:

[<span class="lost-media">Hiányzó kép: <a href="http://4.bp.blogspot.com/-g8SW0AwkMKo/TkJWhXLURWI/AAAAAAAAAis/oug6we3vxqI/s640/%25C3%25A1bra19.png" rel="nofollow noopener">%25C3%25A1bra19.png</a></span>](http://4.bp.blogspot.com/-g8SW0AwkMKo/TkJWhXLURWI/AAAAAAAAAis/oug6we3vxqI/s1600/%25C3%25A1bra19.png)

Ennyiből áll egy mondat elemzése, értelmezése, aminek alapján eldönthető, hogy egy adott utasítás végrehajtható-e vagy sem. Ezek után már csak a végrehajtható UNIX shell scriptet kell előállítani, hogy valóban azt tegye a gép, amit mondunk neki.

**A szerzőről:**

r0ller korábban a KRE Angol nyelv és irodalom szakán illetve az ELTE programozó-matematikus szakán végzett. Innen az érdeklődés a számítógépes nyelvészet iránt, melynek köszönhetően a cikkben említett Alice projekt mint amolyan szabadidős tevékenység megszületett.
