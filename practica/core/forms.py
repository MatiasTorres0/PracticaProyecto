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