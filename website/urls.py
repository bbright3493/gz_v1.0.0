"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from extra_apps import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from website.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView



from apps.major.views import *
from apps.user_relationship.views import *
from apps.users.views import *
from apps.arena.views import *
from apps.library.views import *
from apps.coffee_house.views import *
from apps.teacher.views import *


router = DefaultRouter()
# 专业列表api
router.register(r'major', MajorListViewSet, base_name='major')

# 课程列表api
router.register(r'course', CourseListViewSet, base_name='course')

# 课程章节列表api
router.register(r'chapter', ChapterListViewSet, base_name='chapter')

# 章节详细信息页面api
# router.register(r'chapter_info', ChapterInfoViewSet, base_name='chapter_info')

# 章节完成 和 任务线api
router.register(r'complete', UserChapterEndViewSet, base_name='complete')

# 章节限时练习列表api
router.register(r'practice', PracticeListViewSet, base_name='practice')

# # 章节速度练习列表api
# router.register(r'speed_practice', SpeedPracticeViewSet, base_name='speed_practice')
#
# # 章节编程练习列表api
# router.register(r'Programming_practice', ProgrammingPracticeViewSet, base_name='Programming_practice')

# 章节任务列表api
router.register(r'chaptertask', ChapterTaskViewSet, base_name='chaptertask')

# 用户练习提交api
router.register(r'user_practice', UserPracticeViewSet, base_name='user_practice')

router.register(r'user_practice_create', UserPracticeCreateViewSet, base_name='user_practice_create')


router.register(r'user_major', UserMajorViewSet, base_name='user_major')


# 用户任务提交api
router.register(r'user_mission', UserMissionViewSet, base_name='user_mission')

# 老师评价api
router.register(r'evaluation', TeacherEvaluationViewSet, base_name='evaluation')

# 查看老师评价api
router.register(r'read_evaluation', ReadTeacherEvaluationViewSet, base_name='read_evaluation')

# 用户成绩信息api  未用到此api
# router.register(r'results', UserResultsViewSet, base_name='results')

# # 用户作业信息api
router.register(r'task', UserMissionViewSet, base_name='task')

#所有用户提交的任务信息 班主任查看  临时用
router.register(r'task_all', AllUserMissionViewSet, base_name='task_all')


# 用户blog api
router.register(r'blog', UserBlogViewSet, base_name='blog')

# 用户个人信息、设置API

router.register(r'userinfo', UserResumeViewSet, base_name='resume')

# 用户教育背景api
router.register(r'education', UserEducationViewSet, base_name='education')

# 用户项目经验api
router.register(r'project', UserProjectViewSet, base_name='project')

# 用户专业技能api
router.register(r'skillvi', UserSkillViewSet, base_name='skillvi')



#bb
# 总排行榜
router.register(r'total_rank', TotalRankViewSet, base_name='total_rank')

#周排行榜
router.register(r'week_rank', WeekRankViewSet, base_name='week_rank')

#日排行榜
router.register(r'day_rank', DayRankViewSet, base_name='day_rank')

#关卡信息
router.register(r'pass', PassListViewSet, base_name='pass_list')

#用户关卡信息
router.register(r'user_pass', UserPassListViewSet, base_name='user_pass_list')


#对战模式
#挑战者信息-时间赛
router.register(r'challenger_time', ChallengerTimeModList, base_name='challenger_time')

#挑战者信息-速度赛
router.register(r'challenger_speed', ChallengerSpeedModList, base_name='challenger_speed')

#挑战者信息-编程赛
router.register(r'challenger_program', ChallengerProgramModList, base_name='challenger_program')

#被挑战者信息
router.register(r'be_challengers', WantChallengeredList, base_name='be_challengers')

#pk详情页面
router.register(r'pk_detail', PkDetail, base_name='pk_detail')

#发起挑战 LaunchChallenge
router.register(r'launch_challenge', LaunchChallenge, base_name='launch_challenge')

#团赛模式
#团赛列表页
router.register(r'team_comp', TeamCompList, base_name='team_comp')

#加入团赛接口
router.register(r'join_team_comp', JoinTeamComp, base_name='join_team_comp')



#图书馆首页信息
router.register(r'library_index', KnowledgeListViewSet, base_name='konwledge_index_list')

#图书馆搜索信息页
router.register(r'library_search', SearchKnowledgeListViewSet, base_name='library_search')

#图书馆通过标签搜索信息页
router.register(r'library_search_tag', SearchKnowledgeByTagListViewSet, base_name='library_search_tag')

#图书馆通过父标签搜索信息页
router.register(r'library_search_father_tag', SearchKnowledgeByFatherTagListViewSet, base_name='library_search_father_tag')

