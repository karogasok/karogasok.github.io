---
title: "Kreatív Ruby programozás kezdőknek"
slug: "kreativ-ruby-programozas-kezdoknek"
date: 2010-08-21T15:21:00.001Z
publishDate: 2010-08-21T15:21:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/08/kreativ-ruby-programozas-kezdoknek.html"
regi_cimkek:
  - "kezdő"
  - "tanulás"
regi_cimkek_mind:
  - "Ruby"
  - "_why"
  - "kezdő"
  - "tanulás"
---

**Augusztus 19-én a világ, de legalábbis a Ruby-t ismerő része, ünnepelt. A kiváló hacker [why the lucky stiff](http://en.wikipedia.org/wiki/Why_the_lucky_stiff) pont egy éve tűnt el a virtuális világból, ám hagyatékát soha nem fogjuk elfelejteni, és hála a lelkes közösségnek, elherdálni sem. Hogy ki is volt _why, arról a neten sokat olvashatsz, a lényeg hogy kiválló pedagógiai érzékkel rendelkezett és sokat tett azért hogy a programozás csodás világa könnyen hozzáférhetővé váljon a fiatalok (és lelkes idősebbek) számára.**  
  
Ha szeretnél megismerkedni egy szép, teljesen objektum-orientált szkriptnyelvvel a [Ruby](http://www.ruby-lang.org/en/) remek választás. Könnyű tanulhatósága és megbízhatósága miatt (is) napjainkban nagyon népszerű a webprogramozók körében és az egyik legelterjedtebb framework a Ruby alapú [Ruby on Rails](http://rubyonrails.org/). Persze a könnyű tanulhatóság relatív, kinek? Ezt ismerte fel _why. Míg régen a C64-esek világában amikor nagylemezt és magnókazettás beolvasót használtak az emberek és a BASIC és társai voltak a menő nyelvek (és hazánkban a Süni magazinban két oldalas játékprogramok kódjait olvashattad) még egyszerű volt programozni. Nyilván azért is mert nem hatvanhatezer nyelv közül kellet választani, hanem azt használtad ami éppen adott volt, meg nem hatszáz oldal útmutatót adtak a neten a nyelvhez hanem kb tíz oldalon elfért minden. Szépen kipróbálhattad hogy ha ezt csinálod, ezt és ezt az eredményt kapod és ennyi. Most meg törheted a fejedet hogy akkor itt ez van, de akkor egy hibakezelési blokkot is iderakok ami ugye dob egy ilyen hibát vagy mi a szösz és akkor nekem String kell, de nem olyan sima mert az "immutable", hanem amit tudok dinamikusan változtatni és akkor a legvégén még kell egy statikus változó és őőőőőőő.....  
  
Egy kezdőnek nem ez kell! A másik irányzat "lebutított" nyelvekkel próbálkozott. Azok akik ismerik a Java-t gondolják végig hogy az egyszerű inputot milyen körülményes elérni! Sokan pedagógiai célból csomagokat alkottak hogy leegyszerűsítsék ezt és csak a programozás "logikáját" tanítsák. De így nem egy "élő" és "igazi" nyelvet tanul meg az ember. _why nagy ötlete éppen az hogy egy jó nyelvet kiválasztva, annak egy töredékére koncentrálva és a megfelelő eszközöket megalkotva olyan tudást adhatunk a kezdők kezébe amivel már tudnak haladni. Ha nem kell egy évig azon rágódni hogy milyen típus kezelés is megy végbe akkor a programban, hogyan tanulhatom meg egy IDE használatát, a GUI programozás nem jelent egy szinte teljesen új nyelvet, ha a webprogramozás és az MVC keret tényleg csak egy megközelítési mód és nem megint egy új probléma, akkor a tanuló képes tényleg alkotni, felfedezni. Ha van visszacsatolás, ha képes a tanuló pozitív élményként megélni a programozás folyamatát, akkor gyorsabban fog haladni, bátrabban fedezi fel a számára ismeretlen területeket és sokkal magabiztosabb és kreatívabb lesz.  
  
**Eszközök**

- [HacketyHack](http://hackety-hack.com/)

Egy kezdők számára készített programozási környezet, ami nem csak a programok szerkesztését könnyíti meg, hanem futtatni is lehet benne az elkészült művet.

- [Shoes](http://github.com/shoes/shoes/tree)

A legegyszerűbb és szerintem legintuitívabb GUI amit valaha készítettek. Elég egy kis Ruby tudás, és remek grafikus felülettel ellátott programokat készíthetünk vele. A HacketyHack rendszerbe integrálták a készítők, de önállóan is használható.

- [Camping](http://camping.rubyforge.org/)

A Ruby on Rails kistestvére. Kevesebb mint 4kB a forráskódja mégis használható oldalakat programozhatunk vele. Az [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93View%E2%80%93Controller) filozófiát követi, mégis mellőz minden  olyan elemet ami csak túlbonyolítja a dolgokat egy kezdő számára. A [Heroku](http://heroku.com/) ingyenes tárhelyet is biztosít Camping appjeink számára, feltöltés előtt érdemes elolvasni ezt a kis [tutorialt](http://radiant-sunset-95.heroku.com/how-to-run-camping-2-apps-on-heroku).  
  
**Olvasnivaló**

- [Why's (Poignant) Guide to Ruby](http://mislav.uniqpath.com/poignant-guide/)

Ne egy hagyományos könyvet várj! Nem ez egy posztmodern alkotás, ami (sajnos) nem emészthető mindenkinek. Semmi gond! Ha nem érted, nyugodtan használhatsz más forrást. Gondolom a címéből kiderül hogy a Ruby nyelvbe vezeti be olvasóját.

- [Nobody Knows Shoes  
](http://www.google.com/url?sa=t&source=web&cd=1&ved=0CBcQFjAA&url=http%3A%2F%2Fcloud.github.com%2Fdownloads%2Fshoes%2Fshoes%2Fnks.pdf&rct=j&q=nobody%20knows%20shoes&ei=_ulvTNOcHdGKOJHZqLQL&usg=AFQjCNHstgRnVA-ytn5pqr_i4jgQgPHanQ&cad=rja)

A Poignant Guide stílusában, a Shoes használatába nyújt bevezetést. (A link egy pdf verzióra mutat).  
  
**Összegzés**  
_why hagyatéka rendkívül szerteágazó (pl a Poignant Guide-hoz még zenei CD-t is készített!). Kétségkívül szoftverei nagyobb hatást értek el (nem csak pedagógiai fejlesztései, hanem a Ruby gems-ei is!), stílusa azonban sokak számára érthetetlen. Ezen nem kell csodálkozni és szerintem felesleges vitatkozni, akinek nem tetszik, az olvassa Chris Pine Learn to Program könyvét, vagy annak netes [verzióját](http://pine.fm/LearnToProgram/). A legfontosabb ami ránk maradt a hozzáállás. A programozás világát sokan azért szerették meg mert nyílt, demokratikus és meritokratikus egyben. Bárki elkezdheti a tanulást viszonylag kis befektetéssel, a neten formálódó közösségek nyíltak és segítőkészek és mindenkit érdemei szerint ismernek el. Azon lehet vitatkozni hogy tényleg veszélyben vannak-e ezek az alapértékek, de nem árt ha megjegyezzük bizony ezek egy nyílt és demokratikus társadalom jellemzői is. A programozással nem csak szakmát tanulhat az ember, hanem kreatív módon kifejezheti magát, megtanul másokkal együttműködni és elviselni a kritikát.  
  
A számítógépes nyelvészet és digitális bölcsészet iránt érdeklődők számára mindenképp hasznos tapasztalat a Ruby elsajátítása, különösen az objektum orientált paradigma alapjainak megismerése. Sajnos azonban a közösség a nyelvészeti munkákhoz használatos könyvtárak és csomagok fejlesztésében nem jeleskedik és kezdőknek nagyon nehéz maguknak megírni ezeket, ezért ajánlatos az alapok elsajátítása után az nltk-ra átnyergelni.
