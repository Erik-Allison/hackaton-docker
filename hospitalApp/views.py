from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (CreateView, DetailView, TemplateView, ListView, DeleteView,
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
    

class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

# ------------------ Crud Especialidades -----------------------------------------------------


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer


class EspecialidadesCreateView(CreateView):
    model = Especialidades
    template_name = "especialidades/create-especialidades.html"
    form_class = EspecialidadesForm
    success_url = reverse_lazy('hospital_app:success')
    
    
class EspecialidadesDetailView(DetailView):
    model = Especialidades
    template_name = "especialidades/detail-especialidades.html"
    form_class = EspecialidadesForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class EspecialidadesListView(ListView):
    '''cunado sobreescribimos el metodo query set
    ya no necesitamos llamar al modelo'''
    #model = Especialidades
    context_object_name = 'list'
    paginate_by = 4
    template_name = "especialidades/list-especialidades.html"
    ordering = 'Nombre'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Especialidades.objects.filter(Nombre__icontains=palabra_clave)
        return lista
    

class EspecialidadesUpdateView(UpdateView):
    model = Especialidades
    template_name = "especialidades/especialidades_update.html"
    fields = '__all__'
    success_url = reverse_lazy('hospital_app:success')


class EspecialidadesDeleteView(DeleteView):
    model = Especialidades
    template_name = "especialidades/delete-especialidades.html"
    success_url = reverse_lazy('hospital_app:success')



# -------------------- Crud Medicos -----------------------------------------------


class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    

class MedicosCreateView(CreateView):
    model = Medicos
    template_name = "medicos/create-medicos.html"
    form_class = MedicosForm
    success_url = reverse_lazy('hospital_app:success')
    

class MedicosDetailView(DetailView):
    model = Medicos
    template_name = "medicos/detail-medicos.html"
    form_class = MedicosForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MedicosListView(ListView):
    model = Medicos
    paginate_by: 4
    context_object_name = 'list'
    template_name = "medicos/list-medicos.html"
    ordering = 'Nombres'


class MedicosUpdateView(UpdateView):
    model = Medicos
    template_name = "medicos/medicos_update.html"
    fields = '__all__'
    success_url = reverse_lazy('hospital_app:success')


class MedicosDeleteView(DeleteView):
    model = Medicos
    template_name = "medicos/delete-medicos.html"
    success_url = reverse_lazy('hospital_app:success')


# --------------------------------------------------------------------------------------
class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class PacientesCreateView(CreateView):
    model = Pacientes
    template_name = "pacientes/create-paciente.html"
    form_class = PacientesForm
        
    def upload_file(request):
        if request.method == 'POST':
            form = PacientesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/hospital_app:success/')
        else:
            form = PacientesForm()
            return render(request, 'create-paciente.html', {'form':form})


# --------------------------------------------------------------------------------------
class HorariosViewSet(viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer
