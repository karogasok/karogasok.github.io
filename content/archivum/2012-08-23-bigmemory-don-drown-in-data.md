---
title: "bigmemory - don&#39;t drown in the data"
date: 2012-08-23T09:58:00.001Z
publishDate: 2012-08-23T09:58:00.001Z
author: "Varjú Zoltán"
archiv: true
forras_platform: "blogspot"
forras_cim: "Számítógépes Nyelvészet"
canonical: "https://szamitogepesnyelveszet.blogspot.com/2012/08/bigmemory-don-drown-in-data.html"
regi_cimkek:
  - "rstats"
regi_cimkek_mind:
  - "Significance"
  - "bigmemory"
  - "rstats"
---

**[bigmemory](http://www.bigmemory.org/) is an R package that "supports the creation, storage, access, and manipulation of massive matrices".[ Don't drown in the data](http://onlinelibrary.wiley.com/doi/10.1111/j.1740-9713.2012.00592.x/abstract) is a paper by [John W. Emerson](http://www.stat.yale.edu/%7Ejay/) and [Michael J. Kane](https://sites.google.com/site/kaneplusplus/) in the recent issue of Significance (unfortunately the paper is not open access). The authors describes the basic ideas behind bigmemory and why they started the project.**

Big data sets are becoming the norm these days e.g. [The Netflix Prize ](http://www.netflixprize.com/)data was about 2GB. Analyzing data at this scale causes problems:

> Many statisticians were left behind because their two most widely used software packages, SAS and R, were ill-equipped to handle this class of problem.

R is designed to do its job in the memory:

> R is not well suited for working with data structures larger than about 10-20% of a computer's RAM. Data exceeding 50% of available RAM is essentially unusable...

The solution is bigmemory, an R package that is using the technique of memory-mapped files. [According to Wikipedia](http://en.wikipedia.org/wiki/Memory-mapped_file):

> A memory-mapped file is a segment of virtual memory which has been assigned a direct byte-for-byte correlation with some portion of a file or file-like resource. This resource is typically a file that is physically present on-disk, but can also be a device, shared memory object, or other resource that the operating system can reference through a file descriptor. Once present, this correlation between the file and the memory space permits applications to treat the mapped portion as if it were primary memory.

As disk space is cheaper than memory, this solution is a reasonable and economic choice for analyzing data on a single computer. It doesn't require special knowledge of databses and hardware issues so one can focus on data analysis with his/her regular tools.
