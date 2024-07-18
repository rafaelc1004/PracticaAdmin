from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=6, unique=True, null=False)
    nombre = models.CharField(max_length=30, null=False, unique=True)
    precio = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=False)
    
    def __str__(self):
        return self.codigo + ' ' + self.nombre

