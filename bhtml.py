# TODO:
#	o delete as we render, or soft delete?

import os, glob, random

twheader = """<script>window.twttr = (function(d, s, id) {
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
</style>"""

h = open('t.html', 'w')
h.write(twheader)

favs = []

friends = glob.glob('tweets/*')
for friend in friends:
	tweets = glob.glob(friend + '/*')[0:9]
	for tweet in tweets:
		f = open(tweet)
		favs.append(f.read())
		f.close()

h.write('<table><tr><td>')
for t in range(min(len(favs), 50)):
	randomindex = random.randint(0, len(favs)-1)
	if(t % 10 == 0):
		h.write('</td><td>')
	h.write(favs[randomindex])
	favs.remove(favs[randomindex])
h.write('</td></tr></table>')
h.close()
