from datetime import datetime

from rich import print
from spotipy import Spotify

from .spotify_types import CurrentPlayingTrack, Track, UserSavedTracks
from .track_utils import format_track_info


def display_currently_playing(sp: Spotify) -> None:
    """
    Display the currently playing track.
    """
    currently_playing: CurrentPlayingTrack | None = sp.currently_playing()
    if not currently_playing or not currently_playing.get("item"):
        print("No currently playing track found.\n")
        return

    print(currently_playing)

    track: Track = currently_playing["item"]
    print("[red]Currently playing track:[/]")
    print(format_track_info(track, ["popularity"]))

    progress: float = currently_playing["progress_ms"] / 1000
    duration: float = track["duration_ms"] / 1000
    print(f"Progress: {progress:.2f} s / {duration:.2f} s")

    print()


def display_recently_played(sp: Spotify) -> UserSavedTracks | None:
    """
    Display recently played tracks.
    """
    recently_played: UserSavedTracks | None = sp.current_user_recently_played()
    if not recently_played or "items" not in recently_played:
        print("No recently played tracks found.")
        return None

    print("[cyan]Recently played tracks:[/]")
    for item in recently_played["items"]:
        track: Track = item["track"]
        print(format_track_info(track, ["popularity", "explicit"]))

    print()

    return recently_played


def display_saved_tracks(sp: Spotify) -> None:
    """
    Display user's saved tracks.
    """
    saved_tracks: UserSavedTracks | None = sp.current_user_saved_tracks()
    if not saved_tracks or "items" not in saved_tracks:
        print("No user saved tracks found.")
        return

    print("[cyan]Saved tracks:[/]")
    for item in saved_tracks["items"]:
        track: Track = item["track"]
        print(format_track_info(track, ["popularity", "explicit"]))
        added_at: datetime = datetime.strptime(item["added_at"], "%Y-%m-%dT%H:%M:%S%z")
        print(f"Added at: {added_at}")

    print()
