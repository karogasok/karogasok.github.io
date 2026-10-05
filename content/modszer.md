---
title: "Hogyan készülnek a témák és a kulcsszavak?"
url: "/modszer/"
---

Az írások mellett háromféle jelölés áll: témák, kulcsszavak és címkék. Az első kettő gépi,
a harmadik kézi. Ez az oldal leírja, hogyan készülnek, és mire nem jók.

## Témák

A témalista tizenöt tételből áll, és én gondozom. Egy témamodellből indult, amelyet a
saját írásaimon futtattam; a javaslataiból átnevezéssel, összevonással és néhány új téma
felvételével lett a mostani lista. A műfajokat — lapszemle, meetup-meghívók, a blog
életéről szóló bejegyzések — kivettem, mert azok nem témák.

Minden témát legalább három saját írásom határoz meg, ezek a téma magjai. A besorolást egy
nyelvmodell végzi: minden írást egy számsorrá alakít, és megnézi, mennyire hasonlít az
egyes témák magjainak átlagához. Egy írás akkor kap meg egy témát, ha a hasonlóság eléri a
küszöböt, és legfeljebb három témát kaphat. Ha egyik küszöböt sem éri el, nem kap témát;
ez becsületesebb, mint egy erőltetett besorolás. A heti lapszemlék linkgyűjtemények, ezért
nem kapnak témát.

A küszöböket a régi, kézzel adott címkéim alapján hangoltam be, aztán rögzítettem. Egy új
írás ezért soha nem mozdítja el a régieket.

**Mennyire jó?** Mielőtt az archívumot újrasoroltam, az új módszert olyan írásokon mértem
le, amelyeket a hangolás nem látott: a Kereső Világ 182 bejegyzésén, a blog.hu-n kapott
címkéikkel összevetve. Az egyezés (BCubed F) 0,26-ról 0,35-re javult; a javulás 95%-os
konfidenciaintervalluma +0,03 és +0,12 közé esik. Ez messze nem tökéletes — a régi címkék
sem következetesek —, de mérhetően jobb a korábbinál. A Digitális bölcsészet témát
e mérés után vettem fel, később pedig néhány téma magjai közül kivettem a
vendégposztokat, saját írásokra cserélve őket. A küszöbökhöz egyik esetben sem
nyúltam, és a hangolási adatokon az egyezés nem változott.

## Kulcsszavak

Minden írás mellett legfeljebb öt kulcsszó áll. Ezek azok a szavak, amelyeket az adott
írás a többinél jóval gyakrabban használ. A szövegeket az emtsv bontja szótövekre, így a
*metaforát*, a *metaforák* és a *metaforáról* egy szónak számít; a gyakoriságkülönbséget a
keyflux méri. Egy szónak legalább kétszer kell szerepelnie az írásban.

## Címkék

A címkéket kézzel adom. Ezek szerkesztői döntések, nem gépi kivonatok.

## Mire nem jó

- A besorolás a szöveg egészét nézi, nem a gondolatmenetét. Egy írás, amely sokat idéz egy
  másik területről, oda is kerülhet.
- Rövid szövegeknél kevés a támpont, ezért a rövid bevezetők egy része nem kap témát.
  Jelenleg 818 tételből 219 áll téma nélkül.
- Egy írás néha gyengén illeszkedő második vagy harmadik témát is kap.
- A kulcsszavak gépi szótövek. Néha csonka vagy furcsa alakot hoznak, főleg angol
  szavaknál, és a legjellemzőbb szót adják, nem feltétlenül a legfontosabb fogalmat.

## A projektről

- **Adatok:** a saját írásaim 2010-től, valamint a Kereső Világ, a Média és a Máshol
  oldalak tételei.
- **Témák:** bge-m3 nyelvmodell (MIT-licenc), a vektorok középre igazítása, koszinusz-hasonlóság
  a magok átlagához, rögzített küszöbökkel. A kiinduló témamodell: BERTopic.
- **Kulcsszavak:** emtsv (LGPL-3.0) szótövek, keyflux (MIT-licenc) kulcsszóerősség. A
  keyflux a Crow Intelligence csomagja.
- **Eszközök:** Python, Hugo.
- **Utolsó újrabesorolás:** 2026. szeptember 28.
- **Kód és mérések:** az oldal [forrásában](https://github.com/karogasok/karogasok.github.io),
  az `analysis/` könyvtárban.
- **Licenc:** a tartalom [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.hu).
