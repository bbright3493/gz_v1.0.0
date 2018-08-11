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
from apps.users import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name="login"),
    url(r'register$', views.RegisterView.as_view(), name='register'),
    url(r'logout$', views.LogoutView.as_view(), name='logout'),
    url(r'achievement$', views.UserAchievementView.as_view(), name='UserAchievementView'),
    url(r'resume$', views.UserResumeView.as_view(), name='resume'),
    url(r'setting$', views.UserSettingView.as_view(), name='setting'),
    url(r'task$', views.UserTaskView.as_view(), name='task'),
    url(r'blog$', views.UserBlogView.as_view(), name='blog'),
    # url(r'^$', views.ShowIndexView.as_view(), name="index"),  # 主页

]
