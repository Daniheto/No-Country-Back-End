from django.urls import path
from .views import create_inscription, list_inscriptions, delete_inscription

urlpatterns = [
    path('create/', create_inscription, name='create_inscription'),
    path('get_all/', list_inscriptions, name='list_inscriptions'),
    path('delete/<int:id>/', delete_inscription, name='delete_inscription'),
]
