from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, mean_absolute_error,mean_squared_error,r2_score
import math

from users.Tweetinfo import GetTweetLocatin
import tweepy

class UserNaiveBayesClass:
    def getNaiveResults(self,df):
        df = df[['latitude','longitude', 'userloc']]
        print("df=",df.head())
        X = df[['latitude', 'longitude']]
        y = df[['userloc']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)
        mae = mean_absolute_error(y_pred,y_test)
        mse = mean_squared_error(y_pred,y_test)
        rmse = math.sqrt(mse)
        r_squared =r2_score(y_pred,y_test)
        print("Naivebayes","Accuracy = ",accuracy,"\t MAE=",mae,"\t MSE=",mse,"\t RMSE=",rmse,"\t r_squared = ",r_squared)
        #return round(accuracy,2),round(mae,2),round(mse,2),round(rmse,2),round(r_squared,2)

        # Tests:
        # consumer_key = 'aKBt8eJagd4PumKz8LGmZw'
        # consumer_secret = 'asFAO5b3Amo8Turjl2RxiUVXyviK6PYe1X6sVVBA'
        # access_token = '1914024835-dgZBlP6Tn2zHbmOVOPHIjSiTabp9bVAzRSsKaDX'
        # access_token_secret = 'zCgN7F4csr6f3eU5uhX6NZR12O5o6mHWgBALY9U4'
        # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)
        # api = tweepy.API(auth, wait_on_rate_limit=True)
        # uu = api.get_user(screen_name='DinakarTalari')

        # user_loc = uu.location
        # print("User location: ", user_loc)
        #
        # print("Tweet locations")
        # tweets = api.user_timeline(screen_name='DinakarTalari', count=10)
        # obbj = GetTweetLocatin()
        # for tweet in tweets:
        #     if tweet.place:
        #         # lattitude, longitude, address = obbj.getLatitudeLongitude(tweet.place.full_name)
        #         place_name = tweet.place.name
        #         place_country = tweet.place.country
        #         bbc = tweet.place.bounding_box.coordinates[0]
        #         print(place_name, "\t", bbc)
        #
        #         # print(tweet.place.name if tweet.place else None)
        #         # print(tweet.coordinates)
        #         # print(tweet,"\n")
        #     # else:
        #     #     print("No location data")
        #
        # hashtag = "#RCBvsKKR"
        # tweets = api.search_tweets(q=hashtag)

        # Print the tweet text and user screen name
        # for tweet in tweets:
            # print(tweet.text)
            # print(tweet.user.screen_name)
            # print(twee)

        # uu = api.get_user(screen_name='DinakarTalari')
        # print(uu)
        # tweet = api.get_status('1625831921619189760')
        # lat, long = tweet.coordinates['coordinates']
        # print(lat, '\t', long)

        return accuracy,mae,mse,rmse,r_squared
