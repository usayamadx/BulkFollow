import json, config
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'count' : 5}
res = twitter.get(url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else:
    print("Failed: %d" % res.status_code)
