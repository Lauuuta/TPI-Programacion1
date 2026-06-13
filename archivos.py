import csv

def cargar_csv():
    paises = []

    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            paises.append(fila)
    
    return paises

def guardar_csv(paises):
    with open("paises.csv", "w", encoding="utf-8", newline="") as archivo:
        encabezados = ["nombre"," poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)
