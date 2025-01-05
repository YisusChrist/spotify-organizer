from rich.traceback import install
from spotipy import Spotify

from .auth import authenticate
from .display import (display_currently_playing, display_recently_played,
                      display_saved_tracks)
from .spotify_types import UserSavedTracks
from .track_utils import calculate_total_playtime

# Spotify API scopes
SPOTIFY_SCOPES: list[str] = [
    "user-library-read",
    "user-read-recently-played",
    "user-read-currently-playing",
]


def main() -> None:
    install()

    # Authenticate with Spotify
    sp: Spotify = authenticate(SPOTIFY_SCOPES)

    # Fetch currently playing track
    display_currently_playing(sp)

    # Fetch recently played tracks
    recently_played: UserSavedTracks | None = display_recently_played(sp)
    if not recently_played:
        return

    print(recently_played.keys())

    # Retrieve the user's saved tracks
    display_saved_tracks(sp)

    # You can also calculate total playtime by summing the duration of each track
    total_playtime: float = calculate_total_playtime(recently_played)
    print(f"\nTotal Playtime: {total_playtime:.2f} minutes")


if __name__ == "__main__":
    main()
