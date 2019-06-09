#############################################################################
#
# retrieveTrendingInformation.py                                
#
# Description:
#  
#	This program retrieves the Twitter trending information for a specific 
#   location.
#   It is based on the information found here:
#   https://dev.twitter.com/rest/reference/get/trends/place
#
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
# Comment the next line if testing
#config.read('twitter.ini')
# UnComment the next line if testing
config.read('twitter.blm849.ini')


consumer_key = config.get('DEFAULT', 'consumer_key')
consumer_secret =  config.get('DEFAULT', 'consumer_secret')
access_token = config.get('DEFAULT', 'access_token')
access_token_secret = config.get('DEFAULT', 'access_token_secret')

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret)

# Resource URL 
# https://api.twitter.com/1.1/trends/place.json
# Tweepy APIs
# API.trends_available()
# API.trends_place(id[, exclude])
# API.reverse_geocode([lat][, long][, accuracy][, granularity][, max_results])
# API.geo_id(id)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

trends_available = api.trends_available()
# Canada 23424775, Van 9807, Tor 4118, Cgy 8775, Mtl 3534
# Halifax 4177
trends_place = api.trends_place("4118")
#revgeo = api.reverse_geocode("46.196919", "-59.134123")
#print revgeo.result
#exit

#public_tweets = api.home_timeline()
#for tweets in public_tweets:
#	print tweets
#	print "----------"
	

trends_place = api.trends_place("23424775")
trends1 = api.trends_place("8775") # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
for trend in trends:
	print trend['name']
	
#names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
#trendsName = ' '.join(names)
#print(trendsName)



 
