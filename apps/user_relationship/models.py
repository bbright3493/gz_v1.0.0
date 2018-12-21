from django.db import models
from django.utils import timezone

from extra_apps.DjangoUeditor.models import UEditorField
from apps.users.models import *
from apps.major.models import *


class UserMajor(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学生名')
    major = models.ForeignKey(Major, verbose_name='专业名')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='开通时间')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='结束时间')

    class Meta:
        verbose_name = '学生专业'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.major.name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学生名')
    course = models.ForeignKey(Major, verbose_name='课程名')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='开始学习时间')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='结束时间')
    complete = models.BooleanField(default=False, verbose_name='是否学完')

    class Meta:
        verbose_name = '学生课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name


class UserChapter(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学生名', help_text='用户id')
    chapter = models.ForeignKey(Chapter, verbose_name='章节名', help_text='章节id')
    course = models.ForeignKey(Major, verbose_name='课程名', help_text='课程id')
    course_end = models.BooleanField(default=False, verbose_name='课程是否完成', help_text='课程是否完成，True或False')
    chapter_end = models.BooleanField(default=False, verbose_name='章节是否完成', help_text='章节是否完成，True或False')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='完成时间', help_text='完成时间')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='开始时间', help_text='开始时间')

    class Meta:
        verbose_name = '用户章节信息'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'chapter')

    def __str__(self):
        return self.chapter.chapter_name


class UserPractice(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学生名', help_text='用户id')
    chapter = models.ForeignKey(Chapter, verbose_name='章节名', help_text='章节id')
    practice = models.ForeignKey(Practice, verbose_name='练习名', help_text='练习题id')
    types = models.IntegerField(verbose_name='类别', help_text='类别')
    # start_time = models.DateTimeField(default=timezone.now, verbose_name='开始学习时间', help_text='开始时间')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='结束时间', help_text='结束时间')
    practice_info = models.TextField(default='', verbose_name='练习内容', help_text='练习题提交答案')
    # course_end = models.BooleanField(default=False, verbose_name='课程是否完成')
    # chapter_end = models.BooleanField(default=False, verbose_name='章节是否完成')
    count = models.IntegerField(default=0, verbose_name='作业提交次数', help_text='作业提交次数')

    class Meta:
        verbose_name = '学生练习信息'
        verbose_name_plural = verbose_name
        # unique_together = ("user", "practice")

    def __str__(self):
        return self.practice.practice_name


class UserAchievement(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    class_rankings = models.IntegerField(default=0, verbose_name='班级排名')
    monthly_rankings = models.IntegerField(default=0, verbose_name='月排名')
    total_ranking = models.IntegerField(default=0, verbose_name='总排名')
    total_ranking_time = models.DateTimeField(default=timezone.now, verbose_name='排名时间')
    estimated_time = models.DateTimeField(default=timezone.now, verbose_name='预计完成时间')

    class Meta:
        verbose_name = '学生成绩表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserBlog(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名')
    blog_name = models.CharField(max_length=255, verbose_name='博客名', help_text='博客名')
    blog_body = UEditorField(verbose_name='博客正文', imagePath="goods/images/", width=1000, height=800,
                             filePath="goods/files/", default='', help_text='博客正文')
    blog_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间', help_text='创建时间')

    class Meta:
        verbose_name = '用户博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog_name


class UserTask(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名')
    task_name = models.CharField(max_length=255, verbose_name='作业名字', help_text='作业名字')
    download = models.FileField(upload_to='task/%Y/%m/%d/', null=True, blank=True, verbose_name='作业下载地址', help_text='作业下载地址')
    complete_time = models.DateTimeField(default=timezone.now, verbose_name='提交时间', help_text='提交时间')

    class Meta:
        verbose_name = '学生作业'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name


class UserMission(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户名', help_text='用户名')
    chapter = models.ForeignKey(Chapter, verbose_name='章节id', help_text='章节id')
    mission = models.ForeignKey(ChapterTask, verbose_name='任务id', help_text='任务id')
    data_info = models.TextField(verbose_name='任务完成说明', help_text='任务完成说明')

    status = (
        (1, "未批改"),
        (2, "已批改"),
        #     (3, "三级类目"),
    )
    task_status = models.IntegerField(choices=status, verbose_name="用户任务状态", default=1)

    task_end = models.BooleanField(default=False, verbose_name='任务是否完成', help_text='任务是否完成')
    file = models.FileField(upload_to='mission/%Y/%m/%d/', max_length=1000, null=True, blank=True, verbose_name='上传文件',
                            help_text='上传文件')
    video_file = models.FileField(upload_to='mission/%Y/%m/%d/', max_length=1000, null=True, blank=True, verbose_name='上传视频文件',
                            help_text='上传视频文件')
    image = models.ImageField(upload_to="mission/%Y/%m/%d/", null=True, blank=True, verbose_name="上传图片文件")
    submit_time = models.DateTimeField(default=timezone.now, verbose_name='提交时间', help_text='提交时间')
    complete_time = models.DateTimeField(null=True, blank=True, verbose_name='完成时间', help_text='完成时间')

    class Meta:
        verbose_name = '用户任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s-%s'%(self.user.name, self.mission.name)


# class TeacherEvaluationNew(models.Model):
#     teacher = models.ForeignKey(Teacher, verbose_name='老师id', help_text='老师id')
#     user_mission = models.ForeignKey(UserMission, verbose_name='用户提交任务', related_name='user_task_evalution')
#     content = models.TextField(verbose_name='评价内容', help_text='评价内容')
#     evaluation_time = models.DateTimeField(default=timezone.now, verbose_name='评价时间', help_text='评价时间')
#     pass_type = (
#         (1, "未通过"),
#         (2, "通过"),
#         #     (3, "三级类目"),
#     )
#     is_pass = models.IntegerField(choices=pass_type, verbose_name="是否通过", help_text="是否通过", default=1)
#
#     class Meta:
#         verbose_name = '老师评价新'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.teacher.name


class TeacherEvaluation(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name='老师id', help_text='老师id')
    mission = models.ForeignKey(ChapterTask, verbose_name='任务id', help_text='任务id', related_name='task_evaluation')
    #user_submit_mission = models.ForeignKey(UserMission, verbose_name='用户提交任务', help_text='用户提交任务', related_name='user_mission_evaluation', default=None)
    user = models.ForeignKey(UserProfile, verbose_name='用户名', help_text='用户名')
    data = models.TextField(verbose_name='评价内容', help_text='评价内容')
    evaluation_time = models.DateTimeField(default=timezone.now, verbose_name='评价时间', help_text='评价时间')
    pass_type = (
        (1, "未通过"),
        (2, "通过"),
        #     (3, "三级类目"),
    )
    is_pass = models.IntegerField(choices=pass_type, verbose_name="是否通过", help_text="是否通过", default=1)

    class Meta:
        verbose_name = '老师评价'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher.name


