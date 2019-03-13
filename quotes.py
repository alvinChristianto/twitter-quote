import requests
import json

def getData():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        }
    params = (
        ('category', 'inspire'),    )
    response_1 = requests.get('http://quotes.rest/qod.json', headers=headers, params=params)
    response = response_1.json()

    QUOTE = response['contents']['quotes'][0]['quote']
    AUTHOR = response['contents']['quotes'][0]['author']
    
    return (QUOTE, AUTHOR)
#Data1 = Data['quotes']
#Data2 = Data1[0]
#Data3 = Data2['quote']
#print Data3


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://quotes.rest/qod.json?category=inspire', headers=headers)

