from rest_framework.viewsets import ModelViewSet
from locations.models import Location
from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):

    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter()
