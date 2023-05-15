import tweepy as tw
import pandas as pd
from geopy import geocoders
from geopy.geocoders import Nominatim
from users import TwitterClientAlgo as tca


class GetTweetLocatin:
    def getLocations(self, tweet):
        search_words = "#" + tweet
        date_since = "2023-01-01"
        consumer_key = 'aKBt8eJagd4PumKz8LGmZw'
        consumer_secret = 'asFAO5b3Amo8Turjl2RxiUVXyviK6PYe1X6sVVBA'
        access_token = '1914024835-dgZBlP6Tn2zHbmOVOPHIjSiTabp9bVAzRSsKaDX'
        access_token_secret = 'zCgN7F4csr6f3eU5uhX6NZR12O5o6mHWgBALY9U4'
        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        # Collect tweets
        tweets = tw.Cursor(api.search_tweets, q=search_words, lang="en", since=date_since).items(50)
        print("=====>", tweets.__dict__)

        # user1 = api.get_user("username")
        # location = user.location
        # for x in users_locs:
        #     x[6] = api.get_user(screen_name=x[3])


        # users_locs = [[tweet.id, tweet.user.name, tweet.created_at, tweet.user.screen_name, tweet.text,
        #                tweet.user.location, tweet.coordinates] for tweet in tweets]

        obj = tca.TwitterClient()
        users_locs = [[tweet.id, tweet.user.name, tweet.created_at, tweet.user.screen_name, obj.clean_tweet(tweet.text),
                       tweet.place.name if tweet.place else None,
                       api.get_user(screen_name=tweet.user.screen_name).location]
                      for tweet in tweets]

        # print(users_locs)
        dataframe = pd.DataFrame(data=users_locs,columns=['Tweet ID', 'User Name', 'Created at', 'User Screen Name',
                                                          "Tweets",'Tweet Location', 'User Location'])
        # gn = geocoders.GeoNames()
        # print(gn.geocode("Cleveland, OH 44106"))
        return users_locs, dataframe

        # return users_locs

    def getLatitudeLongitude(self,cityname):

        geolocator = Nominatim(user_agent="saipranavgodishala49@gmail.com")

        location = geolocator.geocode(cityname)
        try:
            return location.latitude, location.longitude,location.address
        except Exception as ex:
            return 0,0,None
