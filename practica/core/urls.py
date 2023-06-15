from django.urls import path
from .views import home, formulario, prueba

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario" ),
    path('prueba/', prueba, name="prueba"),
]