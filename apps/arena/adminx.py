#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午4:58
# @Author  : bb
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin
from .models import *


class PassAdmin(object):
    list_display = ['major', 'name', 'pass_no', 'pass_intr', 'pass_std', 'pass_answer', 'pass_limit_time']
    search_fields = ['name', 'pass_no']
    list_filter = ['name']


class UserPassAdmin(object):
    list_display = ['user_id', 'user_pass', 'pass_score', 'user_submit', 'submit_time', 'complete_time', 'submit_num']
    search_fields = ['user_id', 'user_pass', 'pass_score']
    list_filter = ['user_id', 'user_pass', 'pass_score']


class PkQuestionAdmin(object):
    list_display = ['name', 'content', 'answer', 'complete_time']
    search_fields = ['name', 'content', 'answer', 'complete_time']
    list_filter = ['name', 'content', 'answer', 'complete_time']


class ChallengerAdmin(object):
    list_display = ['be_challenged', 'challenger', 'status']
    search_fields = ['be_challenged', 'challenger', 'status']
    list_filter = ['be_challenged', 'challenger', 'status']


class TeamCompAdmin(object):
    list_display = ['title', 'content', 'start_time', 'end_time', 'member_num', 'recruit']
    search_fields = ['title', 'content', 'start_time', 'end_time', 'member_num', 'recruit']
    list_filter = ['title', 'content', 'start_time', 'end_time', 'member_num', 'recruit']


xadmin.site.register(Pass, PassAdmin)
xadmin.site.register(UserPass, UserPassAdmin)
xadmin.site.register(PkQuestion, PkQuestionAdmin)
xadmin.site.register(Challenger, ChallengerAdmin)
xadmin.site.register(TeamComp, TeamCompAdmin)

