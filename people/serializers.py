from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    headshot = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = People
        fields = ('name', 'title', 'email', 'project', 'address', 'experience', 'completed', 'headshot')
