from django.urls import path
from.import views #importa nossas views

urlpatterns = [
    path('', views.listar_tarefa, name = 'lista_tarefas'),
    path('<int:tarefa_id>/', views.detalhe_tarefa, name = "detalhe_tarefa"),


    #add tarefas
    path('adicionar/', views.adicionar_tarefa, name = 'adicionar_tarefas'),
]
