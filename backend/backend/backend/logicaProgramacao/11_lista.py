#lista inicial de tarefas
minhas_tarefas = ["fazer strogonoff", "viajar", "dormir", "comer brigadeiro"]
print (f"tarefas pendentes: {minhas_tarefas}")

#add uma nova tarefa ao final da lista
minhas_tarefas.append("tirar ferias")
print(f"tarefa adicionada:{minhas_tarefas}")

#add uma tarefa em uuma posição especifica (indice 1)
minhas_tarefas.insert(1, "encontar amigos")
print(f"tarefa inserida em posição especifica: {minhas_tarefas}")

#removendo uma tarefa que ja foi feita (pelo nome)
minhas_tarefas.remove("fazer strogonoff")
print(f"tarefa 'fazer strogonoff' removida: {minhas_tarefas}")

#removendo a ultima tarefa (útil para pilhas)
tarefa_removida = minhas_tarefas.pop() #remove "dormir"
print(f"ultima tarefa removida ('{tarefa_removida}'): {minhas_tarefas}")