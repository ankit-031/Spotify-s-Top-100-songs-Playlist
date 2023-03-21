import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope="playlist-modify-public"
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
songs=input("Enter the song your want to add : ")

while songs!="quit":
    search=sp.search(songs)
    list.append(search["tracks"]["items"][0]["uri"])
    songs = input("Enter the song your want to add : ")
pre=sp.user_playlists(user=username)
play=pre["items"][0]["id"]
sp.playlist_add_items(playlist_id=playlist["id"], items=list)