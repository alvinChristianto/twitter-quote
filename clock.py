#######
import os
import tweepy
from secrets import *
from quotes import *
from time import gmtime, strftime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = 12)
def scheduled_job():
    #print('This job is run every three minutes.')
   
    # Twitter authentication
    QUOTE, AUTHOR = getData() 
    text = QUOTE + "\n by ~  " + AUTHOR
    
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:

        api.update_status(text)
        print("result : "+ text)
        print("len Quotes :"+ len(QUOTE))
    except tweepy.error.TweepError as e:
        pass#log(e.message)
    else:
        pass#log("Tweeted: " + text) 

sched.start()
#timed_job()
