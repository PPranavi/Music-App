import requests
import os
from dotenv import load_dotenv, find_dotenv
import requests

BASE_URL = 'https://api.genius.com/'

def get_header(access_token):
    load_dotenv(find_dotenv())
    token = os.getenv('GENIUS_ACCESS_TOKEN')
    return {'Authorization': 'Bearer {token}'.format(token=token)}
    
def get_lyrics_link(lyrics_id, header):
    return