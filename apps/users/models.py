from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.utils import timezone

from extra_apps.DjangoUeditor.models import UEditorField


# Create your models here.


class Teacher(models.Model):
    """
    老师表 bb
    """
    TYPE_CHOICES = (
        (1, '导师'),
        (2, '讲师'),
        (3, '班主任')
    )

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='名字', help_text='名字')
    types = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name='老师类型')
    intr = models.CharField(max_length=800, verbose_name='老师介绍')
    img = models.ImageField(upload_to='users/image/%Y/%m', default=None, max_length=255,
                            verbose_name='头像', help_text='头像')

    class Meta:
        verbose_name = '老师信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ClassInfo(models.Model):
    """
    班级信息 bb
    """
    name = models.CharField(max_length=100, verbose_name='班级名称')
    notice = models.CharField(max_length=500, verbose_name='班级公告')
    teacher_tutor = models.ForeignKey(Teacher, verbose_name='导师', related_name='tutor', default=None)
    teacher_lector = models.ForeignKey(Teacher, verbose_name='讲师', related_name='lector', default=None)
    teacher_head = models.ForeignKey(Teacher, verbose_name='班主任', related_name='head', default=None)

    class Meta:
        verbose_name = '班级信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_students(self):
        return self.userprofile_set.all()


class CityInfo(models.Model):
    """
    城市信息 bb
    """
    name = models.CharField(max_length=100, verbose_name='城市名称')

    class Meta:
        verbose_name = '城市信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_students(self):
        return self.userprofile_set.all()


class UserProfile(AbstractUser):
    TYPE_CHOICES = (
        (0, '超级管理员'),
        (1, '管理员'),
        (2, '导师'),
        (3, '学员'),
        (4, '游客')
    )

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='名字', help_text='名字')
    types = models.IntegerField(choices=TYPE_CHOICES, default=4, verbose_name='用户类型')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄', help_text='年龄')
    gender = models.CharField(max_length=255, choices=(('男', '男'), ('女', '女')), default='男', verbose_name='性别', help_text='性别')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='地址', help_text='地址')
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name='手机号码', help_text='手机号码')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱地址', help_text='邮箱地址')
    expected_work = models.CharField(max_length=255, null=True, blank=True, verbose_name='期望工作', help_text='期望工作')
    assessment = models.TextField(null=True, blank=True, verbose_name='自我评价', help_text='自我评价')
    img = models.ImageField(upload_to='users/image/%Y/%m', default='users/image/default.jpg', max_length=255, verbose_name='头像', help_text='头像')

    # bb
    in_class = models.ForeignKey(ClassInfo, null=True, blank=True, verbose_name='所属班级')
    score = models.IntegerField(default=0, null=True, blank=True, verbose_name='排序积分')
    city = models.ForeignKey(CityInfo, null=True, blank=True, verbose_name='所在城市')
    want_be_challenged = models.BooleanField(default=False, verbose_name='是否希望被挑战')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name
        unique_together = ("username",)

    def __str__(self):
        return self.username


class UserResume(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名', help_text='用户名')
    Study_time = models.DateTimeField(verbose_name='入学时间', help_text='入学时间')
    end_time = models.DateTimeField(verbose_name='毕业时间', help_text='毕业时间')
    school_name = models.CharField(max_length=255, verbose_name='学校名称', help_text='学校名称')
    major = models.CharField(max_length=255, verbose_name='所学专业', help_text='所学专业')
    education = models.CharField(max_length=255, verbose_name='学历', help_text='学历')
    honor = models.CharField(max_length=255, verbose_name='获得荣誉', help_text='获得荣誉')

    class Meta:
        verbose_name = '教育背景'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_name


class UserProject(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名')
    project_name = models.CharField(max_length=255, verbose_name='项目名')
    technology = models.TextField(verbose_name='使用技术')
    project_function = models.TextField(verbose_name='项目功能')
    create = models.TextField(verbose_name='个人负责板块')
    time_slot = models.CharField(max_length=255, verbose_name='项目时间段')

    class Meta:
        verbose_name = '项目经验'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserSkill(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名')
    skill_name = models.CharField(max_length=255, verbose_name='技能名')
    skill_level = models.CharField(max_length=255, choices=(('know', '了解'), ('shuxi', '熟悉'), ('skilled', '熟练'),
                                   ('master', '精通')), default='shuxi', verbose_name='技能等级')
    skill_introduce = models.CharField(max_length=255, verbose_name='技能介绍')

    class Meta:
        verbose_name = '掌握技能'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name




