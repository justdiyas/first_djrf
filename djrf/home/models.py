from django.db import models


class Sport(models.Model):
    sport_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sport_name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    city_born = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, null=True, blank=True, related_name='favorite_sport', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mountain(models.Model):
    peak = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    height = models.IntegerField()

    def __str__(self):
        return self.peak


class Company(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    founded = models.IntegerField()
    employee = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
