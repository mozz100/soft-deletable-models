from django.db import models
from model_utils.models import SoftDeletableModel


class Group(models.Model):
    name = models.CharField(max_length=127)


class Musician(models.Model):
    name = models.CharField(max_length=127)
    groups = models.ManyToManyField(Group, related_name="members")


class SoftDeletableGroup(SoftDeletableModel):
    name = models.CharField(max_length=127)


class SoftDeletableMusician(SoftDeletableModel):
    name = models.CharField(max_length=127)
    groups = models.ManyToManyField(SoftDeletableGroup, related_name="members")
