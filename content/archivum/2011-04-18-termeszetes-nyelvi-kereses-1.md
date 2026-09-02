---
title: "Természetes nyelvi keresés 1"
slug: "termeszetes-nyelvi-kereses-1"
date: 2011-04-18T09:47:00.002Z
publishDate: 2011-04-18T09:47:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/04/termeszetes-nyelvi-kereses-1.html"
regi_cimkek:
  - "Google"
  - "keresés"
  - "nyelvészet"
  - "számítógépes nyelvészet"
regi_cimkek_mind:
  - "Bing"
  - "Google"
  - "Page Rank"
  - "Powerset"
  - "Swingly"
  - "True Knowledge"
  - "Yebol"
  - "keresés"
  - "nyelvészet"
  - "számítógépes nyelvészet"
---

**A keresés megszokott része digitális hétköznapjainknak; nem csak az interneten szoktunk keresni, hanem dokumentumainkban és azok között és egyre több operációs rendszer integrál egy általános keresőt ami nem csak a szöveges fájlok, hanem minden adat és program között képes keresni. A keresés általánossá vált, része az ember-gép interakciónak (HCI - human computer interaction), s habár egyre megszokottabb a kulcsszavas keresés, nem szabad elfelejtenünk hogy [a begépelt kulcsszavak száma folyamatosan növekszik](http://bit.ly/gA8S5G), miközben az információ mennyisége rohamosan gyarapodik. A megnövekedett komplexitást két oldalról "támadhatjuk", egyrészt az információ mélyebb elemzésével és strukturálásával, másrészt a felhasználó ún. naiv elméletének (a keresőmotor működésére vonatkozó félig-meddig tudatos elképzeléseinek) jobb megértésével és kiszolgálásával. A természetes nyelvi keresés ennek a kettős igénynek próbál megfelelni.**

**Természetes nyelvi keresés - dizájn megfontolások**

Ahogyan már említettük a felhasználók naiv elméleteket alkotnak az általuk használt tárgyak működéséről. Ez nem jelenti azt hogy azok a dolgok tényegesen úgy is működnének, vagy hogy a felhasználó szerint az egy magyarázat lenne a működésre, csupán annyit tesz hogy egy koherens keretet alkot (nem teljesen tudatosan) arról hogy adott viselkedésre (pl. a távkapcsoló piros gombjának megnyomására) milyen választ mutat a szerkezet (be/ki kapcsol a tévé). Ez a viselkedés természetes beállítottság, ugyanígy járunk el embertársaink esetében is ugyanis arra hogy a többi embernek is vannak érzelmeik, és elmeállapotaik csakis viselkedésükből következtethetünk, ezek megértése és észlelése elengedhetetlen része a hétköznapi életnek, azonban korántsem biztos hogy úgy működik agyunk/elménk mint ahogy mi azt elképzeljük (az előbbi két jelenséget nevezik a kognitívtudósok és elmefilozófusok a többi elme problémájának, [*problem of other minds*](http://bit.ly/f06yzK), ill. elmeolvasásnak, [*mind reading*](http://bit.ly/gGNy0x)). A keresés során a két legegyszerűbb analógia a természetes nyelvből vett kérdés és egyszerű parancsok (felszólítások). Le kell szögeznünk hogy maga a keresés nem nyelvi tevékenység, de a felhasználó elméjében lévő keret hasonlít bizonyos nyelvi tevékenységekhez! Erről bővebben a [Keresés természetes nyelven](http://bit.ly/9PHH5E) írásomban olvashat a kedves olvasó a Kereső Világ blogon, most ennek elemzésétől eltekintünk és adottnak vesszük ezt az analógiát.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-gt6QIZYmq8c/TawGc5eOotI/AAAAAAAAAdE/2492CmRv-yM/s1600/hci.gif" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-gt6QIZYmq8c/TawGc5eOotI/AAAAAAAAAdE/2492CmRv-yM/s320/hci.gif" width="271" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Az ember-gép interakció vizsgálata rendkívül összetett terület. <a href="http://www.vhml.org/theses/nannip/HCI_final_files/image001.gif">Forrás.</a></td></tr>
</tbody></table>

Figyelembe véve a felhasználót, így két irány lehetséges. Egyfelől hagyatkozhatunk a már meglévő intuícióira és nem kell változtatunk a keresés eddigi menetén. Ha így döntünk, akkor viszont nagy hangsúlyt kell fektetnünk arra hogy egy adott limitnél tovább ne nőjön a kulcsszavak hossza, és a kulcsszavak szerepét közelítenünk kell a mögöttük rejlő intenciókhoz, azaz egyfajta kérdéssé vagy paranccsá kell alakítanunk őket. Másrészt viszont dönthetünk úgyis hogy lecseréljük az eddig megszokott módszert és természetes nyelvi kérdéseket várunk el a felhasználótól. Így az ember-gép interakciót közelítjük az ember-ember kapcsolatához.

**A természetes nyelvi keresés játékosai**

A megszokott keresők nem alkalmaznak túl sok nyelvészeti háttérismeretet. Bármennyire is az intuíciónk hogy a begépelt kulcsszavakat "érit" a rendszer és azt az oldalt adja ki találatnak amin előfordulnak és pedig abban  használatban ahogy azt mi gondoltuk, ezt pl. a Google Page Rank algoritmusa úgy éri el hogy külső heurisztikát használ - mégpedig a web létrehozóinka tudását. Ugyanis a találatok egyrészt egy adott kifejezés előforulását jelentik egy adott dokumentumban, ám a rangsorolást a dokumentumok közötti linkek adják. Így amelyik forrásra sok link mutat, az bizonyára eléggé releváns, ha ezeket a kapcsolatokat számszerűsítjük, megkapjuk a dokumentumok egy sorrendjét, amit csodák csodájára megfelel elképzeléseinknek. Aki nem fél a matematikától, olvassa el bátran a "[The 25 billion dollar Eigenvector: The Linear Algebra Behind Google](http://bit.ly/fJLItj)" (a link pdf dokumentumra mutat) cikket.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-db8OlzBbkv0/TawIAzN-lyI/AAAAAAAAAdU/oPjpb6aZsIw/s1600/TR02.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="191" src="http://4.bp.blogspot.com/-db8OlzBbkv0/TawIAzN-lyI/AAAAAAAAAdU/oPjpb6aZsIw/s320/TR02.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A TrueKnowledge nem honlapokkal szeretne válaszolni, hanem tényekkel.</td></tr>
</tbody></table>

Ezzel a megoldással alapvetően nincs gond, hiszen látjuk hogy működik. Azonban a seo technikák, a spamek és egyéb trükkös megoldások egyre több problémát okoznak, nem is beszélve arról hogy a rangsorolás nem más mint egy népszerűségi lista és nem biztos hogy a közvélekedés egybeesik a tényekkel. Ezért két, egymástól nem teljesen elkülöníthető irányzat jelent meg. Az egyik egy szűk területen definiált ún. knowledge frame-eket vagyis tudás kereteket keres, ennek helye általában a wikipedia, és az ott található kapcsolatok feltérképezésével próbálja meg listázni a tényeket. A Microsoft által felvásárolt  és a [Bingbe](http://www.bing.com/) többé-kevésbbé integrált Powerset kereső is így kezdte anno. Hasonlóképpen a [TrueKnowledge](http://www.trueknowledge.com/) nem annyira hagyományos kereső, mint inkább egy kérdés megválaszoló rendszer (question answering). A felhasználó természetes nyelvi kérdéseket tehet fel amelyre egy választ kap (gyakran hivatkozással egy wikipedia cikkre), a felhasználók értékelhetik a választ, sőt megadhatják saját válaszukat is egy-egy kérdésre!

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-J79X0Me5bgA/TawG7Qk0DfI/AAAAAAAAAdI/0qrsJJDjkQo/s1600/powerset.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="142" src="http://2.bp.blogspot.com/-J79X0Me5bgA/TawG7Qk0DfI/AAAAAAAAAdI/0qrsJJDjkQo/s320/powerset.jpg" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Így nézett ki a Powerset keresőfelülete, ma már a Bingre mutat az oldala.</td></tr>
</tbody></table>

A Bing azonban nem vált Powerset-té, csupán integrálta a strukturált elemzés módszerét saját keresőjébe,ami azonban "hagyományos" alapon működik. A Yeblo kereső ellenben egy integrált megoldáson dolgozik, a megszokott módszertől eltérően nem a hagyományos mintaillesztés plusz rangsorolás modellben gondolkodik, hanem nagy hangsúlyt fektet a tartalom előzetes elemzésére és az alapján megtalálni a leginformatívabb eredményeket.  Ehhez a klasszikus látens szemantikai elemzéstől az asszociációs algoritmusokig mindent bevet, mivel bevalott célja hogy ne kelljen "speciális keresést" (advanced search) és egyébb eszközöket használnia a felhasználónak.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-Gou4urOTlMQ/TawHRh50arI/AAAAAAAAAdM/dVn4Q3LL_Kg/s1600/yebol02.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-Gou4urOTlMQ/TawHRh50arI/AAAAAAAAAdM/dVn4Q3LL_Kg/s320/yebol02.png" width="256" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A Yebol szépen elkülönítve jeleníti meg a különböző találatokat.</td></tr>
</tbody></table>

Hasonlóan a [Swingly](http://beta.swingly.com/) is törekszik lefedni az egész netet, viszont a TrueKnowledge-hez, de még inkább a szép emlékű Powersethez hasonlóan törekszik szemantikus információt kinyerni a fellelhető dokumentumokból. Mindezt úgy éri el hogy a dokumentumokból szemantikus n-tuple sorokat nyer ki (olyan alapvető szemantikai relációkat mint pl "A ló egy emlős -> LÓ <IS-A> EMLŐS", ahol az <IS-A> reláció megadja mely fogalmak és individuumok tartoznak egy adott fogalom alá) és ezekhez már kvázi előre generálhatók a lehetséges kérdések (pl. "Emlős-e a ló?", "Mi lehet emlős?"). Habár az alapötlet nagyon tetszetős, aki egy kicsit is játszik a rendszerrel, hamar rájön hogy van még hova fejlődnie.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-pcHrHCrmvm4/TawHqYsXY-I/AAAAAAAAAdQ/qIGCwcN-NdE/s1600/swingly01.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="220" src="http://1.bp.blogspot.com/-pcHrHCrmvm4/TawHqYsXY-I/AAAAAAAAAdQ/qIGCwcN-NdE/s320/swingly01.png" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Jellemző hogy annyira hozzászoktunk a kulcsszavakhoz hogy a TR-hez hasonlóan a Swingly is ajánlgat nekünk minta kérdéseket.</td></tr>
</tbody></table>

**Melyik úton?**

Sajnos nem lehet megmondani melyik megoldás fog győzni. Én remélem hogy mindkettő megmarad egymás mellett, habár úgy gondolom hogy a question answering egy kicsit félrenyúl, hiszen egy keresés nem egyenértékű egy kérdéssel. Azonban mindenképpen jó irány a lehetséges találatok szemantikai elemzése. A következő részben bemutatjuk hogy hogyan lehet jól elkapni a felhasználó intuicióját (lelövöm a poént, a Kereső Világnak írt posztomhoz térünk majd vissza), és a sorozat harmadik részében azt is meg fogjuk vizsgálni hogyan lehetne összekapcolni a két területet, mindenki nagy örömére.
