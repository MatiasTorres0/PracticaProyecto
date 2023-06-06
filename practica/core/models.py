from django.db import models

class Medico(models.Model):
  idmedico = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  run = models.CharField(max_length=45)
  especialidad = models.CharField(max_length=45)

class Region(models.Model):
  idregion = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)

class Provincia(models.Model):
  idprovincia = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Comuna(models.Model):
  idcomuna = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

class Paciente(models.Model):
  idPaciente = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  run = models.CharField(max_length=45)
  comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class FamiliarPaciente(models.Model):
  idFamiliarPaciente = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  run = models.CharField(max_length=45)
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Especialidad(models.Model):
  idespecialidad = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)

class Medico_has_Especialidad(models.Model):
  medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
  especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class Institucion(models.Model):
  idInstitucion = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=45)
  descripcion = models.CharField(max_length=45)
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class PreguntasInstrumento(models.Model):
  id = models.IntegerField(primary_key=True)
  idtipoinstrumento = models.IntegerField()
  descripcion = models.CharField(max_length=500)
  TipoRespuesta_idTipoRespuesta = models.IntegerField()
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


class Paciente_has_Preguntas(models.Model):
  Paciente_idPaciente = models.IntegerField(primary_key=True)
  Paciente_comuna_idcomuna = models.IntegerField()
  Paciente_comuna_doctor_iddoctor = models.IntegerField()
  Preguntas_idPreguntas = models.IntegerField()
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class respuestas_has_medico(models.Model):
  informe_idinforme = models.IntegerField(primary_key=True)
  Medico_idmedico = models.IntegerField()
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Medico_has_Paciente(models.Model):
  Medico_idmedico = models.IntegerField(primary_key=True)
  Paciente_idPaciente = models.IntegerField()
  Paciente_comuna_idcomuna = models.IntegerField()
  Paciente_comuna_doctor_iddoctor = models.IntegerField()
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)
    nombrecompleto = models.CharField(max_length=45)
    usuariocol = models.CharField(max_length=45)
    Paciente_idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Paciente_comuna_idcomuna = models.IntegerField()
    Paciente_comuna_doctor_iddoctor = models.IntegerField()
    Medico_idmedico = models.ForeignKey(Medico, on_delete=models.CASCADE)

class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True)
    tipousuario = models.CharField(max_length=45)
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class TipoInstrumento(models.Model):
    idTipoInstrumento = models.IntegerField(primary_key=True)
    Tipo = models.CharField(max_length=60)
    Descripcion = models.CharField(max_length=300)
    PreguntasInstrumento_id = models.IntegerField()
    PreguntasInstrumento_TipoRespuesta_idTipoRespuesta = models.IntegerField()

class Paciente_ProfesionalSalud(models.Model):
    id = models.IntegerField(primary_key=True)
    idusuariopaciente = models.CharField(max_length=45)
    idusuarioprofsinalsalud = models.CharField(max_length=45)

class Paciente_has_Paciente_ProfesionalSalud(models.Model):
    Paciente_idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Paciente_comuna_idcomuna = models.IntegerField()
    Paciente_comuna_doctor_iddoctor = models.IntegerField()
    Paciente_ProfesionalSalud_id = models.ForeignKey(Paciente_ProfesionalSalud, on_delete=models.CASCADE)

class Medico_has_Paciente_ProfesionalSalud(models.Model):
    Medico_idmedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Paciente_ProfesionalSalud_id = models.ForeignKey(Paciente_ProfesionalSalud, on_delete=models.CASCADE)

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

class InstitucionHasMedicoHasEspecialidad(models.Model):
    Institucion_idInstitucion = models.IntegerField()
    Medico_has_especialidad_Medico_idmedico = models.IntegerField()
    doctor_has_especialidad_especialidad_idespecialidad = models.IntegerField()
    primary_key = models.CharField(max_length=100)

    class Meta:
        unique_together = (("Institucion_idInstitucion", "Medico_has_especialidad_Medico_idmedico", "doctor_has_especialidad_especialidad_idespecialidad"),)

