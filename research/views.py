from rest_framework import viewsets
from .serializers import ResearchSerializer
from .models import Research


class ResearchView(viewsets.ModelViewSet):
    serializer_class = ResearchSerializer
    queryset = Research.objects.all()
