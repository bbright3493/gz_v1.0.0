from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination
from django.views.generic.base import View
from django.http import HttpResponse
import json

from apps.users.models import Teacher, ClassInfo, UserProfile
from apps.users.serializers import UserClassSerializers, UserProfileSerializers
from apps.user_relationship.models import UserMission, TeacherEvaluation
from apps.user_relationship.serializers import UserMissionListSerializers, TeacherEvaluationSerializers
from apps.coffee_house.serializers import TeacherMsgSerializers
# Create your views here.


class TeacherLogin(View):
    def post(self, request):
        data_dict = {}
        name = request.POST.get('name', 0)
        password = request.POST.get('password', 0)
        try:
            teacher = Teacher.objects.get(name=name, password=password)
            data_dict['status'] = 'success'
            data_dict['id'] = teacher.id
            data_dict['name'] = teacher.name
            data_dict['types'] = teacher.types
            data_dict['intr'] = teacher.intr
            data_dict['img'] = teacher.img.url

        except:
            data_dict['status'] = 'fail'

        json_data = json.dumps(data_dict)

        return HttpResponse(json_data, content_type='application/json')


class TeacherPracticePagination(PageNumberPagination):
    """
    学生消息分页器
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 30



class TeacherPracticeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取某个老师的所有学生的作业
    list:
        请求：http://xxx.xx.xx.xx:xx/teacher_practice_all/?teacher=id
        请求指定老师下的所有班级列表
    """

    # filter_backends = (DjangoFilterBackend,)
    # filter_class = CourseFilter
    pagination_class = TeacherPracticePagination
    serializer_class = UserMissionListSerializers

    def get_queryset(self):
        #获取老师信息
        #根据老师信息查询该老师下的班级
        #根据班级查询学生
        #根据学生查询任务

        teacher_id = self.request.query_params.get('teacher', None)
        teacher = Teacher.objects.get(id=teacher_id)
        teacher_type = teacher.types
        # teacher_tutor
        if teacher_type == 1:
            classes = ClassInfo.objects.filter(teacher_tutor=teacher)
        elif teacher_type == 2:
            classes = ClassInfo.objects.filter(teacher_lector=teacher)
        else:
            classes = ClassInfo.objects.filter(teacher_head=teacher)

        all_tasks = UserMission.objects.filter(user=1)
        #获取班级的学生
        for stu_class in classes:
            students = UserProfile.objects.filter(in_class=stu_class)
            for stu in students:
                user_tasks = UserMission.objects.filter(user=stu)

                if user_tasks:
                    all_tasks = all_tasks | user_tasks

        return all_tasks


class ClassListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取某个老师的所有班级
    """
    serializer_class = UserClassSerializers

    def get_queryset(self):
        # 获取老师信息
        # 根据老师信息查询该老师下所有学生
        teacher_id = self.request.query_params.get('teacher', None)
        teacher = Teacher.objects.get(id=teacher_id)
        teacher_type = teacher.types
        # teacher_tutor
        if teacher_type == 1:
            classes = ClassInfo.objects.filter(teacher_tutor=teacher)
        elif teacher_type == 2:
            classes = ClassInfo.objects.filter(teacher_lector=teacher)
        else:
            classes = ClassInfo.objects.filter(teacher_head=teacher)

        return classes



class StudentListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取某个班级下的所有学生
    list:
        请求：http://xxx.xx.xx.xx:xx/student/?class=id
        请求指定老师下的所有班级列表
    """
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        #获取班级信息
        #根据班级信息查询该班级下所有学生
        class_id = self.request.query_params.get('class', None)
        my_class = ClassInfo.objects.get(id=class_id)

        students = UserProfile.objects.filter(in_class=my_class)

        return students


"""
根据学生查询该学生的任务信息
"""
class StudentTaskListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取某个学生提交的任务信息列表 如果有教师评语 会同时获取
    list:
        请求：http://xxx.xx.xx.xx:xx/student_task/?student=id
        请求指定学生的任务列表
    """
    serializer_class = UserMissionListSerializers
    def get_queryset(self):
        #获取学生信息
        student_id = self.request.query_params.get('student', None)
        student = UserProfile.objects.get(id=student_id)
        user_tasks = UserMission.objects.filter(user=student)
        return user_tasks


class Teache_EvaluationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    根据学生id，老师id，任务id创建老师点评
    """
    serializer_class = TeacherEvaluationSerializers

    def get_queryset(self):
        return TeacherEvaluation.objects.all()


"""
根据学生查询该学生的留言信息
"""
class StudentMsgListView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    获取某个学生的留言信息以及老师的回复信息
    创建留言
    list:
        请求：http://xxx.xx.xx.xx:xx/student_msg/?student=id
        请求指定学生的留言列表
    create:
        创建留言 教师后台只创建教师留言
    """
    serializer_class = TeacherMsgSerializers

    def get_queryset(self):
        student_id = self.request.query_params.get('student', None)
        student = UserProfile.objects.get(id=student_id)
        return TeacherEvaluation.objects.filter(user=student)



