from django.urls import path
from .views import registro_estudiante

urlpatterns = [
    path('registro/', registro_estudiante, name='registro_estudiante'),
]
