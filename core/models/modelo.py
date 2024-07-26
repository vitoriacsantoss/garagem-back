from django.db import models 
from core.models import Marca, Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="modelos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="modelos")

    def __str__(self):
        return f"{self.nome} - {self.marca}"