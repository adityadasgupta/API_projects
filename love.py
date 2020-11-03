import sys
import os
import json
import tweepy as tw
from datetime import datetime, timedelta 

def Average(lst): 
    return sum(lst) / len(lst)

auth = tw.AppAuthHandler(consumer_api, consumer_api_secret)
api = tw.API(auth)

td = api.get_user("realDonaldTrump")
biden = 'Biden'
sleepy = 'Sleepy'
joe = 'Joe'
bidenCount = 0
count = 0
num = 5000
lst = []

#end_date = datetime.utcnow() - timedelta(days=365)
for i in range(0,20):
    for status in tw.Cursor(api.user_timeline, id = "realDonaldTrump", count = num).items(num):
        string = str(status.text)
        if ((biden in string) or (sleepy in string) or (joe in string)):
            #print(string)
            bidenCount +=1
        count+=1
        if(count!=num):
            continue
    perc = bidenCount*100/count
    if(perc!= 0.0):
        lst.append(perc)
    


print("% of the_TD's tweets about Joe Biden --> ", round(Average(lst), 2))
