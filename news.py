# importing requests package
import requests	
from internet import check_internet_connection
import json

def get_news():
    if check_internet_connection():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
        print("123")
        query_params = { "source": "bbc-news", "sortBy": "top", "apiKey": "5dd86bbde5fe4860ab3e8e7bdb284ca3"}
        print("123")
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            
            # printing all trending news
            print(i + 1, results[i])

        print(results)				
        print("abcd")

    else:
        print("check your internet connection")



