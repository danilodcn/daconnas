from rest_framework import serializers
from core import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Speaker
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = "__all__"



class PublicationsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    speaker = SpeakerSerializer()
    topic = TopicSerializer()
    post = PostSerializer()

    class Meta:
        model = models.Publication
        fields = ["published_at", "visualizations", "author", "speaker", "topic", "post"]