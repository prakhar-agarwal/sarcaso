import tweepy2
import keys

auth = tweepy2.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy2.API(auth)

sarc_twts = api.search_tweets(include_entities='sarcasm')

print "BEGIN:"
print sarc_twts
print "DONE!"
