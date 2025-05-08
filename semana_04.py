import csv
from collections import Counter, defaultdict



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
    

# funcion para leer todo el dataset
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as f:
        return list(csv.DictReader(f))



# Ejercicio 5
# a. El/ los parques con más arboles 
def parque_mas_arboles(arboles):
    conteo = Counter(arbol['espacio_ve'] for arbol in arboles)
    max_cantidad = max(conteo.values())
    return [parque for parque, cantidad in conteo.items() if cantidad == max_cantidad]

    

# b. El/los parques con los árboles más altos en promedio
def parques_promedios_mayor_altura(arboles):
    alturas = defaultdict(list)
    for arbol in arboles:
        try:
            alturas[arbol['espacio_ve']].append(float(arbol['altura_tot']))
        except ValueError:
            continue
    promedios = {p: sum(h)/len(h) for p, h in alturas.items() if h} #dict por comprension, muy buena opcion
    max_prom = max(promedios.values())
    return [p for p, prom in promedios.items() if prom == max_prom]

# c. El/ lo parques con mas variedad de especies
def parques_con_mas_especies(arboles):
    especies = defaultdict(set) # usamos set ya que de esta forma no se aceptan elementos duplicados
    for arbol in arboles:
        especies[arbol['espacio_ve']].add(arbol['nombre_com'])
    mas_variedad = max(len(e) for e in especies.values())
    return [p for p, e in especies.items() if len(e) == mas_variedad]

# d. La especie con más ejemplares en la ciudad
def especie_con_mas_ejemplares(arboles):
    conteo = Counter(arbol['nombre_com'] for arbol in arboles)
    max_cantidad = max(conteo.values())
    return [e for e, c in conteo.items() if c == max_cantidad]

# e. La razon entre especies exoticas y autoctonas
def razon_exoticas_autoctonas(arboles):
    c = Counter(arbol['origen'] for arbol in arboles)
    aut = sum(c[o] for o in c if 'autóctono' in o.lower())
    exo = sum(c[o] for o in c if 'autóctono' not in o.lower())
    return exo / aut if aut else float('inf')


# este para testing

# if __name__ == '__main__':
#     parque = 'CENTENARIO'
#     especie = 'Jacarandá'
#     nombre_archivo = 'arbolado-en-espacios-verdes.csv'
#     arboles = leer_arboles('arbolado-en-espacios-verdes.csv')


#     print(f'Total árboles en {parque}:', len(arboles_parque(nombre_archivo, parque)))
#     popular, cantidad = arbol_mas_popular(parque, nombre_archivo)

#     print(f'Árbol más popular: {popular} ({cantidad})')

#     print(f'nº más altos:', n_mas_altos(parque, 5,  nombre_archivo))

#     print(f'altura promedio del {especie} en {parque} es', altura_promedio(nombre_archivo, parque, especie))

#     print(f'parque/s con más arboles:', parque_mas_arboles(arboles))



# esta funcion permite generar el reporte del md cada vez que se llame al script
# la genere con chatgpt ya que me interesaba entender si se podía hacer esto de esta forma
def generar_reporte(arboles, nombre_archivo='semana_04.md'):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write("# Exploración del arbolado en espacios verdes de Buenos Aires\n\n")

        f.write("## 1. ¿Cuál es el parque con más árboles?\n")
        f.write(f"- Resultado: {', '.join(parque_mas_arboles(arboles))}\n\n")

        f.write("## 2. ¿Cuál tiene los árboles más altos en promedio?\n")
        f.write(f"- Resultado: {', '.join(parques_promedios_mayor_altura(arboles))}\n\n")

        f.write("## 3. ¿Cuál tiene más variedad de especies?\n")
        f.write(f"- Resultado: {', '.join(parques_con_mas_especies(arboles))}\n\n")

        f.write("## 4. ¿Cuál es la especie más común en toda la ciudad?\n")
        f.write(f"- Resultado: {', '.join(especie_con_mas_ejemplares(arboles))}\n\n")

        f.write("## 5. ¿Cuál es la razón entre especies exóticas y autóctonas?\n")
        razon = razon_exoticas_autoctonas(arboles)
        f.write(f"- Resultado: {razon:.2f} especies exóticas por cada autóctona\n")


if __name__ == '__main__':
    arboles = leer_arboles('arbolado-en-espacios-verdes.csv')
    generar_reporte(arboles)

