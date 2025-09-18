from django.urls import path
from.import views #importa nossas views

urlpatterns = [
    path('', views.listar_tarefa, name = 'lista_tarefas') 
]