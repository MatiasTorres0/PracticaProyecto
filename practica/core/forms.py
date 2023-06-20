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
