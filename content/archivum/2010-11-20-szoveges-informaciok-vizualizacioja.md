---
title: "Szöveges információk vizualizációja Gephi és az AlchemyAPI segítségével"
slug: "szoveges-informaciok-vizualizacioja"
date: 2010-11-20T13:01:00.002Z
publishDate: 2010-11-20T13:01:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/11/szoveges-informaciok-vizualizacioja.html"
regi_cimkek:
  - "digitális bölcsészet"
  - "startup"
  - "szöveg vizualizáció"
regi_cimkek_mind:
  - "AlchemyAPI"
  - "Gephi"
  - "digitális bölcsészet"
  - "startup"
  - "szöveg vizualizáció"
---

**Már sokszor szóltunk róla hogy érdekel minket miként is lehet egy szöveget vizualizálni. Persze az első kézenfekvő válasz erre a régi jó öreg Zipf-törvény alapján rajzolt szógyakoriság (ami nekem már egészen kis korom óta a kedvencem), illetve a bigram és n-gram táblák, esetleg szófajok alapján egy piechart. De lehet-e mélyebbre menni ennél? Kelle-e? A második kérdésre én sem tudom a választ, de az elsőre már határozott igen a válasz! Minden különösebb programozási ismeret nélkül betekintést nyerhetünk a szövegek egy mélyebb rétegébe, azonban sajnos anyanyelvünkön ezt még nem tehetjük meg.**  
  
  
  
**Az eszközök**  
  
 Ahhoz hogy végig tud te is csinálni az elemzést, szükséged van működő internetkapcsolatra, némi angol tudásra és józan észre. Telepíteni egyetlen alkalmazást kell csupán, kérlek figyelmesen olvasd el ennek követelményeit mert megeshet hogy egy gyengébb gépre nem tudod telepíteni a Gephit. Végül pedig jó ha észben tartod, *a szabad szoftver mindenféle garancia nélkül, de ingyenesen érhető el. Ezért fontos betartanod a számítógép használat ésszerű szabályait* (rendszeresen mentsd el fontos munkáidat, dokumentumaidat stb), így ha bármi baj történik (és hidd el bármikor történhet bármi!) nem áll meg az élet.  
  
[AlcehmyAPI](http://bit.ly/a8ziZd)  
 Az AlchemyAPI, miképp neve is mutatja, egy eszköz programozási interfész (application programming interface), amiről annyit kell tudnod, hogy távol gépeken csoda történik az adatokkal amik feldolgozására megkéred. A mi esetünkben csak a legalapvetőbb kategóriák azonosítására fogjuk megkérni. Ehhez csupán egy ún API-key, azaz api kulcs szükséges, amit regisztráció után, ingyenesen biztosít számodra az AlcehmyAPI. Az oldalon nem tudod eltéveszteni hova kell kattintanod a kulcsért! (Ha szeretnél többet megtudni mi történik a háttérben, gyere vissza később az oldalra, a készítővel hamarosan elbeszélgetünk és erről poszt is fog születni)  
[Gephi](http://bit.ly/cAcK5v)  
 A Gephi egy interaktív vizualizációs és felfedező platform amivel minden gráf- és hálózatos adatokat tudsz megjeleníteni. Töltsd le értelem szerűen a gépednek megfelelő verziót, installáld és indítsd el a programot. Ezután töltsd le az [AlchemyAPI plugint](http://bit.ly/dj18eu), majd a megnyitott Gephiben Tools > Plugins > > Downloaded > Add Plugins, válaszd ki a letöltött fájlt és a program végig vezet téged az installáláson. Ha ez megvan, lépj ki a Gephiből és indítsd újra.  
  
**Egyszerű elemzés**  
  
 Válassz ki két (vagy több) szöveges fájlt és/vagy honlapot amit elemezni szeretnél. Én az angol Wikipedia Lakatos Imre, Paul Feyerabend és Karl Popper szócikkeit választottam. A Gephiben File > Generate > Semantic Analysis menüpont egy párbeszéd dobozt nyit meg, válaszd ki hogy URL-t, szöveges fájlt (Text), vagy lementett HTML fájlt nyitsz-e meg, értelem szerűen vagy az url-t másold be, vagy a gépeden található elérési útvonalat ad meg a szöveges mezőben, az API Key helyére pedig másold be egyedi API kulcsodat. És ennyi! Hamarosan láthatod hogy a középső részen történik valami. A többi elemezni vágyott szöveggel ugyan így járj el, a Gephi automatikusan hozzáadja majd az adatokat a meglévőkhöz.  
  
 A meglévő adatokkal érdemes eljátszadozni, ehhez kitűnő kiindulópont a Gephi Wikin található [Quick Start Tutorial](http://bit.ly/cjGwNE) és a [Quick Start Visualization](http://bit.ly/dxD2XZ). Fontos végigmenni legalább ezeken a rövid ismertetőköm hogy képet alkothassunk mire is képes a Gephi. Ezek után már képesek vagyunk szűrni datainkat, súlyozni a csomópontokat és az éleket, alakítani az elrendezést stb. Ehhez nem kell három PhD, csak egyszerű józan ész és egy kis türelem! Én pár óra alatt erre jutottam:

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/_SM9YHwWrX6M/TOfHjB4LVZI/AAAAAAAAAWw/7xFkrYHVWUE/s320/tudfil.png" rel="nofollow noopener">tudfil.png</a></span>](http://3.bp.blogspot.com/_SM9YHwWrX6M/TOfHjB4LVZI/AAAAAAAAAWw/7xFkrYHVWUE/s1600/tudfil.png)

**Mire jó akkor ez?**  
  
 Nehéz megválaszolni hogy szöveges információk elemzésében mire jó mindez. A fenti ábrán, ha értelmezni akarjuk látható hogy Lakatosnak van több "érintkezési pontja", hiszen Popperrel és Feyerabenddel is sok ilyen található, ami életútját ismerve nem is meglepő. Ha kellően nagy adathalmazon végzünk elemzést, akkor gyakran sokkal többet mond nekünk egy ilyen kép mint maga a leíró statisztika, hiszen még a matematikus elsősorban vizuális és jobban ért egy történetet képpel illusztrálva, mint a száraz számokat.  
  
 A Gephi egyik alkotóját a LinkedIn foglalkoztatja, ahol tudását és munkájának gyümölcsét arra használják hogy a felhasználók szöveges profiljait elemezve tökéletesítsék a munkakeresők és munkát ajánlók egymásratalálását.  
  
 A digitális bölcsészetben is hasznos lehet az ilyen elemzés és az adatok képi megjelenítése, erről a napokban jelent meg egy érdekes cikk az NY Times-ban, [Digital Keys for Unlocking the Humanities' Riches](http://nyti.ms/d68RHO), amit minden kedves olvasónknak ajánlok.
