from importacion.Importar_xml import  import_xml
from importacion.Cancion import canciones
from importacion.Listas import * 
# Ejemplo de uso
ruta_xml = '/home/arch-ab/Github/IPC2Music/pruebadeddatos.xml'
canciones_cargadas =  import_xml.cargar_canciones_desde_xml(ruta_xml)
lista_doble_enalzada = ListaDobleEnlazada()

# Imprimir información de las canciones cargadas
for cancionpr in canciones_cargadas:
    lista_doble_enalzada.agregar_cancion(cancionpr)
    
lista_doble_enalzada.imprimir_lista()

