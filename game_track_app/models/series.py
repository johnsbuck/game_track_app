from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=130, primary_key=True)

