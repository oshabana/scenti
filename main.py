import sentiment
import crawler
import time

def scenti(query, num, filter=""):
    start_time = time.time()
    text = crawler.retrieve_data(query,num, filter)
    sentiment.sentiment(text,query)
    print("--- %s seconds ---" % (time.time() - start_time))
    

scenti("bitcoin", 7, 0)
    