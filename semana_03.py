import random
import numpy as np

def crear_album(figus_total):
    return [0]*figus_total

def album_incompleto(A):
    return 0 in A


def comprar_figu(figus_total):    
    return random.randint(0,figus_total-1)
# print(comprar_figu(860))

def cuantas_figus(figus_total):
    nuevo = crear_album(figus_total)
    necesarias = 0
    while album_incompleto(nuevo):
        posicion = comprar_figu(figus_total)
        nuevo[posicion] = 1
        necesarias += 1
    return necesarias

def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(resultados)
    print(f'Se necesitan en promedio {promedio} figuritas')
    return promedio


def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0,figus_total-1) for _ in range(figus_paquete)]


def cuantos_paquetes(figus_total, figus_paquete):
    nuevo = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(nuevo):
        paquete = comprar_paquete(figus_total,5)
        for figu in paquete:
            nuevo[figu] = 1
        paquetes += 1
    # print(f'se necesitan {necesarios} paquetes')
    return paquetes
# cuantos_paquetes(860,5)

def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    resultados = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)]
    return np.mean(resultados)
# experimento_paquetes(100,860)
# experimento_paquetes(1000,860)


if __name__ == "__main__":
    figus_total = 860
    figus_paquete = 5
    n_repeticiones = 100
    promedio = experimento_paquetes(n_repeticiones, figus_total, figus_paquete)
    print(f"Promedio de paquetes para completar el álbum: {promedio}")





