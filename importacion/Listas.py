import xml.etree.ElementTree as ET
from importacion.Cancion import Cancion
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamanio = 0

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
            self.tamanio += 1
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
            self.tamanio += 1
    
            
            
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

            cancion = Cancion(nombre, artista, album, imagen, ruta, repeticiones)
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
            
    
    def  filtrar_por_artista(self,nombre_artista):
        nueva_lista=ListaDobleEnlazada()
        actual=self.inicio
        while actual:
            if actual.cancion.getartista()==nombre_artista:
                nueva_lista.agregar_cancion(actual.cancion)
            actual=actual.siguiente
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

    def generar_reporte_html(self):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <title>Reporte de Canciones</title>
        </head>
        <body>
            <div class="container mt-5">
                <h2 class="mb-4">Reporte de Canciones</h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">Nombre</th>
                            <th scope="col">Artista</th>
                            <th scope="col">Álbum</th>
                            <th scope="col">Imagen</th>
                            <th scope="col">Ruta</th>
                            <th scope="col">Repeticiones</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        actual = self.inicio
        while actual:
            html_content += f"""
                <tr>
                    <td>{actual.cancion.getnombre()}</td>
                    <td>{actual.cancion.getartista()}</td>
                    <td>{actual.cancion.getalbum()}</td>
                    <td>{actual.cancion.getimagen()}</td>
                    <td>{actual.cancion.getruta()}</td>
                    <td>{actual.cancion.getrepeticiones()}</td>
                </tr>
            """
            actual = actual.siguiente

        html_content += """
                    </tbody>
                </table>
            </div>
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        </body>
        </html>
        """

        with open('reporte_canciones.html', 'w') as file:
            file.write(html_content)
