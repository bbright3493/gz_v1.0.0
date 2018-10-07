# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-07 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='_type',
            field=models.IntegerField(choices=[(1, '选择练习题'), (2, '判断练习题'), (3, '填空练习题'), (4, '编程练习题')], help_text='类别', verbose_name='类别'),
        ),
    ]