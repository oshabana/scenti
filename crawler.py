from lxml import html
import urllib, re
from bs4 import BeautifulSoup
from googlesearch import GoogleSearch
import datetime




def retrieve_data(query,number_results,filter=0):
    '''(str,int,str) -> str
    this will take data from the google searches and 
    '''
    progress_time = number_results / 100
    progress = 0
    text_data = ""
    today = datetime.date.today()
    today_to_str = str(today.year)+str(today.day)
    if filter == 0:
        crawler = GoogleSearch().search("site:news.google.com " + query + " daterange:" + today_to_str ,num_results = number_results)
        print("Scanning google news for: " + query + " today is " + today_to_str)
    elif filter == 1:
        crawler = GoogleSearch().search(query + " daterange:" + today_to_str+"-"+today_to_str,num_results = number_results)
        print("You searched: " + query + " daterange:" + today_to_str )
    else:
        crawler = GoogleSearch().search(query,num_results = number_results)
    for url in crawler.results:
        print("visiting: " )
        text_data += " " + url.getText()
    return text_data
'''
def save_to_file(query,text_data):
    text_file = open(query+".txt","w+")
    text_file.write(text_data)
    text_file.close()
    return text_file.name
    
  '''  

