#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-4 上午10:52
# @Author  : Shark
# @File    : filters.py
# @Software: PyCharm

import django_filters


class UserTaskFilter(django_filters.rest_framework.FilterSet):
    """
    作业搜索
    """
    task_name = django_filters.CharFilter(task_name='name', lookup_expr='icontains')

    class Meta:
        fields = ['task_name']


class UserBlogFilter(django_filters.rest_framework.FilterSet):
    """
    博客搜索
    """
    blog_name = django_filters.CharFilter(blog_name='name', lookup_expr='icontains')

    class Meta:
        fields = ['blog_name']
