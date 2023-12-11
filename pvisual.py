import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Asegúrate de tener instalada la biblioteca Pillow para trabajar con imágenes
import pygame
import os
from Xml.importar_xml import  importar_xml
from Xml.canciones import canciones

ruta_xml = '/home/arch-ab/Github/IPC2Music/Xml/pruebadeddatos.xml'
canciones_cargadas =  importar_xml.cargar_canciones_desde_xml(ruta_xml)


def reproducir_musica(canciones_cargadas):
    pygame.init()
    pygame.mixer.init()

    # Filtra las canciones cargadas para obtener solo las que terminan con '.mp3'
    canciones_filtradas = [cancionpr.getruta() for cancionpr in canciones_cargadas if cancionpr.getruta().endswith('.mp3')]

    if not canciones_filtradas:
        print("No se encontraron archivos de música en la lista cargada.")
        return

    # Configura la primera canción
    pygame.mixer.music.load(canciones_filtradas[2])

    # Reproduce la música
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    
    
    
# Crear la ventana principal
root = tk.Tk()
root.title("Reproductor")

btn_iniciar_cancion = tk.Button(root, text="Iniciar cancion", command=reproducir_musica(canciones_cargadas))

btn_iniciar_cancion.pack(pady=20)
#btn_iniciar_cancion.pack(side=tk.LEFT, padx=5)
# Ejecutar la aplicación
root.mainloop()