from rest_framework import serializers
from .models import Research


class ResearchSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Research
        fields = ('link', 'image', 'title', 'content1', 'content2', 'content3')
