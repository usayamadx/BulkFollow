import sys
import configparser
import oauth2 as oauth
import json

# CONFIG
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')
API_KEY = config.get('settings', 'API_KEY')
API_SECRET_KEY = config.get('settings', 'API_SECRET_KEY')
ACCESS_TOKEN = config.get('settings', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config.get('settings', 'ACCESS_TOKEN_SECRET')
ENDPOINT = "https://api.twitter.com/1.1/statuses/home_timeline.json"


api = oauth.Consumer(key = API_KEY, secret = API_SECRET_KEY)
access_token = oauth.Token(key = ACCESS_TOKEN, secret = ACCESS_TOKEN_SECRET)
client = oauth.Client(api, access_token)
data = client.request(ENDPOINT)
tweets = json.loads(data)

for tweet in tweets:
    print(tweet['text'])
