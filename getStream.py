import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from elasticsearch import Elasticsearch
import sys

es = Elasticsearch()

class TweetsStreamDataListener(StreamListener):
    # on success
    def on_data(self, data):

        dict_data = json.loads(data)

        print(dict_data)

        es.index(index="tweetstream",
                 doc_type="tweet",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"]})
        return True

    # on failure
    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetsStreamDataListener()

    # set twitter keys/tokens
    consumer_key = "SETKEY"
    consumer_secret = "SETSECRET"
    access_token = "SETACCESSTOKEN"
    access_token_secret = "SETACCESSTOKENSECRET"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=[sys.argv[1]])
