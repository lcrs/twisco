import os, oauth2,json

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth2.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)

def req(url):
	client =oauth2.Client(consumer, token)
	(response, content) = client.request(url)
	return json.loads(content)

acct = req('https://api.twitter.com/1.1/account/verify_credentials.json')

friends = req('https://api.twitter.com/1.1/friends/ids.json?user_id=%s' % acct['id'])

for friend in friends['ids'][0:1]:
	favs = req('https://api.twitter.com/1.1/favorites/list.json?user_id=%s' % friend)
	for fav in favs:
		print fav['text'] + '\n\n'
