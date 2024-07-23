from django.db import models

from clients.models import Client
from config import settings

NULLABLE = {'null':True, 'blank':True}

periods = (
    ('daily', 'Ежедневная'),
    ('weekly', 'Еженедельная'),
    ('monthly', 'Ежемесячная'),
)

statuses = (
    ('active', 'Активна'),
    ('disable', 'Неактивна')
)

class Mailing(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    message_title = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='тело письма')

    start = models.DateTimeField(verbose_name='начало')
    stop = models.DateTimeField(verbose_name='конец')
    period = models.CharField(max_length=25, choices=periods, default='daily', verbose_name='период')
    status = models.CharField(max_length=25, default='Неактивна', choices=statuses, verbose_name='статус', **NULLABLE)

    def __str__(self):
        return f'Рассылка: {self.owner}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'



class LogMailing(models.Model):
    mailing_key = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    date_try = models.DateTimeField(verbose_name='последняя попытка', **NULLABLE, )
    status_try = models.CharField(max_length=25, verbose_name='статус попытки', **NULLABLE, default='Попытки не было')
    response = models.TextField(verbose_name='ответ сервера', **NULLABLE, default='Попытки не было')

    def __str__(self):
        return f'Логи рассылки: {self.mailing_key}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'



