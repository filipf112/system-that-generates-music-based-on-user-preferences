import spotipy
import os
from openai import OpenAI



from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotipy client
client_id = ''
client_secret = ''

a14463ab590542a0bad60caf3ed46af2
38782bd1a3d448b99f440e8b196935c0

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Playlist URI
playlist_uri = 'https://open.spotify.com/playlist/5sgeXXeGZ88ivIAyMFUt4K?si=b3f8d0ce8018490c'

# Get tracks from the playlist
results = sp.playlist_tracks(playlist_uri)

# Print track names and extract genres from each track
print("Track Names and Genres in the playlist:")
for track in results['items']:
    # Retrieve track details
    track_details = track['track']

    # Extract track name
    track_name = track_details['name']

    # Extract artists from the track
    artists = track_details['artists']

    # Initialize a list to store genres for the track
    track_genres = []

    # Iterate over artists to get their genres
    for artist in artists:
        # Get artist details
        artist_details = sp.artist(artist['id'])

        # Extract genres from the artist
        artist_genres = artist_details['genres']

        # Add genres to the list
        track_genres.extend(artist_genres)

    # Remove duplicate genres
    track_genres = list(set(track_genres))

    # Print track name and genres
    print(f"Track Name: {track_name}")
    print("Genres:", ", ".join(track_genres))
    print()



