---
title: "Szöveges információ vizualizációja: szógyakoriság"
date: 2013-04-19T16:14:00.001Z
publishDate: 2013-04-19T16:14:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/04/szoveges-informacio-vizualizacioja.html"
regi_cimkek:
  - "vizualizáció"
regi_cimkek_mind:
  - "szófelhő"
  - "vizualizáció"
---

**Az alábbi ábrákat a[ Heti Válasz](http://hetivalasz.hu/vilag/tet-nelkuli-vita-zajlott-magyarorszagrol-62904/) és a [NOL](http://nol.hu/kulfold/az_eb_nem_var_juniusig_az_eljarasokkal) cikkeinek szövegeiből készítettem. Az írások a héten az Európai Parlamentben hazánk kapcsán lezajlott vitáról szólnak. Minden szófelhő szógyakoriságon alapul, a szövegek tisztításon átmentek, de szótövezésen nem. Engem leginkább az érdekel, hogyan használhatók a szófelhők tartalomelemzésre. Ennek nyilván akkor van értelme, ha nagy mennyiségű adatot akarunk áttekinteni, de most jobban érdekel melyik eljárás felhasználóbarát (azaz informatív).**

**Wordle szófelhő**

A [Wordle](http://www.wordle.net/) nagyon szép felhőket generál, de inkább deskriptív és nem ad lehetőséget az összehasonlításra.

Népszabadság cikk

<span class="lost-media">Hiányzó kép: <a href="http://lh4.ggpht.com/-cLduRyU-rR0/UXFpvFOCpzI/AAAAAAAABG0/Tz_dgracphM/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>

Heti Válasz cikk

<span class="lost-media">Hiányzó kép: <a href="http://lh3.ggpht.com/-9HO0CZYjKxc/UXFqKCv9xVI/AAAAAAAABG8/jfWbXMByH4A/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>

**R wordcloud**

A CRAN-on elérhető standard wordcloud package lehetőséget ad arra, hogy összehasonlítsunk szövegeket. Az összehasonlítás alapja a frekvencia, a comparison azt mutatja meg mely szavak gyakorisága nagyobb egy-egy szövegben, a commonality pedig a közös szavakat ábrázolja.

Comparison cloud

<span class="lost-media">Hiányzó kép: <a href="http://lh6.ggpht.com/-p7ZVcUbMEOA/UXFqYcdj7II/AAAAAAAABHE/gHEvFpf5EX8/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>

Commonality cloud

<span class="lost-media">Hiányzó kép: <a href="http://lh6.ggpht.com/-C9ZKgL82DGs/UXFrEf7XSXI/AAAAAAAABHM/7GhfgGeWJCE/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>

**Conway összehasonlító szófelhője**

Conway szerint egy rendes szófelhő térbeli információval is jelez valamit - mégpedig a frequencia eltéréseket a két szövegben.

<span class="lost-media">Hiányzó kép: <a href="http://lh5.ggpht.com/-MWFraMkIclg/UXFrVap-tPI/AAAAAAAABHU/duzEVppi2xw/%25255BUNSET%25255D.png" rel="nofollow noopener">%25255BUNSET%25255D.png</a></span>
