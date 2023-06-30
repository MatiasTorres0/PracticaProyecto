from django import forms
from .models import Usuario, Paciente, Medico


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'contraseña', 'nombrecompleto', 'usuariocol', 'Paciente_idPaciente', 'Paciente_comuna_idcomuna', 'Paciente_comuna_doctor_iddoctor', 'Medico_idmedico']

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['Paciente_idPaciente'].queryset = Paciente.objects.all()
        self.fields['Medico_idmedico'].queryset = Medico.objects.all()



class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['idPaciente','nombre', 'run', 'comuna']


class CustomUserCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = Usuario
        fields = ['name']  # Asegúrate de agregar 'name' a la lista de campos

class PersonaForm(forms.Form):
    CHOICES = [
        ('si', 'Si'),
        ('no', 'No'),
    ]

    viudez = forms.ChoiceField(label='Viudez menor de un año', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    vivir_solo = forms.ChoiceField(label='Vivir solo', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    cambio_casa = forms.ChoiceField(label='Cambio de casa en el último año', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    no_satisfecho_residencia = forms.ChoiceField(label='No estar satisfecho con su actual lugar de residencia', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    percepcion_salud = forms.ChoiceField(label='Mala percepción de su salud, comparado con otras personas de la misma edad', choices=[(1, 'Muy mala salud'), (2, 'Mala salud'), (3, 'Normal'), (4, 'Buena salud'), (5, 'Muy buena salud')], widget=forms.Select(attrs={'class': 'form-control'}))
    ingesta_farmacos = forms.ChoiceField(label='Ingesta diaria de 5 o más fármacos', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    limitacion_actividades = forms.ChoiceField(label='Limitación para realizar sus actividades por problemas de salud', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    problemas_salud = forms.CharField(label='Problema(s) de salud que le impida salir de la casa', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}))
    hospitalizacion = forms.ChoiceField(label='Haber estado hospitalizado en el último año', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    timestamp = forms.CharField(widget=forms.HiddenInput())


class MiFormulario(forms.Form):
    # Pregunta 1: Mayor de 80 años
    edad = forms.IntegerField(label='Edad', min_value=0, max_value=120)

    # Pregunta 2: Viudez menor de año
    viudez = forms.ChoiceField(label='Viudez menor de año', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 3: Vivir solo
    vivir_solo = forms.ChoiceField(label='Vivir solo', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 4: Cambio de casa en el último año
    cambio_casa = forms.ChoiceField(label='Cambio de casa en el último año', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 5: No estar satisfecho con su actual lugar de residencia
    no_satisfecho_residencia = forms.ChoiceField(label='No estar satisfecho con su actual lugar de residencia', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 6: Mala percepción de su salud, comparado con otras personas de la misma edad
    percepcion_salud = forms.ChoiceField(label='Mala percepción de su salud, comparado con otras personas de la misma edad', choices=[(1, 'Muy mala salud'), (2, 'Mala salud'), (3, 'Normal'), (4, 'Buena salud'), (5, 'Muy buena salud')])

    # Pregunta 7: Ingesta diaria de 5 o más fármacos
    ingesta_farmacos = forms.ChoiceField(label='Ingesta diaria de 5 o más fármacos', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 8: Limitación para realizar sus actividades por problemas de salud
    limitacion_actividades = forms.ChoiceField(label='Limitación para realizar sus actividades por problemas de salud', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 9: Problema(s) de salud que le impida salir de la casa
    problemas_salud = forms.CharField(label='Problema(s) de salud que le impida salir de la casa')

    # Pregunta 10: Haber estado hospitalizado en el último año
    hospitalizacion = forms.ChoiceField(label='Haber estado hospitalizado en el último año', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 11: Haberse caído frecuentemente en el último año
    caidas = forms.ChoiceField(label='Haberse caído frecuentemente en el último año', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 12: Tener problemas graves de memoria
    memoria = forms.ChoiceField(label='Tener problemas graves de memoria', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 13: Sentirse triste o deprimido casi siempre
    depresion = forms.ChoiceField(label='Sentirse triste o deprimido casi siempre', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 14: No ver bien (a pesar de usar lentes)
    vision = forms.ChoiceField(label='No ver bien (a pesar de usar lentes)', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 15: No escuchar bien (a pesar de usar audífono)
    audicion = forms.ChoiceField(label='No escuchar bien (a pesar de usar audífono)', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 16: Usar bastón, andador o silla de ruedas habitualmente
    movilidad = forms.ChoiceField(label='Usar bastón, andador o silla de ruedas habitualmente', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 17: Necesitar ayuda de otras personas para comer, levantarse, vestirse o ir al baño
    dependencia = forms.ChoiceField(label='Necesitar ayuda de otras personas para comer, levantarse, vestirse o ir al baño', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 18: No poder quedarse solo en su casa
    soledad = forms.ChoiceField(label='No poder quedarse solo en su casa', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 19: No contar con la ayuda de alguien cercano en caso de necesidad (si se enfermara, por ejemplo)
    apoyo = forms.ChoiceField(label='No contar con la ayuda de alguien cercano en caso de necesidad (si se enfermara, por ejemplo)', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 20: Haber sufrido la muerte o una enfermedad grave en un familiar cercano en el último año
    duelo = forms.ChoiceField(label='Haber sufrido la muerte o una enfermedad grave en un familiar cercano en el último año', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 21: No comer al menos una comida caliente al día
    comida_caliente = forms.ChoiceField(label='No comer al menos una comida caliente al día', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 22: Comer menos de tres comidas al día
    comida_frecuencia = forms.ChoiceField(label='Comer menos de tres comidas al día', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 23: Necesitar ayuda para contestar la encuesta
    ayuda_encuesta = forms.ChoiceField(label='Necesitar ayuda para contestar la encuesta', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 24: Baja de peso de más de tres kilos en 3 meses
    peso = forms.ChoiceField(label='Baja de peso de más de tres kilos en 3 meses', choices=[('si', 'Si'), ('no', 'No')])

    # Pregunta 25: Sin control médico más de 6 meses
    control_medico = forms.ChoiceField(label='Sin control médico más de 6 meses', choices=[('si', 'Si'), ('no', 'No')])