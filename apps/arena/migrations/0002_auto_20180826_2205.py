# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-26 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('major', '0001_initial'),
        ('arena', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpkdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='userpass',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生名'),
        ),
        migrations.AddField(
            model_name='userpass',
            name='user_pass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.Pass', verbose_name='关卡'),
        ),
        migrations.AddField(
            model_name='pass',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major', verbose_name='专业信息'),
        ),
        migrations.AddField(
            model_name='challenger',
            name='be_challenged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='be_chg', to=settings.AUTH_USER_MODEL, verbose_name='被挑战者'),
        ),
        migrations.AddField(
            model_name='challenger',
            name='challenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chg', to=settings.AUTH_USER_MODEL, verbose_name='挑战者'),
        ),
    ]