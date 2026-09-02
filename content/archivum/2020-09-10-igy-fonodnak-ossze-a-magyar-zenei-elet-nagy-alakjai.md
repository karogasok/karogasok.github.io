---
title: "Így fonódnak össze a magyar zenei élet nagy alakjai"
slug: "igy-fonodnak-ossze-a-magyar-zenei-elet-nagy-alakjai"
date: 2020-09-10T14:05:27Z
publishDate: 2020-09-10T14:05:27Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "wordpress"
forras_cim: "Crow Intelligence blog"
canonical: "https://blog.crowintelligence.org/hu/2020/09/10/igy-fonodnak-ossze-a-magyar-zenei-elet-nagy-alakjai/"
regi_cimkek:
  - "dalszövegek"
  - "nyelvészet"
  - "zene"
regi_cimkek_mind:
  - "Blender"
  - "dalszövegek"
  - "hálózatok"
  - "korpusz nyelvészet"
  - "nyelvészet"
  - "zene"
---

A magyar könnyűzenei élet tele van meglepetésekkel. Ki gondolná például, hogy az 1950-es évek óta több mint 10 000 ember neve került fel a dalszerzők listájára? És azt, hogy Szenes Iván minden idők legmeghatározóbb zenei figurája? Miután megvizsgáltuk [a magyar pop slágerek leggyakoribb szavait](https://blog.crowintelligence.org/hu/2020/08/19/hatvan-ev-dalszovegei/), ezúttal arra voltunk kíváncsiak, hogy ki kivel dolgozik együtt legszívesebben a magyar zeneiparban.

Ahhoz, hogy feltérképezhessük, hogy a zenei életben ki kivel került kapcsolatba az évtizedek során, elkészítettük minden idők legnagyobb magyar zenei hálózatát. Hálózatunk a zeneszoveg.hu oldal adatain alapul. Minden előadó oldaláról lescrapeltük az oldalon fellehlető dalait, azok adatlapja alapján pedig az adott dalt jegyző személyeket. Most pedig lássuk az eredményeket!

### Több mint 230 ezer kapcsolat

Adatbázisunk felhasználásával elkészítettük az együttműködési hálózatot, melyben 10618 személy került és közöttük 234105 kapcsolatot találtunk. Hogy könnyebben átlássuk a hálózatot, gerinchálózatot készítettünk [ez alapján a tanulmány alapján](https://arxiv.org/pdf/0904.2389.pdf), az [ebben a repoban](https://github.com/DerwenAI/disparity_filter) található kód modosításával. A gerinchálózatot 3356 személy alkotja, akik között 86545 kapcsolat található. Először a [Louvain algoritmus](https://en.wikipedia.org/wiki/Louvain_modularity) segítségével 28 csoportot találtunk. Nagyon leegyszerűsítve, algoritmusunk csoportként azonosítja azon csomópontokat, melyek között több kapcsolat van egymás között, mint kifelé, más csoportba tartozó csomópontok felé. Az egyes csoportok nagysága nagyon eltérő.

![](/archivum/img/0c86e18294a8225a.png)

### Haver csak haverral dolgozik együtt?!

Ezután [dotplot](https://www.jstor.org/stable/1390697) vizualizációt készítettünk. Az alábbi ábrán, akár csak egy táblázatban, minden oszlop és minden sor egy-egy személyt reprezentál. Ha két személy együtt dolgozott, akkor az adott cella - esetünkben pont- szürke árnyalatú, ennek erőssége pedig a kapcsolat erősségét mutatja. A vizualizáción szembetűnő, hogy nagyon sok a fehér folt, azaz ritka (sparse) mátrixunk van. Ha figyelmesen nézzük az ábrát, látható hogy a bal felső sarokból a jobb alsó sarokba tartó átló mentén négyzetes mintázatokat találunk - ezek a Louvain algoritmus által azonosított csoportok. Egy-egy csoporton belül természetesnek tekinthetjük az együttműködéseket. Az az igazán izgalmas, amikor az átlótól messzire is találunk pontokat, azaz csoportok közötti együttműködéseket. Ilyenek például a feldolgozások, amelyek során verseket és népdalokat dolgoznak fel a dalszerzők.

![](/archivum/img/efe7088f285cba15.png)

Most vizsgáljuk meg azt, hogy a gerinchálózat tagjai milyen [fokszám centralitással](https://en.wikipedia.org/wiki/Centrality#Degree_centrality) rendelkeznek csökkenő sorrendben, tehát a legmagasabb értéküvel kezdünk.

[Google Docs](https://docs.google.com/spreadsheets/d/e/2PACX-1vSONvfGUxeh4NsFM46TdKENMkQ2-dYC2gP3ucHLD9b3l54RU96NUDKdQdXCM8XPxzh0v2Y2dJLPoQ8h/pubhtml?widget=true&headers=false)

A [PageRank](https://en.wikipedia.org/wiki/PageRank) centralitás nem csak azt mutatja, hogy hány szomszédja van egy-egy csomópontnak, hanem a szomszédok környezetét is figyelembe veszi.

[Google Docs](https://docs.google.com/spreadsheets/d/e/2PACX-1vRtpUUKUalqBUi4MqnCShA_e6tSAPQbQViym7asAv5mPRT5Xsnk4Ss3YmkW1wJ0uPWicvzvK5Gh9y3R/pubhtml?widget=true&headers=false)

### Lakkos csizmát visel a babám,  
A beatzenére bokázik ám!

![](/archivum/img/fc3f8fb8bda7cf66.jpg)

A kép forrása [ezen a linken](https://lh3.googleusercontent.com/proxy/7wj2XIGgUzkpiKDVOer0ay5_ba3kPHCAvE_TFVk7eKr1cxq8WXd9pJBTwocp1BdkLLbROPZYc3FBo6t4sikYfy_kK5DcJAtk) érhető el.

Kicsit tovább szűkítve a kört a 300 legmagasabb fokszám centralitású személy hálózatát interaktív vizualizációra tettük. Ezen az ábrán jól látszik, hogy a könnyűzenét kezdetben egy szűk kör uralta, ugyanis az előadók dalait az 50-es években szinte ugyanazok a zeneszerzők és szövegírók jegyezték. G. Dénes György, Szenes Iván és S. Nagy István voltak a zenei élet akkori nagyágyúi. A figyelmes olvasó azt is kiszúrja, hogy József Attila, Juhász Gyula és sok más magyar költő előkelő helyet foglalnak el a szövegírók közötti népszerűségi versenyben, ahogyan a "Ismeretlen, Nem Védett Szerző" és a "Népzene" is.

[Beágyazott tartalom](https://crow-intelligence.github.io/music-networks/)

Most vessünk egy pillantást az általunk vizsgált dalok időbeli eloszlására. A hetvenes években még kevesebb mint 900 dal szövegét érjük el, a nyolcvanas évekből már több mint kétezerét, a kilencvenes és kétezres években pedig hihetetlen robbanást tapasztalhatunk.

![](/archivum/img/f653f860c538a985.png)

### '89: kinyílt a világ, bárkiből lehet zenész

A könnyűzene kisebb-nagyobb buktatók után a hatvanas évek végére hazánkban is megvetette a lábát, a hetvenes évekre pedig teljesen elfogadottá vált. A nyolcvanas években megkezdődött a szocializmus felpuhulása, a rendszerváltás után bárki szabadon zenélhetett, nem kellett már [ORI vizsga](http://www.uvegpest.hu/ori/ori.html) és [véget ért a Hungaroton monopóliuma](https://www.youtube.com/watch?v=M1VpOxoMAKU). A szabályozói gátak lebontása, a zene "gyártás" költségeinek drasztikus csökkenése, a zenefogyasztás csatornáinak változása mind mind abba az irányba hatott, hogy egyre több ember foglalkozhatott és foglalkozhat azóta is könnyűzenével.

[YouTube](https://www.youtube.com/embed/43Em6umUf4M)

Mindezen változások ellenére azok, akik korán jelentek meg a hálózatban, az idő múlásával csak még jobb pozícióra tettek szert. Ezen itt szimplán annyit értünk, hogy egyre több emberrel dolgoztak geyütt, egyre többen dolgozták fel műveiket. Úgy tűnik, hogy Szenes Iván, vagy éppen G. Dénes György alias Zsüti életműve kitörölhetetlen a magyar könnyűzenéből.

### Az adatokról

Az adatbegyűjtéshez és -feldolgozáshoz használt kód elérhető a [githubon](https://github.com/crow-intelligence/music_networks).

Az borítóképet [ezen tanulmány ](https://www.nature.com/articles/s41586-018-0726-6)alapján generáltuk hálózatunkból[ ennek a repository-nak](https://github.com/nimadehmamy/3D-ELI-FUEL) a módosításával. A végső hálózatot [Blender](https://www.blender.org/)-ben rendereltük. A 3D forgatható hálózat megtekinthető alább.

[Beágyazott tartalom](https://sketchfab.com/models/6022c83ab57f41aeaff04dfc72a13404/embed?autospin=0.2&autostart=1&preload=1&ui_controls=1&ui_infos=1&ui_inspector=1&ui_stop=1&ui_watermark=1&ui_watermark_link=1)

[Music Network - fuel graph](https://sketchfab.com/3d-models/music-network-fuel-graph-6022c83ab57f41aeaff04dfc72a13404?utm_medium=embed&utm_source=website&utm_campaign=share-popup) by [zoltan.varju](https://sketchfab.com/zoltan.varju?utm_medium=embed&utm_source=website&utm_campaign=share-popup) on [Sketchfab](https://sketchfab.com?utm_medium=embed&utm_source=website&utm_campaign=share-popup)
