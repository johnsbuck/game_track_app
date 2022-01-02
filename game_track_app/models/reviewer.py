from django.db import models
from .game import Game


class Reviewer(models.Model):
    name = models.CharField(max_length=130, unique=True)
    recommended_games = models.ManyToManyField(Game, through="Recommendation", through_fields=("reviewer", "game"),
                                               related_name="recommended")
    reviewed_games = models.ManyToManyField(Game, through="Review", through_fields=("reviewer", "game"),
                                            related_name="reviewed")
