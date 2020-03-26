from apscheduler.schedulers.background import BackgroundScheduler
import logging
import time
from DataCollector import get_data


logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

def job_function():
    print("Hello World")

sched = BackgroundScheduler()

# Schedule job_function to be called every 1 second
# FIXME: Do not forget to change end_date to actual date
sched.add_job(get_data, 'cron', hour=0, minute=0, second=0)

sched.start()
