import tweepy2
import threading
import time
import re
import sys


consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy2.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy2.API(auth_handler=auth, proxy_url='172.31.16.10:8080')
scr_name=sys.argv[1]
print scr_name
user = api.me()

tweet_list = api.user_timeline(scr_name, count=200)
f = open(r'user_tweet_history', 'w')
for tweet in tweet_list:
    f.write(re.sub('\n+', ' ', tweet.text.encode('ascii','ignore'))+"\n")
