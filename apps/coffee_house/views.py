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
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
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


class TeacherMsgStatusViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = TeacherMsgStatusSerializers
    queryset = TeacherUserMsg.objects.all()


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


class StudentMsgPagination(PageNumberPagination):
    """
    学生消息分页器
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 30


class StudentMsgStatusViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = StudentMsgStatusSerializers
    queryset = StudentMsg.objects.all()

class StudentMsgViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    获取学生消息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = StudentMsgSerializers
    pagination_class = StudentMsgPagination

    def get_queryset(self):
        return StudentMsg.objects.filter(Q(rev_student=self.request.user)|Q(send_student=self.request.user)).order_by("send_time")

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


class DiscussListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    获取论坛帖子
    """

    serializer_class = DiscussSerializers

    def get_queryset(self):
        return DiscussMsg.objects.all()


class DiscussCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    创建论坛帖子
    """
    serializer_class = DiscussCreateSerializers


class MsgImgCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    创建消息图片
    """
    serializer_class = MsgImgSerializers


from django.views.generic.base import View
import json
class UploadImg(View):
    def post(self, request):
        #post  api/upload_img/


        img_url = {}
        image = request.FILES.get('img')
        if image:
            img = MsgImg(image=image)
            img.save()

            print(img.image.url)

            img_url['url'] = img.image.url

            json_data = json.dumps(img_url)
        else:
            img_url['url'] = 'invalid url'

        print(json_data)

        return HttpResponse(json_data, content_type='application/json')

    def get(self, request):
        return render(request, 'img_upload.html')





class DiscussReplayListViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    写入论坛帖子回复信息
    """

    serializer_class = DiscussReplaySerializers

    def get_queryset(self):
        return DiscussReplay.objects.all()


class DiscussReplayReadListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    获取论坛帖子回复信息
    """

    serializer_class = DiscussReplayReadSerializers

    def get_queryset(self):
        return DiscussReplay.objects.all()


class GroupListViwSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/gruop/ 返回当前用户所在班级的所有小组
    """
    serializer_class = GruopSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return Group.objects.filter(in_class=self.request.user.in_class)


class GroupUserInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    获取学生所在的用户-小组信息
    list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/group_user_info/
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = GruopUserSerializers

    def get_queryset(self):
        user_groups = UserGroup.objects.filter(user=self.request.user)

        return user_groups



class GroupClassListViwSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/group_class/?class=id
            返回某个班级的所有小组
            配合教师端接口
            http://xxx.xx.xx.xx:xx/class/?teacher=id
            请求某个老师下的所有班级
            可以获取教师下面的所有小组
    """
    serializer_class = GruopSerializers

    def get_queryset(self):
        in_class = self.request.query_params.get('class', None)
        return Group.objects.filter(in_class=int(in_class))


class GruopUserListViwSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list:
            请求： http://xxx.xx.xx.xx:xx/gruopuser/？group=id 返回指定小组的所有小组成员信息
    """
    serializer_class = GruopUserSerializers

    def get_queryset(self):
        group = self.request.query_params.get('group', None)
        if group:
            return UserGroup.objects.filter(group=group)
        else:
            return UserGroup.objects.all()


class GroupMsgViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    创建用户小组消息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GruopCreateMsgSerializers


class GroupMsgListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    获取用户小组消息
    list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/group_msg/ 返回当前用户所在小组的消息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GruopMsgSerializers

    def get_queryset(self):
        group = UserGroup.objects.get(user=self.request.user).group
        return GroupMsg.objects.filter(group=group)


class GroupTeacherMsgViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    创建讲师小组消息
    group_teacher_msg_create
    """
    serializer_class = GruopTeacherCreateMsgSerializers







class GroupTeacherMsgListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    获取讲师小组消息
    list:
            需登录
            请求： http://xxx.xx.xx.xx:xx/group_teacher_msg/?teacher=id 返回教师所有小组的消息
    """

    serializer_class = GruopTeacherMsgSerializers

    def get_queryset(self):
        teacher = self.request.query_params.get('teacher', None)
        return GroupMsgTeacher.objects.filter(teacher=teacher)



