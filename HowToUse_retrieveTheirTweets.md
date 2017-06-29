# twitter_sample_code_python

To use retrieveTheirTweets.py, you will need a few things:

1) You will need a computer that can run python programs. From a command prompt, enter: python -V. If you have python
running, you will get a response like this: Python 2.7.10. If you don't, you will need to install python.
2) You will need to download retrieveTheirTweets.py and twitter.ini file
3) You will need to go here https://apps.twitter.com and create a twitter app. When you do, you will be give a set of keys and access tokens.
The names of the keys and access tokens are in the twitter.ini file. 
4) You will need to replace the keys and access tokens in the twitter.ini file with the ones for your twitter app.

Once you have set up the twitter app and modified twitter.ini, you should be able to enter from a command line:
python retrieveTheirTweets.py

If you are successful, the program will retrieve the tweets of the people you follow, wait for a period of time,
and then retrieve the next batch of tweets. It will do this until you cancel the program running (e.g
by entering Ctrl+c)



