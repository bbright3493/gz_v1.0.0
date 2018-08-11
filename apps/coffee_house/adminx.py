#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午4:58
# @Author  : bb
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin
from .models import *





class TeacherUserMsgAdmin(object):
    list_display = ['student', 'teacher', 'message', 'send_time', 'msg_type']
    search_fields = ['student', 'teacher', 'message', 'send_time', 'msg_type']
    list_filter = ['student', 'teacher', 'message', 'send_time', 'msg_type']



class StudentMsgAdmin(object):
    list_display = ['send_student', 'rev_student', 'message', 'send_time']
    search_fields = ['send_student', 'rev_student', 'message', 'send_time']
    list_filter = ['send_student', 'rev_student', 'message', 'send_time']


class DiscussMsgAdmin(object):
    list_display = ['title', 'content', 'user', 'send_time', 'click_num']
    search_fields = ['title', 'content', 'user', 'send_time', 'click_num']
    list_filter = ['title', 'content', 'user', 'send_time', 'click_num']





xadmin.site.register(TeacherUserMsg, TeacherUserMsgAdmin)
xadmin.site.register(StudentMsg, StudentMsgAdmin)
xadmin.site.register(DiscussMsg, DiscussMsgAdmin)

