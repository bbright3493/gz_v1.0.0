from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.utils.tools import format_time
from django.db.models import F, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from apps.major.models import *
from apps.major.serializers import *
from apps.major.filters import *
from apps.utils.permissions import *


# Create your views here.


class MajorListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        请求的url：http://xxx.xxx.xxx.xxx/major
        返回的结果：1级目录专业列表和2级目录课程类别3级目录课程列表
    read:
        指定专业的详细信息
    """
    queryset = Major.objects.filter(category_type=1)
    serializer_class = MajorSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_class = CourseFilter

    # 为扩展做准备
    def get_queryset(self):
        name = self.request.query_params.get('major_name', None)
        if name is not None:
            queryset = Major.objects.filter(id=name)
            return queryset

        return self.queryset


class ChapterListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        课程章节列表
        请求指定课程下的章节 http://127.0.0.1:8000/course/?id=4
        需要指定课程的id
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        course = self.request.query_params.get('id', None)
        if course is not None:
            queryset = self.queryset.filter(course_name_id=str(course))
            return queryset
        return self.queryset


class ChapterInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        课程章节列表
    read:
        请求指定章节的详细页面 http://127.0.0.1:8000/chapter/1/
            需要指定章节的id
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


class PracticeListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        章节练习列表
        请求指定章节下的练习 http://127.0.0.1:8000/chapter/?chapter=2
    read:
        请求指定章节的详细信息 http://127.0.0.1:8000/chapter/1/
        需要指定章节的id
    """

    queryset = Practice.objects.all()
    serializer_class = PracticeSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        chapter = self.request.query_params.get('chapter', None)
        if chapter is not None:
            queryset = self.queryset.filter(chapter_name__id=str(chapter))
            return queryset
        return self.queryset



