
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import keys
import webapp2

text = '<title>sarcaso<title><head>Web under maintnce<br></head>'

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        #print data
	self.response.write(data)
        return True

    def on_error(self, status):
        #print status
	self.response.write(status)


class MainPage(webapp2.RequestHandler):
    def get(self):
	
	self.response.headers['Content-Type'] = 'text/html'
	self.response.write(text)
	    
        l = StdOutListener()
	auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
	auth.set_access_token(keys.access_token, keys.access_token_secret)
	
	stream = Stream(auth, l)
	stream.filter(track=['basketball'])

application = webapp2.WGSIApplication([
    ('/',MainPage),
], debug=True)
