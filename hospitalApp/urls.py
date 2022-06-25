from django.urls import path
from .views import InicioTemplateView

from .views import MedicosDeleteView, MedicosListView, MedicosUpdateView, Success

from .views import (EspecialidadesCreateView, EspecialidadesDetailView,
                    EspecialidadesListView, EspecialidadesUpdateView, EspecialidadesDeleteView)

from .views import (MedicosCreateView)

app_name = 'hospital_app'

urlpatterns = [
    # ------------- urls paginainicio ------------------------------------
    path('inicio/', InicioTemplateView.as_view(),
         name='inicio'),
    # --------- urls Especialidades ---------------------------------------
    path('create-especialidades/', EspecialidadesCreateView.as_view(),
         name='creatEspecialidad'),
    path('EspecialidadesDetailView/<pk>', EspecialidadesDetailView.as_view(),
         name='detailsEspecialidad'),
    path('success/', Success.as_view(), name='success'),
    path('list-especialidades/', EspecialidadesListView.as_view(),
         name='listEspecialidad'),
    path('update-especialidades/<pk>', EspecialidadesUpdateView.as_view(),
         name='updateEspecialidad'),
    path('delete-especialidades/<pk>', EspecialidadesDeleteView.as_view(),
         name='deleteEspecialidad'),

    # --------------- urls medicos --------------------------------------------
    path('create-medicos/', MedicosCreateView.as_view(),
         name='createMedicos'),
    path('list-medicos/', MedicosListView.as_view(),
         name='listMedicos'),
    path('update-medicos/<pk>', MedicosUpdateView.as_view(),
         name='updateMedicos'),
    path('delete-medicos/<pk>', MedicosDeleteView.as_view(),
         name='deleteMedicos'),
]
