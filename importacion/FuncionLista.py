from importacion.Listas import *
import tkinter as tk
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
#Crea la lista de reproduccion ya validando que no exista    
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

def InterfazListaReproduccion(ventana):
        master = ventana
        master.title("Lista de Reproducción")
        #Contenedor para botones
        frame_botones = tk.Frame(master)
        frame_botones.grid(row=3, column=1, columnspan=3, sticky="e")
        #Botones
        boton_nueva_lista = tk.Button(frame_botones, text="Nueva Lista", padx=10, pady=5, command=crear_lista_nueva)
        boton_nueva_lista.grid(row=0, column=1)
        boton_crear_lista_aleatoria = tk.Button(frame_botones, text="Lista Aleatoria", padx=10, pady=5, command=generar_lista_aleatoria)
        boton_crear_lista_aleatoria.grid(row=1, column=1)
        boton_ver_lista = tk.Button(frame_botones, text="Ver Listas", padx=10, pady=5)
        boton_ver_lista.grid(row=2, column=1)
        
     
        
        def agregar_cancion(self):
            cancion = self.entry_cancion.get()
            if cancion:
                self.lista_reproduccion.agregar_cancion(cancion)
                self.entry_cancion.delete(0, tk.END)

        def mostrar_lista(self):
            lista = self.lista_reproduccion.obtener_lista()
            if lista:
                mensaje = "\n".join(lista)
            else:
                mensaje = "La lista de reproducción está vacía."
            tk.messagebox.showinfo("Lista de Reproducción", mensaje)

def iniciar_interfaz_lista_reproduccion():
    ventana = tk.Tk()
    ventana.geometry("400x300")
    interfazReproduccion = InterfazListaReproduccion(ventana)
    ventana.mainloop()

    

