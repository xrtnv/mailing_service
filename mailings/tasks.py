from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import datetime
import pytz

from mailings.models import Mailing, LogMailing
from mailings.services import send_mail

tz = 'Europe/Moscow'
utc = pytz.UTC

def my_background_task():
    objects = Mailing.objects.all()

    try:

        for obj in objects:

            if datetime.datetime.now().replace(tzinfo=utc)>= obj.start.replace(tzinfo=utc) and datetime.datetime.now().replace(tzinfo=utc) <= obj.stop.replace(tzinfo=utc):
                obj.status = 'Активна'
                obj.save()

                if datetime.datetime.now().replace(tzinfo=utc).strftime("%H:%M") == obj.start.replace(tzinfo=utc).strftime("%H:%M"):
                    print('ok')
                    if obj.period == 'daily':
                        send_mail(_to_mail=obj.owner.user.email,
                                  _message=obj.message_body,
                                  _subject=obj.message_title)
                    elif obj.periods == 'weekly':
                        if datetime.datetime.now().replace(tzinfo=utc).weekday() == obj.start.weekday():
                            send_mail(_to_mail=obj.owner.user.email,
                                      _message=obj.message_body,
                                      _subject=obj.message_title)
                    elif obj.periods == 'monthly':
                        if datetime.datetime.now().replace(tzinfo=utc).weekday() == obj.start.weekday() and obj.start.day == datetime.datetime.now().replace(tzinfo=utc).day:
                            send_mail(_to_mail=obj.owner.user.email,
                                      _message=obj.message_body,
                                      _subject=obj.message_title)


            elif datetime.datetime.now().replace(tzinfo=utc) > obj.stop.replace(tzinfo=utc):
                obj.status = 'Неактивна'
                obj.save()
            else:
                obj.status = 'Неактивна'
                obj.save()

            logs = LogMailing.objects.get(id=obj.id)

            logs.response = '200'
            logs.date_try = datetime.datetime.now().replace(tzinfo=utc)
            logs.status_try = 'ok'
            logs.save()



    except Exception as ex:
        print(ex)

        logs.date_try = datetime.datetime.now().replace(tzinfo=utc)
        logs.status_try = 'bad'
        logs.response = '400'
        logs.save()






