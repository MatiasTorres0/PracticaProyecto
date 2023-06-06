from django.contrib import admin
from .models import (
    Medico, Region, Provincia, Comuna, Paciente, FamiliarPaciente,
    Especialidad, Medico_has_Especialidad, Institucion, PreguntasInstrumento,
    Paciente_has_Preguntas, respuestas_has_medico, Medico_has_Paciente,
    Usuario, TipoUsuario, TipoInstrumento, Paciente_ProfesionalSalud,
    Paciente_has_Paciente_ProfesionalSalud, Medico_has_Paciente_ProfesionalSalud,
    PacienteHasFamiliarPaciente, MedicoHasEspecialidad,
    InstitucionHasMedicoHasEspecialidad,
)

admin.site.register(Medico)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Paciente)
admin.site.register(FamiliarPaciente)
admin.site.register(Especialidad)
admin.site.register(Medico_has_Especialidad)
admin.site.register(Institucion)
admin.site.register(PreguntasInstrumento)
admin.site.register(Paciente_has_Preguntas)
admin.site.register(respuestas_has_medico)
admin.site.register(Medico_has_Paciente)
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(TipoInstrumento)
admin.site.register(Paciente_ProfesionalSalud)
admin.site.register(Paciente_has_Paciente_ProfesionalSalud)
admin.site.register(Medico_has_Paciente_ProfesionalSalud)
admin.site.register(PacienteHasFamiliarPaciente)
admin.site.register(MedicoHasEspecialidad)
admin.site.register(InstitucionHasMedicoHasEspecialidad)
