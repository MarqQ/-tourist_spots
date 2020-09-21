from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):

    serializer_class = TouristSpotSerializer
    filter_backends = [SearchFilter]
    search_fields = ('name', 'description', 'location__location1', 'location__location2', 'location__city',
                     'location__state', 'location__country')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        queryset = TouristSpot.objects.all()

        if id:
            queryset = TouristSpot.objects.filter(pk=id)

        if name:
            queryset = TouristSpot.objects.filter(name__iexact=name)

        if description:
            queryset = TouristSpot.objects.filter(name__iexact=description)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).partial_update(request, *args, **kwargs)
