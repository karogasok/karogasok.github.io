---
title: "An Introduction to Scientific Workflows (For Linguists)"
date: 2011-10-04T05:51:00Z
publishDate: 2011-10-04T05:51:00Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2011/10/introduction-to-scientific-workflows.html"
regi_cimkek:
  - "linguistics"
regi_cimkek_mind:
  - "linguistics"
  - "methodology"
  - "scientific workflows"
  - "workflows"
---

A guest post by Richard Littauer

**If you've been following [@richlitt](http://twitter.com/#%21/richlitt) on Twitter for the past six months, you may have noticed that I've been talking about scientific workflows a lot. I was doing an internship for [DataONE](https://www.dataone.org/), an NSF-funded cyberinfrastructure initiative that tasked me with finding out all I could about scientific workflows from a site called [myExperiment](http://www.myexperiment.org/), which is a repository and social network for scientists who use them. However, if you're outside of the fields of bioinformatics or harder sciences, you may not know what I'm talking about when I talk about 'Scientific Workflows'.**

The term came about in the 90s as a result of new changes in the way that science was being done due, largely, to computational advances. Scientists borrowed the term 'workflow' from the business world. A business workflow is basically a schema that shows how information is being transferred through a business.If you imagine a Subway restaurant, a workflow might look like this:

<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="float: left; margin-right: 1em; text-align: left;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/--W_NutfjUWY/Toib8DkX-VI/AAAAAAAAAlA/LWAJSEah1M0/s1600/subway.jpeg" imageanchor="1" style="clear: left; margin-bottom: 1em; margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/--W_NutfjUWY/Toib8DkX-VI/AAAAAAAAAlA/LWAJSEah1M0/s320/subway.jpeg" width="320" /></img></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Subway</td></tr>
</tbody></table>

- Customer order is the input.

- The first person takes that order, and gets the bread and cuts it. He then adds in whatever the main constituents of the sandwich is, and then asks for more information.

- The customer says she wants cheese.

- The 'sandwich artist' (as they are called - I should know, I was one) then adds cheese, and passes on the sandwich to the vegetable handler.

And so on. You can imagine a graph of all of this happening - and you can be sure that someone, at some point, did actually draw that graph. Scientific workflows work in the same way - they are models that are used to take information, do whatever they are supposed to do with it, and then spit out modified information.

You can imagine these as processes that could run half of your lab work for you, as a geneticist - say, it could look up the gene id of the dna information you put in, and then spit out tons of published results from an online repository like [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/) (and, indeed, many workflows do stuff like this, like the one shown below.) Or, it could just convert your .xls file into an .csv so that it can be opened in [R](http://www.r-project.org/) (such workflows, common, are called **shims**.) Or it could do different things, like generate information itself, pass data on via email to other people to check, get information offline, or tell you where in your lab work you - and the proverbial sub, your product - should currently be.

[<span class="lost-media">Hiányzó kép: <a href="http://3.bp.blogspot.com/-RI1TxBbRvro/ToicS-NkyEI/AAAAAAAAAlI/wwGkhSaYM9A/s400/miningworkflow.png" rel="nofollow noopener">miningworkflow.png</a></span> ](http://3.bp.blogspot.com/-RI1TxBbRvro/ToicS-NkyEI/AAAAAAAAAlI/wwGkhSaYM9A/s1600/miningworkflow.png)

Generally, scientific workflows (or pipelines, as they are sometimes known) are on the computer. They could just be shell scripts that run in bash. However, recently, the term has been semantically narrowed to mean workflows that have been made in some sort of workflow workbench. These are programs that are designed to make workflows - they provide an easy way to string together bits of code that will do what you want to do, and mean that not every scientist needs to be a coder. There are many such programs available - [Taverna](http://www.taverna.org.uk/) and [Kepler](https://kepler-project.org/) being the main two, along with others such as [RapidMiner](http://rapid-i.com/content/view/181/190/), [VisTrails](http://www.vistrails.org/index.php/Main_Page), and [Knime](http://www.knime.org/). These workbenches help, specifically, the scientist with:

- **Creation**: of workflows. Two core features that help with this are combinatoriality and recursion - you can combine different components together, and you can embed other workflows in a single workflow. You can see how this would help - you don't need to do the same work twice.

- **Mapping**: Planning out, deciding where things go, doing the heavy work you don't want to do yourself.

- **Scheduling:** You can imagine how this is useful.

- **Execution**: And this - particularly when the code might involve lots of heavy processing, and therefore needs to be run on a cluster. If the program makes sure that it all runs simultaneously, it comes out much faster. There's a lot of grid programs that work like workbenches, and some that are both.

- **Visualisation**: It's important to know exactly what you're doing, especially if your workflow is doing things to the data itself (such as when, say, it might be integrated with R or MATLAB). This helps you see how your experiment is working.

- **Re-use**: This is, for me, the most important bit - workflows help you reproduce your own work, which is incredibly important, and they help others back up your claim by also getting your results. This is a major part of 'good' science practices.

So, this, in effect, is what I've been talking about. You can imagine this being useful for Linguistics. I'll give you an example. My dissertation focused on simulating different mechanisms used by 8-month-old children in word segmentation, using an iterated learning model. I hadn't been *taught* to program specifically before I took this on, and as such, I never had a plan laid out for what I wanted to do - I just started writing, and kept going until I reached the end of what I needed to write. This meant, first off, that there was a lot of bad code. Secondly, it meant that I couldn't clearly see what I was doing - if I had had some sort of visualisation of where the data was going in my code, I might have noticed a major, simple oversight early on. I didn't.

I struggled over a couple of months to understand the data I was getting. I say a couple of months, because the way I was coding it, I didn't know about efficient ways of executing my code, so I would run it overnight each night. I had around 160 runs to do, each taking around an hour. You can imagine how I felt when, three days before the dissertation was due, I found that major error in the code that invalidated all of my work. In case you didn't notice, three days is 72 hours - there as no way I was going to finish it in time.

So, I went for a walk, quickly started smoking again after trying to quit, and bought myself a pint to think about what to do. After some thought, I called up a buddy of mine. He came over, and we worked on it for around three hours. He, a PhD student in Informatics in Edinburgh, at one point started laughing when he saw my code. I didn't mind - by the end of the night, he had managed to schedule them using some simple bash scripts, and to run them on 50 clusters he had access to. We went out to celebrate, and by Saturday morning, I had all of the data to analyse. The next two days were a bit of a haul, and my thesis showed it, but that's not the point.

The point is that all of this could have been avoided - and I've heard similar stories with the same conclusion. If linguists had access to better workbenches, if they had standard practices for coding that start with the first bracket, and if they had any impetus to reuse and share each other's code in the interest of Open Science, I wouldn't have been where I was. I would have planned it better from the start (mapping), created it more efficiently, executed and scheduled it better, and had other open codes to use as a base (my error was in the iterated learning model, which was coded in almost every paper I referenced, although I saw almost none of their code), then this sort of situation would cease to happen (mostly), and we'd be better off a science.

That's why I keep talking about them - I think that they're something that can help linguists, and I don't just mean computational ones. Methodology wasn't a course at Edinburgh University for undergraduates, but it should be. Failing that, there should be an infrastructure for linguists that helps towards these ends.Since I don't see that happening currently, I'm going about making one. So, if you want to help out by designing a repository for pipelines and an open access journal based on reproducible research in the social sciences, get in touch. Otherwise, I hope you at least know what workflows are now.
