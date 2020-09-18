from django.db import models


class TouristSpots(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name
