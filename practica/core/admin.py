from django.contrib import admin
from .models import Medico, Region, Provincia, Comuna, Paciente, FamiliarPaciente, Especialidad, PacienteHasFamiliarPaciente, MedicoHasEspecialidad, Institucion, InstitucionHasMedicoHasEspecialidad

class MedicoAdmin(admin.ModelAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass

class ProvinciaAdmin(admin.ModelAdmin):
    pass

class ComunaAdmin(admin.ModelAdmin):
    pass

class PacienteAdmin(admin.ModelAdmin):
    pass

class FamiliarPacienteAdmin(admin.ModelAdmin):
    pass

class EspecialidadAdmin(admin.ModelAdmin):
    pass

class PacienteHasFamiliarPacienteAdmin(admin.ModelAdmin):
    pass

class MedicoHasEspecialidadAdmin(admin.ModelAdmin):
    pass

class InstitucionAdmin(admin.ModelAdmin):
    pass

class InstitucionHasMedicoHasEspecialidadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(FamiliarPaciente, FamiliarPacienteAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(PacienteHasFamiliarPaciente, PacienteHasFamiliarPacienteAdmin)
admin.site.register(MedicoHasEspecialidad, MedicoHasEspecialidadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(InstitucionHasMedicoHasEspecialidad, InstitucionHasMedicoHasEspecialidadAdmin)
