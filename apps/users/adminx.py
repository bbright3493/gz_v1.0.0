#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午3:55
# @Author  : Shark
# @File    : adminx.py
# @Software: PyCharm


from extra_apps import xadmin
from xadmin import views

from apps.users.models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "格子网塾"
    site_footer = "格子网塾后台管理系统"
    menu_style = "accordion"


class UserResumeAdmin(object):
    list_display = ['user', 'Study_time', 'end_time', 'school_name', 'major', 'education']
    search_fields = ['user', 'school_name', 'major', 'education', 'expected_work']
    list_filter = ['user', 'Study_time', 'end_time', 'school_name', 'major', 'education']
    readonly_filter = ('user', 'Study_time', 'end_time', 'school_name', 'major', 'education')


class TeacherAdmin(object):
    list_display = ['name', 'types', 'intr', 'img']
    search_fields = ['name', 'types', 'intr', 'img']
    list_filter = ['name', 'types', 'intr', 'img']


class UserClassAdmin(object):
    list_display = ['name', 'notice']
    search_fields = ['name', 'notice']
    list_filter = ['name', 'notice']


class UserCityAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class UserProjectAdmin(object):
    list_display = ['user', 'project_name', 'technology', 'project_function', 'time_slot']
    search_fields = ['user', 'project_name', 'technology', 'project_function', 'time_slot']
    list_filter = ['user', 'project_name', 'technology', 'project_function', 'time_slot']
    readonly_filter = ('user', 'project_name', 'technology', 'project_function', 'time_slot')


class UserSkillAdmin(object):
    list_display = ['user', 'skill_name', 'skill_level', 'skill_introduce']
    search_fields = ['user', 'skill_name', 'skill_level', 'skill_introduce']
    list_filter = ['user', 'skill_name', 'skill_level', 'skill_introduce']
    readonly_filter = ('user', 'skill_name', 'skill_level', 'skill_introduce')


class ResourceAdmin(object):
    list_display = ['name','content','image', 'tag']
    search_fields = ['name','content','image', 'tag']
    list_filter = ['name','content','image', 'tag']

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Teacher, TeacherAdmin)#bb
xadmin.site.register(ClassInfo, UserClassAdmin)
xadmin.site.register(CityInfo, UserCityAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(UserResume, UserResumeAdmin)
xadmin.site.register(UserProject, UserProjectAdmin)
xadmin.site.register(UserSkill, UserSkillAdmin)
xadmin.site.register(Resource, ResourceAdmin)
