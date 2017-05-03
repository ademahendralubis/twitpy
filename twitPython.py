import oauth2 as oauth
import json

consumer_key = "2Ur0jIz4F0WUDpIZuX37cHdnX"
consumer_secret = "jARYOQTi6ALsVNX3taUbq673EItsCN8yYBThXlpAGc3mse6V6j"

access_token = "859718216943194112-NerttCXkybHnt01HuPMb699696EX4GN"
access_token_secret = "dLfpIEpw2tnUegiWyMmuvF3VwWJdG5qS6ELL0RQjAQmSA"

consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
access = oauth.Token(key=access_token,secret=access_token_secret)
client = oauth.Client(consumer,access)

home_timeline_endpoint = "https://api.twitter.com/1.1/statuses/update.json?status=tes%20j"

#response, data = client.request(home_timeline_endpoint)
response, data = client.request(uri=home_timeline_endpoint,method="POST")

tweets = json.loads(data.decode())

value = tweets.get('errors')

print(response)

