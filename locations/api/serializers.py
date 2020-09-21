from rest_framework.serializers import ModelSerializer
from locations.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location1', 'location2', 'city', 'state', 'country', 'latitude', 'longitude']
