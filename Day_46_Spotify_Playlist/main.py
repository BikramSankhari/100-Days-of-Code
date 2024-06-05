import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIEND_ID = "92cbfd61e0384cb790f35b243810a8d5"
SECRET_KEY = "a77a1a563a0a44e4a972f4d67d5321c7"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIEND_ID,
        client_secret=SECRET_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]