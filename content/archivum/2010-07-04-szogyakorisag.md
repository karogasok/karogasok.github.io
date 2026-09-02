---
title: "Szógyakoriság"
slug: "szogyakorisag"
date: 2010-07-04T16:39:00.001Z
publishDate: 2010-07-04T16:39:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/07/szogyakorisag.html"
regi_cimkek:
  - "korpusz"
  - "statisztika"
regi_cimkek_mind:
  - "gnuplot"
  - "korpusz"
  - "korpusz nyelvészet"
  - "statisztika"
---

**Egyik kedvenc tanárom mesélte mindig hogy angolos hallgató korában a kiadott olvasmányokból szószedetet kellett készíteniük és amolyan röpdoli-szerűen számon kérték rajtuk a szavakat. Az én tanárom persze rögtön azon gondolkodott el hogy meddig kell elolvasnia egy adott könyvet hogy nagy valószínűséggel meglegyen neki a legtöbb szó. Egyszer amikor ezt mesélte hozzátette; mennyi szót kell ismernie egy helyesírás elemzőnek hogy jól működjön? Érdemes-e még több szót "belepakolni" hogy nagyon jól működjön? Most ezt a kérdés próbáljuk meg eldönteni, amolyan ránézésre!**  
  
**Kellékek**  
[gnuplot](http://www.gnuplot.info/), [Magyar Webkorpusz](http://mokk.bme.hu/resources/webcorpus/)  
Figyelem! Ha te is szeretnéd végig csinálni az "elemzést" akkor előbb telepítened kell a gnuplot-ot és le kell töltened a szövegfájlt!  
  
**Grafikus adatfelfedezés**  
Gyakran a legjobb megoldás egy problémára ha látod magad előtt. Ha olvasol újságot (amit nagyon remélek), biztos megnézed a grafikonokat. Pl ha a GDP eloszlásáról olvasol egy cikket az gyakran lehet száraz, de ha egy szép grafikon mutatja, akkor jobban értheted (és láthatod). Az Excell vagy az OpenOffice Calc csomagok laikusok számára is könnyen kezelhető vizualizációs eszközöket adnak a kezünkbe. Különösebb matematikai ismeretek nélkül is lehet szép grafikonokat alkotni hogy jobban megértsük adatainkat. Az ingyenesen elérhető, nyílt forráskódú gnuplot ebben segít. Mivel "programozható" nem köt minket az Excell vagy az OO előre megadott kerete. Interaktív, azaz kiadott parancsainkat hatását rögtön láthatjuk. Ezen tulajdonságok pedig lehetővé teszik hogy iteratív módon, kis lépésekben fedezzük fel és a számunkra legértelmesebb módon ábrázoljuk adatainkat.  
  
**A Magyar Webkorpusz**  
A magyar nyelvű web feltérképezését tűzte ki céljául a Magyar Webkorpusz. Minket ebből a szógyakorisági vizsgálat fájlja érdekel. Ez tartalmazza a 10000 leggyakoribb szót az első oszlopban. A második oszlopban az adott szavak előfordulása található. Az egyes elemek gyakoriságuk sorrendjében vannak sorba rendezve.  
  
**gnuplot**  
A gnuplot remekül illeszkedik a Unix rendszerek filozófiájába. Egy dolgot tud, de azt remekül! Ez pedig nem más mint az adatok megjelenítése, Ehhez szimpla szöveges fájlokra van szükségünk (a legtöbb táblázatkezelő tud sima fájlba menteni, ez különösen jó dolog ám). Ezt kihasználva sok más program, pl python vagy R is épít a gnuplot-ra, így nem árt legalább az alapjaival megismerkedned.  
  
Gyors és egyszerű grafikon készítés  
Arra vagyunk kíváncsiak hogy egy egy szó milyen gyakran fordul elő. Ez benne van a fájlban, de nagyon nehéz kibogarászni hogy egymáshoz viszonyítva mennyire gyakran fordul elő pl a 50,000. és a 70,000. elem. Próbáljuk meg ábrázolni s második oszlop (darabszámra hányszor fordultak elő az egyes szavak). Ehhez indítsd el a gnuplot-ot, majd gépeld be a következő parancsot:  
  
> plot "web2.2-fre-sorted.top100k.txt" using ($2) with linespoints  
  
Nem sok értelme van annak amit látunk. Miért? Mert nagy számokkal dolgozunk, amik ilyen léptékkel összeérnek ábrázoláskor. Erre jó a logaritmus. Vegyük az y tengelyt, az előfordulási számokat, logaritmikusra a következő paranccsal:  
  
> set logscale y  
és adjuk ki az első parancsot megint. Ez még mindíg nem az igazi, vegyük az x tengelyt is logaritmikusra  
  
> set logscale x  
  
és adjuk ki a következő parancsot.  
  
> plot "web2.2-fre-sorted.top100k.txt" using ($2) with lines  
  
Itt már nem a pontokat és az azokat összekötő vonalakat (with linespoints), hanem csak a vonalakat (lines) rajzoljuk ki. Ez már szebb, de még egy kicsit tegyük szebbé a "kilógó" és egyedi adatok kizárásával (és adjunk nevet a ).  
  
> plot "web2.2-fre-sorted.top100k.txt" using ($2) title "Szogyakorisag" smooth unique with lines  
  
Ha minden jól ment, akkor a következő ábrát kaptad te is.  
<span class="lost-media">Hiányzó kép: <a href="http://lh6.ggpht.com/_SM9YHwWrX6M/TDC2wku72tI/AAAAAAAAARc/4ksYYHIqBHM/%5BUNSET%5D.png?imgmax=800" rel="nofollow noopener">%5BUNSET%5D.png?imgmax=800</a></span>  
  
**Mit látunk?**  
Az y tengelyen azt láthatjuk hogy hányszor fordul elő egy adott szó, az x-en pedig hogy hanyadik a szó a listánkban. Hogy jobban láthassuk az eredményt, minden tengelyen logaritmust alkalmaztunk, így egy lépéssel nem egyet haladunk előre hanem 10-szeres nagyságrendet. Azt látjuk hogy az első tíz elem gyakorisága 10 a nyolcadikon és 10 a hetediken között van valahol, az első száz elemé pedig 10 a hatodikon körül van. Az első ezer elem után már csak 100,000-nél kevesebb előfordulást látunk, még a lista vége felé drasztikusan esik a gyakoriság.  
  
Tudom hogy nem találtuk fel a spanyolviaszt, de könnyen és egyszerűen elemeztünk egy adathalmazt. Egy kis transzformációval még egyszerűbben értelmezhetővé tettük, így kvázi magáért beszél. Ja és a válasz! Rengeteg szót kellene a helyesírás ellenőrzőhöz adni hogy hiper-szuper legyen, nem éri meg, hiszen igen kis javuláshoz is rengeteg szót kell "belepakolnunk".  
**Ha bővebben érdekel a dolog**  
A [Magyar Webkorpusz](http://mokk.bme.hu/resources/webcorpus/) oldala (sajnos csak angolul találtam meg, ha megvan neked magyarul, kérlek írj).  
[Gnuplot in Action](http://www.manning.com/janert/) (Egy remek könyv erről az egyszerű, de csodálatos programról)
