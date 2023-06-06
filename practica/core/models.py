from django.db import models

# Create your models here.
class Medico(models.Model):
    idmedico = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)
    run = models.CharField(max_length=45, null=True)
    # Atributo faltante en el código MySQL
    # nombre_atributo = models.CharField(max_length=45, null=True)


class Region(models.Model):
    idregion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)


class Provincia(models.Model):
    idprovincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    region_idregion = models.ForeignKey(Region, on_delete=models.CASCADE)


class Comuna(models.Model):
    idcomuna = models.IntegerField(primary_key=True)
    nombrecomuna = models.CharField(max_length=45)
    medico_idmedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    provincia_idprovincia = models.IntegerField()
    provincia_region_idregion = models.IntegerField()


class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    run = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    comuna_idcomuna = models.IntegerField()
    comuna_doctor_iddoctor = models.IntegerField()
    fechanac = models.DateField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)


class FamiliarPaciente(models.Model):
    idFamiliarPaciente = models.IntegerField(primary_key=True)
    NombreFamiliar = models.CharField(max_length=45, null=True)
    runfamiliar = models.CharField(max_length=45, null=True)
    FamiliarPacientecol = models.CharField(max_length=45, null=True)


class Especialidad(models.Model):
    idespecialidad = models.IntegerField(primary_key=True)
    nombreespecialidad = models.CharField(max_length=45)


class PacienteHasFamiliarPaciente(models.Model):
    Paciente_idPaciente = models.IntegerField()
    Paciente_comuna_idcomuna = models.IntegerField()
    Paciente_comuna_doctor_iddoctor = models.IntegerField()
    FamiliarPaciente_idFamiliarPaciente = models.IntegerField()
    primary_key = models.CharField(max_length=100)

    class Meta:
        unique_together = (("Paciente_idPaciente", "Paciente_comuna_idcomuna", "Paciente_comuna_doctor_iddoctor", "FamiliarPaciente_idFamiliarPaciente"),)


class MedicoHasEspecialidad(models.Model):
    medico_idmedico = models.IntegerField()
    especialidad_idespecialidad = models.IntegerField()
    primary_key = models.CharField(max_length=100)

    class Meta:
        unique_together = (("medico_idmedico", "especialidad_idespecialidad"),)


class Institucion(models.Model):
    idInstitucion = models.IntegerField(primary_key=True)
    nombre_institucion = models.CharField(max_length=45)
    descripcion_institucion = models.CharField(max_length=45)


class InstitucionHasMedicoHasEspecialidad(models.Model):
    Institucion_idInstitucion = models.IntegerField()
    Medico_has_especialidad_Medico_idmedico = models.IntegerField()
    doctor_has_especialidad_especialidad_idespecialidad = models.IntegerField()
    primary_key = models.CharField(max_length=100)

    class Meta:
        unique_together = (("Institucion_idInstitucion", "Medico_has_especialidad_Medico_idmedico", "doctor_has_especialidad_especialidad_idespecialidad"),)

