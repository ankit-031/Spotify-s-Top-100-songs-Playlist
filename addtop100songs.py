import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
url="https://www.billboard.com/charts/hot-100/"
# date=input("Enter date in YYYY-MM-DD")
response=requests.get(url+"2022-06-07")
web=response.text
soup=BeautifulSoup(web,"html.parser")
texts=[]
link=soup.find_all("h3", class_="a-no-trucate")
for i in link:
    tex=i.get_text().strip("\t\n")
    texts.append(tex)
username="7g1jv5m15sjqzsayrmzfm15ra"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id="dd8e8ce0f39040eb9b5f7b421f755056",
        client_secret="e6543ef229b2485aae78e356acbadece",
        show_dialog=False,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
text=input("Enter the name of Your Playlist you want to Create :")
des=input("Enter the Description of your Playlist: ")
playlist = sp.user_playlist_create(user=user_id, name=f"{text}",description=f"{des}", public=False)

list=[]
# songs=input("Enter the song your want to add : ")

for song in texts:
    search=sp.search(song)
    list.append(search["tracks"]["items"][0]["uri"])
    # songs = input("Enter the song your want to add : ")
pre=sp.user_playlists(user=username)
play=pre["items"][0]["id"]
sp.playlist_add_items(playlist_id=playlist["id"], items=list)
