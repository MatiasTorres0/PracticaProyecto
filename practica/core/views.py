from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, MiFormulario, UsuarioForm, PacienteForm
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

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MiFormulario
from .models import PreguntasInstrumento, Paciente
from django.contrib import messages


def formulario(request):
    formulario = MiFormulario(request.POST)
    pregunta = None

    if formulario.is_valid():
        # Obtener el paciente asociado al usuario actual
        paciente = get_object_or_404(Paciente, idPaciente=request.user.id)
        
        pregunta = PreguntasInstrumento()
        pregunta.idtipoinstrumento = 1
        pregunta.TipoRespuesta_idTipoRespuesta = 1
        pregunta.paciente = paciente
        descripcion = request.POST.get('descripcion')
        if descripcion: # verificar que el campo descripcion tenga un valor
            pregunta.descripcion = descripcion
            pregunta.save()
            # agregar esta línea para mostrar un mensaje de éxito
            messages.success(request, 'La pregunta se guardó correctamente', extra_tags='persistent')

            return redirect('home')
        else:
            # mostrar un mensaje de error o hacer otra cosa
            messages.error(request, 'El campo descripcion es obligatorio')
            return render(request, 'core/formulario.html', {'form': formulario})
    else:
        pacientes = Paciente.objects.all()
        data = {
            'form': formulario,
            'pacientes': pacientes,
            'pregunta': pregunta
        }
        return render(request, 'core/formulario.html', data)


from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404
from .models import Paciente

def prueba(request):
    formulario = MiFormulario(request.POST)
    pregunta = None

    if formulario.is_valid():
        # Obtener el paciente asociado al usuario actual
        paciente = get_object_or_404(Paciente, idPaciente=request.user.id)
        
        pregunta = PreguntasInstrumento(
            idtipoinstrumento=1,
            TipoRespuesta_idTipoRespuesta=1,
            paciente=paciente,
            descripcion=formulario.cleaned_data['descripcion']
        )
        pregunta.save()
        return redirect('home')
    else:
        pacientes = Paciente.objects.all()
        data = {
            'form': formulario,
            'pacientes': pacientes,
            'pregunta': pregunta
        }
        return render(request, 'core/prueba.html', data)


    
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