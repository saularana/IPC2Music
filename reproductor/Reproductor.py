import pygame

def reproducir_musica(nodo, tiempo_reproduccion=0):
    pygame.init()  # Inicializar Pygame completamente

    # Configurar el modo de video para ejecución en segundo plano
    pygame.display.set_mode((1, 1), pygame.NOFRAME)

    ruta_musica = nodo.cancion.getruta()
    sonido = pygame.mixer.Sound(ruta_musica)

    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(start=tiempo_reproduccion)

    # Obtener la duración total de la canción
    duracion_total = sonido.get_length()

    # Esperar hasta que la reproducción termine (sin bloquear)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.event.clear(pygame.USEREVENT)
    
    while pygame.mixer.music.get_busy() or not pygame.event.get(pygame.USEREVENT):
        pygame.time.Clock().tick(30)  # Ajusta la velocidad de actualización según sea necesario

    # Obtener el tiempo actual de reproducción
    tiempo_actual = tiempo_reproduccion + duracion_total

    # Verificar si se reprodujo más de la mitad y agregar una reproducción
    if tiempo_actual >= duracion_total / 2:
        nodo.cancion.setrepeticiones(nodo.cancion.getrepeticiones() + 1)
        print(f"las repeticiones de la cancion {nodo.cancion.getnombre} es {nodo.cancion.get}")

    # Verificar si la canción ha finalizado y agregar una repetición
    if tiempo_actual >= duracion_total:
        nodo.cancion.setrepeticiones(nodo.cancion.getrepeticiones() + 1)
        print(f"las repeticiones de la cancion {nodo.cancion.getnombre} es {nodo.cancion.get}")
