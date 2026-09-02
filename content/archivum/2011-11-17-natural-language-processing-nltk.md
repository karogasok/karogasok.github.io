---
title: "scikit-learn: a gépi tanulás nltk-ja"
slug: "natural-language-processing-nltk"
date: 2011-11-17T19:39:00.002Z
publishDate: 2011-11-17T19:39:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/11/natural-language-processing-nltk.html"
regi_cimkek:
  - "gépi tanulás"
  - "python"
regi_cimkek_mind:
  - "gépi tanulás"
  - "python"
  - "scikit-learn"
---

**A [Natural Language Processing](http://www.nltk.org/) (nltk) keretrendszer a nem csak számítógépes nyelvészt iránt érdeklődők tömegeit vezette/vezeti be a szakma rejtelmeibe, hanem már a "való világban", üzleti alkalmazásokba építve is bizonyított. A nyílt forráskódú projektekre leselkedő veszélyt - hogy nem alakul ki a lelkes önkéntesek köre - elkerülte, és az "alapító atyáknak" hála egy jó minőségű, immár több nyelvre is fordított, [szabadon hozzáférhető](http://www.nltk.org/book) könyv vezeti be a szakma rejtelmeibe a nagyérdeműt. A [scikit-learn](http://scikit-learn.org/stable/) valami hasonlóvá próbál kinőni a gépi tanulás területén - remélem így már érthető a cím :D**

[]()

> Scikit-learn harnesses this rich environment to provide state-of-the-art implementations of many well known machine learning algorithms, while maintaining an easy-to-use interface tightly integrated with the Python language. [1]

A scikit-learn csomag első sorban azok számára készült akik más területekről érkeznek a gépi tanulás problémáihoz; ezek általában fizikusok, biológusok, társadalomtudósok, és nyelvészek, azaz nem számítástudománnyal foglalkoznak. Ahogy a nem rég megjelent [Science Code Manifesto](http://sciencecodemanifesto.org/) is fogalmazott, a programozás vagy szebb névvel kumputációs modellezés a tudományos munka részévé vált - igen, cakk-pakk a TUDOMÁNY praxisa megköveteli hogy programokba öntsük modelljeinket.  Ez azzal jár hogy maga a programozás eszköz (és nem cél, vagy maga végeredmény) sokak számára. Ebből a szempontból a Python programozási nyelv választása telitalálat, nagyon jól dokumentált, kifejezetten kezdőbarát.

Természetes választás lehetne még az R nyelv, hiszen sok [gépi tanulással kapcsolatos csomag áll](http://cran.r-project.org/web/views/MachineLearning.html) a felhasználók rendelkezésére, valamint a korpusznyelvészek és pszicholingvisták körében kávzi lingua franca, azonban elsajátítása jóval több időt vesz igénybe, nem beszélve erről hogy az eltérő csomagok nem annyira egységesek mint a scikit-learn.

A különféle Java csomagok (WEKA, MALLET, stb.) sajnos nem jelentenek megoldást, nem csak azért viszonylag nehéz elsajátítani a nyelvet, hanem úgynevezett dizájn megfontolások miatt nehézkesebb az ilyen eszközök használata. A Java csomagok általában öröklődés útján kerülnek bevetésre, ezért használatuk során sok "felesleges" kódot kell írnunk. A scikit-learn ellenben az ún. interfészekre esküszik, ami a kezdők számára sokkal barátságosabb modell, hiszen egyszerűbben "mixelhetik" össze egy objektumba az adatokat és a rajtuk végzett műveleteket.

Az egyszerűségnek sajnos ára van. A csomag kis és közepes nagyságú adatokon muzsikál jól. Teljesítménye gondos kezek segítségével növelhető, de a kezdők és nem vér profi programozók számára ezek már barokkos díszítőelemek, nem biztos hogy könnyen megoldják. Nem kapunk kézhez egy könyvet a scikit-learn-nel, pláne nem olyat mint az nltk book. User Guide néven alatt fut valami könyvhöz hasonló de ez gyakran hiányos még, a példák és magyarázatok néha mint ha félbeszakadnának. Azonban józan ésszel, némi Python és gépi tanulási (statisztikai) háttérismerettel lehetővé teszi hogy kipróbáljuk, vagy saját munkákban is alkalmazzuk az egyes eljárásokat.

[1] [Scikit-learn: Machine Learning in Python](http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html), Pedregosa *et al.*, JMLR 12, pp. 2825−2830, 2011.
