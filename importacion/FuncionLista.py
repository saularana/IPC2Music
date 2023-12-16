from importacion.Listas import *
import random

#Valida la existencia con el nombre de la lista de reproduccion
def validad_existencia_lista(nombre, listas_de_reproduccion):
    actual= listas_de_reproduccion.inicio
    if actual == None:
        return False
    while actual:
        if actual.lista.nombre == nombre:
            return True
        actual=actual.siguiente
    return False
#Crea la lista de reproduccion ya validadno que no exista    
def crear_lista_nueva(nombre,listas_de_reproduccion):
    if validad_existencia_lista(nombre, listas_de_reproduccion):
        print("La lista de reproduccion ya existe")
    else:
        lista_nueva = ListaDobleEnlazada()
        lista_nueva.nombre = nombre 
        print("Lista de reproduccion creada!")
        return lista_nueva
#Agrega una cancion a la lista de reproduccion
def agregar_cancion_a_lista(lista, cancion):
    lista.agregar_cancion(cancion)
    return True
#Genera una lista de reproduccion aleatoria 
def generar_lista_aleatoria(lista_original, nombre, cantidad):
    nueva_lista=ListaDobleEnlazada()
    nueva_lista.nombre = nombre
    for i in range(cantidad):
        nueva_lista.agregar_cancion(lista_original.obtener_cancion_aleatoria())
    return nueva_lista
#Obtiene una cancion aleatoria de la lista de reproduccion original
def obtener_cancion_aleatoria(lista_original):
    indice = random.randint(0, lista_original.tamanio-1)
    return lista_original.obtener_cancion_por_indice(indice)



    

