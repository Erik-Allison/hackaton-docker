from django.urls import include, path

from hospitalApp.views import (CitasViewSet, EspecialidadesViewSet, HorariosViewSet, MedicosViewSet,
                               PacientesViewSet)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Especialidades', EspecialidadesViewSet)
router.register(r'Medicos', MedicosViewSet)
router.register(r'Pacientes', PacientesViewSet)
router.register(r'Horarios', HorariosViewSet)
router.register(r'Citas', CitasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('especialidades/', include('rest_framework.urls', namespace='rest_framework')),
    path('medicos/', include('rest_framework.urls', namespace='rest_framework')),
    path('pacientes/', include('rest_framework.urls', namespace='rest_framework')),
    path('horarios/', include('rest_framework.urls', namespace='rest_framework')),
    path('citas/', include('rest_framework.urls', namespace='rest_framework')),
]
