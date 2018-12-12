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
    list_display = ['send_student', 'rev_student', 'message', 'send_time', 'rich_message']
    search_fields = ['send_student', 'rev_student', 'message', 'send_time', 'rich_message']
    list_filter = ['send_student', 'rev_student', 'message', 'send_time', 'rich_message']

    style_fields = {"rich_message": "ueditor"}  # bb


class DiscussMsgAdmin(object):
    list_display = ['title', 'content', 'user', 'send_time', 'click_num']
    search_fields = ['title', 'content', 'user', 'send_time', 'click_num']
    list_filter = ['title', 'content', 'user', 'send_time', 'click_num']


class DiscussReplayAdmin(object):
    list_display = ['discuss', 'user', 'content']
    search_fields = ['discuss', 'user', 'content']
    list_filter = ['discuss', 'user', 'content']


class GroupAdmin(object):
    list_display = ['in_class', 'name', 'step_info']
    search_fields = ['in_class', 'name', 'step_info']
    list_filter = ['in_class', 'name', 'step_info']


class UserGroupAdmin(object):
    list_display = ['user', 'group']
    search_fields = ['user', 'group']
    list_filter = ['user', 'group']


xadmin.site.register(TeacherUserMsg, TeacherUserMsgAdmin)
xadmin.site.register(StudentMsg, StudentMsgAdmin)
xadmin.site.register(DiscussMsg, DiscussMsgAdmin)
xadmin.site.register(DiscussReplay, DiscussReplayAdmin)
xadmin.site.register(Group, GroupAdmin)
xadmin.site.register(UserGroup, UserGroupAdmin)

