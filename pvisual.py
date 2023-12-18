import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import threading
from importacion.Cancion import canciones
from importacion.Listas import *
from reproductor.Reproductor import reproducir_musica
import webbrowser

class ReproductorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reproductor")

        self.lista_de_canciones = ListaDobleEnlazada()
        self.ruta_xml = '/home/arch-ab/Github/IPC2Music/pruebadeddatos.xml'
        self.lista_de_canciones.importar_desde_xml(self.ruta_xml)
        self.lista_de_canciones.nodo_actual = self.lista_de_canciones.inicio

        self.reproduciendo = False
        self.tiempo_reproduccion_actual = 0  # Variable para almacenar el tiempo de reproducción

        # Botón de iniciar/pausar canción
        self.btn_iniciar_pausar_cancion = tk.Button(self.root, text="Iniciar canción", command=self.iniciar_pausar_cancion)
        self.btn_iniciar_pausar_cancion.pack(side=tk.LEFT, padx=5)

        # Otros botones
        self.btn_siguiente_cancion = tk.Button(self.root, text="Siguiente", command=self.siguiente_cancion)
        self.btn_anterior_cancion = tk.Button(self.root, text="Anterior", command=self.anterior_cancion)
        self.btn_exportar_lista = tk.Button(self.root, text="Exportar", command=self.exportar)
        self.btn_reporte = tk.Button(self.root, text="Reporte", command=self.generar_reporte_html)

        # Posicionamiento de botones
        self.btn_siguiente_cancion.pack(side=tk.LEFT, padx=5)
        self.btn_anterior_cancion.pack(side=tk.LEFT, padx=5)
        self.btn_exportar_lista.pack(side=tk.LEFT, padx=5)
        self.btn_reporte.pack(side=tk.LEFT, padx=5)

    def iniciar_pausar_cancion(self):
        if not self.reproduciendo:
            # Utilizar threading para reproducir música en segundo plano
            self.music_thread = threading.Thread(target=self.reproducir_musica_en_hilo)
            self.music_thread.start()
            self.reproduciendo = True
        else:
            self.tiempo_reproduccion_actual = pygame.mixer.music.get_pos() // 1000
            pygame.mixer.music.pause()
            self.reproduciendo = False

    def reproducir_musica_en_hilo(self):
        try:
            reproducir_musica(self.lista_de_canciones.nodo_actual, self.tiempo_reproduccion_actual)
        except FileNotFoundError:
            print("¡Archivo no encontrado! Pasando a la siguiente canción.")
            # Pasa automáticamente a la siguiente canción
            self.siguiente_cancion()

    def siguiente_cancion(self):
        self.lista_de_canciones.avanzar_nodo()
        self.music_thread = threading.Thread(target=self.reproducir_musica_en_hilo)
        self.music_thread.start()
        self.reproduciendo = True

    def anterior_cancion(self):
        self.lista_de_canciones.retroceder_nodo()
        self.music_thread = threading.Thread(target=self.reproducir_musica_en_hilo)
        self.music_thread.start()
        self.reproduciendo = True

    def run(self):
        # Ejecutar la aplicación
        self.root.mainloop()
        
    def exportar(self):
        # Utilizar threading para exportar en segundo plano
        export_thread = threading.Thread(target=self.exportar_en_hilo)
        export_thread.start()

    def exportar_en_hilo(self):
        try:
            self.lista_de_canciones.exportar_a_xml("/home/arch-ab/Github/IPC2Music/prueba_exportar.xml")
            print("Exportación exitosa.")
        except Exception as e:
            print(f"Error al exportar: {e}")

    def generar_reporte_html(self):
        lista = ListaDobleEnlazada()
        lista.importar_desde_xml('C:/Users/eg574/OneDrive/Escritorio/IPC2Music-main-1.3/pruebadeddatos.xml')
        lista.generar_reporte_html()

    def abrir_reporte(self):
        self.generar_reporte_html()
        webbrowser.open_new_tab('reporte_canciones.html')

# Crear una instancia de la aplicación
reproductor_app = ReproductorApp()
# Ejecutar la aplicación
reproductor_app.run()
