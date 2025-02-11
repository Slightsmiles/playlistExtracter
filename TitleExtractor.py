import requests
import json
from bs4 import BeautifulSoup
import re
## Paths ##
# Url of playlist
url = 'https://music.apple.com/dk/playlist/pure-cardio/pl.f678e1f1f05a4533930082ecdadfb99d'
# 
scriptPath = "./textScript8.json"




def getPlaylist(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        
        #print(response.content)
        text = response.text
        content = response.content
        soup = BeautifulSoup(response.text, 'html.parser')
        x = soup.prettify()
        
        scripts = []
        for script in soup.find_all('script'):
            scripts.append(script)
        
        with open("./text2.txt", "w", encoding="utf-8") as textFile:
            textFile.write(x)
        with open(scriptPath, "w", encoding="utf-8") as scriptFile:
            scriptFile.write(str(scripts[8]))
            scriptFile.close()
        removeHtmlTag()   

    else:
        print("Something went wrong lad")
        print(response.status_code)
        
   

def removeHtmlTag():
    with open(scriptPath, "r", encoding="utf-8") as scriptFile:
        data = scriptFile.read()
    cleaned_data = re.sub(r'<.*?>', "", data)
    jsonData = json.loads(cleaned_data)
    with open(scriptPath, "w", encoding="utf-8") as scriptFile:
        json.dump(jsonData, scriptFile, ensure_ascii=False, indent=4)

def readSongs():
    with open(scriptPath, "r", encoding="utf-8") as dataFile:
        data_dict = json.load(dataFile)
        print(data_dict[0].keys())
    
    ## Contains a list of song entities, each element containing all the meta-data for a song
    data = data_dict[0]['data']['seoData']['ogSongs'] # highly dependant on this structure lol (can use jsonpath_ng to find the path)
    
    print("The number of loaded songs are:", len(data)) ## verify manually (sad)
    return data


def extractTitles(data):
    songs = []
    for song in data:
        title = song['attributes']['name']
        artist = song['attributes']['artistName']
        albumName = song['attributes']['albumName']
        songs.append((title,artist, albumName))
    

    return songs
    
getPlaylist(url)

data = readSongs()

Songs = extractTitles(data) # Tuple of (title, artistName) items½