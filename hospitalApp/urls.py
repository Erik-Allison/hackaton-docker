from django.urls import path

from .views import (EspecialidadesCreateView, Success)

app_name = 'hospital_app'

urlpatterns = [
    # --------- urls Especialidades ---------------------------------------
    path('create-especialidades/', EspecialidadesCreateView.as_view(), name='creatEspecialidad'),
    path('success/', Success.as_view(), name='success'),
]
