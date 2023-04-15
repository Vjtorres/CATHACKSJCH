#Spotify Import
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'd954230d8951443e9e970b9f3dbc9ad5'
client_secret = 'c22718c41105455eab6a2a13968a9d0d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.current_user_playlists()
for playlist in playlists['items']:
    print(playlist['name'])