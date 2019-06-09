#############################################################################
#
# retrieveList.py                                 
#
# Description:
#  
#	This program retrieves the tweets of the people you follow on 
#	a twitter list.  
#
# History:
#
#       2019.05.21	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python retrieveTheirTweets.py list <sleeptime>
#		where list is mandatory but sleeptime is optional.
#
#############################################################################

import tweepy				# needed to talk to twitter
from tweepy.parsers import JSONParser	# Needed to process json
import json					# needed to process the input file
import ConfigParser			# needed to process the input file
import time					# needed to sleep X seconds
import datetime				# needed for time stamps
import sys					# needed to process input parameters


# Process the input parameters.
if len(sys.argv) == 2:
	myslug = sys.argv[1]
	mysleeptime = 600
	
elif len(sys.argv) == 3:
	myslug = sys.argv[1]
	mysleeptime = int(sys.argv[2])

else:
	print "you need to pass a list name as  input"
	exit(0)

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
#mysleeptime = 600
myhandle = "blm849"
#myslug = "politics"

while True:
	if first_API_call:
		public_tweets = api.list_timeline(myhandle, myslug)
		first_API_call = False
	else:
		public_tweets = api.list_timeline(myhandle,myslug, since_id = my_since_id)
		
	my_count = 0
		
	for tweet in public_tweets:
		print '@' + tweet.user.screen_name, '(' + tweet.user.name + '): ', tweet.text
		if my_count == 0:
			my_since_id = tweet.id
		my_count += 1
	
	# Now sleep before 
        my_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	print '--------------------- ' + my_timestamp + ' --------------------' 
	print 'Retrieved ' + str(my_count) + ' tweets out of ' + str(max_tweets_to_retrieve) +'. Sleeping for ' + str(mysleeptime)
	time.sleep(mysleeptime)
	
    	
