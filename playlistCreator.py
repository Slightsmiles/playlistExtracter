from TitleExtractor import Songs
from dotenv import load_dotenv
import os
import requests
# print (Songs)

load_dotenv()
api_key = os.getenv("client_ID")
api_secret = os.getenv("Client_secret")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Returns an access token usable for 60 minutes
def getAccessToken():
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": api_secret
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=data)

    # Print the response
    if response.status_code == 200:
        print("Access Token:", response.json()["access_token"])
        ACCESS_TOKEN = response.json()["access_token"]
        print(ACCESS_TOKEN)
    else:
        print("Error:", response.json())


def searchForSongs():
        for i in range(len(Songs)):
            songTitle = Songs[i][0]
           # print(songTitle)
        songTitle = Songs[0][0]
        url = "https://api.spotify.com/v1/search"
        data = {
            "q": Songs[0][0],
            "type": "track",
            "limit": 1
                }
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",  # Set Bearer token

        }
        
        response = requests.get(url, headers=headers, params=data)
        json = response.json()
        songs = json["tracks"]["items"]
        #print(songs[0].keys())

        
        
        print(len(songs[0]["artists"]))

        #print(songs[0].keys())
#getAccessToken()


#def extractArtists():

searchForSongs()