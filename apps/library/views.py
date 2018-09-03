from django.shortcuts import render

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

from apps.users.models import UserProfile
from apps.user_relationship.models import UserCourse
from apps.library.serializers import *

from apps.utils.permissions import *

from .models import *

# Create your views here.


class KnowledgeListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    图书馆首页信息 列出用户当前学习课程的相关知识点
    """
    serializer_class = KnowledgeSerializers

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        """
        获取数据
        首先查询该用户当前学习的课程
        查询该课程对应的知识点
        :return:
        """
        knowledges = []
        course = UserCourse.objects.get(user=self.request.user).course
        course_knowledges = KnowledgeCourse.objects.filter(course=course)
        for course_knowledge in course_knowledges:
            knowledges.append(course_knowledge.knowledge)
        return knowledges


class SearchKnowledgeListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点搜索 详情
    """
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializers

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', 'intr')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SearchKnowledgeByTagListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点标签搜索  通过标签搜索知识点 实现路线图中课程章节页面中 相关知识点的搜索
    """
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializers

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('tag', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SearchKnowledgeByFatherTagListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点父标签搜索  通过父标签搜索知识点
    """
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializers

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('father_tag', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class KnowledgeImageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点图片
    """
    serializer_class = KnowledgeImageSerializers

    def get_queryset(self):
        """
        获取知识点图片
        根据知识点id查询图片
        :return:
        """
        try:
            return KnowImage.objects.filter(knowledge=int(self.kwargs['pk']))

        except:
            return KnowImage.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/know_image/1/
        其中的1代表知识点的id号  返回该知识点对应的所有图片
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class KnowledgeVideoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点视频
    """
    serializer_class = KnowledgeVideoSerializers

    def get_queryset(self):
        """
        获取知识点视频
        根据知识点id查询视频
        :return:
        """
        try:
            return KnowVideo.objects.filter(knowledge=int(self.kwargs['pk']))

        except:
            return KnowVideo.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/know_video/1/
        其中的1代表知识点的id号  返回该知识点对应的所有视频
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class KnowledgeMindViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点导图
    """
    serializer_class = KnowMindSerializers

    def get_queryset(self):
        """
        获取知识点导图
        根据知识点id查询导图
        :return:
        """
        try:
            return KnowMind.objects.filter(knowledge=int(self.kwargs['pk']))

        except:
            return KnowMind.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/know_mind/1/
        其中的1代表知识点的id号  返回该知识点对应的所有导图
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class KnowledgeAudioViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    知识点音频
    """
    serializer_class = KnowAudioSerializers

    def get_queryset(self):
        """
        获取知识点音频
        根据知识点id查询音频
        :return:
        """
        try:
            return KnowAudio.objects.filter(knowledge=int(self.kwargs['pk']))

        except:
            return KnowAudio.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """
        url请求 http://127.0.0.1:8000/know_audio/1/
        其中的1代表知识点的id号  返回该知识点对应的所有音频
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
