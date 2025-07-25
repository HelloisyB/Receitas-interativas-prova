#lista de tarefas
minhas_tarefas = ["fazer strogonoff", "viajar", "sair do sesi e associados", "comer brigadeiro", "estudar", "jantar", "fazer compras", "ir ao cinema"]
print(f"Tarefas pendentes: {minhas_tarefas}")

#add 2 registros em posições específicas
minhas_tarefas.insert(2, "encontrar amigos")  # Adiciona "encontrar amigos" na posição 2
minhas_tarefas.insert(5, "tirar ferias")       # Adiciona "tirar ferias" na posição 5
print(f"Ao adicionar registros: {minhas_tarefas}")

#Remove o registro da posição 5
del minhas_tarefas[3]  # Remove o elemento na posição 5
print(f"Ao remover o registro da posição 3: {minhas_tarefas}")

#Remove o último registro
tarefa_removida = minhas_tarefas.pop()  # Remove o último elemento
print(f"Ao remover o último registro ('{tarefa_removida}'): {minhas_tarefas}")
