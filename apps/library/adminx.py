#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午4:58
# @Author  : bb
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin
from .models import *



class KnowledgeAdmin(object):
    list_display = ['name', 'intr', 'tag', 'father_tag', 'level', 'intr_text_pic']
    search_fields = ['name', 'intr', 'tag', 'father_tag', 'level', 'intr_text_pic']
    list_filter = ['name', 'intr', 'tag', 'father_tag', 'level', 'intr_text_pic']

    style_fields = {"intr_text_pic": "ueditor"}  # bb


class KnowledegImageAdmin(object):
    list_display = ['knowledge', 'name', 'image', 'intr']
    search_fields = ['knowledge', 'name', 'image', 'intr']
    list_filter = ['knowledge', 'name', 'image', 'intr']


class KnowVideoAdmin(object):
    list_display = ['knowledge', 'name', 'video_url', 'intr']
    search_fields = ['knowledge', 'name', 'video_url', 'intr']
    list_filter = ['knowledge', 'name', 'video_url', 'intr']


class KnowMindAdmin(object):
    list_display = ['knowledge', 'name', 'file', 'intr', 'mind_image']
    search_fields = ['knowledge', 'name', 'file', 'intr', 'mind_image']
    list_filter = ['knowledge', 'name', 'file', 'intr', 'mind_image']


class KnowAudioAdmin(object):
    list_display = ['knowledge', 'name', 'file', 'intr']
    search_fields = ['knowledge', 'name', 'file', 'intr']
    list_filter = ['knowledge', 'name', 'file', 'intr']


class KnowSoftAdmin(object):
    list_display = ['knowledge', 'name', 'file', 'intr']
    search_fields = ['knowledge', 'name', 'file', 'intr']
    list_filter = ['knowledge', 'name', 'file', 'intr']


class KnowledgeCourseAdmin(object):
    list_display = ['course', 'knowledge']
    search_fields = ['course', 'knowledge']
    list_filter = ['course', 'knowledge']


xadmin.site.register(Knowledge, KnowledgeAdmin)
xadmin.site.register(KnowImage, KnowledegImageAdmin)
xadmin.site.register(KnowVideo, KnowVideoAdmin)
xadmin.site.register(KnowMind, KnowMindAdmin)
xadmin.site.register(KnowAudio, KnowAudioAdmin)
xadmin.site.register(KnowSoft, KnowSoftAdmin)
xadmin.site.register(KnowledgeCourse, KnowledgeCourseAdmin)

