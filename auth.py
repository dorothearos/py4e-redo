"""
Create auth() to retrieve token from .env
"""

import os 

def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

bearer_token = auth()
headers = create_headers(bearer_token)