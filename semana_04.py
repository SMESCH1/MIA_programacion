# Ej 1
import csv

def arboles_parque(nombre_archivo, nombre_parque):
    arboles = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [fila for fila in reader if fila['espacio_ve'] == nombre_parque]

        # for fila in reader:
        #     if fila['espacio_ve'] == nombre_parque:
        #         print(fila)



            # valores = linea.strip().split(',')
            # arboles = dict(zip(columnas, valores))
        #     print(arboles)
        # arboles = []

        # for l in nombre_archivo:
        #     arbol = dict(zip(id_arbol, l))
        # id_arbol in nombre_parque:
        #     arboles = dict(zip(id_arbol,))
        # long,lat,id_arbol,altura_tot,diametro,inclinacio,id_especie,nombre_com,nombre_cie,tipo_folla,espacio_ve,ubicacion,nombre_fam,nombre_gen,origen,coord_x,coord_y

nombre_archivo = "/home/sebastian-mesch-henriques/Escritorio/MIA/MIA_programacion/arbolado-en-espacios-verdes.csv"
arbolado = arboles_parque(nombre_archivo,'CENTENARIO')
print(arbolado)


if __name__ == "__main__":
    nombre_archivo = "arbolado-en-espacios-verdes.csv"
    print(f"")





