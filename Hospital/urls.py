from django.urls import include, path
from hospitalApp.views import EspecialidadesViewSet
from rest_framework import routers
from hospitalApp import views

router = routers.DefaultRouter()
router.register(r'Especialidades', EspecialidadesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('especialidades/', include('rest_framework.urls', namespace='rest_framework'))
]
