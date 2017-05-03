import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from elasticsearch import Elasticsearch

es = Elasticsearch()

class TweetsStreamDataListener(StreamListener):

    def on_data(self, data):

        dict_data = json.loads(data)

        print(dict_data)

        es.index(index="tweetstream",
                 doc_type="tweet",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"]})
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    listener = TweetsStreamDataListener()

    consumer_key = "RK6Gn5h3cq1llfXTz1zY7Hsjx"
    consumer_secret = "X6cqtrIH6Pe8HFk5I9MaKmcW0SjsEksqk8b3fUfcL9L4Vye4LV"
    access_token = "206985484-ZR2aQPnxdzBOpSeuobtH3dDLkO4NLhJRwwGLtrmQ"
    access_token_secret = "lUerNXEmhVlXydVi03tn3LWNPcp1Iy9vaBMeLH2QmRIFZ"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=['#india'])
