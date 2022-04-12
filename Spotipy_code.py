import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests 
import json 

#scope = "user-library-read"

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='58594f38045e4e0389f0e52dca5df990', client_secret='e8acf222626b4f129cde3a55778e66e6')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#export SPOTIPY_CLIENT_ID='58594f38045e4e0389f0e52dca5df990'
#export SPOTIPY_CLIENT_SECRET='e8acf222626b4f129cde3a55778e66e6'
#export SPOTIPY_REDIRECT_URI='https://www.spotify.com/us/'

#how many plays an artist is getting on spotify#
artist_link = "https://open.spotify.com/artist/13y7CgLHjMVRMDqxdx0Xdo?si=cTv72xSSQBWmobHO9GmjHQ" #gucci mane
artist = sp.artist(artist_link)
#artist_data = artist.json()
#print(artist)
artist_id = requests.get(artist_link).json()
#print(json.dumps(artist_id, indent = 2))
#print (artist_id)
#playlist_URI = playlist_link.split("/")[-1].split("?")[0]
#track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]


'''def SpotifySearch(search_term):
    #only music tracks
    website = requests.get('https://itunes.apple.com/search', params = {'term':search_term,
                                                                        'media':'music',
                                                                
        
    })
    term_data = website.json()
#     print(term_data)
song_lst = [] #lst of dictionaries returned by iTunessearch
user_input = input('Enter a search term (or "done" to stop): ')
while True:
    if user_input == 'done':
        break
    else:
        song_lst += (iTunesSearch(user_input))'''
