from django.urls import path

from .views import Success
from .views import (EspecialidadesCreateView,
                    EspecialidadesListView, EspecialidadesUpdateView, EspecialidadesDeleteView)

app_name = 'hospital_app'

urlpatterns = [
    # --------- urls Especialidades ---------------------------------------
    path('create-especialidades/', EspecialidadesCreateView.as_view(),
         name='creatEspecialidad'),
    path('success/', Success.as_view(), name='success'),
    path('list-especialidades/', EspecialidadesListView.as_view(),
         name='listEspecialidad'),
    path('update-especialidades/<pk>', EspecialidadesUpdateView.as_view(),
         name='updateEspecialidad'),
    path('delete-especialidades/<pk>', EspecialidadesDeleteView.as_view(),
         name='deleteEspecialidad')
]