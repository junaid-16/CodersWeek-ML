import tweepy
import csv
import pandas as pd

consumer_key='UP58QSui5J78pjsTK6giWNvCZ'
consumer_secret='tIKjFuqmfNwgczHn5Zp4ZEYb20H1mZEn8ta9SgQZjYbevoZ75N'
access_token='854948293868011520-sFnj4GbxUX32Pf64pDPcgbN0JIYB02y'
access_token_secret='BJTWlUBLprZT9P0LaYuTrwWxJO7Ur43ygPsbSmmwDZQVJ'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('tweets2.csv','a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#China", count = 200,lang='en',since='2020-06-01').items():
    print(tweet.created_at,tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8')])
