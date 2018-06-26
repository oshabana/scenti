# -*- coding: utf-8 -*-

import os
import sys
import nltk
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(text_data,query):
    #text_file = open(file_location,permissions)
    #string = text_file.read()
    sia = SentimentIntensityAnalyzer()
    senti = sia.polarity_scores(text_data)
    senti_list = [senti['pos'],senti['neg'],senti['neu'],senti['compound']]
    scenti = sia.score_valence(senti_list,text_data)
   # text_file.close()
    print (query + " has a positivity score of: " + str(senti['pos']*100 ) + "%"
           + " \n"+query +" has a negativity score of: " + str(senti['neg']*100)
           + "%"
           )
    print(query + " has a neutrality score of " + str(senti['neu']*100) + "%")
    print(query + " has a score valence of: "+str(scenti))