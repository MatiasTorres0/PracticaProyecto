from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UsuarioForm, PacienteForm
from .models import Paciente
from django.contrib.auth.models import User
from core.models import PreguntasInstrumento

def home(request):
    return render(request, 'core/home.html')

def buscar(request):
    mensaje = "Nombre paciente: %r" % request.GET["prd"]
    return HttpResponse(mensaje)

def formulario(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            # Guardar los datos en la base de datos
            formulario.save()

            return redirect('home')  # Redirige a la página de inicio después de procesar el formulario
    else:
        formulario = CustomUserCreationForm()

    data = {
        'form': formulario
    }
    return render(request, 'core/formulario.html', data)

def prueba(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            # Guardar los datos en la base de datos
            formulario.save()
            return redirect('home')  # Redirige a la página de inicio después de guardar el formulario
    else:
        formulario = CustomUserCreationForm()

    data = {
        'form': formulario
    }
    return render(request, 'core/prueba.html', data)

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = UsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'formulario': formulario})

def registrar_paciente(request):
    if request.method == 'POST':
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = PacienteForm()
    return render(request, 'registrar_paciente.html', {'formulario': formulario})
