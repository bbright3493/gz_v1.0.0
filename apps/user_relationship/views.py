from django.shortcuts import redirect
from rest_framework import viewsets, generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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


class UserChapterEndViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        需登录
        请求：http://xxx.xxx.xx.xx:xx/complete/ 返回用户章节完成信息展示，也是个人中心任务线API

    create:
        post请求：http://xxx.xxx.xx.xx:xx/complete/ 为添加用户章节完成信息API

    update:
        put请求：http://xxx.xxx.xx.xx:xx/complete/{id}/ 为更新指定的章节完成信息API


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


class UserPracticeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求： http://xx.xx.xx.xx:xx/user_practice/ 返回用户完成练习题信息

    """
    serializer_class = UserPracticeReadSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserPractice.objects.filter(user_id=self.request.user)


class UserPracticeCreateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    """
    create:
        post请求： http://xx.xx.xx.xx:xx/user_practice/ 用户练习题完成时添加信息接口
    update:
       put请求： http://xx.xx.xx.xx:xx/user_practice/{id}/  更新指定的完成练习题接口
    delete：
       put请求： http://xx.xx.xx.xx:xx/user_practice/{id}/ 删除指定的完成练习题接口
    """
    serializer_class = UserPracticeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


# class UserPracticeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
#     queryset = A(value=2, user=None)
#     serializer_class = Test
#     permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
#
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = A(value=2, user=self.request.user)
#         serializer = Test(queryset)
#         print(serializer.data)
#         return Response(serializer.data)


class UserResultsView(View):
    """
    需登录
    请求：http://xxx.xx.xx.xx:xx/results/ 返回用户成绩信息

    """

    def get(self, request):
        info_dict = dict()
        if request.user.is_authenticated:
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

        else:
            return redirect('login')


# ----------------------------------------------------------------------------------------------------
# 未使用
class UserResultsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户成绩信息
    """
    serializer_class = UserResultsSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserAchievement.objects.filter(user=self.request.user)


# ----------------------------------------------------------------------------------------------------


class UserTaskListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求： http://xxx.xx.xx.xx:xx/task/ 返回用户作业信息列表
        请求： http://xxx.xx.xx.xx:xx/task/?search= （模糊搜索）
    create:
        psot请求：http://xxx.xx.xx.xx:xx/task/ 用户作业上传，创建

    """
    serializer_class = UserTaskSerializers
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('task_name',)

    def get_queryset(self):
        user_task = UserTask.objects.filter(user=self.request.user)
        return user_task


class UserBlogViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求： http://xxx.xx.xx.xx:xx/blog/ 返回用户blog信息列表
        请求： http://xxx.xx.xx.xx:xx/blog/?search= （模糊搜索）
    create:
        psot请求：http://xxx.xx.xx.xx:xx/blog/ 用户blog 创建

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


class AllUserMissionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
       list:
           需登录
           请求： http://xxx.xx.xx.xx:xx/task_all/ 返回所有用户的任务 临时用 班主任看
    """

    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('mission__name',)
    serializer_class = UserMissionListSerializers

    def get_queryset(self):
        return UserMission.objects.all().order_by('user')


class UserMissionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
        需登录
        请求： http://xxx.xx.xx.xx:xx/task/ 返回用户所有任务完成情况
    read:
         请求： http://xxx.xx.xx.xx:xx/task/{id} 返回指定任务完成情况
    create:
        psot请求：http://xxx.xx.xx.xx:xx/task/ 用户任务完成 创建
    """

    # serializer_class = UserMissionSerializers

    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    search_fields = ('mission__name',)

    def get_serializer_class(self):
        if self.action == "list":
            return UserMissionListSerializers
        elif self.action == "create":
            return UserMissionSerializers

        return UserMissionListSerializers

    def get_queryset(self):
        return UserMission.objects.filter(user=self.request.user)


class UserMissionStautsViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    update:
        psot请求：http://xxx.xx.xx.xx:xx/user_mission_status/ 用户任务完成 创建
    """
    serializer_class = UserMissionStatusSerializers
    def get_queryset(self):
        return UserMission.objects.all()


class TeacherEvaluationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
        list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/user_mission/ 返回老师评价列表
        create:
            psot请求：http://xxx.xx.xx.xx:xx/user_mission/ 老师评价 创建
    """

    # serializer_class = UserMissionSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "list":
            return TeacherEvaluationListSerializers
        elif self.action == "create":
            return TeacherEvaluationSerializers

        return TeacherEvaluationListSerializers

    def get_queryset(self):
        return TeacherEvaluation.objects.all()


class ReadTeacherEvaluationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/user_mission/ 返回当前用户任务所有的老师评价列表

            请求： http://xxx.xx.xx.xx:xx/user_mission/？task=id 返回当前用户指定任务的老师评价
    """

    serializer_class = TeacherEvaluationListSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        user = self.request.user
        task = self.request.query_params.get('task', None)
        if task:
            queryset = TeacherEvaluation.objects.filter(user=user, mission=task)
            return queryset

        else:
            queryset = TeacherEvaluation.objects.filter(user=user).all()
            return queryset
