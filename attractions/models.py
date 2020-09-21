from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    schedule = models.TextField()
    pal = models.IntegerField()
    picture = models.ImageField(upload_to='attraction', null=True, blank=True)

    def __str__(self):
        return self.name
