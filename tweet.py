import tweepy
# import schedule
import time
import requests
import json
from fact import get_fact

# Authenticate to Twitter
with open('twitter_key.json') as f:
    data = json.load(f)
# Credentials
api_key = data['API_key']
api_secret = data['API_Key_Secret']
bearer_token = r"bearer_token"
access_token = data['access_token']
access_token_secret = data['access_token_secret']


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
# Creating API instance.
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



# Function to tweet a fact
def tweet_fact():
    fact = get_fact()  # Get a fact from the API
    if fact is not None:
        client.create_tweet(text=fact)  # Tweet the fact

# Tweet a fact once
tweet_fact()
