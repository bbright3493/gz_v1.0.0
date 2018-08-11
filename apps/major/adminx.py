#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午4:58
# @Author  : Shark
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin
from apps.major.models import *


class MajorAdmin(object):
    list_display = ['name', 'category_type', 'parent_category', 'add_time']
    search_fields = ['name', 'category_type', 'parent_category']
    list_filter = ['name', 'category_type', 'parent_category', 'add_time']


class ChapterAdmin(object):
    list_display = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']
    search_fields = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']
    list_filter = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']


class PracticeAdmin(object):
    list_display = ['chapter_name', 'practice_name', 'Practice_standard', 'standard_explain']
    search_fields = ['chapter_name', 'practice_name', 'Practice_standard', 'standard_explain']
    list_filter = ['chapter_name', 'practice_name', 'Practice_standard', 'standard_explain']


xadmin.site.register(Major, MajorAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Practice, PracticeAdmin)
