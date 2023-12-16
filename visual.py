import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Asegúrate de tener instalada la biblioteca Pillow para trabajar con imágenes
import pygame
import os

def cargar_imagen():
    # Aquí puedes cargar tu propia imagen
    imagen_path = "/run/media/arch-ab/Archivos/Pictures/optimus-prime-peleando_3600x2025_xtrafondos.com.jpg"
    imagen = Image.open(imagen_path)
    imagen = ImageTk.PhotoImage(imagen)
    panel_imagen.config(image=imagen)
    panel_imagen.image = imagen

def iniciar_proceso():
    # Aquí puedes agregar la lógica de tu proceso
    for i in range(101):
        barra_progreso['value'] = i
        root.update_idletasks()

def boton_presionado():
    label_estado.config(text="¡Botón presionado!")
    
def reproducir_musica(carpeta_musica):
    pygame.init()
    pygame.mixer.init()

    # Obtén la lista de archivos de música en la carpeta
    canciones = [archivo for archivo in os.listdir(carpeta_musica) if archivo.endswith('.mp3')]

    if not canciones:
        print("No se encontraron archivos de música en la carpeta.")
        return

    # Configura la primera canción
    pygame.mixer.music.load(os.path.join(carpeta_musica, canciones[0]))

    # Reproduce la música
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    carpeta_musica = "pruebadeddatos.xml"
    reproducir_musica(carpeta_musica)

# Crear la ventana principal
root = tk.Tk()
root.title("Entorno Visual con Python")

# Barra de progreso
barra_progreso = ttk.Progressbar(root, length=300, mode='determinate')
barra_progreso.pack(pady=10)

# Panel para la imagen
panel_imagen = tk.Label(root)
panel_imagen.pack(pady=10)

# Botones
btn_cargar_imagen = tk.Button(root, text="Cargar Imagen", command=cargar_imagen)
btn_cargar_imagen.pack(side=tk.LEFT, padx=5)
btn_iniciar_proceso = tk.Button(root, text="Iniciar Proceso", command=iniciar_proceso)
btn_iniciar_proceso.pack(side=tk.LEFT, padx=5)
btn_boton_personalizado = tk.Button(root, text="Botón Personalizado", command=boton_presionado)
btn_boton_personalizado.pack(side=tk.LEFT, padx=5)

# Etiqueta de estado
label_estado = tk.Label(root, text="")
label_estado.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
