---
title: "A benchmark nem a képességet méri, hanem a benchmarkot"
date: 2026-08-30T07:00:00+02:00
publishDate: 2026-08-30T07:00:00+02:00
author: "Varjú Zoltán"
forras: "https://arxiv.org/abs/2405.01470"
forras_cim: "Lessons from the Trenches on Reproducible Evaluation of Language Models"
tags: ["llm-kiertekeles", "nyilt-forras"]
draft: false
---

Az EleutherAI csapata a saját kiértékelő könyvtáruk három évének tapasztalatát
írta össze. A dolgozat nem új mérőszámot javasol, hanem azt dokumentálja,
mennyire törékeny az, amit ma egy modell „eredményének" nevezünk: ugyanaz a
feladat, ugyanaz a modell, más prompt-formázás vagy más normalizálás, és a
pontszám akár tíz százalékponttal is elmozdul. A szerzők végigveszik, hogy a
publikált számok összehasonlíthatatlanok, ha a kiértékelő kód és a pontos
prompt nem utazik velük együtt.

Ez az a fajta írás, amit ritkán idéznek, mert nem állít semmi izgalmasat. Pedig
a következménye elég kellemetlen: a legtöbb modellösszehasonlítás, amit
sajtóhírben látunk, két különböző mérés két különböző eredményét teszi egymás
mellé. Nem arról van szó, hogy a benchmarkok „nem elég jók" — arról, hogy a
mérési eljárás maga is paraméter, és ha nincs rögzítve, akkor nincs mérés sem,
csak egy szám. A dolgozat legerősebb mondata az, hogy a reprodukálhatóság nem
utólagos ellenőrzés kérdése, hanem annak eldöntése, hogy egyáltalán mit
állítottunk.

Itt kapcsolódik ahhoz, amivel ez a napló legtöbbször foglalkozik: mit tudunk
arról, hogy mit tudnak a gépek. Ha egy képességről szóló állítás egy nem
rögzített eljárás kimenete, akkor az állítás nem a modellről szól, hanem a
mérésről. A kérdés innentől nem az, hogy „tud-e", hanem hogy ki döntötte el, mit
jelent a tudni ebben az esetben — és leírta-e valahol.
