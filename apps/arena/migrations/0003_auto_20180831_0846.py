# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-31 08:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0002_auto_20180826_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpass',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 8, 46, 2, 16039), verbose_name='用户提交时间'),
        ),
    ]