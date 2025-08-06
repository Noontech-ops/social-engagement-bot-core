import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def poll_twitter_mentions():
    auth = tweepy.OAuth1UserHandler(
        os.getenv('TWITTER_API_KEY'),
        os.getenv('TWITTER_API_SECRET'),
        os.getenv('TWITTER_ACCESS_TOKEN'),
        os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    api = tweepy.API(auth)
    mentions = api.mentions_timeline()
    return [
        {
            "id_str": mention.id_str,
            "text": mention.text,
            "user": mention.user.screen_name,
            "responded": False
        } for mention in mentions
    ]
