from os import system
import requests
import json
import mac_say

def speak(str):
    system(str)

if __name__=='__main__':
    

    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c474659cc91c473c8b0ffeb9418bbda3')
    response_dict = response.json()

    j_dump=json.dumps(response_dict, indent=4, sort_keys=True)

    articles=response_dict.get("articles")

    for article in articles:
        title = article.get("title", "")
        print(title)
        mac_say.say(title)

    
    # speak()