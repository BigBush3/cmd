import datetime

import schedule

def job():
    print('Ку')

if datetime.datetime.now().minute == 00:
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
