from django.db import models
from apps.users.models import UserProfile
from apps.major.models import Major
from django.utils import timezone


# Create your models here.

# 闯关模式数据库





class Pass(models.Model):
    """
    单个关卡
    """
    major = models.ForeignKey(Major, verbose_name='专业信息')
    name = models.CharField(max_length=255, verbose_name='关卡名称')
    pass_no = models.CharField(max_length=20, verbose_name='关卡编号')
    pass_intr = models.CharField(max_length=500, verbose_name='关卡说明')
    pass_std = models.CharField(max_length=600, verbose_name='过关标准')
    pass_answer = models.CharField(max_length=800, verbose_name='关卡答案')
    pass_limit_time = models.CharField(max_length=20, verbose_name='限时时间')

    class Meta:
        verbose_name = '单个关卡'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#注意：还需要建立一个表  用户存储用户和关卡的关系  即用户 关卡表  该表在user下体现
class UserPass(models.Model):
    """
    用户-关卡表
    """
    user = models.ForeignKey(UserProfile, verbose_name='学生名')
    user_pass = models.ForeignKey(Pass, verbose_name='关卡')
    pass_score = models.IntegerField(default=0, verbose_name='关卡评分')
    user_submit = models.CharField(max_length=2000, verbose_name='用户提交代码', blank=True, null=True)
    submit_time = models.DateTimeField(default=timezone.now(), verbose_name='用户提交时间')
    complete_time = models.IntegerField(default=0, verbose_name='完成用时')
    submit_num = models.IntegerField(default=0, verbose_name='用户提交次数')

    class Meta:
        verbose_name = '用户关卡表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_pass.name


class PkQuestion(models.Model):
    """
    pk题库
    """
    name = models.CharField(max_length=50, verbose_name='题目名称')
    content = models.CharField(max_length=500, verbose_name='题目内容')
    answer = models.CharField(max_length=500, verbose_name='题目答案')
    complete_time = models.CharField(max_length=30, verbose_name='完成时间')

    class Meta:
        verbose_name = 'pk题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Challenger(models.Model):
    """
    挑战者表
    """
    PK_TYPE = (
        (1, "时间赛"),
        (2, "速度赛"),
        (3, "编程赛"),
    )
    PK_STATUS = (
        (1, "发起挑战"),
        (2, "挑战进行中"),
        (3, "挑战完成"),
    )
    be_challenged = models.ForeignKey(UserProfile, verbose_name='被挑战者', related_name="be_chg")
    challenger = models.ForeignKey(UserProfile, verbose_name='挑战者', related_name='chg')
    pk_mode = models.IntegerField(default=1, choices=PK_TYPE, verbose_name="挑战类别")
    status = models.IntegerField(default=1, choices=PK_STATUS, verbose_name='挑战状态')

    class Meta:
        verbose_name = '挑战者表'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class UserPkDetail(models.Model):
    """
    当前pk详情表
    """
    challenger = models.ForeignKey(Challenger, verbose_name='挑战者信息')
    user = models.ForeignKey(UserProfile, verbose_name="用户信息")
    user_comp_status = models.IntegerField(default=0, verbose_name='用户完成题数')
    challenger_comp_status = models.IntegerField(default=0, verbose_name='挑战者完成题数')
    user_score = models.IntegerField(default=0, verbose_name='用户得分')
    chalenger_score = models.IntegerField(default=0, verbose_name='挑战者得分')

    class Meta:
        verbose_name = 'pk详情表'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class UserPkExercise(models.Model):
    """
    用户pk题目
    """
    question = models.ForeignKey(PkQuestion, verbose_name='pk题目')
    user_pk_info = models.ForeignKey(UserPkDetail, verbose_name='当前用户pk详情', related_name='user_pk_exec')
    user_answer = models.CharField(max_length=500, verbose_name='用户答案')
    challenger_answer = models.CharField(max_length=500, verbose_name='挑战者答案')

    class Meta:
        verbose_name = '用户pk题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#团赛页面
class TeamComp(models.Model):
    """
    团赛表
    """
    title = models.CharField(max_length=100, verbose_name='团赛题目')
    content = models.CharField(max_length=500, verbose_name='团赛内容')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    member_num = models.IntegerField(verbose_name='成员数量')
    recruit = models.CharField(max_length=500, verbose_name='征召说明')

    class Meta:
        verbose_name = '团赛'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserTeamComp(models.Model):
    """
    用户团赛表
    """
    user = models.IntegerField(default=0, verbose_name=u'用户id')
    team_comp = models.ForeignKey(TeamComp, verbose_name=u'参与团赛')
    join_time = models.DateTimeField(default=timezone.now, verbose_name=u'加入时间')
    duty = models.CharField(max_length=50, verbose_name=u'担任岗位')

    class Meta:
        verbose_name = '用户团赛信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s"%(self.team_comp.title)




