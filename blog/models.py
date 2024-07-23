from django.db import models

from users.models import NULLABLE


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='изображение')
    date = models.DateTimeField(verbose_name='дата публикации', auto_now_add=True, blank=True, null=True)

    views_count = models.IntegerField(verbose_name='просмотры', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'