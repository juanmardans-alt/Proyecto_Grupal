from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Aquí irán tus rutas más adelante
]