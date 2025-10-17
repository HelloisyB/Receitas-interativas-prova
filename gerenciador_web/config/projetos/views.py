
from django.shortcuts import render

# Create your views here.
from .models import Projeto

def listar_projetos(request):
   
    projetos_salvos = Projeto.objects.all()
    
    
    contexto = {
        'meus_projetos': projetos_salvos 
    }

    return render(request, 'projetos/lista.html', contexto)
