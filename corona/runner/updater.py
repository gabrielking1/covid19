from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from runner import worker


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(worker.worker, 'interval', minutes=5)
    scheduler.start()