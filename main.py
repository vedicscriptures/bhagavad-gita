import tweepy
from bgapi import *
import os

# Getting sloks from Bhagavad Gita API
Slok = Slokm()

# Tweet Text limit
Post = (Slok[:277] + '..') if len(Slok) > 280 else Slok

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ["APIKey"],os.environ["APISecretKey"])
auth.set_access_token(os.environ["AccessToken"],os.environ["AccessTokenSecret"])
api = tweepy.API(auth)

# Tweet Posting
try:
    api.verify_credentials()
    print("Authentication OK")
    api.update_status(Post)
    print("Posted")
except Exception as error:
    print(f"Error during authentication :\n{error}")
