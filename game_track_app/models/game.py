from django.db import models
from .console import Console
from .series import Series
from .developer import Developer
from .genres import Genre


class Game(models.Model):
    name = models.CharField(max_length=130, unique=True)
    consoles = models.ManyToManyField(Console)
    series = models.ManyToManyField(Series)
    developers = models.ManyToManyField(Developer)
    genres = models.ManyToManyField(Genre)
