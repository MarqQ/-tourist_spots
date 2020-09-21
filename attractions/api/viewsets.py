from rest_framework.viewsets import ModelViewSet
from attractions.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):

    serializer_class = AttractionSerializer

    def get_queryset(self):
        return Attraction.objects.filter()
