from django.db import models
from django.utils import timezone


class TCourses(models.Model):
    Docente = models.CharField(max_length=200)
    Hora = models.CharField(max_length=200)
    Fecha = models.CharField(max_length=200)
    Aula = models.CharField(max_length=200)
    Ingenieria = models.CharField(max_length=200)

    