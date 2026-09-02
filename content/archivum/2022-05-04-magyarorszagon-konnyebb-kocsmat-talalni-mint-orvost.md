---
title: "Magyarországon könnyebb kocsmát találni mint orvost"
slug: "magyarorszagon-konnyebb-kocsmat-talalni-mint-orvost"
date: 2022-05-04T13:54:12Z
publishDate: 2022-05-04T13:54:12Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "wordpress"
forras_cim: "Crow Intelligence blog"
canonical: "https://blog.crowintelligence.org/hu/2022/05/04/magyarorszagon-konnyebb-kocsmat-talalni-mint-orvost/"
---

Az [Overpass API ](https://wiki.openstreetmap.org/wiki/Overpass_API)segítségével megnéztük pár kategória területi eloszlását. Úgy tűnik tényleg igaz, hogy minden településen található egy templom és egy kocsma, sajnos az orvosokról és az ipari felhasználású épületekről ugyanez már nem mondható el.

![](/archivum/img/cd4b2b84b681725a.png)

A "doctors" kategória területi eloszlása

![](/archivum/img/57cc84a6bb6d7152.png)

A "building: industrial" kategória területi eloszlása

![](/archivum/img/6841560d0452c292.png)

A "pub" kategória területi eloszlása

![](/archivum/img/06578b83ec0b1a8e.png)

A "place_of_worship" kategória területi eloszlása

Az adatokat az Overpass API-tól az overpy csomaggal kérdeztük le, a megjelenítéshez a numpy, pyproj és bpy csomagokat hívtuk segítségül.
