from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
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
from apps.user_relationship.models import UserMajor


# Create your views here.
from utils.serializers_format import value_format


class MajorListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        请求：http://xxx.xx.xx.xx:xx/major/  列出所有专业和它下面的课程分类
        在用户未登录或不是未添加专业的用户登录会显示全部课程，添加专业的用户会像是本专业
    read:
        请求：http://xxx.xx.xx.xx:xx/major/id/ 获得指定专业的信息，id为专业的数据库中存储的id值
    """
    queryset = Major.objects.all()
    serializer_class = MajorSerializers
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = CourseFilter

    def get_queryset(self):
        print(self.request.user)
        #if self.request.user == 'AnonymousUser': #bug
        if not self.request.user.is_authenticated(): #bb
            return self.queryset
        try:
            queryset = UserMajor.objects.filter(user=self.request.user)

            if queryset:
                for user in queryset:
                    queryset = self.queryset.filter(id=user.major_id)
                return queryset
            else:
                return self.queryset

        except:
            pass


class CourseListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        请求：http://xxx.xx.xx.xx:xx/course/  列出所有课程
        请求：http://xxx.xx.xx.xx:xx/course/?category=id 列出指定类别下的课程， id为类别数据库id

    """
    queryset = CategoryAndCourse.objects.all()
    serializer_class = CategoryAndCourseSerializers
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        name = self.request.query_params.get('category', None)
        if name is not None:
            queryset = CategoryAndCourse.objects.filter(category=name)
            return queryset

        return self.queryset


class ChapterListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求：http://xxx.xx.xx.xx:xx/course/ 获得所有课程章节
        请求：http://xxx.xx.xx.xx:xx/course/?id=1 指定课程下的章节 需要指定课程的id

    read:
        请求：http://xxx.xx.xx.xx:xx/chapter/id/ 获得指定章节的详细页面 需要指定章节的id

    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        course = self.request.query_params.get('id', None)
        print(course)
        if course is not None:
            queryset = self.queryset.filter(course_name=course)
            return queryset
        return self.queryset


# class ChapterInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     list:
#         课程章节列表
#     read:
#         请求指定章节的详细页面 http://127.0.0.1:8000/chapter/1/
#             需要指定章节的id
#     """
#     queryset = Chapter.objects.all()
#     serializer_class = ChapterSerializers
#     permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


class PracticeListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求：http://xxx.xx.xx.xx:xx/practice/ 获得所有章节练习列表
        请求：http://xxx.xx.xx.xx:xx/practice/?chapter=2 指定章节下的练习 chapter为数据库中章节的id
    read:
        请求：http://xxx.xx.xx.xx:xx/practice/1/ 获得指定章节的详细信息  需要指定章节的id
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


# class TimeLimitPracticeViewSet(PracticeListViewSet):
#     """
#         list:
#             需登录
#             请求：http://xxx.xx.xx.xx:xx/practice/ 获得所有限时章节练习列表
#             请求：http://xxx.xx.xx.xx:xx/practice/?chapter=2 指定章节下的练习 chapter为数据库中章节的id
#         read:
#             请求：http://xxx.xx.xx.xx:xx/practice/1/ 获得指定章节的详细信息  需要指定章节的id
#         """
#     queryset = TimeLimitPractice.objects.all()
#     serializer_class = TimeLimitPracticeSerializers
#     print(queryset)
#
#
# class SpeedPracticeViewSet(PracticeListViewSet):
#     """
#         list:
#             需登录
#             请求：http://xxx.xx.xx.xx:xx/practice/ 获得所有章节速度练习列表
#             请求：http://xxx.xx.xx.xx:xx/practice/?chapter=2 指定章节下的练习 chapter为数据库中章节的id
#         read:
#             请求：http://xxx.xx.xx.xx:xx/practice/1/ 获得指定章节的详细信息  需要指定章节的id
#         """
#     queryset = SpeedPractice.objects.all()
#     serializer_class = SpeedPracticeSerializers
#
#
# class ProgrammingPracticeViewSet(PracticeListViewSet):
#     """
#         list:
#             需登录
#             请求：http://xxx.xx.xx.xx:xx/practice/ 获得所有章节编程练习列表
#             请求：http://xxx.xx.xx.xx:xx/practice/?chapter=2 指定章节下的练习 chapter为数据库中章节的id
#         read:
#             请求：http://xxx.xx.xx.xx:xx/practice/1/ 获得指定章节的详细信息  需要指定章节的id
#         """
#     queryset = ProgrammingPractice.objects.all()
#     serializer_class = ProgrammingPracticeSerializers


class ChapterTaskViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        需登录
        请求：http://xxx.xx.xx.xx:xx/chaptertask/ 获得所有章节任务列表
        请求：http://xxx.xx.xx.xx:xx/chaptertask/?chapter=2 指定章节下的任务 chapter为数据库中章节的id
    read：
        请求：http://xxx.xx.xx.xx:xx/chaptertask/1/ 获得指定章节任务的详细信息  需要指定章节任务的id
    """
    queryset = ChapterTask.objects.all()
    serializer_class = ChapterTaskSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def list(self, request, *args, **kwargs):
        """
        获取所有章节任务列表
        :param request: 内置全局属性
        :param args:
        :param kwargs:
        :return:
        """
        info = []
        print(self.request.META['HTTP_HOST'])
        for queryset in self.queryset:
            serializers = MyChapterTaskSerializers(value_format(queryset, self.request.META['HTTP_HOST']))
            info.append(serializers.data)
        return Response(info)

    def retrieve(self, request, *args, **kwargs):
        """
        获取某个任务的详细信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        print(instance)
        serializer = MyChapterTaskSerializers(value_format(queryset, self.request.META['HTTP_HOST']))
        return Response(serializer.data)

    def get_queryset(self):
        """
        获取指定章节的任务列表
        :return:
        """
        chapter = self.request.query_params.get('chapter', None)
        if chapter is not None:
            queryset = self.queryset.filter(chapter_name__id=str(chapter))
            info = []
            for queryset in self.queryset:
                serializers = MyChapterTaskSerializers(value_format(queryset, self.request.META['HTTP_HOST']))
                info.append(serializers.data)
            return Response(info)

        return self.queryset

