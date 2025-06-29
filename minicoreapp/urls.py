from django.urls import path
from . import views

urlpatterns = [
    path('', views.filtrar_ventas, name='filtro_ventas'),
]
