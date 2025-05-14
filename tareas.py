def agregar_tarea(lista, tarea):    
    lista.append(tarea)    
    return lista

def eliminar_tarea(lista,indice):
    for i, tarea in enumerate(lista):
        if i==indice:
            lista.remove(tarea)

def listar_tareas(lista):
    for tarea in lista:
        print(tarea)