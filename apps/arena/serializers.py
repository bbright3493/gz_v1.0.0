

from rest_framework import serializers

from apps.user_relationship.models import UserAchievement
from .models import *


class TotalRankSerializers(serializers.ModelSerializer):
    """
    总排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"
        depth = 1


class WeekRankSerializers(serializers.ModelSerializer):
    """
    周排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"
        depth = 1


class ClassRankSerializers(serializers.ModelSerializer):
    """
    日排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"
        depth = 1


class PassSerializer(serializers.ModelSerializer):
    """
    关卡信息序列化
    """
    class Meta:
        model = Pass
        fields = "__all__"


class UserPassSerializer(serializers.ModelSerializer):
    """
    用户关卡信息序列化
    """
    class Meta:
        model = UserPass
        fields = "__all__"


class ChallengerSerializer(serializers.ModelSerializer):
    """
    挑战者信息序列化
    """
    class Meta:
        model = Challenger
        fields = "__all__"


class UserPkExerciseSerializers(serializers.ModelSerializer):
    """
    pk题目信息序列化
    """
    class Meta:
        model = UserPkExercise
        fields = "__all__"


class PkDetailSerializers(serializers.ModelSerializer):
    """
    pk详情信息序列化
    """
    user_pk_exec = UserPkExerciseSerializers(many=True)
    class Meta:
        model = UserPkDetail
        fields = "__all__"


class TeamCompSerializers(serializers.ModelSerializer):
    """
    团赛信息序列化
    """
    class Meta:
        model = TeamComp
        fields = "__all__"


class UserTeamCompSerializers(serializers.ModelSerializer):
    """
    用户团赛信息序列化
    """
    class Meta:
        model = UserTeamComp
        fields = "__all__"
