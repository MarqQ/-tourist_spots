from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    score = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
