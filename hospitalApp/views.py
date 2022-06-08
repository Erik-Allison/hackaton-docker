#from django.shortcuts import render

# Create your views here.
from hospitalApp.serializers import EspecialidadesSerializer
from rest_framework import viewsets
from .models import (Especialidades, Medicos, Pacientes, Horarios, Citas)


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
