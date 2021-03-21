from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=145)
    telefone = models.CharField(max_length=145)
    email = models.CharField(max_length=145)