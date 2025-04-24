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
    alturas = []

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
    n_altos = alturas[:n]

    # Tomar los n primeros
    return n_altos
    
def altura_promedio(nombre_archivo, nombre_parque, especie):
    arboles = arboles_parque(nombre_archivo, nombre_parque)

    # lista por comprension para obtener las alturas de los arboles
    try:
        alturas = [float(info_arbol['altura_tot']) for info_arbol in arboles.values() 
                  if info_arbol['nombre_com'] == especie]

        # manejo de excepciones si no hay arboles para ese parque
        if not alturas:
            return None
            
        return sum(alturas) / len(alturas)
        
    except (ValueError, KeyError) as e:
        # 5. Manejar posibles errores
        print(f"Error al procesar los datos: {e}")
        return None
    


if __name__ == '__main__':
    parque = 'CENTENARIO'
    especie = 'Jacarandá'
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    datos = arboles_parque(nombre_archivo, parque)
    print(f'Total árboles en {parque}:', len(datos))
    popular, cantidad = arbol_mas_popular(parque, nombre_archivo)
    print(f'Árbol más popular: {popular} ({cantidad})')
    mas_altos = n_mas_altos(parque, 5,  nombre_archivo)
    print(f'nº más altos: {mas_altos}')


    altura_promedio = altura_promedio(nombre_archivo, parque, especie)
    print(f'altura promedio del {especie} en {parque} es {altura_promedio}')


