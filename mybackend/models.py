from django.db import models

from django.db import models


class App(models.Model):
    title = models.CharField(max_length=100)
    year = models.FloatField()
    age_rating = models.CharField(max_length=100)
    imdb_rating = models.FloatField()
    on_netflix = models.IntegerField()
