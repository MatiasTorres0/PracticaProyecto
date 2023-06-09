from django.urls import path
from .views import home, buscar, formulario, prueba, registrar_paciente, procesar_formulario


urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario" ),
    path('prueba/', prueba, name="prueba"),

    path('registrar_paciente/', registrar_paciente, name='registrar_paciente'),
    path('buscar/', buscar),
    path('procesar_formulario/', procesar_formulario, name='procesar_formulario')
]