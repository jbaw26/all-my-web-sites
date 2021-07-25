from django.db import models


class Carte(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name