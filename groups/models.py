from django.db import models
from model_utils.models import SoftDeletableModel


class NameMixin:
    def __str__(self):
        return self.name

class Group(NameMixin, models.Model):
    name = models.CharField(max_length=127)


class Musician(NameMixin, models.Model):
    name = models.CharField(max_length=127)
    groups = models.ManyToManyField(Group, related_name="members")


class SoftDeletableGroup(NameMixin, SoftDeletableModel):
    name = models.CharField(max_length=127)


class SoftDeletableMusician(NameMixin, SoftDeletableModel):
    name = models.CharField(max_length=127)
    groups = models.ManyToManyField(SoftDeletableGroup, related_name="members")
