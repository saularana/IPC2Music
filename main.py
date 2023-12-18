import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import ttk
from importacion.Listas import ListaDobleEnlazada

lista_de_listas = []
tu_lista_de_canciones = ListaDobleEnlazada()
lista_de_listas.append(tu_lista_de_canciones)

def expandir_ultima_columna(event):
    ancho_ventana = event.width
    frame_inferior.grid_columnconfigure(num_columnas_frame_inferior - 1, weight=1)

def agregar_items_treeview(lista_items):
    actual = lista_items.inicio
    index = 1
    while actual:
        tree.insert("", "end", text=str(index), values=(actual.cancion.getnombre(), actual.cancion.getartista(), actual.cancion.getalbum()))
        actual = actual.siguiente
        index += 1

def importar_xml():
    archivo_seleccionado = filedialog.askopenfilename(
        title="Seleccionar Archivo",
        filetypes=[("Archivos XML", "*.xml"), ("Todos los archivos", "*.*")]
    )
    if archivo_seleccionado:
        tu_lista_de_canciones.importar_desde_xml(archivo_seleccionado)
        # Limpia el Treeview antes de agregar nuevos elementos
        for item in tree.get_children():
            tree.delete(item)
        # Agrega los elementos actualizados al Treeview
        agregar_items_treeview(tu_lista_de_canciones)

# Crear la ventana
ventana = tk.Tk()
ventana.bind('<Configure>', expandir_ultima_columna)
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
frame_superior_derecha.grid_columnconfigure(0, weight=1)

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
frame_inferior.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
frame_inferior.grid_rowconfigure(1, weight=1)

# Botones
btn_iniciar_pausar_cancion = tk.Button(frame_inferior, text="Play")
btn_anterior_cancion = tk.Button(frame_inferior, text="Prev")
btn_siguiente_cancion = tk.Button(frame_inferior, text="Next")
btn_importar_xml = tk.Button(frame_inferior, text="Importar Xml", command=importar_xml)
btn_exportar_xml = tk.Button(frame_inferior, text="Exportar Xml")

# Posicionamiento de los botones usando grid
btn_iniciar_pausar_cancion.grid(row=0, column=0, padx=5, pady=2)
btn_anterior_cancion.grid(row=0, column=1, padx=5, pady=2)
btn_siguiente_cancion.grid(row=0, column=2, padx=5, pady=2)
btn_importar_xml.grid(row=0, column=3, padx=5, pady=2)
btn_exportar_xml.grid(row=0, column=4, padx=5, pady=2)

# Treeview
tree = ttk.Treeview(frame_inferior, columns=("Nombre", "Artista", "Álbum"))
tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E)

# Configurar encabezados de columnas
tree.heading("#0", text="Índice")
tree.heading("Nombre", text="Nombre")
tree.heading("Artista", text="Artista")
tree.heading("Álbum", text="Álbum")

# Agregar elementos al Treeview (puedes personalizar esto)
agregar_items_treeview(tu_lista_de_canciones)

ventana.mainloop()
