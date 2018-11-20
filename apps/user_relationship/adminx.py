#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-4 上午10:28
# @Author  : Shark
# @File    : adminx.py
# @Software: PyCharm

from extra_apps import xadmin

from apps.user_relationship.models import *


class UserMajorAdmin(object):
    list_display = ['user', 'major', 'create_time', 'end_time']
    search_fields = ['user', 'major']
    list_filter = ['user', 'major', 'create_time', 'end_time']
#    readonly_fields = ['user', 'major', 'create_time', 'end_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'start_time', 'end_time', 'complete']
    search_fields = ['user', 'course', 'complete']
    list_filter = ['user', 'course', 'start_time', 'end_time', 'complete']
#    readonly_fields = ['user', 'course', 'start_time', 'end_time', 'complete']


class UserChapterAdmin(object):
    list_display = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']
    search_fields = ['user', 'chapter', 'course', 'course_end', 'chapter_end']
    list_filter = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']
#    readonly_fields = ['user', 'chapter', 'course', 'course_end', 'chapter_end', 'end_time']


class UserPracticeAdmin(object):
    list_display = ['user', 'chapter', 'practice', 'types', 'end_time', 'practice_info']
    search_fields = ['user', 'chapter', 'practice', 'types', 'practice_info']
    list_filter = ['user', 'chapter', 'practice', 'types', 'end_time', 'practice_info']
#    readonly_fields = ['user', 'chapter', 'practice', 'start_time', 'end_time', 'practice_info', 'count']


class UserAchievementAdmin(object):
    list_display = ['user', 'class_rankings', 'monthly_rankings', 'total_ranking', 'estimated_time']
    search_fields = ['user', 'estimated_time']
    list_filter = ['user', 'estimated_time']
    # readonly_fields = ('user', 'class_rankings', 'monthly_rankings', 'total_ranking', 'estimated_time', 'total_ranking_time')


class UserTaskAdmin(object):
    list_display = ['user', 'task_name', 'complete_time']
    search_fields = ['user', 'task_name']
    list_filter = ['user', 'task_name', 'complete_time']
 #   readonly_filter = ('user', 'task_name', 'complete_time', 'task_info')


class UserBlogAdmin(object):
    list_display = ['user', 'blog_name', 'blog_body', 'blog_time']
    search_fields = ['user', 'blog_name', 'blog_body']
    list_filter = ['user', 'blog_name', 'blog_body', 'blog_time']
    # readonly_filter = ['user', 'blog_name', 'blog_body', 'blog_time']


class UserMissionAdmin(object):
    list_display = ['user', 'chapter', 'mission', 'data_info', 'task_end', 'file', 'submit_time', 'complete_time']
    search_fields = ['user', 'chapter', 'mission', 'data_info', 'task_end', 'file']
    list_filter = ['user', 'chapter', 'mission', 'data_info', 'task_end', 'file', 'submit_time', 'complete_time']


class TeacherEvaluationAdmin(object):
    list_display = ['teacher', 'mission', 'user', 'data', 'evaluation_time', 'category_type']
    search_fields = ['teacher', 'mission', 'user', 'data', 'category_type']
    list_filter = ['teacher', 'mission', 'user', 'data', 'evaluation_time', 'category_type']


xadmin.site.register(TeacherEvaluation, TeacherEvaluationAdmin)
xadmin.site.register(UserMajor, UserMajorAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserChapter, UserChapterAdmin)
xadmin.site.register(UserPractice, UserPracticeAdmin)
xadmin.site.register(UserAchievement, UserAchievementAdmin)
# xadmin.site.register(UserTask, UserTaskAdmin)
xadmin.site.register(UserBlog, UserBlogAdmin)
xadmin.site.register(UserMission, UserMissionAdmin)

