from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django.views.generic.base import View
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

from apps.users.serializers import *
from apps.utils.permissions import *
from apps.users.filters import *

# class Index(View):
#     def get(self, request):
#         return render(request, 'index.html')


class LogoutView(View):
    """
    用户退出

    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class UserResumeViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户个人信息展示
    update:
        用户个人信息修改
    """
    # queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserProfileSerializers

        elif self.action == 'update' or self.action == 'partial_update':
            return UserProfileSerializers2

        return UserProfileSerializers


class UserEducationViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户教育背景
    update:
        用户教育背景修改
    """
    serializer_class = UserResumeSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):

        return UserResume.objects.filter(user=self.request.user)


class UserProjectViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户项目经验
    update：
        用户项目信息修改
    """

    serializer_class = UserProjectSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        return UserProject.objects.filter(user=self.request.user)


class UserSkillViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    list:
        用户专业技能
    update：
        用户专业技能信息修改
    """

    serializer_class = UserSkillSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user)


class UserClassMateListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取班级同学 用于显示同学页面左侧同学列表
        搜索 api http://127.0.0.1:8000/classmate
    """
    serializer_class = UserProfileSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        """
        查询用户所在班级
        查询该班级的所有学生

        :return:
        """
        students = UserProfile.objects.filter(in_class=self.request.user.in_class)

        return students