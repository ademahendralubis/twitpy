import oauth2 as oauth
import json
import urllib

class TwitterPy:

    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        self.consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
        self.access = oauth.Token(key=access_token,secret=access_token_secret)
        self.client = oauth.Client(self.consumer,self.access)
    
    def show_timeline(self):
        home_timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
        response, data = self.client.request(uri=home_timeline_endpoint)
        if response['status'] == "200":
            tweets = json.loads(data.decode())
            for tweet in tweets:
                print("@{} : {}".format(tweet['user']['screen_name'],tweet['text']))
            print("\n")
            return True
        else:
            print("\nTerjadi kesalahan\n")
            return False
        
    def post_tweet(self,message):
        post_timeline_endpoint = "https://api.twitter.com/1.1/statuses/update.json?status={}".format(urllib.parse.quote(message))
        response, data = self.client.request(uri=post_timeline_endpoint,method="POST")
        if response['status'] == "200":
            print("\npesan berhasil dipost\n")
            return False
        else:
            print("\npesan tidak berhasil berhasil dipost\n")
            return True
        
        
    