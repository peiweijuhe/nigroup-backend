from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News


class NewsView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
