from django.db import models

from .reviewer import Reviewer
from .game import Game


class User(Reviewer):
    game_library = models.ManyToManyField(Game, through="GameStat",
                                          through_fields=("user", "game"),
                                          related_name="library")
