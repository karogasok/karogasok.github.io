---
title: "Mire jó a probabilisztikus programozás?"
date: 2013-04-10T07:56:00.001Z
publishDate: 2013-04-10T07:56:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2013/04/mire-jo-probabilisztikus-programozas.html"
regi_cimkek_mind:
  - "Noah D Goodman"
  - "kognitív tudomány"
  - "probabilisztikus programozás"
---

> *"No man is an island,*  
> *Entire of itself.*  
> *Each is a piece of the continent,*  
> *A part of the main.*  
> *If a clod be washed away by the sea,*  
> *Europe is the less.*  
> *As well as if a promontory were.*  
> *As well as if a manor of thine own*  
> *Or of thine friend's were.*  
> *Each man's death diminishes me,*  
> *For I am involved in mankind.*  
> *Therefore, send not to know*  
> *For whom the bell tolls,*  
> *It tolls for thee. "*

> (John Donne)

**Manapság egyre elterjedtebb az ún. dinamikus rendszerek vizsgálata. A logikában ez a dinamikus episztemikus logikát jelenti, amit van Benthem [One is a Lonely Number: on the logic of communication](http://staff.science.uva.nl/~johan/Muenster.pdf) c. tanulmányában gyönyörűen mutat be. Másrészt itt van ez a big data és sokan úgy gondolják, az adatok mindent megoldanak hiszen korlátlanul gyűjthetjük őket. Anderson [The End of Theory](http://www.wired.com/science/discoveries/magazine/16-07/pb_theory) című cikke akár meggyőző is lehetne, de vegyük észre, minden adat begyűjtése tkp. egy omnipotens állapot elérhetőségét jelenti - így csöbörből vödörbe kerülünk.**

A kognitív modellezés (ami ma szinte kizárólag bayesiánus modellezést jelent) területén ismeretes mennyire sok gond akadhat azokkal a fránya adatokkal. Minden nyelvész ismeri a mantrát, poverty of stimulus, change over time stb. [Noah D. Goodman](http://www.stanford.edu/~ngoodman/) az ún. generatív modellek (nem keverendők össze a generatív grammatikákkal!!!) segítségével igen ötletes megoldást talált arra, miképp lehet a dinamikus folyamatokat (pl. társas-kognitív viselkedés, társas nyelvhasználat stb) szimulálni:

> *Is language understanding a special case of social cognition? To help evaluate this view, we can formalize it as the rational speech-act theory: Listeners assume that speakers choose their utterances approximately optimally, and listeners interpret an utterance by using Bayesian inference to “invert” this model of the speaker. We apply this framework to model scalar implicature (“some” implies “not all,” and “N” implies “not more than N”). This model predicts an interaction between the speaker’s knowledge state and the listener’s interpretation. We test these predictions in two experiments and ﬁnd good ﬁt between model predictions and human judgments.* ([Knowledge and Implicature: Modeling Language Understanding as Social Cognition](http://www.stanford.edu/~ngoodman/papers/GS-TopiCS-2013.pdf))

És mindehhez probabilisztikus programozást használ Goodman. Hogy miért?

> *Probabilities describe degrees of belief, and probabilistic inference describes rational reasoning under uncertainty. It is no wonder, then, that probabilistic models have exploded onto the scene of modern artiﬁcial intelligence, cognitive science, and applied statistics: these are all sciences of inference under uncertainty. But as probabilistic models have become more sophisticated, the tools to formally describe them and to perform probabilistic inference have wrestled with new complexity. Just as programming beyond the simplest algorithms requires tools for abstraction and composition, complex probabilistic modeling requires new progress in model representation—probabilistic programming languages. These languages provide compositional means for describing complex probability distributions; implementations of these languages provide generic inference engines: tools for performing efﬁcient probabilistic inference over an arbitrary program.* ([The Principles and Practice of Probabilistic Programming](http://www.stanford.edu/~ngoodman/papers/POPL2013-abstract.pdf))
