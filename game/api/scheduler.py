from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from game.api.rankapi import job

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun', hour=16, minute=20)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
    job()

sched.start()