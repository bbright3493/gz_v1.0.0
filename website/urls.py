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

router = DefaultRouter()
# 专业列表api
router.register(r'major', MajorListViewSet, base_name='major')

# 课程列表api
#router.register(r'course', CourseListViewSet, base_name='course')

# 课程章节列表api
router.register(r'course', ChapterListViewSet, base_name='course')

# 章节详细信息页面api
router.register(r'chapter', ChapterInfoViewSet, base_name='chapter')


# 章节完成api
router.register(r'complete', UserChapterEndViewSet, base_name='complete')

# 章节练习列表api
router.register(r'practice', PracticeListViewSet, base_name='practice')

# 用户练习提交api
router.register(r'user_practice', UserPracticeViewSet, base_name='user_practice')

# 用户成绩信息api
#router.register(r'results', UserResultsViewSet, base_name='results')


# 用户作业信息api
router.register(r'task', UserTaskListViewSet, base_name='task')

# 用户blog api
router.register(r'blog', UserBlogViewSet, base_name='blog')

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

#图书馆首页信息
router.register(r'library_index', KnowledgeListViewSet, base_name='konwledge_index_list')

#图书馆搜索信息页
router.register(r'library_search', SearchKnowledgeListViewSet, base_name='knowledge_seerch_list')

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


#论坛列表组件
router.register(r'discuss_msg', DiscussListViewSet, base_name='discuss_msg')




urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title='格子网塾数据api接口说明文档')),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/', obtain_jwt_token),  # jwt认证
    url(r'logout/', LogoutView.as_view(), name='logout'),  # 退出登录
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),  # 资源文件加载地址
]

# if DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(
#         MEDIA_URL, document_root=MEDIA_ROOT)
# else:
#     urlpatterns = [
#         url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),  # 静态文件加载地址
#     ]