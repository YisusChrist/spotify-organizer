from datetime import timedelta
from typing import Optional

from .spotify_types import Track, UserSavedTracks


def format_track_info(track: Track, extra_info: Optional[list[str]] = None) -> str:
    """
    Format track information as a string.
    """
    artist: str = track["artists"][0]["name"]
    name: str = track["name"]
    album: str = track["album"]["name"]
    track_id: str = track["id"]

    info: list[str] = [f"([orange1]{track_id}[/]) '{album}' - '{name}' by '{artist}'"]
    if extra_info:
        for key in extra_info:
            if key in track:
                info.append(f"{key.capitalize()}: {track[key]}")

    return "\n".join(info)


def calculate_total_playtime(recently_played: UserSavedTracks) -> float:
    """
    Calculate total playtime in minutes from a list of recently played tracks.
    """
    total_duration_ms: int = sum(
        item["track"]["duration_ms"] for item in recently_played["items"]
    )
    return timedelta(milliseconds=total_duration_ms).total_seconds() / 60
