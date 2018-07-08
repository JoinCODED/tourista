from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    pretty_picture = models.ImageField()
    activities = models.TextField()
    optimal_visiting_season = models.CharField(max_length=10)

