from rest_framework import serializers
from core.models import Publication, Topic


class PublicationsSerializers(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(many=True)
    speaker = serializers.StringRelatedField(many=True)
    topic = serializers.StringRelatedField(many=True)
    post = serializers.StringRelatedField(many=True)

    class Meta:
        model = Publication
        fields = ["published_at", "visualizations", "autor", "speaker", "topic", "post"]