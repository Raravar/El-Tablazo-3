from django.urls import path
from .views import home, contacto, about, dulce, salada, mixta, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('about', about, name="about"),
    path('dulce', dulce, name="dulce"),
    path('salada', salada, name="salada"),
    path('mixta', mixta, name="mixta"),
    path('registro', registro, name="registro"),
]