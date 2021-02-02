from flask import Flask, render_template
import random
import requests
import os
from dotenv import load_dotenv, find_dotenv
from methods import get_access_token
from spotify import get_header, get_top_10_tracks, get_artist_image, get_tracks_images, get_tracks_previews

app = Flask(__name__)

@app.route('/')

def hello_world():
    access_token = get_access_token()
    
    header = get_header(access_token)
    
    reference = ["Shawn Mendes", "BLACKPINK", "Panic! At The Disco", "Dua Lipa", "Zedd"]
    artists_id = ["7n2wHs1TKAczGzO7Dd2rGr", "41MozSoPIsD1dJM0CLPjZF", "20JZFwl6HVl6yg8a4H3ZqK", "6M2wZ9GZgrQXHCFfjv46we", "2qxJFvFYMEDqd7ui6kSAcq"]
    
    random_number = random.randint(0,4) 
    random_track = random.randint(0,9)
    
    artist_name = reference[random_number]
    artist_id = artists_id[random_number]
    artist_img = get_artist_image(artist_id, header)
    
    tracks = get_top_10_tracks(artist_id, header)
    tracks_images = get_tracks_images(artist_id, header)
    tracks_previews = get_tracks_previews(artist_id, header)
    
    print(tracks[random_track])
    print(tracks_images[random_track])
    print(tracks_previews[random_track])
    
    return render_template(
        "index.html",
        name = artist_name,
        image = artist_img,
        tracks = tracks,
        len = len(tracks),
        track_name = tracks[random_track],
        track_preview = tracks_previews[random_track],
        track_image = tracks_images[random_track]
    )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)