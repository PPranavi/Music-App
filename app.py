from flask import Flask, render_template
import random
import requests
import os
from dotenv import load_dotenv, find_dotenv
from spotify import get_access_token, get_header, get_top_10_tracks, get_artist_image, get_tracks_images, get_tracks_previews, get_artist_spotify_link
from genius import get_all_tracks_lyrics_links
from twitter import get_twitter_page

app = Flask(__name__)

@app.route('/')

def hello_world():
    # authorization flow for Spotify API
    access_token = get_access_token()
    header = get_header(access_token)
    
    # hardcoded artist ids
    reference = ["Shawn Mendes", "BLACKPINK", "Panic! At The Disco", "Dua Lipa", "Zedd"]
    artists_id = ["7n2wHs1TKAczGzO7Dd2rGr", "41MozSoPIsD1dJM0CLPjZF", "20JZFwl6HVl6yg8a4H3ZqK", "6M2wZ9GZgrQXHCFfjv46we", "2qxJFvFYMEDqd7ui6kSAcq"]
    
    # to simulate dynamic functionality in web app
    random_number = random.randint(0,4) 
    random_track = random.randint(0,9)
    
    # retrieved from hardcoded information
    artist_name = reference[random_number]
    artist_id = artists_id[random_number]
    
    # retrieved from helper methods from Spotify methods class
    artist_img = get_artist_image(artist_id, header)
    artist_spotify_link = get_artist_spotify_link(artist_id)
    artist_twitter_link = get_twitter_page(artist_name)
    tracks = get_top_10_tracks(artist_id, header)
    tracks_images = get_tracks_images(artist_id, header)
    tracks_previews = get_tracks_previews(artist_id, header)
    
    # retrieved from helper methods from Genius methods class
    tracks_lyrics_links = get_all_tracks_lyrics_links(tracks)
    
    # push variable information to html file
    return render_template(
        "index.html",
        name = artist_name,
        image = artist_img,
        spotify_link = artist_spotify_link,
        twitter_link = artist_twitter_link,
        tracks = tracks,
        len = len(tracks),
        track_name = tracks[random_track],
        track_preview = tracks_previews[random_track],
        track_image = tracks_images[random_track],
        tracks_lyrics_links = tracks_lyrics_links
    )

# ensures that web app runs on port 8080
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)