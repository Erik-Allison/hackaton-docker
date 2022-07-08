from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework import routers

from hospitalApp import views


router = routers.DefaultRouter()
router.register(r'Especialidades', views.EspecialidadesViewSet)
router.register(r'Medicos', views.MedicosViewSet)
router.register(r'Pacientes', views.PacientesViewSet)
router.register(r'Horarios', views.HorariosViewSet)
router.register(r'Citas', views.CitasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('hospitalApp.urls')),
    path('hospitalApp/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('hospitalApp/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
