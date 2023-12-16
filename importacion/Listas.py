import xml.etree.ElementTree as ET
from importacion.Cancion import canciones


class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.nombre=""
        self.inicio = None
        self.fin = None
        self.tamanio=0
        
    def obtener_nodo_actual(self):
        # Devuelve el nodo actual
        return self.nodo_actual

    def avanzar_nodo(self):
        # Avanza al siguiente nodo
        if self.nodo_actual and self.nodo_actual.siguiente:
            self.nodo_actual = self.nodo_actual.siguiente

    def retroceder_nodo(self):
        # Retrocede al nodo anterior
        if self.nodo_actual and self.nodo_actual.anterior:
            self.nodo_actual = self.nodo_actual.anterior

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
            self.tamanio+=1
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
            self.tamanio+=1
            
            
    def importar_desde_xml(self, ruta_archivo):
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        for cancion_elem in root.findall('cancion'):
            nombre = cancion_elem.get('nombre')
            artista = cancion_elem.find('artista').text
            album = cancion_elem.find('album').text
            imagen = cancion_elem.find('imagen').text
            ruta = cancion_elem.find('ruta').text
            repeticiones = cancion_elem.find('repeticiones')

            cancion = canciones(nombre, artista, album, imagen, ruta, repeticiones)
            self.agregar_cancion(cancion)
            
    def exportar_a_xml(self, ruta_archivo):
        root = ET.Element("canciones")
    
        actual = self.inicio
        while actual:
            cancion_elem = ET.SubElement(root, "cancion")
            cancion_elem.set('nombre', actual.cancion.getnombre())
    
            artista_elem = ET.SubElement(cancion_elem, "artista")
            artista_elem.text = actual.cancion.getartista()
    
            album_elem = ET.SubElement(cancion_elem, "album")
            album_elem.text = actual.cancion.getalbum()
    
            imagen_elem = ET.SubElement(cancion_elem, "imagen")
            imagen_elem.text = actual.cancion.getimagen()
    
            ruta_elem = ET.SubElement(cancion_elem, "ruta")
            ruta_elem.text = actual.cancion.getruta()
    
            repeticiones_elem = ET.SubElement(cancion_elem, "repeticiones")
            repeticiones_elem.text = str(actual.cancion.getrepeticiones())
    
            actual = actual.siguiente
    
        tree = ET.ElementTree(root)
        tree.write(ruta_archivo)
    
    def filtrar_por_artista(self, nombre_artista):
        nueva_lista = ListaDobleEnlazada()
        actual = self.inicio
        while actual:
            if actual.cancion.getartista() == nombre_artista:
                nueva_lista.agregar_cancion(actual.cancion)
            actual = actual.siguiente
        return nueva_lista
    

        
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