---
title: "The Life of a Computational Linguits V - Interview with Vincenzo Pallotta"
date: 2011-01-17T20:19:00Z
publishDate: 2011-01-17T20:19:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/01/life-of-computational-linguits-v.html"
regi_cimkek:
  - "computational linguistics"
  - "interview"
regi_cimkek_mind:
  - "computational linguistics"
  - "interview"
---

**After a long hiatus we continue our series. We interviewed [Vincenzo Pallotta](http://bit.ly/gHyodz) who is a research professor at the [Webster University, Geneva](http://bit.ly/fN3tpj), a core group member at [ThinkServices](http://bit.ly/hE8UpK), and co-founder and CTO at [ InterAnalytics](http://bit.ly/h23aPi). Vincenzo is a unique mix of strong scholarly interest and a vein for business with a broad interest spanning from theoretical computer science to human computer interaction and computational linguistics.**  
  
  
  
  
  
**Please tell us something about yourself.**  
  
 I am Italian and now living in Switzerland for 13 years. I always had two great passions: Music and Technology. When I was kid my preferred toys were a toy piano and a mini lab for building electronic circuits. Eventually, I had to drop the musician career and moved to computers. I bought my first micro-computer, a [Sinclair ZX80](http://bit.ly/ftV6VN) when I was 15 years old and everything developed from that purchase.  
  
**According to your [LinkedIn profile](http://linkd.in/ha4XXs), you re-oriented your career towards research after a couple of years spent in the industry, you completed a PhD at [EPFL](http://bit.ly/eq0FQe) and lectured at top-notch Swiss unis,  now you have foot in both academia and business. Is there any barrier between the two fields?**  
  
 Yes, and now re-orienting again towards industry, but as an entrepreneur! :-) There is still a barrier between the two worlds, unfortunately, at least here in Europe. Things are changing, but very slowly. There are initiatives by higher-education institutions to enable technology transfer with industry, but these are too weak at the moment. What is really missing is a "generous" support to startups in their prototyping phases, regardless of the market perspectives.  
  
 In Switzerland (and in Europe) investors (public and private) tend to be very risk-avoiding and thus one has to provide a robust business plan right from the beginning of a venture. This is not feasible for a young startup that wants to innovate. Besides, innovation is not possible in universities (probably, with the exception of the [ETHZ](http://bit.ly/dJl5SM) and EPFL) as the funds for the projects are limited and oriented to academic results (i.e. publications).  
  
 Making a (obvious) comparison, Google started as a student's idea and went to a global scale only when Stanford provided an infrastructure for early deployment. I presume that Google was not the unique project that has been supported by Stanford even if it is the one which grew to an extraordinary scale.  
  
**In your [PhD thesis](http://bit.ly/exQacw), you characterize a new approach called cognitive language engineering. What does it mean? How does it relate to cognitive engineering? How do you put it into work in 'real life'?**  
  
 With Cognitive Language Engineering I meant introducing cognitive aspects in language engineering (not the other way around). This means that analysis of language needs to be mapped into representations of mental states of speakers and listeners if we want to achieve natural language understanding.  
  
 I developed (better assembled) a toolbox to help language engineers to build language analysis applications enhanced with cognitive aspects. For instance, in Dialog Management (e.g. those systems that let you to book a flight over a telephone), this approach would allow designers to build better systems by modeling the client's mental state and how it changes over the conversation. An important issue in this modeling is being able to perform inference and reasoning for guessing what the current mental state could be by looking at speaker's utterances and the domain's context.  
  
**With InterAnalytics, you are involved in the "data boom". What are you doing there and what can we know about your natural language understanding system that "moving standard text mining beyond simple words or even sentences to a full semantic understanding of interaction text thus revolutionizing (business) analytics."?**  
  
 In this project, we are leveraging a natural language understanding technology to cope with the issue that when analyzing language data from conversation, context is larger than a single sentence. In conversations one has to understand the whole dialog in order to make sense of single contributions. Moreover, people don't just express opinions about a topic, but they interact with each others. This interaction has a meaning that needs to be discovered.  
  
 Nowadays, most of Social Media analytics application focus on what is called "[Sentiment Analysis](http://bit.ly/9wrvGs)". Basically, each sentence is classified as being positive, negative or neutral with respect to a key search term. This is done regardless of any relationship between the sentences and the participants in a conversation (e.g. a Twitter, Facebook or Reddit thread). This naive approach leads very often to inaccurate results and most of all, it does not provide a wider scope view of a conversation around a topic.  
  
 What we are able to highlight from a conversation goes beyond accurate Sentiment analysis. We can provide an overview of how sentiment evolves during a conversation, if there is a consensus or a dissent between the participants, and eventually to track back where the issue lies if a topic gets a negative sentiment.  
  
**As a computational linguist, what do you think about the field; is it a branch of linguistics, a sub-discipline of computer science or is it a science on its own?**  
  
 There are different views on this aspect. I thing it is both a branch of linguistics and a sub-field of computer science. But taking one of the two perspectives means adopting a different methodological approach. As a branch of linguistics, computational linguists should focus on how to use computational techniques to build theories and models of language. As a sub-field of computer science, they should be more pragmatic and exploit knowledge of language competence to build systems that process and possibly understand natural language for specific purposes (e.g. information retrieval and extraction, automatic translation, speech recognition).  
  
 The two perspective are often blurred, but I guess that a distinction makes still sense. However, I don't think it is a science on its own.  
  
 Actually, there is a third aspect of computational linguistics which is somehow neglected by mainstream computational linguistics: the cognitive aspects of language production and understanding. This is the work made by the Berkeley's group in cognitive linguistics (by George Lakoff, Charles Fillmore and others). I had the chance to meet and work with this group while my visit at[ ICSI Berkeley](http://bit.ly/eUoVrU). I suggest this book about the topic: [http://www.m2mbook.org/](http://www.m2mbook.org/)  
  
**What do you think, what are the 'hot topics' in computational linguistics that's worth studying for the youngsters and will be used in the systems of the near future?**  
  
 Mainstream Computational Linguistics is focused on statistical approaches to natural language processing. I personally think that these methods are very effective but they are now all facing the obvious shortcomings of supervised learning. First they need huge amount data to be collected and annotated in order to train models for classifiers. This is not always possible and it is resource consuming. Second, if the training is done on one language genre, it will be hardly re-usable on other genre. Another issue is that the more sophisticated the analysis is needed, the less adequate these methods are. This means that for semantic and pragmatic language understanding these methods are practically useless.  
  
 Nowadays, there is a wealth of semantic data around (e.g. DBpedia and all the Open Linked Data initiative) which would provide the necessary knowledge to perform semantic and pragmatic analysis. What are missing are tractable reasoning methods and ways of mapping surface analysis (e.g. syntactic parsing) to semantic and pragmatic knowledge.  
  
 Applications such as high-quality machine translation, abstractive summarization and dialog system will necessary require this level of analysis.  
  
**In your opinion, what should a computational linguist's toolbox contain?**  
  
 A computational linguist should be first aware that not everything can be learned from data. They should of course master statistical machine learning techniques, but also be comfortable with knowledge-based techniques (and related language theories). Moreover, in Machine Learning, feature engineering is a not trivial task and best results are only obtained by a careful selection of linguistic features from analyzed data (e.g. Part of Speech labels, syntactic structures).  
  
 Hence a good computational linguist's toolbox should be a balanced mixture of data and knowledge driven methods. There are many textbooks on data-driven methods (e.g. Jurafsky&Martin, Manning&Schultze), but very few on knowledge-based ones. I suggest a nice work of my friend and colleague Prof. Rodolfo Delmonte (also co-founder of Interanalytics): [https://www.novapublishers.com/catalog/advanced_search_result.php?keywords=Rodolfo+Delmonte&osCsid=&x=0&y=0](https://www.novapublishers.com/catalog/advanced_search_result.php?keywords=Rodolfo+Delmonte&osCsid=&x=0&y=0)  
  
**As a practising teacher what kind of route would you advise for youngsters wishing to start a career in computational linguistics; start a computer science degree programme and catch up on linguistics parallel or later, enroll in a linguistics programme where there is some compling in the curriculum or look for specialist programmes?**  
  
 It much depends on what orientation one wants to go. If one wants to study language with computational tools (e.g. corpus linguistics) then I would suggest studying linguistics in a language department and have some side courses in computation. If one wants to build NLP systems, I would definitely go for a major in computer science with a minor or specialization in linguistics.
