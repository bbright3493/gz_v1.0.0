from django.db import models

from apps.users.models import UserProfile, Teacher
from django.utils import timezone
from apps.users.models import ClassInfo
from DjangoUeditor.models import UEditorField


# Create your models here.
class TeacherUserMsg(models.Model):
    """
    老师发送给学生的消息
    """
    TYPE_CHOICES = (
        (0, '学生消息'),
        (1, '讲师消息')
    )

    STATUS_CHOICES = (
        (0, '未读'),
        (1, '已读')
    )
    student = models.ForeignKey(UserProfile, verbose_name='学生信息')
    teacher = models.ForeignKey(Teacher, verbose_name='老师信息')
    message = models.CharField(max_length=1000, verbose_name='发送的消息')
    rich_message = UEditorField(verbose_name='富文本消息', imagePath="course/images/", width=1000, height=500,
                                filePath="course/files/", default='', null=True, blank=True)
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    msg_type = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name='消息类型')

    msg_status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='消息状态')

    class Meta:
        verbose_name = '老师学生消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '老师学生消息'


class MsgImg(models.Model):
    """
    消息图片
    """
    image = models.ImageField(upload_to="coffee_house/images/", null=True, blank=True, verbose_name="消息图")

    class Meta:
        verbose_name = '消息图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '消息图片'


class StudentMsg(models.Model):
    """
    学生消息 需改成富文本
    """
    TYPE_CHOICES = (
        (0, '未读'),
        (1, '已读')
    )
    send_student = models.ForeignKey(UserProfile, verbose_name='发送消息的学生', related_name='send_stu')
    rev_student = models.ForeignKey(UserProfile, verbose_name='接收消息的学生', related_name='rev_stu')
    message = models.CharField(max_length=1000, verbose_name='发送的消息', default='', null=True, blank=True)
    rich_message = UEditorField(verbose_name='富文本消息', imagePath="course/images/", width=1000, height=500,
                                filePath="course/files/", default='', null=True, blank=True)

    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    msg_status = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name='消息状态')

    class Meta:
        verbose_name = '学生消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '学生消息'


class DiscussMsg(models.Model):
    """
    论坛信息
    """
    TYPE_CHOICES = (
        (0, '应用'),
        (1, '站内')
    )
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.CharField(max_length=20000, verbose_name='内容')
    user = models.ForeignKey(UserProfile, verbose_name='发帖人')
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    click_num = models.IntegerField(default=0, verbose_name='浏览数')

    class Meta:
        verbose_name = '论坛信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class DiscussReplay(models.Model):
    """
    帖子回复
    """
    discuss = models.ForeignKey(DiscussMsg, verbose_name='被回复的帖子', related_name='discuss_replay')
    user = models.ForeignKey(UserProfile, verbose_name='回复人')
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    content = models.CharField(max_length=20000, verbose_name='回复内容')

    class Meta:
        verbose_name = '论坛信息回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '帖子回复'


class Group(models.Model):
    """
    小组
    """
    in_class = models.ForeignKey(ClassInfo, verbose_name='小组所在班级')
    name = models.CharField(max_length=200, verbose_name='小组名称')
    step_info = models.CharField(max_length=500, verbose_name='小组进度信息', default='编程基础')
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'小组创建时间')

    class Meta:
        verbose_name = '小组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UserGroup(models.Model):
    """
    用户小组表
    """
    user = models.ForeignKey(UserProfile, verbose_name='小组用户')
    group = models.ForeignKey(Group, verbose_name='小组')
    join_time = models.DateTimeField(default=timezone.now, verbose_name=u'加入小组时间')

    class Meta:
        verbose_name = '用户小组表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  '%s-%s'%(self.user.name, self.group.name)


class GroupMsg(models.Model):
    """
    小组聊天信息
    """
    user = models.ForeignKey(UserProfile, verbose_name='发送消息的学生')
    group = models.ForeignKey(Group, verbose_name='小组')
    message = models.CharField(max_length=1000, verbose_name='发送的消息')
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = '学生小组消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '学生小组消息'









