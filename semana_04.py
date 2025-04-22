import csv
from collections import Counter

def arboles_parque(nombre_archivo, nombre_parque):
    arboles = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # return [fila for fila in reader if fila['espacio_ve'] == nombre_parque]
        for fila in reader:
            if fila['espacio_ve'].strip().upper() == nombre_parque.strip().upper():
                arboles[fila['id_arbol']] = fila
    return arboles

# funcion arbol mas popular del parque
def arbol_mas_popular(nombre_parque, nombre_archivo):
    arboles = arboles_parque(nombre_archivo, nombre_parque)
    contador = Counter(fila['nombre_com'] for fila in arboles.values())
    mas_comun = contador.most_common(1)
    return mas_comun[0] if mas_comun else (None, 0)

# funcion arboles mas altos
def n_mas_altos(nombre_parque, n, nombre_archivo):
    arboles = arboles_parque(nombre_archivo, nombre_parque)
    alturas = {}

    for fila in arboles.values():
        try:
            altura = float(fila['altura_tot'])
            especie = fila['nombre_com']
            id_arbol = fila['id_arbol']
            alturas.append((altura, especie, id_arbol))
        except ValueError:
            continue  # salta si no puede convertir la altura a número

    # Ordenar por altura en orden descendente
    alturas.sort(reverse=True, key=lambda x: x[0])

    # Tomar los n primeros
    return alturas[:n]
    





if __name__ == '__main__':
    parque = 'CENTENARIO'
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    datos = arboles_parque(nombre_archivo, parque)
    print(f'Total árboles en {parque}:', len(datos))
    popular, cantidad = arbol_mas_popular(parque, nombre_archivo)
    print(f'Árbol más popular: {popular} ({cantidad})')
