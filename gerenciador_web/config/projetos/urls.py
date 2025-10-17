from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='nome_projetos'),
]
