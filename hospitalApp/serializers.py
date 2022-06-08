from .models import (
    Especialidades, Medicos, Pacientes, Horarios, Citas)

from rest_framework import serializers


class EspecialidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidades
        fields = ['Nombre', 'Descripcion', 'FechaRegistro', 'FechaModificacion', 'UsuarioRegistro',
                  'UsuarioModificacion', 'Activo']
