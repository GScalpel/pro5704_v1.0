# Generated by Django 2.0.7 on 2018-07-31 05:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sys5704', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowmanage',
            name='starttime',
            field=models.CharField(blank=True, default=datetime.datetime(2018, 7, 31, 5, 50, 50, 606367, tzinfo=utc), max_length=15, verbose_name='借阅时间'),
        ),
    ]
