from typing import Optional, TypedDict


class ExternalURLs(TypedDict):
    spotify: str


class Artist(TypedDict):
    external_urls: ExternalURLs
    href: str
    id: str
    name: str
    type: str
    uri: str


class Image(TypedDict):
    height: int
    width: int
    url: str


class Restrictions(TypedDict):
    reason: str


class Album(TypedDict):
    album_type: str
    artists: list[Artist]
    available_markets: list[str]
    external_urls: ExternalURLs
    href: str
    id: str
    images: list[Image]
    is_playable: bool
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str


class ExternalIDs(TypedDict):
    isrc: str
    ean: Optional[str]
    upc: Optional[str]


class LinkedFrom(TypedDict):
    # If required fields exist in the actual implementation, add them here
    pass


class Track(TypedDict):
    album: Album
    artists: list[Artist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIDs
    external_urls: ExternalURLs
    href: str
    id: str
    is_playable: bool
    linked_from: Optional[LinkedFrom]
    restrictions: Optional[Restrictions]
    name: str
    popularity: int
    preview_url: Optional[str]
    track_number: int
    type: str
    uri: str
    is_local: bool


class Device(TypedDict):
    id: Optional[str]
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    type: str
    volume_percent: Optional[int]
    supports_volume: bool


class Context(TypedDict):
    type: str
    href: str
    external_urls: ExternalURLs
    uri: str


class Actions(TypedDict):
    interrupting_playback: bool
    pausing: bool
    resuming: bool
    seeking: bool
    skipping_next: bool
    skipping_prev: bool
    toggling_repeat_context: bool
    toggling_shuffle: bool
    toggling_repeat_track: bool
    transferring_playback: bool


class PlayedTrack(TypedDict):
    track: Track
    played_at: str
    context: Optional[Context]


class Cursors(TypedDict):
    after: str
    before: str


class UserSavedTracks(TypedDict):
    added_at: str
    track: Track


class CurrentPlayingTrack(TypedDict):
    device: Device
    repeat_state: Optional[str]
    shuffle_state: Optional[bool]
    context: Optional[Context]
    timestamp: int
    progress_ms: int
    is_playing: bool
    item: Track
    currently_playing_type: Optional[str]
    actions: Optional[Actions]


class RecentlyPlayedTracks(TypedDict):
    href: str
    limit: int
    next: Optional[str]
    cursors: Cursors
    total: int
    items: list[PlayedTrack]
