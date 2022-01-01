from django.db import models
from .console import Console
from .series import Series
from .developer import Developer
from .genres import Genre
from .game_status import GameStatus


class Game(models.Model):
    name = models.CharField(max_length=130, primary_key=True)
    owned = models.BooleanField(default=False)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    consoles = models.ManyToManyField(Console)
    developers = models.ManyToManyField(Developer)
    genres = models.ManyToManyField(Genre)
    game_status = models.CharField(max_length=4, choices=GameStatus.choices, default=GameStatus.NOT_PLANNED)
