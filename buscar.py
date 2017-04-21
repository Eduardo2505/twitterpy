
from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['comida', 'barato']) # let's define all words we would like to have a look for
    tso.set_language('es') # we want to see German tweets only
    tso.set_geocode(19.350000,-99.150002,5,imperial_metric=True)
    tso.set_result_type('recent')
    tso.set_count(42)
    #tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
    	consumer_key = 'aFXfsYucGeY1JDVYd0jZBQRDy',
    	consumer_secret = 'w3ZFtpJiyYFz0aAUhJMc6pBK9bFDzkTWQGlo6thI9BkdmW9T84',
    	access_token = '3033706820-ibVYRaDKIRlgsDDQQ0gwM0tb811FYjWNeH42LeC',
    	access_token_secret = 'LsseJl4Xpnx8cT9ukAQtqM755YXz43lk3YcZTBRHcX1AD'
    	)

     # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
     	   print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
print(e)