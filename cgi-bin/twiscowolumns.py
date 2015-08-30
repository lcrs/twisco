#!/usr/bin/python
# Render tweets from twiscod.py's tweets folder into a webpage
# lewis@lewissaunders.com
# TODO:
#	o balance amongst friends?

import os, glob, random

print """Content-Type: text/html

<head>
<title>Twisco</title>
<script>window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
	t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);
 
  t._e = [];
  t.ready = function(f) {
	t._e.push(f);
  };
 
  return t;
}(document, "script", "twitter-wjs"));</script>
<style>
td {
	vertical-align: top;
}
</style>
</head>
<table><tr><td>
"""

tweets = glob.glob('tweets/*/*')

shown = 0
while(shown < min(len(tweets), 35)):
	r = random.randint(0, len(tweets) - 1)
	tweet = tweets[r]
	(friend, twid) = tweet.split('/')[1:]
	seenpath = 'seen/%s/%s' % (friend, twid)
	if(os.path.exists(seenpath)):
		os.rename(tweet, seenpath)
		continue
	
	f = open(tweet)
	html = f.read()
	f.close()

	print html.replace('twitter-tweet', 'twitter-tweet tw-align-center')
	if(shown > 0 and shown % 7 == 0):
		print '\n</td><td>\n'

	try:
		os.makedirs('seen/%s' % friend)
	except:
		pass
	os.rename(tweet, seenpath)
	tweets.pop(r)

	shown = shown + 1

print '\n</td></tr></table>\n'
