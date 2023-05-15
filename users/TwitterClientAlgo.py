import re
import tweepy
from tweepy import OAuthHandler

class TwitterClient(object):
	def __init__(self):
		# keys and tokens from the Twitter Dev Console
		consumer_key = 'aKBt8eJagd4PumKz8LGmZw'
		consumer_secret = 'asFAO5b3Amo8Turjl2RxiUVXyviK6PYe1X6sVVBA'
		access_token = '1914024835-dgZBlP6Tn2zHbmOVOPHIjSiTabp9bVAzRSsKaDX'
		access_token_secret = 'zCgN7F4csr6f3eU5uhX6NZR12O5o6mHWgBALY9U4'

		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)

			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
