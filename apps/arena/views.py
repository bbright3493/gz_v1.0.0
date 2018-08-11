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




class UserPassListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
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



#对战模式
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


class PkDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    pk详情信息
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = PkDetailSerializers

    def get_queryset(self):
        return UserPkDetail.objects.get(user=self.request.user)



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


