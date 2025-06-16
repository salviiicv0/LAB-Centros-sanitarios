from coordenadas import *

def test_calcular_distancia(coord1, coord2):
    res = calcular_distancia(coord1, coord2)
    print(res)

def test_calcular_media_coordenadas(coords):
    res = calcular_media_coordenadas(coords)
    print(res)

def main():
    coord1 = Coordenadas(36.86846114144969, -6.174778817404322)
    coord2 = Coordenadas(36.7414196395626, -6.4297973898168905)
    # test_calcular_distancia(coord1, coord2)
    coords = [coord1, coord2]
    # print(coords)
    # test_calcular_media_coordenadas(coords)


if __name__ == "__main__":
    main()