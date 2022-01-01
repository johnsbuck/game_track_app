from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    