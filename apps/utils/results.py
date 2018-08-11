#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-4 下午5:17
# @Author  : Shark
# @File    : results.py
# @Software: PyCharm

import json
from django.core import serializers
from django.views.generic.base import View

from apps.user_relationship.models import *
from apps.major.models import Chapter


class UserResultsView(View):

    def get(self, request):
        results = UserAchievement.objects.filter(user=self.request.user)
        chapter = UserChapter.objects.filter(user=self.request.user).order_by('-end_time')[0]
        chapter = Chapter.objects.filter(id=chapter.chapter_id)
        json_data = serializers.serializer('json', results)
        json_data = serializers.serialize('json', chapter)
        print(return_info)

# def return_info(user):
#     info_dict = dict()
#     chapter = UserChapter.objects.filter(user=user).order_by('-end_time')[0]
#     print(chapter.chapter_id)
#     chapter = Chapter.objects.filter(id=chapter.chapter_id)
#     json_data = serializers.serialize('json', chapter)
#     print(json_data)
#     info_dict['chapter'] = json_data
#     results = UserAchievement.objects.filter(user=user)
#
#     return json_data
