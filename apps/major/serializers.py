#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-22 下午2:41
# @Author  : Shark
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from apps.major.models import *


# class MajorSerializers3(serializers.ModelSerializer):
#     """
#     3级目录序列化(专业课程类别下的课程)
#     """
#     class Meta:
#         model = Major
#         fields = "__all__"


class MajorSerializers2(serializers.ModelSerializer):
    """
    2级目录序列化(专业课程类别)
    """
    # sub_cat = MajorSerializers3(many=True)

    class Meta:
        model = Major
        fields = "__all__"


class MajorSerializers(serializers.ModelSerializer):
    """
    父级目录序列化(专业)
    """
    sub_cat = MajorSerializers2(many=True)

    class Meta:
        model = Major
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    """
    课程序列化
    """
    class Meta:
        model = Course
        fields = "__all__"


class CategoryAndCourseSerializers(serializers.ModelSerializer):
    """
    课程和课程类别序列化
    """
    category = MajorSerializers2()
    course = CourseSerializers()

    class Meta:
        model = CategoryAndCourse
        fields = "__all__"


class ChapterTaskSerializers(serializers.ModelSerializer):
    """
    章节任务序列化
    """
    #chapter_name = ChapterSerializers()

    class Meta:
        model = ChapterTask
        fields = "__all__"


class ChapterSerializers(serializers.ModelSerializer):
    """
    课程章节序列化
    """
    tasks = ChapterTaskSerializers(many=True)
    course_name = CourseSerializers()

    class Meta:
        model = Chapter
        fields = "__all__"
        depth = 1


class PracticeSerializers(serializers.ModelSerializer):
    """
    章节练习序列化
    """
    chapter_name = ChapterSerializers()
    submit_num = 2

    class Meta:
        model = Practice
        fields = "__all__"


# class TimeLimitPracticeSerializers(PracticeSerializers):
#     """
#     章节限时练习题序列化
#     """
#     class Meta:
#         model = TimeLimitPractice
#         fields = "__all__"
#
#
# class SpeedPracticeSerializers(PracticeSerializers):
#     """
#     章节速度练习题序列化
#     """
#
#     class Meta:
#         model = SpeedPractice
#         fields = "__all__"
#
#
# class ProgrammingPracticeSerializers(PracticeSerializers):
#     """
#     章节编程练习题序列化
#     """
#     submit_num = ''
#
#     class Meta:
#         model = ProgrammingPractice
#         fields = "__all__"





class MyChapterTaskSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    chapter_name = serializers.PrimaryKeyRelatedField(required=True, queryset=Chapter.objects.all(), label='章节', help_text='章节id')
    name = serializers.CharField()
    info = serializers.CharField()
    image = serializers.ListField()
    add_time = serializers.DateTimeField()


class ChapterTaskImageSerializers(serializers.ModelSerializer):
    """
    任务图片序列化
    """
    ChapterTask_name = ChapterTaskSerializers()

    class Meta:
        model = TaskImage
        fields = "__all__"





