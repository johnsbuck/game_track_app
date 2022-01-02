from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .recommendation import Recommendation


class Review(Recommendation):
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
