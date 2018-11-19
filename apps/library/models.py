
# Create your models here.

from django.db import models
from datetime import datetime
from apps.major.models import Course
from DjangoUeditor.models import UEditorField
# Create your models here.


class Knowledge(models.Model):
    """
    单个知识点
    """
    name = models.CharField(max_length=100, verbose_name='单个知识点')
    intr = models.CharField(max_length=5000, verbose_name='知识点文字介绍', default='', null=True, blank=True)
    intr_text_pic = UEditorField(verbose_name='知识点图文介绍', imagePath="library/images/", width=1000, height=500,
                                filePath="library/files/", default='', null=True, blank=True)
    tag = models.CharField(max_length=200, verbose_name='知识点标签')
    father_tag = models.CharField(max_length=200, verbose_name='知识点父标签')
    level = models.IntegerField(default=0, verbose_name='知识点级别')


    class Meta:
        verbose_name = '单个知识点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_imgs(self):
        return self.knowimage_set



class KnowledgeCourse(models.Model):
    """
    知识点课程表
    """
    course = models.ForeignKey(Course, verbose_name='所属课程')
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点')

    class Meta:
        verbose_name = '知识点对应课程'
        verbose_name_plural = verbose_name



class KnowImage(models.Model):
    """
    知识点图片
    """
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点', related_name='images')
    name = models.CharField(max_length=100, verbose_name='图片名称')
    image = models.ImageField(verbose_name='知识点图片')
    intr = models.CharField(max_length=2000, verbose_name='图片介绍')

    class Meta:
        verbose_name = '知识点图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class KnowVideo(models.Model):
    """
    知识点视频
    """
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点', related_name='videos')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    video_url = models.URLField(verbose_name='知识点视频路径')
    intr = models.CharField(max_length=2000, verbose_name='视频介绍')

    class Meta:
        verbose_name = '知识点视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class KnowMind(models.Model):
    """
    知识点导图
    """
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点', related_name='minds')
    name = models.CharField(max_length=100, verbose_name='导图名称')
    # video_url = models.URLField(verbose_name='知识点导图下载路径')
    intr = models.CharField(max_length=2000, verbose_name='导图介绍')
    mind_image = models.ImageField(verbose_name='导图展示图片')
    file = models.FileField(upload_to='library/%Y/%m/%d/', max_length=1000, null=True, blank=True, verbose_name='导图文件',
                            help_text='导图文件')

    class Meta:
        verbose_name = '知识点导图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class KnowAudio(models.Model):
    """
    知识点音频
    """
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点', related_name='audios')
    name = models.CharField(max_length=100, verbose_name='音频名称')
    #Audio_url = models.URLField(verbose_name='知识点音频路径')
    intr = models.CharField(max_length=2000, verbose_name='音频介绍')
    file = models.FileField(upload_to='library/%Y/%m/%d/', max_length=1000, null=True, blank=True, verbose_name='音频文件',
                            help_text='音频文件')

    class Meta:
        verbose_name = '知识点音频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class KnowSoft(models.Model):
    """
    知识点软件
    """
    knowledge = models.ForeignKey(Knowledge, verbose_name='知识点', related_name='softs')
    name = models.CharField(max_length=100, verbose_name='软件名称')
    #Audio_url = models.URLField(verbose_name='知识点音频路径')
    intr = models.CharField(max_length=2000, verbose_name='软件介绍')
    file = models.FileField(upload_to='library/%Y/%m/%d/', max_length=1000, null=True, blank=True, verbose_name='软件文件',
                            help_text='软件文件')

    class Meta:
        verbose_name = '知识点软件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name