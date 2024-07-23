from django.db import models

from users.models import User, NULLABLE


class Client(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE
    )
    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    comment = models.CharField(max_length=150, verbose_name='комментарий')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name='клиент'
        verbose_name_plural='клиенты'
