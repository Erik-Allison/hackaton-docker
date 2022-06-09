from .models import (
    Especialidades, Medicos, Pacientes, Horarios, Citas)

from rest_framework import serializers


class EspecialidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidades
        fields = ['Nombre', 'Descripcion', 'FechaRegistro', 'FechaModificacion', 'UsuarioRegistro',
                  'UsuarioModificacion', 'Activo']


class MedicosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicos
        fields = ['Nombres', 'Apellidos', 'Dni', 'EspecialidadId', 'Direccion',
                  'correo', 'telefono', 'sexo', 'NumColegiatura', 'FechaNacimiento', 'FechaRegistro',
                  'FechaModificacion', 'UsuarioRegistro', 'Activo']


class PacientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pacientes
        fields = ['Nombres', 'Apellidos', 'Dni', 'Direccion',
                  'Telefono', 'sexo', 'FechaNacimiento', 'FechaResgistro', 'FechaModificacion',
                  'UsuarioRegistro', 'UsuarioModificacion', 'Activo']


class HorariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horarios
        fields = ['MedicoId', 'FechaAtencion', 'InicioAtencio', 'FinAtencion',
                  'Activo', 'FechaRegistro', 'UsuarioRegistro', 'FechaModificacion',
                  'UsuarioModificacion']


class CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = ['MedicoId', 'PacienteId', 'FechaAtencion', 'InicioAtencion',
                  'FinAtencion', 'Estado', 'Observaciones', 'Activo', 'FechaRegistro',
                  'UsuarioRegistro', 'FechaModificacion', 'UsuarioModificacion']
