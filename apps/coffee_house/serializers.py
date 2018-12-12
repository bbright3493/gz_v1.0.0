

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


class DiscussReplaySerializers(serializers.ModelSerializer):
    """
    论坛帖子回复信息序列化
    """
    class Meta:
        model = DiscussReplay
        fields = "__all__"


class DiscussReplayReadSerializers(serializers.ModelSerializer):
    """
    论坛帖子回复信息序列化
    """
    class Meta:
        model = DiscussReplay
        fields = "__all__"
        depth = 2



class DiscussSerializers(serializers.ModelSerializer):
    """
    论坛帖子信息序列化
    """
    discuss_replay = DiscussReplayReadSerializers(many=True)
    class Meta:
        model = DiscussMsg
        fields = "__all__"
        depth = 2


class DiscussCreateSerializers(serializers.ModelSerializer):
    """
    论坛帖子信息序列化
    """
    class Meta:
        model = DiscussMsg
        fields = "__all__"


class GruopSerializers(serializers.ModelSerializer):
    """
    小组信息序列化
    """
    class Meta:
        model = Group
        fields = "__all__"


class GruopUserSerializers(serializers.ModelSerializer):
    """
    小组用户信息序列化
    """
    class Meta:
        model = UserGroup
        fields = "__all__"
        depth = 1


class GruopCreateMsgSerializers(serializers.ModelSerializer):
    """
    小组创建消息序列化
    """
    class Meta:
        model = GroupMsg
        fields = "__all__"


class GruopMsgSerializers(serializers.ModelSerializer):
    """
    小组消息列表序列化
    """
    class Meta:
        model = GroupMsg
        fields = "__all__"
        depth = 1


class MsgImgSerializers(serializers.ModelSerializer):
    """
    消息图片
    """
    class Meta:
        model = MsgImg
        fields = "__all__"

