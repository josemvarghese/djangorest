from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Kitten(Animal):
    pass


class Puppy(Animal):
    pass
