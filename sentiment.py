# -*- coding: utf-8 -*-

import os
import sys
import nltk
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file = open("C:\\Users\\omars\scenti\\Text.txt","r")
string = file.read()
sia = SentimentIntensityAnalyzer()
senti = sia.polarity_scores(string)
senti_list = [senti['pos'],senti['neg'],senti['neu'],senti['compound']]
scenti = sia.score_valence(senti_list,string)
#print(string)
print(senti)
print(scenti['pos'])
print(scenti)