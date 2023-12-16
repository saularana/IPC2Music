from importacion.Cancion import canciones
from importacion.Listas import * 




# Ejemplo de uso
ruta_xml = 'pruebadeddatos.xml'
# canciones_cargadas =  import_xml.cargar_canciones_desde_xml(ruta_xml)
lista_doble_enalzada = ListaDobleEnlazada()
lista_doble_enalzada.importar_desde_xml(ruta_xml)


def filtrar_por_artista(lista_original, nombre_artitsta):
    nueva_lista=ListaDobleEnlazada()
    actual = lista_original.inicio
    while actual:
        if actual.cancion.getartista() == nombre_artitsta:
            nueva_lista.agregar_cancion(actual.cancion)
        actual=actual.siguiente
    return nueva_lista


# Imprimir información de las canciones cargadas
# for cancionpr in canciones_cargadas:
#     lista_doble_enalzada.agregar_cancion(cancionpr)
    
lista_doble_enalzada.imprimir_lista()
print ("================================================================")
print ("Filtra por artista")
listaartista = filtrar_por_artista(lista_doble_enalzada,"Pedro Capo")
listaartista.imprimir_lista()
listaartista.exportar_a_xml("pruebaexport.xml")


