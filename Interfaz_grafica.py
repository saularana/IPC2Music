import tkinter as tk

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

# Ventana principal
ventana = tk.Tk()
ventana.title("IPC Music")

# Título
titulo = tk.Label(text="IPC Music", bg="lightblue", pady=10)
titulo.grid(columnspan=3)

# Botones menú
boton_archivo = tk.Button(text="Archivo")
boton_archivo.grid(row=1, column=0, sticky="w")

boton_reporte = tk.Button(text="Reporte")
boton_reporte.grid(row=1, column=1, sticky="w")

# Barra de búsqueda
barra_busqueda = tk.Entry(width=40)
barra_busqueda.grid(row=1, column=2, sticky="e", padx=(10, 5), pady=25)

# Contenedor para los botones de control
frame_botones = tk.Frame()
frame_botones.grid(row=2, column=1, columnspan=3, sticky="e")

# Botones control
boton_iniciar = tk.Button(frame_botones, text="▶", padx=10, pady=5)
boton_iniciar.grid(row=0, column=0)

boton_pausar = tk.Button(frame_botones, text="⏸️", padx=10, pady=5)
boton_pausar.grid(row=0, column=1)

boton_parar = tk.Button(frame_botones, text="⏹️", padx=10, pady=5)
boton_parar.grid(row=0, column=2)

# Contenedor para los labels
frame_labels = tk.Frame()
frame_labels.grid(row=4, column=1, columnspan=3, sticky="e")

# Labels canción con texto
lbl_cancion = tk.Label(frame_labels, text="Cancion", padx=10, pady=5)
lbl_cancion.grid(row=0, column=0, sticky="w")

lbl_artista = tk.Label(frame_labels, text="--", padx=10, pady=5)
lbl_artista.grid(row=0, column=1, sticky="w")

lbl_artista = tk.Label(frame_labels, text="Artista", padx=10, pady=5)
lbl_artista.grid(row=1, column=0, sticky="w")

lbl_artista = tk.Label(frame_labels, text="Juan Gabriel", padx=10, pady=5)
lbl_artista.grid(row=1, column=1, sticky="w")

lbl_album = tk.Label(frame_labels, text="Álbum", padx=10, pady=5)
lbl_album.grid(row=2, column=0, sticky="w")

lbl_album = tk.Label(frame_labels, text="--", padx=10, pady=5)
lbl_album.grid(row=2, column=1, sticky="w")

# Botones cambiar canción
boton_atras = tk.Button(frame_labels, text="⏮️", padx=10, pady=5)
boton_atras.grid(row=3, column=0)

boton_adelante = tk.Button(frame_labels, text="⏭️", padx=10, pady=5)
boton_adelante.grid(row=3, column=1)

# Nuevo contenedor para el bloque adicional
frame_bloque_adicional = tk.Frame()
frame_bloque_adicional.grid(row=5, column=1, columnspan=3, sticky="e")


# Separador vertical entre el bloque adicional y la Listbox
separador_vertical = tk.Label(frame_bloque_adicional, text=" ", padx=10, pady=5)
separador_vertical.grid(row=0, column=2)

# Contenedor para la Listbox y el botón "Agregar a Lista"
frame_lista = tk.Frame()
frame_lista.grid(row=6, column=1, columnspan=3, sticky="e")

# Listbox
lista_canciones = tk.Listbox(frame_lista, width=30, height=5)
lista_canciones.grid(row=0, column=0)

# Botón "Agregar a Lista"
boton_agregar_lista = tk.Button(frame_lista, text="Agregar a Lista", padx=10, pady=5)
boton_agregar_lista.grid(row=0, column=1)

centrar_ventana(ventana)
ventana.mainloop()
