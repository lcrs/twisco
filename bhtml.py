# TODO:
#	o delete as we render, or soft delete?
#	o layout

import os, glob

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
}(document, "script", "twitter-wjs"));</script>"""

h = open('t.html', 'w')
h.write(twheader)

friends = glob.glob('tweets/*')
for friend in friends:
	tweets = glob.glob(friend + '/*')[0:0]
	for tweet in tweets:
		f = open(tweet)
		h.write(f.read())
		f.close()
