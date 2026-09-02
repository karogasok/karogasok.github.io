---
title: "Dzsudzsák a Twitteren!"
slug: "dzsudzsak-twitteren"
date: 2011-06-18T11:25:00.004Z
publishDate: 2011-06-18T11:25:00.004Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/06/dzsudzsak-twitteren.html"
regi_cimkek:
  - "python"
  - "twitter"
regi_cimkek_mind:
  - "Dzsudzsák"
  - "python"
  - "twitter"
---

**Először egy népszerű oldal  Twitter feedjét szerettem volna elemezni, jobban mondva hogy mennyi RT-t kap egy-egy hír, de úgy tűnik a magyar felhasználókat nem kapta el a Twitter láz és nem lehet elég adatot találni egy-egy hírre. Így hát váltottam a [nyest.hu](http://www.nyest.hu/) [Hol van az a Mahacskala](http://www.nyest.hu/hirek/hol-van-az-a-mahacskala) cikkétől inspirálva első körben begyűjtöttem pár Dzsudzsákról szóló csiripelést, mivel mostanában sok hír kering(ett) leghíresebb futballistánk körül és a hab a tortán hogy nem csak magyarul! Így a begyűjtött tweeteken sok-sok dolgot bemutathatunk :D Figyelem, ez egy technikai poszt, Python kóddal, pip_/easy_install használatát lehet hogy nem úszod meg.**

**Előzetes megjegyzések**

- Az összes szükséges kódot feltöltöttem egy [github repoba](https://github.com/zolizoli/Dzsudzsak).

- A kódrészleteket minimális módosításokkal Matthew A. Russel, Mining the Social Web könyvének első fejezetéből vettem át (könyvismertetőnket [itt](http://szamitogepesnyelveszet.blogspot.com/2011/02/konyvismerteto-mining-social-web.html) olvashatod).

**A probléma**

Hogyan tudjuk meg hogy egy adott téma hogyan terjedt el a Twitteren. Alapesetben ha érdekele minket hogy Dzsudzsákról milyen tweetek jelentek meg, beírjuk a nevet a Twitter-keresőbe ([http://search.twitter.com/](http://search.twitter.com/)) és valami ilyesmit kapunk:

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-hQRK69mRovM/TfyFB3N_00I/AAAAAAAAAeE/kpHfJitvSnQ/s1600/dzsudzs%25C3%25A1k_twitter_search.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://1.bp.blogspot.com/-hQRK69mRovM/TfyFB3N_00I/AAAAAAAAAeE/kpHfJitvSnQ/s640/dzsudzs%25C3%25A1k_twitter_search.png" width="417" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">searc.twitter.com keresési eredmények</td></tr>
</tbody></table>

Ebből nem derül még ki hogy kikeket retweeteltek a legtöbben és hogyan haladtak a hírek, milyen "körök" csiripeltek Dzsudzsákról és hogyan kapcsolódnak. Most csak erre szűkítjük figyelmünket.

**Kellékek**

Az alábbi könyvtárakra lesz szükséged:

Ha ezek közül hiányzik valamelyik, akkor az [EasyInstall](http://en.wikipedia.org/wiki/EasyInstall) vagy[ pip install](http://www.pip-installer.org/en/latest/index.html) csomagkezelőkkel könnyedén telepítheted (hasonlóak az Ubuntu apt-get csomagkezelőjéhez).

**Keresés a TwitterApi-val, az eredmények elmentése**

Először elindítunk egy keresést Dzsudzsákra ami visszaadja a webes felület eredményeihez. A tweets változóba elraktároztuk a az egyes tweeteket, majd a words-be ezeket szétbontva az egyes szavakat.

Ahogy a komment is mutatja a cPickle segítségével elmetjük a words változóban tárolt adatokra, hogy később is tudjuk használni. Érdemes [megismerkedni behatóbban a cPickle csomaggal](http://docs.python.org/library/pickle.html), mivel segít sok időt megspórolni hiszen nem kell mindig lefutattni az API felé a keresést ha lementjük az eredményeket (ill mivel a pl a TwitterAPI csak az utolsó 6-10 nap eredményeit mutatja, egy longitudinális vizsgálathoz feltétlenül le kell mentenünk az eredményeket mert különben elvesznek!).

**Készítsük el az RT gráfot!**

A következő kóddal kikeressük a "retweetelés nyomait". Ennek egyezményes jele az "RT @XY", ill. a "via @XY" beillesztése a szövegbe. A get_rt_sources függvény kibányássza azokat akiket újracsiripeltek és ennek segítségével vizsgáljuk meg hogy ezeket a "forrásokat" kik ismételték meg, így építjük fel a gráf éleit, amik a forrásra mutatnak.

**Rajzoljuk meg a gráfot!**

A következő kóddal két formátumban elmentjük a gráfot. A write_dot_output() függvény a Graphviz program által értelmezhető formátumra hozza az eredményeket, melynek segítségével egyszerűen generálhatunk majd képet. A write_protovis_output() függvény egy html oldalt generál ami a Protovis js keretrendszerben készített gráfot mutatja (szükséges hozzá a github repoban megtalálható template!!!).

Minden kimenet az out/ könyvtárba kerül! Szükséges hogy a Protovis-t is idemásoljuk, továbbá az itt található dot.dot fájlon futattnunk kell a következő parancsot:

<table border="0" cellpadding="0" cellspacing="0" style="margin-left: 0px; margin-right: 0px; text-align: left;"><tbody>
<tr><td></td>   <td><pre class="textmate-source"><pre class="sunburst">circo -Tpng -Ortgraph dot.dot</pre><pre class="sunburst"></pre></pre></td></tr>
</tbody></table>

És ezt a képet kapjuk.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-QfLZecp_p6c/TfyH-vD1NcI/AAAAAAAAAeM/Jt6qlQ6t3AM/s1600/dot.dot.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="571" src="http://2.bp.blogspot.com/-QfLZecp_p6c/TfyH-vD1NcI/AAAAAAAAAeM/Jt6qlQ6t3AM/s640/dot.dot.png" width="640" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A Graphviz egyszerű gráfot produkál, de ez is megteszi!</td></tr>
</tbody></table>

A Protovis sokkal szebben mutat:

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-B-f_xhf0hjs/TfyIhcZBCNI/AAAAAAAAAeQ/M5rKVVj_FS0/s1600/Protovis+Graph_1308395615993.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="376" src="http://3.bp.blogspot.com/-B-f_xhf0hjs/TfyIhcZBCNI/AAAAAAAAAeQ/M5rKVVj_FS0/s640/Protovis+Graph_1308395615993.png" width="640" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Protovis vizualizáció</td></tr>
</tbody></table>

**Hogyan tovább?**

Az elmentett csiripeken további elemzéseket végezhetünk az nltk segítségével, a következő posztban ezzel foglalkozunk.
