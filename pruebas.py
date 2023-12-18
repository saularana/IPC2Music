from importacion.Cancion import canciones
from importacion.Listas import ListaDobleEnlazada,Nodo




# Ejemplo de uso
ruta_xml = 'pruebadeddatos.xml'
lista_doble_enalzada = ListaDobleEnlazada()
lista_doble_enalzada.importar_desde_xml(ruta_xml)
# Imprimir información de las canciones cargadas

    
lista_doble_enalzada.imprimir_lista()
print ("================================================================")
print ("Filtra por artista")
listaartista = ListaDobleEnlazada()
listaartista = lista_doble_enalzada.filtrar_por_artista("Daddy Yankee")
listaartista.imprimir_lista()
listaartista.exportar_a_xml("pruebaexport.xml")


