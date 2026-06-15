import csv
import os 
def cargar_csv(nombre_archivo):
    lista = []
    """Valida si el archivo existe, si no existe lo crea y escribe los encabezados"""
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe. Se creara uno nuevo.")
        return lista
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                pais = {
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                }
                lista.append(pais)
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return None
    
    return lista
def guardar_csv(paises, nombre_archivo):
    """Escribe los datos en un archivo CSV, si el archivo no existe lo crea"""
    try:
        with open(nombre_archivo, mode='w',encoding='utf-8', newline='') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
            escritor_csv.writeheader()
            for pais in paises:
                escritor_csv.writerow(pais)
    except Exception as e:
        print(f"Error al escribir en el archivo {nombre_archivo}: {e}")