import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests 
import json 
import sqlite3
import os

#scope = "user-library-read"

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='58594f38045e4e0389f0e52dca5df990', client_secret='e8acf222626b4f129cde3a55778e66e6')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#print(sp.artist_top_tracks('13y7CgLHjMVRMDqxdx0Xdo', 'US'))

artist_link = "https://open.spotify.com/artist/13y7CgLHjMVRMDqxdx0Xdo?si=cTv72xSSQBWmobHO9GmjHQ" #gucci mane


#getting artist data, song names, and each of their popularity levels

def ArtistData(artistlink):
    artist = sp.artist(artistlink) #json
    #print(artist)
    artist_id = artist['id']
    results = sp.artist_top_tracks(artist_id)
    track_info = results['tracks']
    #print(track_info)
    lst = []
    for track in track_info:
        trackname = track['name']
        trackpop = track['popularity']
        lst.append((trackname,trackpop)) 
    #print(lst)
    sorted_lst = sorted(lst, key = lambda x:x[1], reverse = True)
    #print(sorted_lst)
    return sorted_lst

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Tracks")
    cur.execute('CREATE TABLE Tracks (name TEXT, popularity INTEGER)')
    lst = ArtistData(artist_link)
    #print(lst)
    for item in lst:
        #print(item)
        cur.execute("INSERT OR IGNORE INTO Tracks (name, popularity) VALUES (?,?)" ,
        (item[0],item[1]))
    conn.commit()
    


ArtistData(artist_link)
setUpDatabase('Tracks.db')


