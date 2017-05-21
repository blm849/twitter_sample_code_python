#############################################################################
#
# retrieveTheirTweets.py                                 
#
# Description:
#  
#	This program retrieves the tweets of the people you follow on Twitter.
#	It depends on a twitter.ini which contains your API information, such
#	as consumer_key, etc.
#
# History:
#
#       2017.05.21	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python retrieveTheirTweets.py
#
#############################################################################

import tweepy
import json
from tweepy.parsers import JSONParser
import ConfigParser
import time

# The format of twitter.ini is like this (minus the #). Note, no quote around the string
#[DEFAULT]
#consumer_key = your consumer key string
#consumer_secret = your consumer secret string
#access_token = your access token key string
#access_token_secret =your access token secret string	

config = ConfigParser.ConfigParser()
config.read('twitter.ini')

consumer_key = config.get('DEFAULT', 'consumer_key')
consumer_secret =  config.get('DEFAULT', 'consumer_secret')
access_token = config.get('DEFAULT', 'access_token')
access_token_secret = config.get('DEFAULT', 'access_token_secret')

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# For more information (E.g. tweet.id) from https://dev.twitter.com/rest/reference/get/statuses/home_timeline
# Never stop checking until the user cancels the program

mysince_id = 852954224874991616
first_API_call = True
max_tweets_to_retrieve = 100
mysleeptime = 600

while True:
	if first_API_call:
		public_tweets = api.home_timeline()
		first_API_call = False
	else:
		public_tweets = api.home_timeline(since_id = my_since_id)
		# public_tweets = api.home_timeline(count = max_tweets_to_retrieve)
		
	my_count = 0
		
	for tweet in public_tweets:
		# print tweet.id, '@' + tweet.user.screen_name, '(' + tweet.user.name + '): ', tweet.text
		print '@' + tweet.user.screen_name, '(' + tweet.user.name + '): ', tweet.text
		if my_count == 0:
			my_since_id = tweet.id
		my_count += 1
	
	# Now sleep before 
	print '---------------------'
	print 'Retrieved ' + str(my_count) + ' tweets out of ' + str(max_tweets_to_retrieve) +'. Sleeping for ' + str(mysleeptime)
	time.sleep(mysleeptime)
	
    	
