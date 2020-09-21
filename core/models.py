from django.db import models
from attractions.models import Attraction
from commentreviews.models import Comment
from reviews.models import Review


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approval = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Attraction)
    comment = models.ManyToManyField(Comment)
    review = models.ManyToManyField(Review)

    def __str__(self):
        return self.name
