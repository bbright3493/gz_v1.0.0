#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-5 下午11:22
# @Author  : Shark
# @File    : tage_filter.py
# @Software: PyCharm

import datetime
from django import template

register = template.Library()

from apps.major.models import *

@register.simple_tag
def couser_list(id, types):
    cuoser = Major.objects.get(id=id)
    couser_list = cuoser.course_set.filter(course_type=types).all()

    return len(couser_list)
