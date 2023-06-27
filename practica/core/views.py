from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UsuarioForm, PacienteForm
from .models import Paciente
from django.contrib.auth.models import User
from core.models import PreguntasInstrumento

def home(request):
    return render(request, 'core/home.html')

def view(request):
    user = request.user
    return render(request, 'index.html', {'user': user})

#def formulario(request):
    nombre_buscado = "John Doe"
    personas_encontradas = Paciente.objects.filter(nombre=nombre_buscado)
    return render(request, 'core/formulario.html')

def formulario(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            # Guardar los datos en la base de datos
            pregunta = PreguntasInstrumento(
                idtipoinstrumento=formulario.cleaned_data['idtipoinstrumento'],
                descripcion=formulario.cleaned_data['descripcion'],
                TipoRespuesta_idTipoRespuesta=formulario.cleaned_data['TipoRespuesta_idTipoRespuesta'],
                paciente=formulario.cleaned_data['paciente']
            )
            pregunta.save()

            # Buscar el nombre en la base de datos
            nombre = formulario.cleaned_data['nombre']
            personas_encontradas = Paciente.objects.filter(nombre=nombre)

            # Obtener todos los pacientes
            pacientes = Paciente.objects.all()

            # Mostrar la lista de personas encontradas
            data = {
                'form': formulario,
                'personas': personas_encontradas,
                'pacientes': pacientes
            }
            return render(request, 'core/formulario.html', data)

    else:
        # Create a new CustomUserCreationForm object
        formulario = CustomUserCreationForm()

        # Buscar el nombre en la base de datos
        nombre_buscado = "John Doe"
        personas_encontradas = Paciente.objects.filter(nombre=nombre_buscado)

        # Obtener todos los pacientes
        pacientes = Paciente.objects.all()

        # Return the template with the form, the list of people found, and the list of patients
        data = {
            'form': formulario,
            'personas': personas_encontradas,
            'pacientes': pacientes
        }
        return render(request, 'core/formulario.html', data)



def buscar(request):
	mensaje="Nombre paciente: %r" %request.GET["prd"]
	return HttpResponse(mensaje)

def prueba(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            # Guardar los datos en la base de datos
            formulario.save()
            return redirect('core/home.html')  # Reemplaza 'nombre_de_la_vista' por el nombre de la vista a la que deseas redirigir después de guardar el formulario
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
