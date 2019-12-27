from rest_framework import viewsets
from .serializers import GallerySerializer
from .models import Gallery


class GalleryView(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
