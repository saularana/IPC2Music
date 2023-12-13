class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def imprimir_lista(self):
        actual = self.inicio
        while actual:
            print(f"Nombre: {actual.cancion.getnombre()}")
            print(f"Artista: {actual.cancion.getartista()}")
            print(f"Álbum: {actual.cancion.getalbum()}")
            print(f"Imagen: {actual.cancion.getimagen()}")
            print(f"Ruta: {actual.cancion.getruta()}")
            print("----------------------")
            actual = actual.siguiente
