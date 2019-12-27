from rest_framework import viewsets  # add this
from .serializers import PeopleSerializer  # add this
from .models import People  # add this


class PeopleView(viewsets.ModelViewSet):  # add this
    serializer_class = PeopleSerializer  # add this
    queryset = People.objects.all()  # add this