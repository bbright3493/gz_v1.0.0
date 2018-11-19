

from rest_framework import serializers
from apps.library.models import *





class KnowledgeImageSerializers(serializers.ModelSerializer):
    """
    知识点图片信息序列化
    """

    class Meta:
        model = KnowImage
        fields = "__all__"


class KnowledgeVideoSerializers(serializers.ModelSerializer):
    """
    知识点视频信息序列化
    """

    class Meta:
        model = KnowVideo
        fields = "__all__"


class KnowMindSerializers(serializers.ModelSerializer):
    """
    知识点导图信息序列化
    """

    class Meta:
        model = KnowMind
        fields = "__all__"


class KnowAudioSerializers(serializers.ModelSerializer):
    """
    知识点音频信息序列化
    """

    class Meta:
        model = KnowAudio
        fields = "__all__"


class KnowSoftSerializers(serializers.ModelSerializer):
    """
    知识点软件信息序列化
    """

    class Meta:
        model = KnowSoft
        fields = "__all__"



class KnowledgeSerializers(serializers.ModelSerializer):
    """
    知识点信息序列化
    """
    images = KnowledgeImageSerializers(many=True)
    videos = KnowledgeVideoSerializers(many=True)
    minds = KnowMindSerializers(many=True)
    audios = KnowAudioSerializers(many=True)
    softs = KnowSoftSerializers(many=True)
    class Meta:
        model = Knowledge
        fields = "__all__"

