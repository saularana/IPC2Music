import xml.etree.ElementTree as ET
from importacion.Cancion import canciones

class import_xml:
    @staticmethod
    def cargar_canciones_desde_xml(ruta_archivo):
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        lista_canciones=[]

        for cancion_elem in root.findall('cancion'):
            nombre = cancion_elem.get('nombre')
            artista = cancion_elem.find('artista').text
            album = cancion_elem.find('album').text
            imagen = cancion_elem.find('imagen').text
            ruta = cancion_elem.find('ruta').text
            repeticiones = cancion_elem.find('repeticiones')

            cancion = canciones(nombre,artista,album,imagen,ruta,repeticiones)
            lista_canciones.append(cancion)

        return lista_canciones

