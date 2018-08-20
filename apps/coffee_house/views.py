from django.shortcuts import render

# Create your views here.


# Create your views here.
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.utils.tools import format_time
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django.db.models import Q

from apps.users.serializers import UserClassSerializers



from apps.utils.permissions import *

from apps.coffee_house.serializers import *
from apps.users.models import ClassInfo


class TeacherMsgListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    老师的留言信息列表
    url请求 http://127.0.0.1:8000/teacher_msg/tutor
    其中的后缀代表不同老师的类型 tutor：导师  lector：讲师 head：班主任
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = TeacherMsgSerializers

    def get_queryset(self):
        """
        1 查询学生所在班级
        2 根据url查询对应老师的留言
        :return:
        """
        in_class = self.request.user.in_class
        if 'pk' in self.kwargs:
            if self.kwargs['pk'] == 'tutor':
                return TeacherUserMsg.objects.filter(Q(student=self.request.user), Q(teacher=in_class.teacher_tutor)).order_by('send_time')
            elif self.kwargs['pk'] == 'lector':
                return TeacherUserMsg.objects.filter(Q(student=self.request.user), Q(teacher=in_class.teacher_lector)).order_by(
                    'send_time')
            else:
                return TeacherUserMsg.objects.filter(Q(student=self.request.user), Q(teacher=in_class.teacher_head)).order_by(
                    'send_time')
        else:
            return TeacherUserMsg.objects.filter(student=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/teacher_msg/tutor
        其中的后缀代表不同老师的类型 tutor：导师  lector：讲师 head：班主任
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class ClassViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取用户的班级信息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserClassSerializers

    def get_queryset(self):
        return [self.request.user.in_class]

    def list(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/user_class/
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class StudentMsgViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    获取用户的班级信息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = StudentMsgSerializers

    def get_queryset(self):
        return StudentMsg.objects.filter(rev_student=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/student_msg/
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class DiscussListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    获取论坛帖子
    """

    serializer_class = DiscussSerializers

    def get_queryset(self):
        return DiscussMsg.objects.all()

