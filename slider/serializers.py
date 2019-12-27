from rest_framework import serializers
from .models import Slider


class SliderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Slider
        fields = ('title', 'image','key')
