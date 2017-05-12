from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from tkinter import *
import os
from tkinter.filedialog import askopenfilename
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizerurl
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
root = Tk()

titleFrame = Frame(root)
titleFrame.pack(fill=X)

mainFrame = Frame(root)
mainFrame.pack(fill=Y)

def summarize():
    SENTENCES_COUNT = numOfSent.get()
    parser = PlaintextParser.from_file(fileName.cget("text"), Tokenizer(LANGUAGE))
        
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    outputFile = open("C://Users//rakesh chandra//Desktop//ATS//output.txt", 'w')
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        outputFile.write("->  ")
        outputFile.write(str(sentence))
        outputFile.write("\n \n")
    os.startfile((fileName.cget("text")))
    os.startfile("C://Users//rakesh chandra//Desktop//ATS//output.txt")
    
def browse():
    filename = askopenfilename()
    fileName.config(text=filename)
    

def webBrowse():
    SENTENCES_COUNT = numOfSent.get()
    parser = HtmlParser.from_url(url.get(), Tokenizer(LANGUAGE))
        
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizerurl(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    outputFile = open("C://Users//rakesh chandra//Desktop//ATS//outputU.txt", 'w')
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        outputFile.write("->  ")
        outputFile.write(str(sentence))
        outputFile.write("\n \n")
    os.startfile("C://Users//rakesh chandra//Desktop//ATS//outputU.txt")

titleLabel = Label(titleFrame, text="Automatic Text Summarizer", bg="black", fg="white", font=('Arial', 28, 'bold'))
titleLabel.pack(fill=X, pady=50, padx=20)

selectLabel = Label(mainFrame, text=": Document Summarization :", font=('Arial', 20))
selectLabel.grid(row=1, column=0, columnspan=4, pady=20)

fileName = Label(mainFrame, text="Choose a Path :",font=('Aerial',10))
fileName.grid(row=2, column=0, pady=20)

selectButton = Button(mainFrame, text="Browse", bg="white", fg="black", font=('Arial', 14), command=browse)
selectButton.grid(row=2, column=2, pady=20)

webLabel = Label(mainFrame, text=": Link Summarization :", font=('Arial', 20))
webLabel.grid(row=4, column=0, columnspan=4, pady=20)


webButton = Button(mainFrame, text="Summarize", bg="white", fg="black", font=('Arial', 14), command=webBrowse)
webButton.config(width=20)
webButton.grid(row=6, column=0, pady=20, columnspan=4)

paste = Label(mainFrame, text="Paste Url here :",font=('Aerial',10))
paste.grid(row=5, column=0, pady=20, padx=10)
url = Entry(mainFrame,text="PAste URl")
url.grid(row=5, column=2, pady=20)

sent = Label(mainFrame, text="Enter the Sentence Count :")
sent.grid(row=0, column=0, pady=20, padx=20)

numOfSent = Entry(mainFrame)
numOfSent.grid(row=0, column=2, pady=20)

summarizeButton = Button(mainFrame, text="Summarize", bg="gray", fg="white", font=('Arial', 14), command=summarize)
summarizeButton.config(width=20)
summarizeButton.grid(row=3, column=0, columnspan=4, pady=20)


    
