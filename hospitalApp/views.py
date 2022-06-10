from django.urls import reverse_lazy

from django.views.generic import (CreateView, TemplateView, ListView, DeleteView,
                                  UpdateView)

from .models import (Especialidades, Medicos, Pacientes, Horarios, Citas)

from hospitalApp.forms import (
    EspecialidadesForm, MedicosForm, PacientesForm, HorariosForm, CitasForm)

from hospitalApp.serializers import (CitasSerializer, EspecialidadesSerializer,
                                     HorariosSerializer, MedicosSerializer, PacientesSerializer)

from rest_framework import viewsets


# mensaje de proc satisfactorio para todos los procesos
class Success(TemplateView):
    template_name = "success.html"

# ------------------ Crud Especialidades -----------------------------------------------------


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer


class EspecialidadesCreateView(CreateView):
    model = Especialidades
    template_name = "especialidades/create-especialidades.html"
    form_class = EspecialidadesForm
    success_url = reverse_lazy('hospital_app:success')

# -------------------- Crud Medicos -----------------------------------------------


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
