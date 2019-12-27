from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Gallery
        fields = ('title', 'image','key')
