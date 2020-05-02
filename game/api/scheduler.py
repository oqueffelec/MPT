from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from game.api.rankapi import job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, trigger='cron', day_of_week='sat', hour='12', minute='30')
    scheduler.start()