import urllib2
import json
import requests
import re

def get_dict(qurl,desc):
    qid = qurl.split('/')[4]
    url = "https://api.stackexchange.com/2.2/questions/{}?site=stackoverflow".format(qid)
    response = requests.get(url)
    data = (json.loads(response.text))
    return {"question": data['items'][0]['link'],
            "tags": data['items'][0]['tags'],
            "title": data['items'][0]['title'],
            "desc": desc}


def get_Json():
    filename = "Canonicals.md"
    list_of_data = (open(filename).read().split("\n\n"))
    list_of_split = [re.match(r'\[(.*?)\]\((.*?)\) ?(.*)',i).groups() for i in list_of_data]
    
    list_of_canons  = [get_dict(i,j) for _,i,j in list_of_split]
    with open("Canonicals.json", 'wb') as outfile:
        json.dump(list_of_canons, outfile)

get_Json()