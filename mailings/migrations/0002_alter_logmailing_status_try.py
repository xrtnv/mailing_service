# Generated by Django 5.0 on 2024-01-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmailing',
            name='status_try',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='статус попытки'),
        ),
    ]
