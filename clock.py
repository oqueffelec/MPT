from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from game.api.rankapi import job

sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=3)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
    #job()

sched.start()