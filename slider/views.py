from rest_framework import viewsets
from .serializers import SliderSerializer
from .models import Slider


class SliderView(viewsets.ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()
