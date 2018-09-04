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
from apps.user_relationship.models import UserAchievement
from .serializers import *

from apps.utils.permissions import *

from .models import *
from users.serializers import UserProfileSerializers



#排行榜页面
class TotalRankViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取总排行信息
    """
    queryset = UserAchievement.objects.order_by('total_ranking')
    serializer_class = TotalRankSerializers



class WeekRankViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取周排行信息
    首先查询用户信息
    获取用户所在城市
    查询该城市下用户排行信息
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = WeekRankSerializers

    def get_queryset(self):
        return UserAchievement.objects.filter(user__city=self.request.user.city).order_by('monthly_rankings')


class DayRankViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取日排行信息
    首先查询用户信息
    获取用户班级
    查询该班级下用户排行信息
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ClassRankSerializers


    def get_queryset(self):
        return UserAchievement.objects.filter(user__in_class=self.request.user.in_class).order_by('class_rankings')

#闯关模式
class PassPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class PassListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取关卡信息
    http://127.0.0.1:8000/pass/访问所有关卡 内含分页信息
    http://127.0.0.1:8000/pass/2/ 按关卡id访问某一个关卡
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Pass.objects.all().order_by('pass_no')
    serializer_class = PassSerializer
    pagination_class = PassPagination


class UserPassListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    获取用户关卡信息
    http://127.0.0.1:8000/pass/访问用户所有关卡 内含分页信息
    http://127.0.0.1:8000/pass/2/ 按关卡id访问某一个关卡
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Pass.objects.all().order_by('pass_no')
    serializer_class = UserPassSerializer
    pagination_class = PassPagination

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserPass.objects.filter(user_id=self.request.user)


    def update(self, request, *args, **kwargs):
        import os
        from django.utils import timezone
        #获取用户的代码
        #保存代码为xxx.java文件
        #编译代码 os.popen("javac test.java")
        #执行代码 os.popen("java mypack.test").read()
        #将执行结果和答案比较


        cur_user_pass = UserPass.objects.get(id=kwargs['pk'])

        cur_user_pass.submit_num += 1 #提交次数加1

        request.data['submit_num'] = cur_user_pass.submit_num

        request.data['submit_time'] = timezone.now()

        code = request.data['user_submit']


        print(code)
        with open('test.java', 'w+') as f:
            f.write(code)
        ret = os.popen("javac test.java")
        print(ret)
        result = os.popen("java test").read()
        print(result)

        if result and result[0:5] in cur_user_pass.user_pass.pass_answer:
            request.data['pass_score'] = 100
            #cur_user_pass.pass_score = 100
        else:
            request.data['pass_score'] = 0

        return mixins.UpdateModelMixin.update(self, request, args, kwargs)

"""
pk页面 前端查询逻辑如下：
pk首页 首先按照各种挑战模式 查询挑战者表 相关信息显示在首页上部
如果挑战者表中的挑战状态为 发起挑战 按钮显示迎战 否则显示继续挑战
再查询被挑战者信息 显示可以接受挑战的人员
点击迎战按钮后 向后端发起请求 生成pk信息  生成后 利用返回的pk信息构建pk详情页面
点击继续挑战按钮后  直接获取当前进行的pk信息 并显示pk详情页
"""


class ChallengerTimeModList(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取挑战者列表信息 竞技场对战模式上方发起挑战者人员数据 时间赛
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = ChallengerSerializer

    def get_queryset(self):
        return Challenger.objects.filter(be_challenged=self.request.user).filter(pk_mode=1)


class ChallengerSpeedModList(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取挑战者列表信息 竞技场对战模式上方发起挑战者人员数据 速度赛
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = ChallengerSerializer

    def get_queryset(self):
        return Challenger.objects.filter(be_challenged=self.request.user).filter(pk_mode=2)


class ChallengerProgramModList(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取挑战者列表信息 竞技场对战模式上方发起挑战者人员数据 编程赛
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = ChallengerSerializer

    def get_queryset(self):
        return Challenger.objects.filter(be_challenged=self.request.user).filter(pk_mode=3)


class WantChallengeredList(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    获取希望被挑战的人员列表 竞技场对战模式下方候选挑战者显示数据
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(want_be_challenged=True)[0:5]


class LaunchChallenge(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    获取用户发起的挑战列表 详情 创建新的挑战
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = ChallengerSerializer

    def get_queryset(self):
        return Challenger.objects.filter(challenger=self.request.user)


class PkDetail(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    pk详情信息
    bb 实现创建pk详情页的接口
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = PkDetailSerializers

    def get_queryset(self):
        return UserPkDetail.objects.get(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return mixins.CreateModelMixin.create(self, request, args, kwargs)


class TeamCompPagination(PageNumberPagination):
    """
    团赛信息分页器
    """
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 30


class TeamCompList(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    团赛列表页
    """
    queryset = TeamComp.objects.all()
    serializer_class = TeamCompSerializers
    pagination_class = TeamCompPagination


class JoinTeamComp(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    加入团赛
    """
    serializer_class = UserTeamCompSerializers

