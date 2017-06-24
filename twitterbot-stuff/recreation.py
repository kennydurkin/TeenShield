# Rec centers

import twitter
import json
import time
from twitterkeys import settings
from pprint import pprint

#OAuth credentials
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

with open('recreation.json') as data_file:    
    rec_center_data = json.load(data_file)

pprint(rec_center_data)

# for rec_center in rec_center_data:
	# tweet = time.strftime("%I:%M%p") + ': Check out ' + shelter['center_name'] + ' shelter. ' + shelter['location_1_location'] + ' in ' + shelter['borough'] + '. ' + shelter['comments'] + '.'
	# print tweet
	# print len(tweet)

	#post to twitter
	# try:
	#     api = twitter.Api(
	#     consumer_key = consumer_key,
	#     consumer_secret = consumer_secret,
	#     access_token_key = access_token_key,
	#     access_token_secret = access_token_secret)

	#     # print(api.VerifyCredentials())

	#     status = api.PostUpdate(tweet)
	#     print ' post successful!!!'

	# except twitter.TwitterError as err:
	# 	print err.message
	# 	print 'error posting!'

	# time.sleep(2.0) # wait 2 seconds before sending another tweet