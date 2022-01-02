from django.utils.translation import gettext as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .user import User
from .game import Game


class GameStatEnum(models.TextChoices):
    NOT_PLANNED = "NP", _("Not Planned")  # Not playing and not planning on playing in the upcoming future
    WAITLISTED = "WL", _("Wait-listed")  # Planning on playing in the upcoming future
    ON_HOLD = "OH", _("On Hold")  # Stopped playing at some point
    DROPPED = "DP", _("Dropped")  # No long playing and have no intention on playing
    IN_PROGRESS = "IP", _("In Progress")  # Currently playing
    FINISHED_MAIN_STORY = "FMS", _("Finished Main Story")  # Completed the main story
    FINISHED_MAIN_STORY_PLUS = "FMSP", _("Finished Main Story + Extra")  # Finished main story and extra content
    COMPLETED = "CMP", _("Completed")  # 100% or near 100% completion
    CONTINUOUS = "CTN", _("Continuous")  # Never finishing (i.e. multiplayer games)


class GameStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=GameStatEnum.choices, default=GameStatEnum.NOT_PLANNED)
    percentage = models.PositiveSmallIntegerField(blank=True,
                                                  null=True,
                                                  default=0,
                                                  validators=[MinValueValidator(0), MaxValueValidator(100)])
