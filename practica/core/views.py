from django.shortcuts import render, redirect
from .forms import UsuarioForm, PacienteForm

def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def prueba(request):
    return render(request, 'core/prueba.html')

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
