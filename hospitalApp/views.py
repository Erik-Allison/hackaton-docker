from hospitalApp.serializers import (CitasSerializer, EspecialidadesSerializer,
                                     HorariosSerializer, MedicosSerializer, PacientesSerializer)
from rest_framework import viewsets
from .models import (Especialidades, Medicos, Pacientes, Horarios, Citas)


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer


class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class HorariosViewSet(viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer
