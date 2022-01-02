from django.db import models
from .reviewer import Reviewer
from .game import Game


class Recommendation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    notes = models.TextField(default="", blank=True)
