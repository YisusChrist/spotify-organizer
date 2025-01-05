import os

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Set this in your Spotify Developer Dashboard
REDIRECT_URI = "http://localhost:3000/callback"


def authenticate(scopes: list[str]) -> Spotify:
    # Load environment variables
    load_dotenv()

    # Load the Client ID and Client Secret from environment variables
    client_id: str | None = os.getenv("SPOTIFY_CLIENT_ID")
    if not client_id:
        raise ValueError("SPOTIFY_CLIENT_ID is not set in the environment.")
    client_secret: str | None = os.getenv("SPOTIFY_CLIENT_SECRET")
    if not client_secret:
        raise ValueError("SPOTIFY_CLIENT_SECRET is not set in the environment.")

    # Create a Spotify object
    return Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=REDIRECT_URI,
            scope=" ".join(scopes),
        )
    )
