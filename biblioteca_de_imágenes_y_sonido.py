import pygame

pygame.mixer.init()

def cargar_imagen(ruta:str, tamaño=(20, 20))->None:
    '''
    Carga una imagen y la escala de la misma
    '''
    imagen = pygame.image.load(ruta) # Cargar una imagen
    imagen = pygame.transform.scale(imagen, tamaño) # Escalar la imagen

    return imagen
