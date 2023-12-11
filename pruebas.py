from importar_xml import  importar_xml
from canciones import canciones
# Ejemplo de uso
ruta_xml = '/home/arch-ab/Github/IPC2Music/pruebadeddatos.xml'
canciones_cargadas =  importar_xml.cargar_canciones_desde_xml(ruta_xml)

# Imprimir información de las canciones cargadas
for cancionpr in canciones_cargadas:
    print(f"Nombre: {cancionpr.getnombre()}")
    print(f"Artista: {cancionpr.getartista()}")
    print(f"Álbum: {cancionpr.getalbum()}")
    print(f"Imagen: {cancionpr.getimagen()}")
    print(f"Ruta: {cancionpr.getruta()}")
    print("----------------------")