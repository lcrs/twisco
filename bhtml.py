# Render tweets from twiscod.py's tweets folder into a webpage
# lewis@lewissaunders.com
# TODO:
#	o balance amongst friends or random overall?
#	o delete as we render, or soft delete by moving?

import os, glob, random

print """<script>window.twttr = (function(d, s, id) {
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
<table><tr><td>"""

favs = []
friends = glob.glob('tweets/*')
for friend in friends:
	tweets = glob.glob(friend + '/*')
	for tweet in tweets:
		f = open(tweet)
		favs.append(f.read())
		f.close()

for t in range(min(len(favs), 50)):
	randomindex = random.randint(0, len(favs)-1)
	if(t % 10 == 0):
		print '</td><td>'
	print favs[randomindex]
	favs.pop(randomindex)

print '</td></tr></table>'
