from collections import namedtuple
import math


Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia(coord1, coord2):
    coord1 = Coordenadas(float(coord1.latitud), float(coord1.longitud))
    coord2 = Coordenadas(float(coord2.latitud), float(coord2.longitud))
    res = float(math.sqrt(((coord2.latitud-coord1.latitud)**2)+((coord2.longitud-coord1.longitud)**2)))
    return res

def calcular_media_coordenadas(coords):
    res = []
    sumlat = 0
    sumlon = 0
    for c in coords:
        sumlat += c.latitud
        sumlon += c.longitud
    res.append((sumlat/len(coords), sumlon/len(coords)))
    return res