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



# class CategoryAdmin(object):
#     list_display = ['name', 'major_name', 'add_time']
#     search_fields = ['name', 'major_name']
#     list_filter = ['name', 'major_name', 'add_time']


class CourseAdmin(object):
    list_display = ['name', 'course_task', 'add_time']
    search_fields = ['name', 'course_task']
    list_filter = ['name', 'course_task', 'add_time']


class CategoryAndCourseAdmin(object):
    list_display = ['category', 'course']
    search_fields = ['category', 'course']
    list_filter = ['category', 'course']


class ChapterAdmin(object):
    list_display = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']
    search_fields = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']
    list_filter = ['course_name', 'chapter_name', 'chapter_introduce', 'chapter_task', 'chapter_target']
    style_fields = {"chapter_task": "ueditor"}

    style_fields = {"chapter_task": "ueditor"}  #bb


class PracticeAdmin(object):
    list_display = ['chapter_name', 'practice_name', '_type', 'Practice_standard', 'standard_explain']
    search_fields = ['chapter_name', 'practice_name', '_type', 'Practice_standard', 'standard_explain']
    list_filter = ['chapter_name', 'practice_name', '_type', 'Practice_standard', 'standard_explain']


# class TimeLimitPracticeAdmin(PracticeAdmin):
#     pass
#
#
# class SpeedPracticeAdmin(PracticeAdmin):
#     pass
#
#
# class ProgrammingPracticeAdminn(PracticeAdmin):
#     pass


class ChapterTaskAdmin(object):
    list_display = ['chapter_name', 'name', 'info', 'image', 'add_time']
    search_fields = ['chapter_name', 'name', 'info', 'image']
    list_filter = ['chapter_name', 'name', 'info', 'image', 'add_time']


class ImageAdmin(object):
    list_display = ['ChapterTask_name', 'name', 'image', 'add_time']
    search_fields = ['ChapterTask_name', 'name', 'image']
    list_filter = ['ChapterTask_name', 'name', 'image', 'add_time']


xadmin.site.register(Major, MajorAdmin)
# xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CategoryAndCourse, CategoryAndCourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
# xadmin.site.register(TimeLimitPractice, TimeLimitPracticeAdmin)
# xadmin.site.register(SpeedPractice, SpeedPracticeAdmin)
# xadmin.site.register(ProgrammingPractice, ProgrammingPracticeAdminn)
xadmin.site.register(Practice, PracticeAdmin)
xadmin.site.register(ChapterTask, ChapterTaskAdmin)
xadmin.site.register(Image, ImageAdmin)
