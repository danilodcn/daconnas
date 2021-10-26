from django.db import models

# Create your models here.

class Diarista(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank= False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=11, blank=False, null=False)
    logradouro = models.CharField(max_length=60, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    bairro = models.CharField(max_length=30, blank=False, null=False)
    complemento = models.CharField(max_length=100, blank=True, null=False)
    cep = models.CharField(max_length=8, blank=False, null=False)
    estado = models.CharField(max_length=2, blank=False, null=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    codigo_ibge = models.IntegerField(blank=False, null=False)
    foto_usuario = models.ImageField(null=False)

