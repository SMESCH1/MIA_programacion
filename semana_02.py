### Ej 1: Invertir una lista
def invertir_lista(lista):
    lista = lista[::-1]
    return lista

# def invertir_lista2(l):
#     res = []
#     for i in range(len(l)):
#             res.append(l[-i-1])
#     return res

# lista = [1, 2, 3, 4, 5]
# invertir_lista2(lista)

### Ej 2: Conjetura Collatz
def collatz(nro):    
    if nro == 1:        # caso base
        return(nro)
    else:
        if nro%2 == 0:
            return nro/2
        else:
            return nro*3+1

print(collatz(5))



### Ej 3: Diccionarios
def contar_definiciones(d):
    count_defs = {}
    for c,defs in d.items():
        count_defs[c] = len(defs)
    return count_defs
## solucion mucho mejor con dict por compresion
## return {clave: len(definiciones) for clave, definiciones in d.items()}

def cantidad_de_claves_letra(d, l):
    contador = 0
    for clave in d:
        if clave.startswith(l):
            contador += 1
    return contador
### opcion mejor, generador en sum:
### return sum(1 for clave in d if clave.startswith(l))

### Ej 4: Propagación

def propagar(fosforos):
    # Propagación hacia la derecha
    for i in range(1, len(fosforos)):
        if fosforos[i] == 0 and fosforos[i - 1] == 1:
            fosforos[i] = 1

    # Propagación hacia la izquierda
    for i in range(len(fosforos) - 2, -1, -1):
        if fosforos[i] == 0 and fosforos[i + 1] == 1:
            fosforos[i] = 1
    return fosforos
    # si quisieramos convertir los fósforos que estaban encendidos en carbonizados
    return [-1 if x == 1 else x for x in fosforos]



        
