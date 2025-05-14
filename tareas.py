def agregar_tarea(lista, tarea):    
    lista.append(tarea)    
    return lista

def listar_tareas(lista):
    for tarea in lista:
        print(tarea)