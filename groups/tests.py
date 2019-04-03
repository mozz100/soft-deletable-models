from django.test import TestCase
from .models import Group, Musician, SoftDeletableGroup, SoftDeletableMusician
from django.db.models import Count


class MusicTestCode:
    def setUp(self):
        self.beatles = self.GroupClass.objects.create(name="The Beatles")
        for name in ("John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"):
            musician = self.MusicianClass.objects.create(name=name)
            self.beatles.members.add(musician)
        # Delete a musician
        self.beatles.members.get(name="John Lennon").delete()

    def test_deleted_musician(self):
        self.assertEqual(3, len(self.beatles.members.all()))
        self.assertEqual(3, self.beatles.members.all().count())
        self.assertEqual(3, self.beatles.members.count())

    def test_counts(self):
        bands = (
            self.GroupClass.objects.annotate(num_members=Count("members"))
            .filter(num_members__gte=3)
            .order_by("name")
        )
        self.assertEqual(1, bands.count())
        the_beatles = bands.get(name="The Beatles")
        self.assertEqual(3, the_beatles.members.all().count())
        self.assertEqual(3, the_beatles.num_members)


class NormalTestCase(MusicTestCode, TestCase):
    GroupClass = Group
    MusicianClass = Musician


class SoftDeletableTestCase(MusicTestCode, TestCase):
    GroupClass = SoftDeletableGroup
    MusicianClass = SoftDeletableMusician
