from core.models import Pais, Proveedor
from django.contrib import admin
from .models import Pais, Proveedor

# Register your models here.
admin.site.register(Pais)
admin.site.register(Proveedor)