#知识点图片页
router.register(r'know_image', KnowledgeImageViewSet, base_name='knowledge_image')

#知识点视频页
router.register(r'know_video', KnowledgeVideoViewSet, base_name='knowledge_video')

#知识点导图页
router.register(r'know_mind', KnowledgeMindViewSet, base_name='knowledge_mind')

#知识点音频页
router.register(r'know_audio', KnowledgeAudioViewSet, base_name='knowledge_audio')

#咖啡厅 老师交流页
#老师留言组件
router.register(r'teacher_msg', TeacherMsgListViewSet, base_name='teacher_msg')

#班级信息组件
router.register(r'user_class', ClassViewSet, base_name='user_class')

#最近消息组件
router.register(r'class_blog', UserClassBlogViewSet, base_name='class_blog')


#咖啡厅 学生交流页
#同班同学列表组件
router.register(r'classmate', UserClassMateListViewSet, base_name='classmate')


#消息组件
router.register(r'student_msg', StudentMsgViewSet, base_name='student_msg')


router.register(r'student_msg_status', StudentMsgStatusViewSet, base_name='student_msg_status')

router.register(r'teacher_msg_status', TeacherMsgStatusViewSet, base_name='teacher_msg_status')


# router.register(r'msg_img', MsgImgCreateViewSet, base_name='msg_img')


#论坛列表组件
router.register(r'discuss_msg', DiscussListViewSet, base_name='discuss_msg')


router.register(r'discuss_msg_create', DiscussCreateViewSet, base_name='discuss_msg_create')


#论坛列表组件 写入回复信息
router.register(r'discuss_replay', DiscussReplayListViewSet, base_name='discuss_repaly')

#读取回复信息
router.register(r'discuss_replay_read', DiscussReplayReadListViewSet, base_name='discuss_repaly_read')

router.register(r'group', GroupListViwSet, base_name='group')


router.register(r'group_user', GruopUserListViwSet, base_name='gruop_user')


router.register(r'group_msg', GroupMsgListViewSet, base_name='gruop_msg')

router.register(r'group_msg_create', GroupMsgViewSet, base_name='group_msg_create')

router.register(r'resource', ResourceViewSet, base_name='resource')

#学生管理接口
router.register(r'class', ClassListViewSet, base_name='calss')
router.register(r'student', StudentListViewSet, base_name='student')

router.register(r'teacher_practice_all', TeacherPracticeListViewSet, base_name='teacher_practice_all')

router.register(r'teacher_practice_correct', TeacherPracticeCorrectedListViewSet, base_name='teacher_practice_correct')

router.register(r'user_mission_status', UserMissionStautsViewSet, base_name='user_mission_status')

router.register(r'user_mission_end', UserMissionTaskEndViewSet, base_name='user_mission_end')


# 老师评价api
#创建老师评价
router.register(r'teacher_evaluation', Teache_EvaluationViewSet, base_name='teacher_evaluation')
#查询消息
router.register(r'teacher_student_msg', StudentMsgListView, base_name='teacher_student_msg')
#根据用户任务id查询老师评价
router.register(r'teacher_evaluation_user_task', TeacherEvaluationByTaskIdViewSet, base_name='teacher_evaluation_user_task')

#根据班级查询小组
router.register(r'group_class', GroupClassListViwSet, base_name='group_class')



router.register(r'group_stu_teacher_msg', GroupStuTeacherMsgListViewSet, base_name='group_stu_teacher_msg')

router.register(r'group_teacher_msg', GroupTeacherMsgListViewSet, base_name='group_teacher_msg')

router.register(r'group_teacher_stu_msg', GroupTeacherStuMsgListViewSet, base_name='group_teacher_stu_msg')



router.register(r'group_user_info', GroupUserInfoViewSet, base_name='group_user_info')

router.register(r'group_teacher_msg_create', GroupTeacherMsgViewSet, base_name='group_teacher_msg_create')

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/teacher_login/', TeacherLogin.as_view(), name='teacher_login'),

    url(r'^api/upload_img/', UploadImg.as_view(), name='upload_img'),

    url(r'^login/', obtain_jwt_token),  # jwt认证
    url(r'docs/', include_docs_urls(title='格子网塾api接口说明')),
    url(r'^results/', UserResultsView.as_view(), name='results'),  # 用户成绩api

    url(r'logout/', LogoutView.as_view(), name='logout'),  # 退出登录
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),  # 资源文件加载地址
#    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'teacher', TemplateView.as_view(template_name="index_teacher.html"), name="index_teacher"),
    url(r'^', TemplateView.as_view(template_name="index.html"), name="index"),


]

# if DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(
#         MEDIA_URL, document_root=MEDIA_ROOT)
# else:
#     urlpatterns = [
#         url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),  # 静态文件加载地址
#     ]