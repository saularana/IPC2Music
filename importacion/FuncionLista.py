from importacion.Listas import *
import random

def generar_lista_aleatoria(lista_original, cantidad):
    nueva_lista=ListaDobleEnlazada()
    for i in range(cantidad):
        nueva_lista.agregar_cancion(lista_original.obtener_cancion_aleatoria())
    return nueva_lista

def obtener_cancion_aleatoria(lista_original):
    indice = random.randint(0, lista_original.tamanio-1)
    return lista_original.obtener_cancion_por_indice(indice)


    

    

