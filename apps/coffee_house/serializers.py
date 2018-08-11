

from rest_framework import serializers

from apps.coffee_house.models import *


class TeacherMsgSerializers(serializers.ModelSerializer):
    """
    老师留言信息序列化
    """
    class Meta:
        model = TeacherUserMsg
        fields = "__all__"


class StudentMsgSerializers(serializers.ModelSerializer):
    """
    学生消息信息序列化
    """
    class Meta:
        model = StudentMsg
        fields = "__all__"




class DiscussSerializers(serializers.ModelSerializer):
    """
    论坛帖子信息序列化
    """
    class Meta:
        model = DiscussMsg
        fields = "__all__"