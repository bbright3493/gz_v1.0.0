#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-26 上午12:02
# @Author  : Shark
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from apps.user_relationship.models import *
from apps.major.models import Practice, Chapter
from apps.major.serializers import ChapterSerializers, MajorSerializers3


class UserChapterEndSerializer(serializers.ModelSerializer):
    """
    用户章节完成功能序列化
    """
    # chapter = ChapterSerializers()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 自动填充user
    )

    class Meta:
        model = UserChapter
        validators = [
            UniqueTogetherValidator(
                queryset=UserChapter.objects.all(),
                fields=('user', 'chapter'),
                message="已经学完"
            )
        ]
        fields = ('user', 'course', 'chapter', 'id', 'course_end', 'chapter_end', 'end_time')


class UserChapterEndInfoSerializer(serializers.ModelSerializer):
    """
    任务线序列化
    """
    chapter = ChapterSerializers()
    course = MajorSerializers3()

    class Meta:
        model = UserChapter
        fields = "__all__"


class UserPracticeSerializer(serializers.Serializer):
    """
    用户练习序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault() # 自动填充user
    , help_text='用户id')

    chapter = serializers.PrimaryKeyRelatedField(required=True, queryset=Chapter.objects.all(), label='章节', help_text='章节id')

    practice = serializers.PrimaryKeyRelatedField(required=True, queryset=Practice.objects.all(), label='练习', help_text='练习题id')

    start_time = serializers.DateTimeField(default=timezone.now, label='开始时间', help_text='开始时间')

    end_time = serializers.DateTimeField(default=timezone.now, label='完成时间', help_text='结束时间')

    practice_info = serializers.CharField(allow_blank=True, label='练习答案', help_text='练习题提交答案')

    def create(self, validated_data):
        user = self.context["request"].user
        chapter = validated_data["chapter"]
        practice = validated_data["practice"]
        practice_info = validated_data["practice_info"]
        # count = validated_data["count"]

        existed = UserPractice.objects.filter(user=user, practice=practice)

        if existed:
            existed = existed[0]
            existed.count += 1
            existed.save()
        else:
            existed = UserPractice.objects.create(**validated_data)

        return existed

    class Meta:
        model = UserPractice
        fields = ('user', 'chapter', 'practice', 'practice_info', 'count')


class UserResultsSerializers(serializers.ModelSerializer):
    """
    学生成绩信息序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault() # 自动填充user
        , help_text='用户id')

    class Meta:
        model = UserAchievement
        fields = '__all__'


class UserTaskSerializers(serializers.ModelSerializer):
    """
    学生作业信息序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 自动填充user
    )

    class Meta:
        model = UserTask
        fields = "__all__"


class UserBlogSerializers(serializers.ModelSerializer):
    """
    学生blog信息序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 自动填充user
    )

    class Meta:
        model = UserBlog
        fields = "__all__"

