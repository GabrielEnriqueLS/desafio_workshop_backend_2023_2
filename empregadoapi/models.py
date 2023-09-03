from django.db import models

# Create your models here.

class Empregado(models.Model):
    NomeCompleto = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    telefone = models.CharField(max_length=25)
