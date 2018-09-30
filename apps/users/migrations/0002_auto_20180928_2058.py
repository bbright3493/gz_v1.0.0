# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-28 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, default='users/image/default.jpg', help_text='头像', max_length=255, null=True, upload_to='users/image/%Y/%m', verbose_name='头像'),
        ),
    ]
