from django.db import models
from attractions.models import Attraction


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approval = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Attraction)

    def __str__(self):
        return self.name
