from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=130, unique=True)
