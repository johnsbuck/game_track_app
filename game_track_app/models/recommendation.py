from django.db import models
from .game import Game


class Recommendation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    recommender = models.CharField(max_length=130)
    notes = models.TextField(default="")
