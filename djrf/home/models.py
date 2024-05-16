from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    city_born = models.CharField(max_length=200)

    def __str__(self):
        return self.name
