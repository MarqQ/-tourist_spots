from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from locations.models import Location
from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):

    serializer_class = LocationSerializer
    filter_backends = [SearchFilter]
    search_fields = ('location1', 'location2', 'city')

    def get_queryset(self):
        return Location.objects.filter()
