# TODO:
#	o ignore favs of replies, search for @username

import os, sys, time, oauth2, json

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

while(True):
	acct = req('https://api.twitter.com/1.1/account/verify_credentials.json')
	friends = req('https://api.twitter.com/1.1/friends/ids.json?user_id=%s' % acct['id'])
	for friend in friends['ids']:
		try:
			os.makedirs('tweets/%s' % friend)
		except:
			pass
		try:
			favs = req('https://api.twitter.com/1.1/favorites/list.json?user_id=%s' % friend)
			for fav in favs:
				f = open('tweets/%s/%s' % (friend, fav['id']), 'w')
				oembed = req('https://api.twitter.com/1.1/statuses/oembed.json?id=%s&omit_script=true' % fav['id'])
				html = oembed['html'].encode('utf-8')
				print html
				f.write(html)
				f.close()
			time.sleep(80)
		except Exception as e:
			print e
			print "Sleeping for 16 minutes..."
			time.sleep(60*16)
			continue
	time.sleep(60)
