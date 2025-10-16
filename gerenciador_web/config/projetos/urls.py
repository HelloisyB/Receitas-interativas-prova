from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projetos, name='nome_projetos'),
]
