from time import time

from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Utilizator(User):
    gender_list = (
        ('M', 'Barbat'),
        ('F', 'Femeie')
    )
    data_nasterii = models.DateTimeField(null=True, )
    gender = models.CharField(choices=gender_list, max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Film(models.Model):
    titlu = models.CharField(max_length=150, )
    descriere = models.TextField(default=' ')
    data_lansare = models.DateField(null=True)
    imagine = models.CharField(max_length=255,default='')
    link_Youtube = models.URLField()
    link_IMDB = models.URLField()
    rating = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Filme'

    def __str__(self):
        return self.titlu


class Actor(models.Model):
    gender = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    sex = models.CharField(max_length=7, choices=gender)

    class Meta:
        verbose_name_plural = 'Actori'

    def __str__(self):
        return self.nume + ' ' + self.prenume


class Regizor(models.Model):
    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Regizori'

    def __str__(self):
        return self.nume + ' ' + self.prenume


class Gen(models.Model):
    denumire = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Genuri'

    def __str__(self):
        return self.denumire


class GenuriFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=CASCADE)
    gen = models.ForeignKey(Gen, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Gen Film'


class Distributie(models.Model):
    film = models.ForeignKey(Film, on_delete=CASCADE)
    actors = models.ManyToManyField(Actor)
    rol = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Distributie'


class Regie(models.Model):
    film = models.ForeignKey(Film, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Regie'
