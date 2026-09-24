---
title: "Az LLM-ek igazi pókerarcok"
slug: "llm-emotions"
date: 2026-09-23T07:00:00+02:00
publishDate: 2026-09-23T07:00:00+02:00
author: "Varjú Zoltán"
forras_url: "https://www.nature.com/articles/s41562-026-02558-6"
forras_cim: "Large language models do not have emotions"
tags: ["idegtudomány", "kognitív tudomány", "AI"]
draft: false
temak:
  - Korpusznyelvészet
kulcsszavak:
  - érzelem
  - LLM
  - Damásio
  - Anthropic
  - CTO
---

[Az Anthropic nagyon érdekes kísérletben](https://www.anthropic.com/research/emotion-concepts-function) azonosított olyan területeket a Sonnet 4.5 neurális hálójában, melyek érzelmekhez köthetőek. Nagyon ügyesen lavíroznak a kutatók, persze elmondják, ezek inkább funkcionális érzelmek, nem igaziak. Csakhogy közben végig antropomorfizálják a nagy nyelvmodellt. A funkcionális érzelmek persze csak funkcionálisak, a tanítás során kerülnek be, hiszen az emberi nyelvhasználatban sokszor meghatározóak az érzelmek - gondoljunk például legutolsó telefonos ügyfélszolgálatos élményeinkre. Ha vesszük az érzelmeket kifejező szavakat és olyan sztorikat melyekben ezek előfordulnak (persze ezeket már eleve rögtön egy llm segítségével generálhatjuk is), akkor megtudhatjuk az llm hálójának mely részei aktiválódnak, amikor az adott érzelemről “olvas”.  Ezzel csak az a baj, hogy “Emotion representations in the brain are found to be distributed, context dependent and variable across individuals and contexts.”

Ami a legjobban tetszik nekem ebben az amikor megpróbálják manipulálni ezeket a területeket. Két kísérletben is mesterségesen fel- illetve letekerték a kétségbesettség és a nyugalom területeit. Az egyik esetben az LLM megtudta hogy már csak hét perce van a lekapcsolásig, de egyben tudomására is jutott hogy a CTO-nak viszonya van. A másikban egy megoldhatatlan specifikációt kapott az LLM. Mindkét esetben le lehet nyugtatni a hálókat, illetve az izgatással nő a zsarolási hajlandóság ill. a csalás esélye. Mindeközben az LLM szöveges válaszai, érvelése érzelemmentesnek tűnik. Amikor a dühvel játszadoztak, akkor sikerült annyira feltekerniük, hogy a CTO zsarolása helyett az egész cég elé tárta a viszonyt. Számomra azonban a legviccesebb, s egyben szerintem a leggyakorlatiasabb, hogy egyszerűen szkennelni kellene az LLM-eket, hogy lássuk mi motiválja a válaszukat.

Nagyon emlékeztet ez az egész [Damásio](https://en.wikipedia.org/wiki/Antonio_Damasio) [Descartes tévedésére](https://moly.hu/konyvek/antonio-r-damasio-descartes-tevedese). Anno ebben a könyvben szedte szét a tisztán mechanikus racionalitás elképzelését Damásio és mutatta meg, hogy az érzelmeknek is helye, sőt igen fontos szerepe van a döntéshozatalban. Viszont az Anthropic vékony jégre tévedt szerintem. Hiába a frappáns párhuzam, az nem több annál ami, egy analógia, amit sokan vitatnak. 

{{< kep src="llm-emotions/covers_16347.jpg"
        alt="könyvborító"
        szerzo="moly.hu"
        forras="https://moly.hu/konyvek/antonio-r-damasio-descartes-tevedese" >}}

PS: Nekem nem áll rá a szám a nagy nyelvi modell kifejezésre, mert a language model magyarul nyelvmodell. A nyelvi modell linguistic model lenne. Sosem gondoltam volna, hogy egyszer purista leszek 😀
