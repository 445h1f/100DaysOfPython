import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import os
from pprint import pprint

# getting spotify environment variable
envFile = dotenv.find_dotenv()
dotenv.load_dotenv(envFile)
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# setting spotifyClient to communicate spotify API

spotifyClient = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

spotifyUser = spotifyClient.current_user()
# pprint(spotifyUser)

# greeting user
print(f'Hello {spotifyUser["display_name"]}!')

# asking user to enter date
date = input('Which year do you want to tarvel to? Type the date in format YYYY-MM-DD: ')

print(f'Hang on! Getting top 100 songs of {date}.')

topSongsUrl = f'https://www.billboard.com/charts/hot-100/{date}'

# making request to topSongsUrl and getting content
response = requests.get(topSongsUrl)
html = response.text

# parsing html to beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# scraping all song names
songElements = soup.select('li > #title-of-a-story')
songNames = [element.getText().strip() for element in songElements]
# print(songNames)
print(f'Got songs! Searching them Spotify now...')
songData = {}

# searching song on spotify and storing in dict
for song in songNames:
    search = spotifyClient.search(q=song, type="track")
    try:
        items = search['tracks']['items']
        for result in items:
            name = result['name']
            # adding song uri in dict if song name matches with query
            if name.lower() == song.lower():
                songURI = result['uri']
                songData[song] = songURI
                break # exiting loop because search found (no need to look next item)
    except:
        print(f'Error for {song}!')
songURIs = [songData[data] for data in songData]

print(f'Search Completed! Creating playlist and adding them now...')

# creating spotify playlist for user and adding top 100 songs in it.

playlistName = f'Top 100 of {date}'
createPlaylist = spotifyClient.user_playlist_create(
    user=spotifyUser['id'],
    name=playlistName,
    public=False # private playlist
    )

spotifyClient.playlist_add_items(
    playlist_id=createPlaylist['id'],
    items=songURIs
)

print(f'{spotifyUser["display_name"]}, your song memories of {date} has been created!')