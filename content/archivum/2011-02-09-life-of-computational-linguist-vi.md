---
title: "The Life of a Computational Linguist VI - Interview with Jeremy Kahn (Director of Research, Wordnik)"
date: 2011-02-09T18:36:00.002Z
publishDate: 2011-02-09T18:36:00.002Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/02/life-of-computational-linguist-vi.html"
regi_cimkek:
  - "Wordnik"
  - "computational linguistics"
  - "interview"
regi_cimkek_mind:
  - "Wordnik"
  - "computational linguistics"
  - "interview"
---

**Are you keen on words? You'll love [Wordnik](http://www.wordnik.com/) "the place for all the words, and everything known about them". Jeremy Kahn the director of research at Wordnik was so kind and answered our questions. Jeremy got his AB in Linguistics from Brown University and recently defended his PhD thesis at the University of Washington. He is a very active member of the linguistics community on Twitter, where you can find him as [@trochee](http://twitter.com/#%21/trochee).**  
  
  
  
**Please tell us something about yourself.**  
  
 What a question! I struggle with the Gricean pragmatics here -- mostly with the maxim of relevance, since I'm not sure what you my virtual readers would want to know about me.  
  
 Well, I'm *dashingly* handsome, and perhaps a bit over-fond of self-deprecating humor.  
  
 Now that I've violated the Maxim of Relevance rather thoroughly, let's see:  
  
 I'm not entirely sure what made me a linguist.  I was partially deaf for about a year of my young childhood -- somewhere in the middle of the 'critical period' between age three and five -- and that may have something to do with how interesting I find language as a system of communication: a system of signal among us mostly-hairless primates which has become such an important part of our lives that we sometimes even forget we communicate in other ways. I got into linguistics through the [Brown department of Cognitive Science and Linguistics](http://www.brown.edu/Departments/CLPS/), because I was interested in how people think, but discovered the appealing systematicity of (e.g.) morphemes and syntax as part of the breadth requirements within the cognitive science degree.  
  
 I did NOT set out to be a computer programmer in college.  I took two CS courses in college, but they were low-level and fairly straightforward. I became a programmer because I was hired into a speech technology company to encode some of what I knew (as a linguist) into computer-readable instructions, and then I discovered that I was actually pretty good at programming.  But two years of my postgraduate life disappeared into the process of learning-how-to-program.  
  
