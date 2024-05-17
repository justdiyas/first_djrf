from django.db import models


class Sport(models.Model):
    sport_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    city_born = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, null=True, blank=True, related_name='favorite_sport', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
