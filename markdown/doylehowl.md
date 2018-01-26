-   [Introduction](#introduction)
    -   [Gallon-guzzling technique](#gallon-guzzling-technique)
    -   [The right to forget](#the-right-to-forget)
-   [A brief history of time](#a-brief-history-of-time)
    -   [Reed Releases](#reed-releases)
    -   [Reed Emissions](#reed-emissions)
    -   [Reed Relieves](#reed-relieves)
-   [The frequentist approach](#the-frequentist-approach)
    -   [Posting patterns](#posting-patterns)
    -   [Common words](#common-words)
    -   [Variation in language over
        time](#variation-in-language-over-time)
    -   [Use of gender](#use-of-gender)
-   [A sentimental journey](#a-sentimental-journey)
    -   [A basic sentiment pass](#a-basic-sentiment-pass)
    -   [What was triggering](#what-was-triggering)
-   [The gaps](#the-gaps)
    -   [All the likes we can not see](#all-the-likes-we-can-not-see)
-   [Appendix](#appendix)
    -   [About me](#about-me)
    -   [The code](#the-code)
    -   [Data preperation](#data-preperation)
    -   [Basic statistics](#basic-statistics)
    -   [](#section)

An investigation into the murmurs, musings, and mentions from a memory
long forgotten.

------------------------------------------------------------------------

Introduction
============

Gallon-guzzling technique
-------------------------

It was Dec 6th, 2012 at exactly twenty-seven minutes past midnight that
the first howl was heard. Fourteen days before the end of the world, a
precursor to what would become confessional apocalypse began. Somewhere,
someone, had collected a brief anonymous testimony and posted it on the
popular blogging site tumblr.com. The text of this first spark of what
would be a raging emotional inferno was simply,

> I know you are leaving Reed forever, but you will never leave my
> heart. DAT GALLON-GUZZLING TECHNIQUE

A forlorn exaltation into the cyber-sphere, a weary lover lamenting the
invetible departure of their sexual compatriot; and - to add emphasis, a
praise of fallacious talent.

> DAT GALLON-GUZZLING TECHNIQUE

The first of thousands confessions to follow, all produced anonymously,
all managed by a shadowy few secret keepers who would come and go over
the proceeding months. In total three incarnations of the service would
be wrought over a course of aproximately 18 months, from winter 2012
through the early autumn 2014. 11,485 posts would be made across the
three Tumblr pages, which to this day still rest as a memorial to the
emotional milue of a point in time; and for many, a continuing source of
Google-able nostalgia, and embarassment.

With this memorial though, we can over the distance of time look back at
those thoughts, those memories, those incarnations, and begin to
understand through the lens of data and analysis what themes, trends,
and cultural shifts occured over those 18 months. Although what comes to
follow is by no means exhaustive, it is a first pass at what may be a
rich source of information at a raw point in time in the lives of
students at the Reed College, in Portland, OR.

The right to forget
-------------------

For the sake of privacy, all names have been removed from the quoted
posts. Furthermore, the raw data of this analysis, and the location of
the pages, is intentionally removed from this analysis and Github page.
As we will all begin to see, some things we forget should remain
forgotten

------------------------------------------------------------------------

A brief history of time
=======================

Reed Releases
-------------

Reed Emissions
--------------

Reed Relieves
-------------

------------------------------------------------------------------------

The frequentist approach
========================

Posting patterns
----------------

Common words
------------

Variation in language over time
-------------------------------

Use of gender
-------------

------------------------------------------------------------------------

A sentimental journey
=====================

A basic sentiment pass
----------------------

### The days we wept

### The days we laughed

What was triggering
-------------------

### The horrors we held

### \#MeToo

------------------------------------------------------------------------

The gaps
========

All the likes we can not see
----------------------------

------------------------------------------------------------------------

Appendix
========

### About me

### The code

### Data preperation

Extracted with `tumblr_utils.py`. Cleaned in R.

    files <- c(
        list.files("../tumblr-utils/homers-smut.tumblr.com/json/")
      , list.files("../tumblr-utils/reed-emissions.tumblr.com/json/")
      , list.files("../tumblr-utils/reedrelieves.tumblr.com/json/")
    )
    length(files)

    ## [1] 11485

### Basic statistics

###