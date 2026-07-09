import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# .env laden
load_dotenv()

print("🚀 Script gestartet...")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-top-read",
    show_dialog=True
))

print("🔐 Warte auf Login / Token...")

# Test: Top Tracks abrufen
results = sp.current_user_top_tracks(limit=5)

print("\n🎧 Deine Top Tracks:\n")

for i, item in enumerate(results["items"]):
    name = item["name"]
    artist = item["artists"][0]["name"]
    print(f"{i+1}. {name} - {artist}")

print("\n✅ Fertig!")