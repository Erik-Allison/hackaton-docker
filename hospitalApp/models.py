from django.db import models

# Create your models here.


class Especialidades(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    FechaRegistro = models.DateField(auto_now_add=True)
    FechaModificacion = models.DateField(auto_now_add=True)
    UsuarioRegistro = models.CharField(max_length=30)
    UsuarioModificacion = models.CharField(max_length=30)
    Activo = models.BooleanField(default=True)


class Medicos(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Dni = models.CharField(max_length=30)
    EspecialidadId = models.ForeignKey(
        Especialidades, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=150)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    NumColegiatura = models.CharField(max_length=30)
    FechaNacimiento = models.DateField(auto_now_add=False)
    FechaRegistro = models.DateField(auto_now_add=True)
    FechaModificacion = models.DateField(auto_now_add=True)
    UsuarioRegistro = models.CharField(max_length=30)
    Activo = models.BooleanField(default=True)


class Pacientes(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Dni = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    FechaNacimiento = models.DateField(auto_now_add=False)
    FechaResgistro = models.DateField(auto_now_add=True)
    FechaModificacion = models.DateField(auto_now_add=True)
    UsuarioRegistro = models.CharField(max_length=50)
    UsuarioModificacion = models.CharField(max_length=50)
    Activo = models.BooleanField(default=True)


class Horarios(models.Model):
    MedicoId = models.ManyToManyField(Medicos)
    FechaAtencion = models.DateField(auto_now_add=False)
    InicioAtencio = models.DateTimeField(auto_now_add=False)
    FinAtencion = models.DateTimeField(auto_now_add=False)
    Activo = models.BooleanField(default=True)
    FechaRegistro = models.DateField(auto_now_add=True)
    UsuarioRegistro = models.CharField(max_length=50)
    FechaModificacion = models.DateField(auto_now_add=True)
    UsuarioModificacion = models.CharField(max_length=50)


class Citas(models.Model):
    MedicoId = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    PacienteId = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    FechaAtencion = models.DateField(auto_now_add=False)
    InicioAtencion = models.DateTimeField(auto_now_add=False)
    FinAtencion = models.DateTimeField(auto_now_add=False)
    Estado = models.BooleanField(default=True)
    Observaciones = models.TextField()
    Activo = models.BooleanField(default=True)
    FechaRegistro = models.CharField(max_length=50)
    UsuarioRegistro = models.CharField(max_length=50)
    FechaModificacion = models.DateField(auto_now_add=True)
    UsuarioModificacion = models.CharField(max_length=50)
