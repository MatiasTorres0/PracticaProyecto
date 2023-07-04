from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UsuarioForm, PacienteForm
from .models import PreguntasInstrumento, Paciente
from django.contrib.auth.models import User
from core.models import PreguntasInstrumento
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .forms import MiFormulario
def home(request):
    return render(request, 'core/home.html')

def buscar(request):
    mensaje = "Nombre paciente: %r" % request.GET["prd"]
    return HttpResponse(mensaje)

def formulario(request):
    formulario = CustomUserCreationForm(request.POST)
    if formulario.is_valid():
        # Crear una instancia de PreguntasInstrumento con los datos que quieras guardar
        pregunta = PreguntasInstrumento(
            idtipoinstrumento = 1, # Aquí puedes poner el valor que corresponda
            TipoRespuesta_idTipoRespuesta = 1, # Aquí puedes poner el valor que corresponda
            paciente = request.user # Aquí puedes poner el usuario que corresponda
        )
        # Asignar el valor del campo descripcion al atributo descripcion de la instancia de PreguntasInstrumento
        pregunta.descripcion = formulario.cleaned_data['descripcion']
        # Guardar la instancia de PreguntasInstrumento en la base de datos
        pregunta.save()
                    # Obtener todos los pacientes
        pacientes = Paciente.objects.all()
        nombre = "John Doe"
        personas_encontradas = Paciente.objects.filter(nombre=nombre)
            # Mostrar la lista de personas encontradas
        data = {
                'form': formulario,
                'personas': personas_encontradas,
                'pacientes': pacientes
            }
        return redirect('home')
    
    
    else:
        # Obtener todos los pacientes
        pacientes = Paciente.objects.all()
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


def procesar_formulario(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            # Obtener el paciente actual
            paciente = Paciente.objects.get(id=1)  # Supongamos que el paciente tiene el ID 1, debes ajustar esto según tu lógica de obtención del paciente

            # Guardar los datos en la base de datos
            pregunta_instrumento = PreguntasInstrumento(
                idtipoinstrumento=form.cleaned_data['idtipoinstrumento'],
                descripcion=form.cleaned_data['descripcion'],
                TipoRespuesta_idTipoRespuesta=form.cleaned_data['TipoRespuesta_idTipoRespuesta'],
                paciente=paciente
            )
            pregunta_instrumento.save()

            return render(request, 'resultado.html')
    else:
        form = MiFormulario()

    return render(request, 'formulario.html', {'form': form})