from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField


# Create your models here.


class Major(models.Model):
    """
    专业
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
    #     (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", default="self")
    # courses = models.ForeignKey(Course, verbose_name='课程', null=True, blank=True)
    # course_task = models.CharField(max_length=255, null=True, blank=True, verbose_name='内容介绍')
    # image = models.ImageField(upload_to="course/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "专业类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    课程
    """
    name = models.CharField(max_length=255, verbose_name='课程名字')
    course_task = models.CharField(max_length=255, null=True, blank=True, verbose_name='内容介绍')
    image = models.ImageField(upload_to="course/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CategoryAndCourse(models.Model):
    """
    课程类别
    """
    category = models.ForeignKey(Major, verbose_name='类别')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '课程关系'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name


class Chapter(models.Model):
    """
    章节
    """
    course_name = models.ForeignKey(Course, verbose_name='课程')
    chapter_name = models.CharField(max_length=255, verbose_name='章节名字', help_text='章节名字')
    chapter_number = models.IntegerField(verbose_name='章节数')
    chapter_introduce = models.CharField(max_length=255, verbose_name='章节介绍')
    chapter_video = models.CharField(max_length=255, null=True, blank=True, verbose_name='视频')
    chapter_task = UEditorField(verbose_name='章节任务说明', imagePath="course/images/", width=1000, height=500,
                                filePath="course/files/", default='')
    chapter_target = models.CharField(max_length=255, verbose_name='章节目标')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        unique_together = ("course_name", "chapter_number")

    def __str__(self):
        return self.chapter_name


class Practice(models.Model):
    """
    练习
    """
    CATEGORY_TYPE = (
        (1, "限时练习题"),
        (2, "速度练习题"),
        (3, "编程练习题"),
    )
    chapter_name = models.ForeignKey(Chapter, verbose_name='章节', help_text='章节id')
    practice_name = models.CharField(max_length=255, verbose_name='练习名', help_text='练习id')
    _type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类别", help_text="类别")
    info = models.CharField(max_length=255, default=None, null=True, blank=True, verbose_name='提示信息', help_text='提示信息')
    data = models.TextField(null=True, blank=True, verbose_name='练习题内容', help_text='习题内容')
    Practice_standard = models.TextField(null=True, blank=True, verbose_name='过关标准', help_text='练习过关标准信息')
    standard_explain = models.TextField(null=True, blank=True, verbose_name='题目说明', help_text='练习说明')
    standard_answer = models.TextField(verbose_name='练习答案', help_text='练习答案')
    return_score = models.TextField(null=True, blank=True, verbose_name='评分返回', help_text='评分返回')
    submit_num = models.IntegerField(null=True, blank=True, verbose_name='提交次数', help_text='占位字段')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = '练习'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.practice_name


# class TimeLimitPractice(Practice):
#
#     class Meta:
#         verbose_name = '限时练习题'
#         verbose_name_plural = verbose_name
#
#
# class SpeedPractice(Practice):
#
#     class Meta:
#         verbose_name = '速度练习题'
#         verbose_name_plural = verbose_name
#
#
# class ProgrammingPractice(Practice):
#
#     class Meta:
#         verbose_name = '编程题'
#         verbose_name_plural = verbose_name


class ChapterTask(models.Model):
    """
    章节任务
    """
    chapter_name = models.ForeignKey(Chapter, verbose_name='章节')
    name = models.CharField(max_length=255, verbose_name='任务名')
    info = models.TextField(verbose_name='任务介绍')
    # file_data = models.FileField(upload_to='/task/file/', max_length=1000, null=True, blank=True, verbose_name='上传文件')
    # image = models.ImageField(upload_to="task/images/", null=True, blank=True, verbose_name="任务截图")
    # hostip = models.URLField(verbose_name='主机地址')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '章节任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Image(models.Model):
    ChapterTask_name = models.ForeignKey(ChapterTask, verbose_name='任务')
    name = models.CharField(max_length=100, verbose_name='截图名')
    image = models.ImageField(upload_to="task/images/", null=True, blank=True, verbose_name="任务截图")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name='上传时间')

    class Meta:
        verbose_name = '任务截图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

