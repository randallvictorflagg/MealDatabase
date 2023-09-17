import schedule
import time,sched
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def inactivate_expired_users():
    pass

def delete_expired_meals():
    pass

def delete_all_meals():
    pass

def job():
    print("I'm working -->",datetime.now().strftime("%Y-%m-%d %H:%M:%S") )


params ={'time_job':30} 