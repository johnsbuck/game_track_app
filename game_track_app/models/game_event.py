from django.db import models
from django.utils import timezone

from .game_stat import GameStat


class GameEvent(models.Model):
    stat = models.ForeignKey(GameStat, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(default="")
