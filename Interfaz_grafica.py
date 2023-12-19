from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import importacion.FuncionLista as FuncionLista
import importacion.Listas as Listas
#Listas de Reproduccion
lista_de_Canciones = Listas.ListaDobleEnlazada()
listas_de_reproduccion = Listas.ListaDobleEnlazada()
lista_actual_reproduccion = Listas.ListaDobleEnlazada()

def reproducir_cancion():
    # Obtener el item seleccionado en el Treeview
    seleccion = tree.selection()
    if not seleccion:
        mostrar_alerta("Selecciona una canción antes de reproducir.")
        return

    # Obtener los datos de la canción seleccionada
    item_seleccionado = tree.item(seleccion, "values")
    artista, titulo, album = item_seleccionado

    # Buscar la canción en la lista_de_Canciones
    actual = lista_de_Canciones.inicio
    while actual:
        if actual.cancion.getartista() == artista and actual.cancion.getnombre() == titulo and actual.cancion.getalbum() == album:
            # Encontró la canción, añadir una reproducción
            repeticiones_actuales = actual.cancion.getrepeticiones()
            actual.cancion.setrepeticiones(repeticiones_actuales+1)
            mostrar_alerta(f"Se añadió una reproducción a la canción: {titulo} - {artista}")
            lista_de_Canciones.imprimir_lista()
            lbl_album1.config(text=album)
            lbl_artista1.config(text=artista)
            lbl_cancion1.config(text=titulo)
            return
        actual = actual.siguiente

    # Si llega aquí, no se encontró la canción
    mostrar_alerta("No se encontró la canción en la lista.")
    lbl_album1.config(text="--")
    lbl_artista1.config(text="--")
    lbl_cancion1.config(text="--")

def mostrar_alerta(mensaje):
    messagebox.showinfo("Alerta", mensaje)

def seleccionar_archivo():
       try: 
            opciones_archivo = {
            'filetypes': [('Archivos XML', '*.xml')],
            'title': 'Seleccionar Archivo XML'
            }   
            ruta_archivo = filedialog.askopenfilename(**opciones_archivo)
            lista_de_Canciones.importar_desde_xml(ruta_archivo)
            mostrar_alerta("Se han cargado las canciones correctamente correctamente")
            print(lista_de_Canciones.tamanio)
            # Limpiar el Treeview antes de agregar nuevos datos
            tree.delete(*tree.get_children())

            actual = lista_de_Canciones.inicio
            while actual:
                # Formatear los datos como desees antes de insertarlos
                datos_formateados = (actual.cancion.getartista(), actual.cancion.getnombre(), actual.cancion.getalbum())

                # Insertar en el Treeview
                tree.insert("", tk.END, values=datos_formateados)

                # Mover al siguiente nodo
                actual = actual.siguiente
       except:
            print(f"Error al cargar el archivo: {e}")
       

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
ventana.resizable(False,False)

# Título
titulo = tk.Label(text="IPC Music", bg="lightblue", pady=10)
titulo.grid(columnspan=3)

# Botones menú
boton_archivo = tk.Button(text="Carga Canciones")
boton_archivo.grid(row=1, column=0, sticky="w") 
boton_archivo.config(command=seleccionar_archivo)   
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
boton_iniciar.config(command=reproducir_cancion)

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

lbl_cancion1 = tk.Label(frame_labels, text="--", padx=10, pady=5)
lbl_cancion1.grid(row=0, column=1, sticky="w")

lbl_artista = tk.Label(frame_labels, text="Artista", padx=10, pady=5)
lbl_artista.grid(row=1, column=0, sticky="w")

lbl_artista1 = tk.Label(frame_labels, text="--", padx=10, pady=5)
lbl_artista1.grid(row=1, column=1, sticky="w")

lbl_album = tk.Label(frame_labels, text="Álbum", padx=10, pady=5)
lbl_album.grid(row=2, column=0, sticky="w")

lbl_album1 = tk.Label(frame_labels, text="--", padx=10, pady=5)
lbl_album1.grid(row=2, column=1, sticky="w")

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
frame_lista.grid(row=5, column=0, columnspan=3, sticky="e")

# Treeview
columnas = ("Artista", "Título", "Álbum")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")

# Configurar nombres de columnas
for columna in columnas:
    tree.heading(columna, text=columna)
    tree.column(columna, width=150)

tree.grid(row=0, column=0)

# Botón "Agregar a Lista"
boton_agregar_lista = tk.Button(frame_lista, text="Listas de Reproduccion", padx=10, pady=5, command=FuncionLista.iniciar_interfaz_lista_reproduccion)
boton_agregar_lista.grid(row=0, column=1)





# Botón "Agregar a Lista"
boton_agregar_lista = tk.Button(frame_lista, text="Listas de Reproduccion", padx=10, pady=5, command=FuncionLista.iniciar_interfaz_lista_reproduccion)
boton_agregar_lista.grid(row=0, column=1)
ventana.geometry("700x500")
centrar_ventana(ventana)
ventana.mainloop()
