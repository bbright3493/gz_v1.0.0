from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import filters
from django.views.generic.base import View
from django.http import JsonResponse
import json
from itertools import chain

from apps.user_relationship.models import *
from apps.utils.permissions import *
from apps.user_relationship.serializers import *
from apps.utils.results import *
# Create your views here.


class UserChapterEndViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户学完章节列表展示、任务线页面接口
    create:
        添加用户章节完成信息接口
    update:
        更新用户章节完成信息接口


    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "list":
            return UserChapterEndInfoSerializer
        elif self.action == "create":
            return UserChapterEndSerializer

        return UserChapterEndSerializer

    def get_queryset(self):

        return UserChapter.objects.filter(user_id=self.request.user)


class UserPracticeViewSet(viewsets.ModelViewSet):
    """
    list:
        用户完成练习题展示接口
    create:
        用户练习题完成时添加信息接口
    update:
        更新用户完成练习题接口
    delete：
        删除用户完成练习题接口
    """
    serializer_class = UserPracticeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserPractice.objects.filter(user_id=self.request.user)


class UserResultsView(View):

    def get(self, request):
        info_dict =dict()
        results = UserAchievement.objects.filter(user=self.request.user)
        chapter = UserChapter.objects.filter(user=self.request.user).order_by('-end_time')[0]
        chapter = Chapter.objects.filter(id=chapter.chapter_id)
        json_data = serializers.serialize('json', results)
        json_data2 = serializers.serialize('json', chapter)
        # json_data = json_data.replace(']', '').replace('[', '')
        # json_data2 = json_data2.replace(']', '').replace('[', '')
        print(json_data2)
        info_dict['results'] = json.loads(json_data)
        info_dict['chapter'] = json.loads(json_data2)
        return JsonResponse(info_dict, safe=False)


class UserResultsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户成绩信息
    """
    serializer_class = UserResultsSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):

        return UserAchievement.objects.filter(user=self.request.user)


class UserTaskListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户作业信息列表展示
        搜索 api http://127.0.0.1:8000/task/?search= （模糊搜索）
    create:
        用户作业上传，创建

    """
    serializer_class = UserTaskSerializers
    filter_backends = (filters.SearchFilter, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('task_name',)

    def get_queryset(self):

        return UserTask.objects.filter(user=self.request.user)


class UserBlogViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户blog信息列表展示
        搜索 api http://127.0.0.1:8000/blog/?search= （模糊搜索）
    create:
        用户blog 创建

    """
    serializer_class = UserBlogSerializers
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('blog_name',)

    def get_queryset(self):
        return UserBlog.objects.filter(user=self.request.user)


class UserClassBlogViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户所在班级blog信息列表展示 用于显示班级页面左侧的最新消息
        搜索 api http://127.0.0.1:8000/class_blog/?search= （模糊搜索）
    """
    serializer_class = UserBlogSerializers
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('blog_name',)

    def get_queryset(self):
        """
        查询用户所在班级
        查询该班级的所有学生
        获取所有学生的博客
        按时间排序返回
        :return:
        """
        students = UserProfile.objects.filter(in_class=self.request.user.in_class)

        class_blogs = UserBlog.objects.filter(user=self.request.user)
        for student in students:
            user_blogs = UserBlog.objects.filter(user=student)
            class_blogs = class_blogs | user_blogs


        return class_blogs.order_by('blog_time')


