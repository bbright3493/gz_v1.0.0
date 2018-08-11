from django.db import models

from apps.users.models import UserProfile, Teacher
from django.utils import timezone


# Create your models here.
class TeacherUserMsg(models.Model):
    """
    老师发送给学生的消息
    """
    TYPE_CHOICES = (
        (0, '学生消息'),
        (1, '讲师消息')
    )
    student = models.ForeignKey(UserProfile, verbose_name='学生信息')
    teacher = models.ForeignKey(Teacher, verbose_name='老师信息')
    message = models.CharField(max_length=1000, verbose_name='发送的消息')
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    msg_type = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name='消息类型')

    class Meta:
        verbose_name = '老师学生消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '老师学生消息'


class StudentMsg(models.Model):
    """
    学生消息
    """
    TYPE_CHOICES = (
        (0, '未读'),
        (1, '已读')
    )
    send_student = models.ForeignKey(UserProfile, verbose_name='发送消息的学生', related_name='send_stu')
    rev_student = models.ForeignKey(UserProfile, verbose_name='接收消息的学生', related_name='rev_stu')
    message = models.CharField(max_length=1000, verbose_name='发送的消息')
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
    content = models.CharField(max_length=2000, verbose_name='内容')
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
    discuss = models.ForeignKey(DiscussMsg, verbose_name='被回复的帖子')
    user = models.ForeignKey(UserProfile, verbose_name='回复人')
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u'发送时间')
    content = models.CharField(max_length=2000, verbose_name='回复内容')

    class Meta:
        verbose_name = '论坛信息回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '帖子回复'



