import requests
import os
from dotenv import load_dotenv, find_dotenv
import requests

def get_twitter_page(artist_name):
    search_url = "https://twitter.com/"
    artist_name = artist_name.split(" ")
    artist_name = ''.join(artist_name)
    return search_url+artist_name