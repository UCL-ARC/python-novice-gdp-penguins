---
permalink: index.html
site: sandpaper::sandpaper_site
---

The best way to learn how to program is to do something useful,
so this introduction to Python is built around a common scientific task:
**data analysis**.

### Scenario: Analysing GDP data from countries around the world

We've got a set of files containing GDP data from countries around the world, separated 
into CSV files per continent.  Each CSV file contain one row per country and multiple 
columns per years when the GDP were recorded.

We need to analyse it to see if we understand some global trends across the years.

To do so we would like to:

1. Calculate the minimum, maximum and  average GDP per continent per year.
2. Plot the result to discuss and share with colleagues.

<!-- TODO: flowchart of the analysis -->
<!-- ![](episodes/fig/lesson-overview.svg "Lesson Overview"){alt='3-step flowchart shows inflammation data records for patients moving to the Analysis stepwhere a heat map of provided data is generated moving to the Conclusion step that asks thequestion, How does the medication affect patients?'} -->

### Data Format

The data sets are stored in
[comma-separated values](learners/reference.md#comma-separated-values) (CSV) format:

- each row holds information for a single country,
- columns represent years when the GDP were recorded.

The first three rows of our first file look like this, first line contains the header of the file:

```source
country,1952,1957,1962,1967,1972,1977,1982,1987,1992,1997,2002,2007
Algeria,2449.008185,3013.976023,2550.81688,3246.991771,4182.663766,4910.416756,5745.160213,5681.358539,5023.216647,4797.295051,5288.040382,6223.367465
Angola,3520.610273,3827.940465,4269.276742,5522.776375,5473.288005,3008.647355,2756.953672,2430.208311,2627.845685,2277.140884,2773.287312,4797.231267
```

Each number represents the GDP per capita for that particular country on the given year.

For example, value "3008.647355" at row 3 column 7 of the data set above means that Angola had a
GDP per capita of approximately $3,008.65 in 1977.

In order to analyze this data and report to our colleagues, we'll have to learn a little bit
about programming.

::::::::::::::::::::::::::::::::::::::::::  prereq

## Prerequisites

You need to understand the concepts of **files** and **directories** and how to start a Python
interpreter before tackling this lesson. This lesson sometimes references Jupyter
Lab although you can use any Python interpreter mentioned in the [Setup][lesson-setup].

The commands in this lesson pertain to any officially supported Python version, currently **Python
3\.7+**.  Newer versions usually have better error printouts, so using newer Python versions is
recommend if possible.


::::::::::::::::::::::::::::::::::::::::::::::::::

### Getting Started

To get started, follow the directions on the "[Setup][lesson-setup]" page to download data
and install a Python interpreter.




