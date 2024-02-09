from django.db import models


class Info(models.Model):
    author = models.CharField()
    address = models.CharField()
    description = models.CharField()


class MapModel(models.Model):
    name = models.CharField()
    preview = models.CharField()
    image = models.CharField()
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
