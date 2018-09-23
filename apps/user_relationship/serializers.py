#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-26 上午12:02
# @Author  : Shark
# @File    : serializers.py
# @Software: PyCharm
import json

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from apps.user_relationship.models import *
from apps.major.models import Practice, Chapter
from apps.major.serializers import ChapterSerializers, CourseSerializers, ChapterTaskSerializers
from apps.users.serializers import TeacherSerializers, UserProfileSerializers


class UserChapterEndSerializer(serializers.ModelSerializer):
    """
    用户章节完成功能序列化
    """
    # chapter = ChapterSerializers()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 自动填充user
    )
    chapter = serializers.PrimaryKeyRelatedField(required=True, queryset=Chapter.objects.all(), label='章节',
                                                 help_text='章节id')

    course = serializers.PrimaryKeyRelatedField(required=True, queryset=Course.objects.all(), label='课程',
                                                  help_text='课程id')
    course_end = serializers.BooleanField(default=False, label='课程是否完成', help_text='课程是否完成')

    chapter_end = serializers.BooleanField(default=True, label='章节是否完成', help_text='章节是否完成')

    end_time = serializers.DateTimeField(default=timezone.now, label='完成时间', help_text='结束时间')

    def create(self, validated_data):
        user = self.context["request"].user
        chapter = validated_data["chapter"]
        course = validated_data["course"]
        course_end = validated_data["course_end"]
        chapter_end = validated_data["course_end"]
        end_time = validated_data["end_time"] if "end_time" in validated_data.keys() else timezone.now()

        course = Course.objects.get(name=course)
        userchapter = Chapter.objects.get(chapter_name=chapter)
        chapters = Chapter.objects.filter(course_name_id=course.id).reverse()[0]
        if chapters.id == chapter.id:
            userchapter = UserChapter()
            userchapter.user = user
            userchapter.chapter = chapter
            userchapter.course = course
            userchapter.course_end = True
            userchapter.chapter_end = True
            userchapter.end_time = end_time
            userchapter.save()

        else:
            userchapter = UserChapter.objects.create(**validated_data)

        return userchapter

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
    # course = CourseSerializers()

    class Meta:
        model = UserChapter
        fields = "__all__"


class UserPracticeSerializer(serializers.Serializer):
    """
    用户练习序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
        , help_text='用户id')

    chapter = serializers.PrimaryKeyRelatedField(required=True, queryset=Chapter.objects.all(), label='章节', help_text='章节id')

    practice = serializers.PrimaryKeyRelatedField(required=True, queryset=Practice.objects.all(), label='练习', help_text='练习题id')

    types = serializers.IntegerField(label='类别', help_text='类别')

    end_time = serializers.DateTimeField(default=timezone.now, label='完成时间', help_text='结束时间')

    practice_info = serializers.CharField(allow_blank=True, label='练习答案', help_text='练习题提交答案')

#  需要修改
    def create(self, validated_data):
        chapter_id = validated_data['chapter'].id
        _type = validated_data['types']
        practice_answer = Practice.objects.filter(chapter_name=chapter_id, _type=_type).all()
        answer = dict()
        return_answer = dict()
        value = json.loads(validated_data['practice_info'])
        for practice in practice_answer:
            answer[practice.id] = practice.standard_answer
        print(answer)
        print(value)
        for k, v in answer.items():
            if v == value[str(k)]:
                return_answer[k] = True
            else:
                return_answer[k] = False
        print(return_answer)
        user = self.context["request"].user
        chapter = validated_data["chapter"]
        practice = validated_data["practice"]
        types = validated_data["types"]
        practice_info = [value, return_answer]

        validated_data = {"user": user, "chapter": chapter, "practice": practice, "types": types, "practice_info": practice_info}
        existed = UserPractice.objects.create(**validated_data)

        return existed

        #
        # existed = UserPractice.objects.filter(user=user, practice=practice)
        #
        # if existed:
        #     existed = existed[0]
        #     existed.count += 1
        #     existed.save()
        # else:
        #     existed = UserPractice.objects.create(**validated_data)
        #
        # return existed

    class Meta:
        model = UserPractice
        fields = ('user', 'chapter', 'practice', 'practice_info', 'count')


class A(object):
    def __init__(self, value, user):
        self.num = value
        self.user = user


class Test(serializers.Serializer):
    num = serializers.IntegerField()


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


class UserMissionSerializers(serializers.ModelSerializer):
    """
    用户任务完成信息序创建列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 自动填充user
    )

    class Meta:
        model = UserMission
        fields = "__all__"


class UserMissionListSerializers(serializers.ModelSerializer):
    """
    用户任务完成列表序列化
    """
    user = UserProfileSerializers()
    chapter = ChapterSerializers()
    mission = ChapterTaskSerializers()

    class Meta:
        model = UserMission
        fields = "__all__"


class TeacherEvaluationListSerializers(serializers.ModelSerializer):
    """
    老师评价列表序列化
    """
    teacher = TeacherSerializers()

    class Meta:
        model = TeacherEvaluation
        fields = "__all__"


class TeacherEvaluationSerializers(serializers.ModelSerializer):
    """
    老师评价创建序列化
    """

    class Meta:
        model = TeacherEvaluation
        fields = "__all__"
