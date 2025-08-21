from django.db import models

# Create your models here.

class Personita(models.Model):
    name = models.CharField(max_length=200)

class Pene(models.Model):
    largo = models.IntegerField()
    team = models.CharField(max_length=8) #sangre o carne
    color = models.CharField(max_length=10) #de piel
    propietario = models.ForeignKey(
        Personita,
        on_delete=models.CASCADE,
        related_name="penes")

