from django.db import models

# Create your models here.

class Tarefa(models.Model):

    titulo = models.CharField(max_length=200)
    descriçao = models.TextField(blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now_add = True)
    cocluida = models.BooleanField(default = False)

    #exibir titulo por padrão
    def __str__(self):
        return self.titulo
    
