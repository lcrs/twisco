import os, oauth2
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth2.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth2.Client(consumer, token)

print client.request('https://api.twitter.com/1.1/statuses/home_timeline.json')
