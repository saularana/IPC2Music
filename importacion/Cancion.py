class canciones:
    def __init__(self,nombre,artista,album,imagen,ruta,repeticiones):
        self.__nombre=nombre
        self.__artista=artista
        self.__album=album
        self.__imagen=imagen
        self.__ruta=ruta
        self.__repeticiones=repeticiones

    def getnombre(self):
        return self.__nombre        
    def getartista(self):
        return self.__artista        
    def getalbum(self):
        return self.__album        
    def getimagen(self):
        return self.__imagen        
    def getruta(self):
        return self.__ruta
    def getrepeticiones(self):
        return self.__repeticiones

    def setnombre(self,nombre):
        self.__nombre=nombre        
    def setartista(self,artista):
        self.__artista=artista        
    def setalbum(self,album):
        self.__album=album        
    def setimagen(self,imagen):
        self.__imagen=imagen        
    def setruta(self,ruta):
        self.__ruta=ruta
    def setrepeticiones(self,repeticiones):
        if (repeticiones>self.__repeticiones) :
            self.__repeticiones=repeticiones
