# Automatic Text Summarizer

This is a python implementation of automatic text summarizer using LexRank and Luhn algorithm for extracting summary from a single plain text document and HTML pages also supports json file format.

## Implemented summarization methods

[LexRank](http://tangra.si.umich.edu/~radev/lexrank/lexrank.pdf) - Unsupervised approach inspired by algorithms PageRank and HITS 

[Luhn - heurestic method](http://dl.acm.org/citation.cfm?doid=321510.321519)


## Installation:

Make sure you have Python 2.7/3.3+ and pip (Windows, Linux) installed and run the following commands: 

```$ [sudo] pip install numpy```

```$ [sudo] pip install nltk```

```$ [sudo] pip install summa```

```$ [sudo] pip install networkx```
 
## Usage:

* Change outputFile directory in textSummarizerGui.py edit file path for output where you want to save the file.

* Run <b>textSummarizerGui.py</b>

* In summarizer GUI - set number of sentences you want in summary (Senetence count)

  Two options are there :

  1. <b>Document summarization</b>: (if you want to summarize any plain text document)

  2. <b>Link summarization</b>: (if you want to summarize from HTML page)
      * Enter URL : (for HTML page) 
      * Click Summarize button
      * Two windows will be shown: 1) Input file and 2)Output file with summarized text.
      
<hr>      