# Generated by Django 2.2 on 2020-05-16 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20200516_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='first',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 21, 39, 7, 877107), verbose_name='date_published'),
        ),
    ]