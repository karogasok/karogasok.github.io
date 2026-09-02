---
title: "Sublexical Semantics"
slug: "sublexical-semantics"
date: 2011-10-02T17:56:00.002Z
publishDate: 2011-10-02T17:56:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/10/sublexical-semantics.html"
regi_cimkek:
  - "guest post"
  - "linguistics"
regi_cimkek_mind:
  - "guest post"
  - "linguistics"
  - "semantics"
  - "sublexical semantics"
  - "theoretical linguistics"
---

A guest post by Richard Littauer

**I was asked by Zoltan a long time ago to write something for this post, and have so far neglected to come up with anything. I'm about to start a two year Computational Linguistics masters at the University of Saarbrücken, so I figure it is about time I do this, before I am too bogged down to do anything. So, here is some original research I did a couple of years ago for a Lexical Semantics assignment at the University of Edinburgh, while I was in my undergraduate, being taught by Nikolas Gisbourne. His research in this area is largely within the framework of Word Grammar, and he specialises in the [event structure of perception verbs](http://ukcatalogue.oup.com/product/9780199577798.do) (which is the title of his 2010 book released with OUP. I had wanted to take his word grammar and apply it some sort of binary system, but my thoughts quickly went in a different direction. I cover a lot of ground responding to Rappaport Hovav and Levin's work in this are, as well as Pustejovsky, mostly as I didn't want to risk quoting Gisbourne wrong at the time. Here is that different direction, then - it's very rough, and I had no computational background at the time, so it might be a bit out there. Hopefully, I'll get some feedback on this, though, as I think it's interesting and might be an interesting route to pursue. (NB: It's mostly edited from a longer essay, if it sound a bit formal.)**

Rappaport Hovav and Levin (1998) and Pustejovsky (1991) both posit representations that map the varying subevents for different types of verbs. Rappaport Hovav and Levin front an articulated, linear structure which uses rules following the aspectual, Vendler-Dowty classification of verbs. They show the varying complexity of verbs by embedding subevents within subevents. Pustejovesky (1991), on the other hand, uses a tiered, minimalist theory to cover the same ground. So, let's outline the differences and similarities between their representations, and then I'll go on to present my original theory that seeks to deal with some of the issues not covered by the other representations - generally by putting forth a system that codes the sublexical information in a computational-like framework.

### Rappaport Hovav & Levin's Theory

Rappaport Hovav and Levin distinguish two components of verb meaning: the ‘constant’ and the primitive predicate. The former is useful as an idiosyncratic element of meaning for distinguishing a verbs classification, whereas the latter is “the lexical property of a verb that is taken to determine it’s syntactic behaviour...[so] a verb’s meaning consists of an association of a constant with a particular lexical semantic template.” (Rappaport Hovav and Levin 1998: 107) Lexical semantic templates, called event structure templates (ES) by Rappaport Hovav and Levin, are the rules presented in order to understand this meaning and what influences it. The classification is based on the aspectual classification of verbs first laid out by Vendler (1967) and Dowty (1979) , which essentially delegate a verb or a subevent into the template of a simple state; a simple action; a complex, inchoative/change-of-state achievement; or a complex, causative accomplishment. Rappaport Hovav and Levin posit the following ESs:

- a. Activity: [ x ACT <MANNER> ]

- b. State: [ x <STATE> ]

- c. Achievement: [ BECOME [ x <STATE> ]

- d. Accomplishment: [ [ x ACT <MANNER> ] CAUSE [ BECOME [ y <STATE> ] ] ]

- e. Accomplishment: [ x CAUSE [ BECOME [ y <STATE> ] ] ]

As these are templates of verbal polysemy, not syntactic or categorical constructions, each verb aligns by default to one of these mappings. Importantly, they state that some verbs may be augmented to fill different templates: the result construction, for instance, allows an achievement verb to fit into the accomplishment template, as seen below: (Rappaport Hovav and Levin 1988: 103)

- a. Cinderella scrubbed her fingers to the bone.

- b. *The clumsy child broke his knuckles to the bone.

This system has its flaws, I think. Rappaport Hovav and Levin submit the Subevent Identification Condition, which demands that “each subevent in the event structure must be identified by a lexical head.” (Rappaport Hovav and Levin 1988: 112) They, correctly, do admit that a prototypical argument can be underspecified. However, their model does not specify participants for each subevent, nor does it clearly state how the semantic arguments and events link to the syntax. I may only want these because I'm used to studying this with Word Grammar as the framework, but I still think it is necessary in a theory. As well, the <MANNER> and <STATE> predicates are not clearly defined: <STATE> is identified in different examples as WITH <THING>, <PLACE>, and <DRY>, without adequate expression of the argument slots or their ability to be modified; <MANNER> is used as a specifier of the ‘constant’ for in- strumental, transitive verbs like HAMMER, without mapping hammer onto an participant. This would be expected for John hammers the nail, where a hammer is underspecified syntactically but understood semantically (that is, the verb constant is inconceivable without an expression of instrumentality). Finally, It is also not clear why there are two types of accomplishments: an example for an ‘untypical’ situation is not presented, even though “accomplishments are complex events composed of two subevents: the causing event - *typically an activity* - and the change of state it brings about.” (Rappaport Hovav and Levin 1988: 104 (stress added)).

### Pustejovsky's Theory

Pustejovsky (1991) also works with an aspectual system, but he approaches it using a tiered system organised through formal logic. He factors out the event structure (ES) from two lexical conceptual structures (LCS), one an annotaion on the event structure, which essentially maps out the specifications of the arguments (LCS’), and the other with lexicalisation of the participants (LCS). His system has transitions, processes, and states. A transition is a complex event which has an initial process and a resultant state, equivalent to Rappaport Hovav and Levin’s ”BECOME”. A process maps the basic relationships between events and states. The purpose of the tiered nature of the system is to stop erroneous conflation of meaning, and to present a logic-based but psychologically real system. An example of his accomplishment structure is given here: (Pustejovsky 1991: 60)

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/--wQv-nOtLSA/ToihQeUR25I/AAAAAAAAAlQ/46I-V51L9Iw/s640/pustejovsky.png" rel="nofollow noopener">pustejovsky.png</a></span>](http://1.bp.blogspot.com/--wQv-nOtLSA/ToihQeUR25I/AAAAAAAAAlQ/46I-V51L9Iw/s1600/pustejovsky.png)

I think this has its drawbacks, as well. The main flaw in this system is that factoring out the relations between events into a separate tier fundamentally would change the way that the event is conceptualised, as well as changing the participant’s relations to events. As well, the temporal relationships between subevents is completely underspecified: Pustejovsky states that the difference between an accomplishment and an achievement is specified in the LCS’ (Pustejovsky 1991: 59), such that an accomplishment has [act(x, y)], as above, but this disregards the temporal differences, which would most clearly lie in the event structure. This can be seen clearly in *John closed the door slowly*, where the [act(j, the-door)] must have a different temporal aspect from the transition from [¬closed(the-door)] to [closed(the-door)].

### My Theory

So, skipping out on a lot of comparison between the two and tje pointing out of some individual failures in either theory - If it follows that a good theory is one that explains all of the data, then a mix of Pustejovsky and Rappaport Hovav and Levin could perhaps offer more than either alone. Pustejovsky fined tuned his minimalism, but neglected some of the finer details, particularly involving temporal elements and participants. Rappaport Hovav and Levin, on the other hand, failed to suitably provide a general theory, instead splitting up the data into more LCSs than were strictly necessary: a good example of this is the two accomplishment rules, even though for x to influence ‘CAUSE’ it would have to perform [x ACT <MANNER>] in any event (as the nature of ‘CAUSE’ is underspecified in their system). A proposed theory, then, would need to present suitable processes for the realisation of subevents, as well as a system of mapping each subevent onto it’s particular participants, and finally an output that can link it suitably to the syntax. So, that's what I propose here.

This system has four functions, each representing a different Vendler-Dowty classification. There are four tiers, but it does not factor out event structure as Pustejovsky does.

- The first tier specifies the input, which is only of importance in an Accomplishment, when there is a third variable. (Note - I haven't considered ditransitives here, and probably would have to in a fuller system.)

- The second tier is the function by which the verb’s primitive predicate is called, and the ‘constant’ features (identified with the variable c ) are altered or spread to the participants. This roughly equates to the ES tier in Pustejovsky, and to the implied ESs in Rappaport Hovav and Levin’s linear system.

- The third tier is the mapping of participants for each event or state: each classification is taken to have embedded within it the lower classification. The linear, embedded nature present in Rappaport Hovav and Levin and Pustejovsky is employed here, as well.

- The fourth tier is the output, which specifies what arguments can be recalled semantically or syntactically. This is most important for Achievements, where the subject’s pre-functional state cannot be recalled, thus performing the function of ‘BECOME’ or Pustejovsky’s transition. This does not entail cognitive memory, which can clearly recall, say, *John*, after the sentence '*John died*' is processed: what it entails is semantic mapping, such that *John* in '*John died'* has undergone a change of state. This change is represented by the pre-functional mapping of x as x1 , and the post-functional mapping as x2.

In this system ”the accomplishment representation is the most complex representation.” (Rappaport Hovav and Levin 1998: 105) This is most likely due to processing limits, as generally more than two embedded clauses are too complex to parse (evident in the failure to process '*John, who the cat, who the dog that the mouse scared didn’t like hated ran away*'). The justification for the fourth-degree depth in Accomplishments is that ‘State(x, y)’ can be stored as a variable, as the bottle being broken does not have to be syntactically analysed for the parsing of '*John broke the bottle'*. Finally, it should be noted that in each function tier, a temporal relation is specified as a time index. These (as well as an uncertain amount of features in the predicate) can be modified by adverbials, prepositional phrases, and certain constructions. The resultive construction, for instance, would specify telicity by demanding an extra event for +bounded in the achievement phase, thus positing ‘manner’ verb in the accomplishment template.

Finally: A state is the function of X = xc + yc, where x is the subject and y is the predicate, and c is the ‘constant’ qualia of each. The definition or the subject is changed by the function, and that change is the spreading of features from y. (If I haven't lost you yet, don't worry, I probably will in a few seconds.)

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-6Aktd4ejgas/ToihhSrwsfI/AAAAAAAAAlU/Vuqhi0WnN-Q/s640/state.png" rel="nofollow noopener">state.png</a></span>](http://3.bp.blogspot.com/-6Aktd4ejgas/ToihhSrwsfI/AAAAAAAAAlU/Vuqhi0WnN-Q/s1600/state.png)

Note that the copula in a state does not need to be specified syntactically, necessarily.

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-5K1oDO3gp9w/Toihrn_qMcI/AAAAAAAAAlY/EUH-dH_f67w/s640/event.png" rel="nofollow noopener">event.png</a></span>](http://3.bp.blogspot.com/-5K1oDO3gp9w/Toihrn_qMcI/AAAAAAAAAlY/EUH-dH_f67w/s1600/event.png)

‘dancing c’ is included in the output, as it can be syntactically called as a gerund. An event specifies the manner of existence for a state, with it’s own mapped arguments.

[<span class="lost-media">Hiányzó kép: <a href="http://1.bp.blogspot.com/-g52qHiB7DAU/Toih3Es8HwI/AAAAAAAAAlc/w56wDl6QO7A/s640/achievemnet.png" rel="nofollow noopener">achievemnet.png</a></span>](http://1.bp.blogspot.com/-g52qHiB7DAU/Toih3Es8HwI/AAAAAAAAAlc/w56wDl6QO7A/s1600/achievemnet.png)

An achievement verb entails a specification of temporality, with an inability to semantically recall the previous argument as an argument.

[<span class="lost-media">Hiányzó kép: <a href="http://2.bp.blogspot.com/-3vYnuxfhIoY/ToiiGnLngaI/AAAAAAAAAlg/87a6UyGNyGA/s640/accomplishment.png" rel="nofollow noopener">accomplishment.png</a></span>](http://2.bp.blogspot.com/-3vYnuxfhIoY/ToiiGnLngaI/AAAAAAAAAlg/87a6UyGNyGA/s1600/accomplishment.png)

I guess I think this is pretty self-explanatory, because I didn't have any notes on this in my original write-up. That might be a grave mistake - this didn't just confuse me just now -- it also confused the heck out of my professors.

### Conclusion?

Pustejovsky’s and Rappaport Hovav and Levin’s theories come from different standpoints. Pustejovsky acknowledges the four main terms of aspectual classifications, and then seeks the most minimal theory to encapsulate them in general. Rappaport Hovav and Levin seek to provide templates the cover all possible sublexical polysemic constructions, and so have sacrificed generality for detail. In doing so, they put more meaning into the lexical: their verbs are split into ‘manner’ and ‘result’ groups, the first of which Pustejovsky equates merely to a simple process. He puts meaning somewhere else from event complexity - but his representations are necessarily linear, as there is no ordering. The claim of event ordering is in the event structuring of the representation, whereas in Rappaport Hovav and Levin the event ordering is actually in the template.

The theory presented in this paper seeks to bridge the divide between these two theories by clearly mapping out arguments, by specifying the manner of feature spreading, by indexing temporal quality for each event, and by attempting to link up the semantic arguments with syntactic input. It is hoped that the algorithmic application of such a model illuminates the need for further work and clarification of the present representations of lexical complexity structures.

And that pretty much sums up that paper. If you have any comments or suggested reading or further research, I would love to hear them.
