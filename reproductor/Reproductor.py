import pygame

def reproducir_musica(nodo, tiempo_reproduccion=0):
    ruta_musica = nodo.cancion.getruta()
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(start=tiempo_reproduccion)

    # Esperar hasta que la reproducción termine
    pygame.mixer.music.wait()

    # Obtener la duración total y el tiempo actual de reproducción
    duracion_total = pygame.mixer.music.get_length()
    tiempo_actual = pygame.mixer.music.get_pos() / 1000

    # Verificar si se reprodujo más de la mitad
    if tiempo_actual >= duracion_total / 2:
        nodo.cancion.setrepeticiones(nodo.cancion.getrepeticiones() + 1)
        print(f"las repeticiones de la cancion {nodo.cancion.getnombre} es {nodo.cancion.getrepeticiones}")
