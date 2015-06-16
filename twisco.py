# TODO:
#	o ignore favs of replies, search for @username

import os, sys, time, tempfile, oauth2, json

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
	for friendid in friends['ids']:
		friendname = req('https://api.twitter.com/1.1/users/show.json?user_id=%s' % friendid)['screen_name']
		friendfolder = 'tweets/%s' % friendid
		try:
			os.makedirs(friendfolder)
		except:
			pass
		try:
			favs = req('https://api.twitter.com/1.1/favorites/list.json?user_id=%s' % friendid)
			for fav in favs:
				if(friendname in fav['text']):
					print "%s Ignoring boring reply %s" % (time.strftime("%Y%m%d %H:%M:%S"), fav['text'])
					continue
				oembed = req('https://api.twitter.com/1.1/statuses/oembed.json?id=%s&omit_script=true' % fav['id'])
				html = oembed['html'].encode('utf-8')
				tmp = tempfile.NamedTemporaryFile(dir='.', delete=False)
				tmp.write(html)
				tmp.close()
				os.rename(tmp.name, '%s/%s' % (friendfolder, fav['id']))
				print "%s From friend %s collected %s" % (time.strftime("%Y%m%d %H:%M:%S"), friendid, fav['id'])
			time.sleep(80)
		except Exception as e:
			print "%s Exception, sleeping for 16 minutes: %s %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e)
			time.sleep(60*16)
			continue
	time.sleep(60)
