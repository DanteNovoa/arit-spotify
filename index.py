from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
from dict_raperos import artistas_dict1
import createcsv

app = Flask(__name__)

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

def get_top_100():
    sp_client = get_client()
    for artista in artistas_dict1:
        artista_id = artista["id"]
        try:
            artista = sp_client.artist(artista_id)
        except Exception as e:
            print(f"Se produjo una excepción: {e}")

        artistas_result1[artista['name']] = artista['followers']['total']
    top = dict(sorted(artistas_result1.items(), key=lambda item: item[1], reverse=True))
    return top

def get_top_track_for_artist(artist: str):
    sp_client = get_client()
    result = sp_client.artist_top_tracks(artist)
    for track in result['tracks'][:11]:
        pprint(track['name'])

@app.route('/')
def index():
    get_top = get_top_100()
    nombres = get_top.keys()
    valores = get_top.values()

    lista = get_top.items()
    top100 = list(lista)[:120]
    top100dict = dict(lista)
    createcsv.create_csv(top100)

    return render_template('index.html', nombres=nombres, valores=valores)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        song_name = request.form['song_name']
        sp_client = get_client()
        result = sp_client.search(q=song_name, type='track', limit=1)

        if result['tracks']['items']:
            song = result['tracks']['items'][0]
            song_name = song['name']
            song_image = song['album']['images'][0]['url']
            
            return render_template('search_result.html', song_name=song_name, song_image=song_image)
        else:
            return render_template('search_result.html', error_message="Song not found")

if __name__ == '__main__':
    app.run(debug=True)
