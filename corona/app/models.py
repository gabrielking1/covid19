"""
Definition of models.
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class World(models.Model):
    country = models.CharField(max_length=50)
    RecoveryProporation = models.CharField(max_length = 50)
    TotalCases = models.CharField(max_length = 50)
    NewCases =  models.CharField(max_length = 50)
    TotalDeath =  models.CharField(max_length = 50)
    NewDeath =  models.CharField(max_length = 50)
    TotalRecovered =   models.CharField(max_length = 50)
    NewRecovered =  models.CharField(max_length = 50)
    ActiveCases =   models.CharField(max_length = 50)
    SeriousCritical = models.CharField(max_length = 50)
    

    class Meta:
        verbose_name = ("World")
        verbose_name_plural = ("Worlds")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("World_detail", kwargs={"pk": self.pk})


class Worlds(models.Model):
    world_id = models.CharField(max_length = 100)
    country = models.CharField(max_length=50)
    RecoveryProporation = models.CharField(max_length = 50)
    TotalCases = models.CharField(max_length = 50)
    NewCases =  models.CharField(max_length = 50)
    TotalDeath =  models.CharField(max_length = 50)
    NewDeath =  models.CharField(max_length = 50)
    TotalRecovered =   models.CharField(max_length = 50)
    NewRecovered =  models.CharField(max_length = 50)
    ActiveCases =   models.CharField(max_length = 50)
    SeriousCritical = models.CharField(max_length = 50)
    

    class Meta:
        verbose_name = ("Worlds")
        verbose_name_plural = ("Worldss")

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse("Worlds_detail", kwargs={"pk": self.pk})

class Country(models.Model):
    country_id = models.CharField(max_length = 100)
    country = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    rank = models.CharField(max_length = 50)
    RecoveryProporation = models.CharField(max_length = 50)
    TotalCases = models.CharField(max_length = 50)
    NewCases =  models.CharField(max_length = 50)
    TotalDeath =  models.CharField(max_length = 50)
    NewDeath =  models.CharField(max_length = 50)
    TotalRecovered =   models.CharField(max_length = 50)
    TotalTests =   models.CharField(max_length = 50)
    Population =   models.CharField(max_length = 50)
    NewRecovered =  models.CharField(max_length = 50)
    ActiveCases =   models.CharField(max_length = 50)
    SeriousCritical = models.CharField(max_length = 50)
    Fatality = models.CharField(max_length = 50)

    

    class Meta:
        verbose_name = ("Country")
        verbose_name_plural = ("Countrys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})
