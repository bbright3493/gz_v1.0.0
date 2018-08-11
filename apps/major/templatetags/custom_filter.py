#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-5 下午10:23
# @Author  : Shark
# @File    : custom_filter.py
# @Software: PyCharm

from django import template
register = template.Library()

from apps.major.models import *



@register.filter
def claen_value(value, types):
    print(type(value))
    couser_list = value.course_set.filter(course_type=types)
    return couser_list