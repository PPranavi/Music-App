import requests
import os
from dotenv import load_dotenv, find_dotenv
import requests

BASE_URL = 'https://api.genius.com/'

def get_header():
    load_dotenv(find_dotenv())
    token = os.getenv('GENIUS_ACCESS_TOKEN')
    return {'Authorization': 'Bearer {token}'.format(token=token)}
    
def get_lyrics_link(track_title):
    header = get_header()
    search_url = BASE_URL + "search"
    data = requests.get(search_url, data={'q':track_title}, headers=header).json()
    return "https://genius.com" + data["response"]["hits"][0]["result"]["path"]

def get_all_tracks_lyrics_links(tracks):
    tracks_lyrics_links = []
    for track in tracks:
        lyrics_link = get_lyrics_link(track)
        tracks_lyrics_links.append(lyrics_link)
    return tracks_lyrics_links
    
    