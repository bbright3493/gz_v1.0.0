#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-29 上午10:19
# @Author  : Shark
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import *

User = get_user_model()


class UserClassSerializers(serializers.ModelSerializer):
    """
    班级信息序列化
    """
    class Meta:
        model = ClassInfo
        fields = '__all__'


class UserCitySerializers(serializers.ModelSerializer):
    """
    城市信息序列化
    """

    class Meta:
        model = CityInfo
        fields = '__all__'


class UserProfileSerializers(serializers.ModelSerializer):
    """
    用户基本信息
    """
    in_class = UserClassSerializers()
    city = UserCitySerializers()

    class Meta:
        model = User
        fields = ('id', 'name', 'age', 'gender', 'address', 'mobile', 'email', 'expected_work', 'assessment', 'img',
                  'city', 'want_be_challenged', 'in_class')


class UserProfileSerializers2(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=255, allow_null=True, label='头像')

    class Meta:
        model = User
        fields = ('id', 'name', 'age', 'gender', 'address', 'mobile', 'email', 'expected_work', 'assessment', 'img',
                  'city', 'want_be_challenged', 'in_class')


class UserResumeSerializers(serializers.ModelSerializer):
    """
    用户教育背景
    """

    class Meta:
        model = UserResume
        fields = "__all__"


class UserProjectSerializers(serializers.ModelSerializer):
    """
    用户项目
    """

    class Meta:
        model = UserProject
        fields = "__all__"


class UserSkillSerializers(serializers.ModelSerializer):
    """
    用户技能
    """

    class Meta:
        model = UserSkill
        fields = "__all__"


class TeacherSerializers(serializers.ModelSerializer):
    """
    老师列表序列化
    """

    class Meta:
        model = Teacher
        fields = "__all__"
