from django.db import models
from .game import Game


class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    review = models.TextField(default="")
