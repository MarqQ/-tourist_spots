from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from attractions.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):

    serializer_class = AttractionSerializer
    filter_backends = [SearchFilter]
    search_fields = ('name', 'description')

    def get_queryset(self):
        return Attraction.objects.filter()
