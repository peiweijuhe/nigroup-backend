from rest_framework import viewsets
from .serializers import PublicationSerializer
from .models import Publication


class PublicationView(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()
