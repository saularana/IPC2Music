import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Crear la ventana
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ventana.geometry("800x500")  # Ancho x Alto

# Evitar que la ventana sea redimensionable
ventana.resizable(width=False, height=False)

ventana.title("IPC2Music")

# Frame superior para la imagen y los labels
frame_superior_izquierda = tk.Frame(ventana)
frame_superior_izquierda.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Ruta relativa de la imagen
ruta_imagen = os.path.join(os.path.dirname(__file__), "IPC2Music.jpg")

# Cargar la imagen con Pillow
imagen_pil = Image.open(ruta_imagen)

# Redimensionar la imagen para ajustarse al área
width, height = 200, 200  # Ajusta según sea necesario
imagen_pil.thumbnail((width, height))

imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Mostrar la imagen en un Label
label_imagen = tk.Label(frame_superior_izquierda, image=imagen_tk)
label_imagen.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

frame_superior_derecha = tk.Frame(ventana)
frame_superior_derecha.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

# Labels
label_artista = tk.Label(frame_superior_derecha, text="Artista:")
label_cancion = tk.Label(frame_superior_derecha, text="Canción:")
label_album = tk.Label(frame_superior_derecha, text="Álbum:")

# Posicionamiento de Labels usando grid
label_artista.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
label_cancion.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
label_album.grid(row=2, column=1, rowspan=3, padx=5, pady=5, sticky=tk.E)

# Frame inferior para botones y Listbox
frame_inferior = tk.Frame(ventana)
frame_inferior.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

# Botones
btn_iniciar_pausar_cancion = tk.Button(frame_inferior, text="Play")
btn_anterior_cancion = tk.Button(frame_inferior, text="Prev")
btn_siguiente_cancion = tk.Button(frame_inferior, text="Next")

# Posicionamiento de los botones usando grid
btn_iniciar_pausar_cancion.grid(row=0, column=0, padx=5, pady=2)
btn_anterior_cancion.grid(row=0, column=1, padx=5, pady=2)
btn_siguiente_cancion.grid(row=0, column=2, padx=5, pady=2)

# Listbox
listbox = tk.Listbox(frame_inferior)
listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E)

# Agregar elementos al Listbox (puedes personalizar esto)
listbox.insert(tk.END, "Canción 1")
listbox.insert(tk.END, "Canción 2")
listbox.insert(tk.END, "Canción 3")

# Iniciar el bucle principal de Tkinter
num_columnas_ventana = ventana.grid_size()[0]
print("Número de columnas en la ventana:", num_columnas_ventana)

ventana.mainloop()
