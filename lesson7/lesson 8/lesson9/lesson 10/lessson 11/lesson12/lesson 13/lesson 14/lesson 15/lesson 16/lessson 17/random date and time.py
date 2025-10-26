import random
import time

def getrandomdate(startdate,enddate):
    randomgenerator =random.random()
    dateformat="%m/%d/%Y"
    
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate

print("ramdom date is",getrandomdate("1/1/2016","12/12/2018"))