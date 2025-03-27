import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BASE_URL = "https://www.billboard.com/charts/hot-100/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

SPOTIFY_CLIENT_ID = os.environ.get("SPOt_CLIENT_ID")
SPOTIFY_SECRET = os.environ.get("SPOt_SECRET")
SPOTIFY_NAME = os.environ.get("SPOt_NAME")


def get_user_date():
    date_string = input("What date would like to travel too? Use this format YYYY-MM-DD: ")
    return date_string

def get_song_list(user_url):
    try:
        response = requests.get(url=user_url, headers=header)
    except e:
        print(e)
    else:
        billboard_webpage = response.text
        soup = BeautifulSoup(billboard_webpage, 'html.parser')
        song_title_elems = soup.select("li ul li h3")

        song_list = [song.getText().lstrip().rstrip() for song in song_title_elems if song.getText().lstrip().rstrip() not in ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', 'Follow Us', 'Have a Tip?', 'The Daily', 'Have a Tip?', 'Subscriptions']]
        return song_list

#user_date = get_user_date()
user_date = "2000-08-12"

user_url = BASE_URL + user_date

song_list = get_song_list(user_url)
print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_NAME,
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = user_date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)