**As a director of research, what are you doing at Wordnik? How did bring your knowledge of linguistics into the 'real-word'?**  
  
 At Wordnik, my job is to explore what we know about how English speakers and writers use English, and figure out how to relate that sort of knowledge to the way that we use dictionaries (and our informative APIs). I spend a lot of time reading papers from the Association for Computational Linguistics ([http://www.aclweb.org](http://www.aclweb.org/)/) and interpreting them for our use ("can we do task X?" "why would we want to do task X?"  "what assumptions does this paper make about how to do task X?").  I also spend a lot of time in conversations with our development engineers about structuring our own data and algorithm processes so that we can do empirical linguistics research (and get results!) without starting from the ground floor every time.  
  
**Wordnik has got a nice API, for what kind of applications is it used for?**  
  
 Most of our current API users are applying the [Wordnik APIs](http://api.wordnik.com/signup/) to things like powering word games and EFL/ESL learning applications, which we are pleased by: it suggests that our interfaces are powerful enough for the most straightforward dictionary uses. However, we support some more general and high-power uses, like cleanup and normalization for language data.  We have a few API users who are doing more sophisticated things with our APIs, including sentiment analysis and others.  We're looking for more such users; we've just re-released our new and improved developer website: [http://developer.wordnik.com](http://developer.wordnik.com/)/ ; I daresay it's pretty snazzy.  
  
**You are a linguist who's been working in the field of computational linguistics for more than a decade. How do you see the relationship of academic research and the industry?**  
  
 Computational linguistics is a complicated field. There are some academic computational linguists who are working on computational models of language that have no relationship to the business (or military!) applications, and others who are essentially working on industry (or military) problems from within the "ivory tower" of academia.  In general, this division mirrors the general academic/industry splits, but it is particularly difficult in computational linguistics, which straddles linguistics, computer science, and electrical engineering disciplines.  
  
 CS and EE departments have closer ties to industry in general, but it's not strictly based on the department you come from: the computational linguists (and computer scientists) who have the strongest relationships to industry are those who have placed an emphasis on the automatic discovery of language behavior based on observation -- the new empiricism, we might call it. Google's success in search and elsewhere out of a Stanford-area garage is only the best-known of these fence-hoppers.  
  
**How do you see computational linguistics; is it a separate discipline or it is a part of computer science or linguistics?**  
  
 My somewhat inflammatory rant above notwithstanding, I believe that computational linguistics *should* be part of linguistics, and computer science people who want to work with human language will need to learn some parts of it.  Some parts of computational linguistics are strictly applications to very large data sets, but linguistics provides (at least) some perspective on how to assemble that data-set: what parameters may be tied together; what regularities or irregularities need to be captured and encoded, and a strong understanding of the nature of the signal that is language.  
  
 Let me answer this in the most annoyingly empirical way I know how: by addressing what I *do* rather than what I *believe*.  
  
 I would say that most of the "formal" linguistics knowledge I use daily is limited to the linguistic concepts that are introduced at the undergraduate level: the underlying concepts of morphology, phonology, and syntax.  Graduate school introduced me to a wide variety of computational-linguistic applications and techniques, which I learned from professors in the departments of Electrical Engineering, Computer Science, and (to a lesser extent) Linguistics.  From the professors in the Linguistics department, my education was much more foundational, because it gave me a great overview of the sorts of analyses that would go into those CL applications and techniques.  
    
**You did your doctoral research at the University of Washington, the place where the "[A Grand Challenge](http://bit.ly/cUGq9W)" white paper was written by Bender and Good. Do you think so that we have to update our methodologies and scale them up? Is this a methodological change - like the digital humanities movement - or a paradigmatic one?**  
  
 I find the Grand Challenge tremendously inspiring.  I really hope that the community -- of which I am a part -- can step up and take on this challenge. There are a lot of pieces missing where we currently stand, though, not least of which is the funding and interest to get a host of linguistically- and computationally-informed people working on the same questions.  
  
 I think there are two useful research projects in linguistics that come from different directions; we might consider them "computationally-aware scientific study of language" and "linguistically-aware application of computational tools".

From the scientific perspective, linguistic research in the 21st century will require that computational tools be used -- no sociolinguist today would do research without spreadsheet programs and statistical analysis languages like R, and phoneticians have happily adopted Praat. It's almost absurd to me to imagine that this trend will not spread into the rest of linguistics: using computational tools to describe, explore, create hypotheses and test them will become part of becoming a linguist, just as it is becoming part of being a biologist or an anthropologist.  To the degree that this change is a paradigmatic change, I welcome it and I think the shock (it will be a shock to some!) is worth absorbing.  
  
 On the other hand, the application of computational linguistics tools in industry applications (internet search or Twitter trend-spotting) does *not* push linguistics (or computational linguistics) towards a paradigm shift -- it's a tremendously important set of tools, not least because it provides a job market for linguists -- but it doesn't actually change what computational linguistics students need to study.  
  
**In your opinion, what should a computational linguist's toolbox contain?**

Like it or not, quantitative analysis tools -- particularly statistical techniques that can cope with multiple confounding factors -- are a fundamentally key piece of scientific and engineering work. These tools require the ability to think at scale -- dozens of examples should no longer be considered "thorough".

Scientists and engineers of language alike should be comfortable with the idea that their models are *only* models: finding a single counterexample is not proof that the model is worthless -- it's proof of existence of a single counterexample.  New computational linguists should know how to measure the utility or informativeness of any proposed model they are exploring: not whether it is True (and my rival's opposing model is False) but *how* informative is my model?

To answer the question, then: learn perplexity, learn evaluation techniques, understand generative and discriminative models (and their differences), think in high-dimensional spaces.  
  
**What would you advise for a the youngsters wishing to start a career in computational linguistics: start reading a degree in cs or linguistics, double major, or find a specialist programme?**

Larval computational linguists of either the scientific or engineering orientation would do well to learn programming tools -- and this is sometimes difficult to learn in a linguistics department.  It's important to have some foundation in programming skills; one way to do this is to enroll in a CS degree.

Those excited about the science side of things should definitely consider linguistics departments, but I would encourage actively seeking mentors and education in strongly empirical departments that are philosophically nearby. Good external resources for empirical computationally-informed students of linguistics include some psychologists (neat things are happening in brain science!), electrical engineers (speech and signal processing!), computer science (information retrieval work).  Avoid faculty in any department that are pushing a single Theory; look for those who are clear on their own internal measures of success (they should know how they know when they're working!)

Those excited about the engineering application of computational linguistics techniques might do better within computer science, computer engineering or electrical engineering departments -- it is *very* difficult to learn advanced machine-learning techniques outside of those departments.  A few exceptions exist: the linguistics groups at Stanford and at the University of Washington (two I know fairly well) are building strong bridges to the other departments. If your university is doing this, you might consider double-majoring or finding particular faculty who have double-appointments and asking their opinions.
