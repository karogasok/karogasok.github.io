---
title: "On (Computational) Corpus Linguistics - an interview with Stefan Th. Gries"
date: 2010-11-02T05:56:00.003Z
publishDate: 2010-11-02T05:56:00.003Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2010/11/on-computational-corpus-linguistics.html"
regi_cimkek:
  - "interview"
  - "linguistics"
regi_cimkek_mind:
  - "corpus linguistics"
  - "interview"
  - "linguistics"
---

**This week we interviewed [Stefan Th. Gries](http://www.linguistics.ucsb.edu/faculty/stgries/) from University of California, Santa Barbara. He is the author of [Quantitative Corpus Linguistics with R: A Practical Introduction](http://www.amazon.com/Quantitative-Corpus-Linguistics-Practical-Introduction/dp/0415962706) and [Statistics for Linguistics with R: A Practical Introduction](http://www.amazon.com/Statistics-Linguistics-Practical-Introduction-Textbook/dp/3110205653/ref=pd_sim_b_4), two extremely popular books among linguists and students of linguistics.**  
  
  
  
**Számítógépes nyelvészet: Please tell us something about yourself.**  
 Stefan Th Gries: Uh ... there is nothing interesting to say about me that's not on my website. Here are three arbitrary factoids:

-  I was in the German army for four years;

-  I was a cab driver for a few years and worked as a self-employed  
 consultant in communication and sales skills for companies;

-  I am a trekkie.

What else could there possibly be to say ...  
**Which is your favorite linguistic theory and why?**  
 My favorite 'theory' is a cognitive-linguistic exemplar-based approach. The main idea of this approach is that speakers/listeners encounter (aspects of) usage events - i.e., saying/hearing/reading/writing something - and store these tokens/exemplars into a multidimensional memory space / network such that the location of that token is determined by the values it exhibits in the dimensions of the memory space. This is probably easiest to conceptualize for phonemes, because many of the dimensions with regard to which phonemes are described are inherently quantitative anyway, such as their formant frequencies: a vowel sound will be placed at a location in the multidimensional space that corresponds to its perceived F1, F2, etc. frequencies. Once a speaker hears a new stimulus - such as another vowel - that stimulus will also be placed into the multidimensional space accordingly and will be classified by the speaker as an instance of that stored vowel that is most similar to the incoming stimulus. Note that this does not imply that speakers/listeners remember each exemplar and everything about each exemplar: (aspects of) memories of individual exemplars may still not be accessible because they may decay (aka be forgotten) or be subject to generalization/abstraction as well as reconstruction or they also may never make it into long-term memory. Also, this approach is not restricted to quantitative dimensions, such as formant frequencies. For example, in the case of words and constructions, it means that constructional slots (for, say, subjects) are associated with distributions of words that occur in these slots and that in turn make up a (usually semantically fairly coherent) category. For example, for X killed Y it is immediately clear that the Y slot will be filled with animate entities, while the X slot can also be inanimate. The crucial point is in fact that the distributional aspects of exemplars that can be remembered are numerous and involve phonetic, phonological, prosodic, morphemic, lexical (co-)occurrence as well as extra-linguistic / contextual aspects including utterance context, sociolinguistic speaker factors, and information concerning register / mode.  
  
 Why is this my favorite approach? Basically because it

-  is non-modular (it doesn't assume a sharp separation between  
 linguistic and other knowledge);

-  involves less rather than more innate structure (and thus places  
 much emphasis on cognitive aspects and learning);

-  has a pronounced learning and categorization component to it;

-  is able to accommodate variation/graded effects; ...

all in a very elegant manner.  
**You criticized the recent linguistic curriculum because it doesn't reflect to the recent shift from rule-based generative/logical approaches to probabilistic (and data-intensive) theories. What should that new curriculum contain? How does it differ from computational linguistics?**  
 Since I think corpus linguistics is a methodological approach or commitment, I think corpus linguists need a large amount of methodological knowledge. As I have asked elsewhere,

-  Why is it that we corpus linguists look at something (language) that  
 is completely based on distributional/frequency-based probabilistic  
 data and just as complex as what psychologists, psycholinguists,  
 cognitive scientists sociologists, etc. look at, but most of our  
 curricula do not contain even a single course on statistical methods  
 (while psychologists etc. regularly have two to three basic and one or  
 two advanced courses on such methods)? ([See my own attempt at advancing  
 the field](http://tinyurl.com/StatForLingWithR))

-  And why is it that we corpus linguists often must retrieve complex  
 patterns from gigabytes of messy data in various encodings and forms  
 of organization, but most of our curricula do not contain even a  
 single course on basic programming skills or relational databases  
 (while psychologists, computational linguists, cognitive scientists  
 etc. devote years to acquiring the required methodological skills)?  
 ([See my own attempt at advancing the field:  
](http://tinyurl.com/QuantCorpLingWithR))

I think, as corpus linguists we need **programming skills** (to get the data out of corpora), **statistical skills** (to analyze the data with regard to the patterns we expect or that they exhibit), **linguistic knowledge** (to guide the statistical analysis and its interpretation), and **a (psycho)linguistic theory or framework** (within which we interpret the results). I will touch upon many of these things and also the relation to computational linguistics and NLP below. In particular, it is ABSOLUTELY essential that we develop this knowledge with tools that don't imprison our analytic minds. As I mentioned elsewhere, I know corpus linguists whose corpus-linguistic skills are defined by what WordSmith Tools (or AntConc, or KwicFinder, or  
 Concgram, etc.) or, even worse, their web interface can do - if you take whatever program they use away from them, they can't pursue their  
 corpus studies anymore. At the risk of redundantly mentioning the obvious, let me make even clearer what this means: If these corpus  
 linguists' program(s) can't lemmatize, neither can they. If their program(s) can't do regular expressions, neither can they. If their program(s) can't do keywords for bigrams, neither can they. And if their program(s) can't do collocational or other statistics, neither can they, etc. etc. Note, by the way, that I am neither saying nor believing that these corpus linguists have not made or can't make important contributions to linguistics in general and/or corpus linguistics in particular - they can and they have! But I am blaming part of the lack of methodological skills on the fact that some corpus  
 linguists just go the path of least resistance and as long as, say, Mike Scott's very comprehensive program suite makes many things available, think, why do more and why require students to do more …  
 From my own experience, I know at least two reasons why one should do more: First, I believe that a scientist's analytical skills must not be dictated by limited and commercial software, and as useful each of the above applications is, each is limited:

-  limited in terms of availability: several of the programs are only  
 available for one operating system and many programs are commercial  
 and, thus, not available to researchers from less affluent  
 affiliations/countries;

-  limited in terms of functionality: several of the programs compute  
 collocational statistics, but provide only one or two of the available  
 measures of collocational strength; or they compute collocational  
 statistics, but only for words, not for bigrams, trigrams, etc.; or  
 they cannot handle Unicode, corpora with standoff annotation, or  
 annotation on different tiers; etc; even worse, web interfaces do not  
 make the whole corpus available and, thus, do not permit the analyst  
 to perform larger-scale analyses that require the complete corpus;

-  limited in terms of user control: users are at the mercy of the  
 developers. If, for instance, the creator of one of the above programs  
 changed the way key words are computed by means of an update function  
 but did not inform the users, then users would have no explanation for  
 why the same data set suddenly yields different results, and with  
 non-open source software, no user could find out what exactly has  
 happened and how the software is changed. More trivially even, if one  
 developer decided to discontinue a program, then what?

And, as if all the above were not enough, I also just generally don't like the thought that scientists' possibilities of analysis are limited by a piece of commercial software as opposed to the limits of our knowledge, understanding, sources of data, etc.  
**Do you have a favorite programming language and/or technology? Why do you prefer it?**  
 My favorite programming language is, of course, R. It's one downside I see is that it is slower than, say, Perl,but I still strongly prefer it over, say, Perl because I think

- R is simpler than Perl. My favorite example: this is how you  
 generate a sorted frequency list of an array in Perl:

[GitHub Gist](http://gist.github.com/655682)

- And this is how you do that same thing in R:

[GitHub Gist](http://gist.github.com/655680)

Another way in which it is simpler than Perl and, from what I hear, Python, is its handling of multidimensional data structures. The ugliness of arrays of arrays and hashes of hashes and all that in Perl was one of the first things that made me stray away from Perl! In R, those things are really easy. R combines all the advantages of a (simple) general-purpose programming language with a huge variety of high-level statistical-analysis functions as well as [extraordinary graphics](http://addictedtor.free.fr/graphiques/). Thus, all of an analysis can be done in R. One doesn't have to do the concordance/frequency list in Perl, export it to SPSS for the stats, then do some graphs in SPSS and some in Excel, and ... It can all be done in one language, one environment. Very efficient ... Put differently, many linguists are learning the stats stuff of R already anyway - why not use the fact that you only need to learn a little bit more and then you can also do everything else a corpus linguist needs, too?  
**You published quite a lot on corpus linguistics, a topic which has got impetus recently. How do you see its status within nlp and  
 linguistics?**  
 I will talk about the relation of corpus linguistics to NLP in the next answer, but with regard to corpus linguistics and linguistics, I have been arguing that, to me, corpus linguistics is a methodology, or a methodological commitment, in linguistics, but not a theory. Corpus linguistics consists of a set of observational methods (frequency lists, collocations/colligations/collostructions, concordances, and dispersions) that involve computerized retrieval of strings from corpora (electronic databases of spoken or written text that was produced in largely authentic settings) to learn something about the acquisition/use/etc. human language. To me, that is the exact same stance that I would have towards, say, eye-tracking or acceptability judgments: eye-tracking in linguistics is an experimental method that involves tracking subjects' saccades while subjects perceive/act on linguistically relevant input to learn something about the processing/representation of human language. Acceptability judgments is an experimental method that involves obtaining subjects' graded reactions to auditory/visual linguistic stimuli to learn something about human language. Thus, contrary to at least some, I think corpus linguistics is not a theory but a method. A theory makes predictions, corpus linguistics doesn't; a theory can be falsified, how would you falsify a frequency list? Thus, corpus linguistics is, I believe, one very interesting, very useful and revealing method, and certainly one that I am most interested in right now, but also certainly not a theory.  
**In a few papers of yours you made a distinction between computational linguistics and using computational tools in linguistic research. Do you think that we can draw a line between the two approaches?**  
 I am not sure whether WE can do that - in my own mind, however, I make a distinction but then may of course not be widely shared/accepted. First, I think "computational linguistics" is only one of several terms to refer to a huge and interesting (and increasingly diverse) field - with "natural language processing" being one of the other most widely used terms. And obviously, some areas of computational linguistics of course border on, or overlap with, corpus linguistics. When asked where I see the (main) difference between these fields, I usually say (a bit polemically and simplistically) that some areas of computational linguistics are in fact mislabeled: taking the notion of head-modifier structure very literally, I think there are many areas  
 that should be labeled "linguistic computing" rather than "computational linguistics", and this distinction also has to with corpus linguistics. I want to call something "___ linguistics", if it is linguistics ;-), i.e., if its ultimate goal is to increase our understanding of (the use of) human language, or even the linguistic system's place in the larger domain of human cognition. And I want to call something "___ computing" if its ultimate goal is not concerned  
 with understanding (the foundation or use of) human language but its computational application or implementation. For example, for me, developing a talking ticketing machine for the airport parking lot falls under the heading of "natural language processing", but I would not call it "___ linguistics" (even if frequency data from corpora are used to tweaks how the machine parses its input), but, if pressed, would call it "linguistic computing". (Of course, there are cases where such a forced binary decision is difficult to make.)  
  
**As a practicing teacher, what do you advise to students wishing to catch up on the new trend but studying at an 'old school' department?**  
 Uh ... well, I don't think I have any advice to offer that goes beyond what anybody else would say ... Read a lot, sign up to relevant newsgroups and websites (e.g., the Corpora list), attend my bootcamps ;-), etc.
