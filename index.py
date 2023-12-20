from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
from dict_raperos import artistas_dict1
import createcsv


MAX_RESULTS = 5
author = 'Tino el'
id_aleman = '4QFG9KrGWEbr6hNA58CAqE'
artistas_result1 = {}
id_aczino = '4r1ZDYKzPt3iIjuq8LbT6X'

def get_client():
    client_id = '5b0c6adf9d764c30bcf055369080e7a4'
    client_secret = '81fa5a3f1419487e8987b67af94f97f0'
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    return sp 

def get_artists_data():
    sp_client = get_client()
    for element in artistas_dict1:
        artista_id = element["id"]
        try:
            artista = sp_client.artist(artista_id)
        except Exception as e:
            print(f"Se produjo una excepción: {e}")

        artistas_result1[artista['name']] = artista['followers']['total']
    top = dict(sorted(artistas_result1.items(), key=lambda item: item[1], reverse=True))
    return top

top_100 = get_artists_data()
print(len(top_100))
