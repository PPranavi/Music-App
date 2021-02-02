import requests
import os
from dotenv import load_dotenv, find_dotenv
import requests

BASE_URL = 'https://api.spotify.com/v1/'

def get_access_token():
    load_dotenv(find_dotenv())
    
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    
    return access_token

def get_header(access_token):
    return {'Authorization': 'Bearer {token}'.format(token=access_token)}
    
def get_artist_image(artist_id, header):
     global BASE_URL
     get_url = BASE_URL + 'artists/' + artist_id
     data = requests.get(get_url, headers=header).json()
     image = data['images'][0]['url']
     return image

def get_top_10_tracks(artist_id, header):
    global BASE_URL
    get_url = BASE_URL + 'artists/' + artist_id + '/top-tracks'
    data = requests.get(get_url, headers=header, params={'market':'US'}).json()
    tracks = []
    for i in range(10):
        tracks.append(data["tracks"][i]["name"])
    return tracks
    
def get_tracks_images(artist_id, header):
    global BASE_URL
    get_url = BASE_URL + 'artists/' + artist_id + '/top-tracks'
    data = requests.get(get_url, headers=header, params={'market':'US'}).json()
    tracks_images = []
    for i in range(10):
       tracks_images.append(data["tracks"][i]["album"]["images"][0]["url"])
    return tracks_images
    
def get_tracks_previews(artist_id, header):
    global BASE_URL
    get_url = BASE_URL + 'artists/' + artist_id + '/top-tracks'
    data = requests.get(get_url, headers=header, params={'market':'US'}).json()
    tracks_previews = []
    for i in range(10):
       tracks_previews.append(data["tracks"][i]["preview_url"])
    return tracks_previews