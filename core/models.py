from django.db import models

# Create your models here.
class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name="Id de Pais")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre del Pais")
    class Meta:
        verbose_name_plural = "Países"
    def __str__(self):
        return self.nombrePais

#Modelo para Proveedor

class Proveedor(models.Model):
    Identificacion = models.CharField(max_length=9, primary_key=True, verbose_name="Número de identificación")
    Nombre = models.CharField(max_length=50, verbose_name="Nombre completo")
    Telefono = models.CharField(max_length=9, null=True, blank=True, verbose_name="Teléfono")
    Direccion = models.CharField(max_length=9, null=True, blank=True, verbose_name="Dirección")
    Correo = models.CharField(max_length=9, null=True, blank=True, verbose_name="Correo")
    Contraseña = models.CharField(max_length=9, null=True, blank=True, verbose_name="Contraseña")
    Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.Identificacion