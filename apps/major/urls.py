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
from django.conf.urls import url

from apps.major import views

# urlpatterns = [
#     url(r'^list/(?P<major_id>\d+)$', views.CourseListView.as_view(), name='course'),
#     url(r'chapter_list/(?P<course_id>\d+)$', views.ChapterListView.as_view(), name='chapter_list'),
#     url('chapter_info/(?P<chapter_id>\d+)$', views.ChapterInfoView.as_view(), name='chapter_info'),
#
# ]
