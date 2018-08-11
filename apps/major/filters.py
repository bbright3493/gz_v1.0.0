#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-23 下午11:22
# @Author  : Shark
# @File    : filters.py
# @Software: PyCharm

import django_filters
from django.db.models import Q

from apps.major.models import Major, Chapter


class CourseFilter(django_filters.rest_framework.FilterSet):
    """
    过滤课程
    """
    course = django_filters.NumberFilter(method='course_filter', help_text='用不到')

    def course_filter(self, queryset, name, value):
        if value:
            return queryset.filter(parent_category_id=value)
        return queryset

    class Meta:
        model = Major
        fields = ['id']


# class ChapterFilter(django_filters.rest_framework.FilterSet):
#     """
#     过滤课程章节
#     """
#     chapter = django_filters.NumberFilter(method='chapter_filter')
#
#     def chapter_filter(self, queryset, name, value):
#         print(value)
#         a = queryset.filter(parent_category_id=value)
#         return queryset.filter(Q(parent_category_id=value) | Q(course_name_id=value))
#
#     class Meta:
#         model = Chapter
#         fields = ['chapter_name']
