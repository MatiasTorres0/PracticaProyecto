from django.urls import path
from .views import home, formulario

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario" ),
]