from archivos import cargar_csv, guardar_csv
from funciones import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
paises = cargar_csv('paises.csv')
ruta = 'paises.csv'
def test_cargar_csv():
    print("Probando cargar_csv...")
    print("Paises cargados:")
    for pais in paises:
        print(pais)

if __name__ == "__main__":
    test_cargar_csv()
    print("Que desea hacer?")
    print("1. Agregar un nuevo país")
    print("2. Actualizar datos de poblacion o superficie de un país existente")
    print("3. Buscar un país por su nombre")
    print("4. Filtrar países por continente, población o superficie")
    print("7. Ordenar países por nombre")
    print("8. Ordenar países por población")
    print("9. Ordenar países por superficie")    
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        filtro = input("¿Desea filtrar por continente, población o superficie? (Ingrese 'continente', 'poblacion' o 'superficie'): ").lower()
        while filtro not in ['continente', 'poblacion', 'superficie']:
            filtro = input("Opción no válida. Por favor, ingrese 'continente', 'poblacion' o 'superficie': ").lower()
        if filtro == 'continente':
            continente_usuario = input("Ingrese el continente a filtrar: ")
            resultados = filtrar_por_continente(paises, continente_usuario)
            if not resultados:
                print(f"\nNo se encontraron países en el continente '{continente_usuario}'.") 
            else:
                print(f"\n✅ Se encontraron {len(resultados)} países:")
                for pais in resultados:
                    print(f"- {pais['nombre']} (Pob: {pais['poblacion']} | Sup: {pais['superficie']} km²)")
        elif filtro == 'poblacion':
            poblacion_maxima = int(input("\nIngrese la población máxima: "))
            poblacion_minima = int(input("Ingrese la población mínima: "))
            resultados = filtrar_por_poblacion(paises, poblacion_maxima, poblacion_minima)
            if not resultados:
                print(f"\nNo se encontraron países con una población entre {poblacion_minima} y {poblacion_maxima}.")
            else:
                print(f"\n✅ Se encontraron {len(resultados)} países:")
                for pais in resultados:
                    print(f"- {pais['nombre']} (Pob: {pais['poblacion']} | Sup: {pais['superficie']} km²)")
        elif filtro == 'superficie':
            superficie_maxima = int(input("\nIngrese la superficie máxima: "))
            superficie_minima = int(input("Ingrese la superficie mínima: "))
            resultados = filtrar_por_superficie(paises, superficie_maxima, superficie_minima)
            if not resultados:
                print(f"\nNo se encontraron países con una superficie entre {superficie_minima} y {superficie_maxima} km².")
            else:
                print(f"\n✅ Se encontraron {len(resultados)} países:")
                for pais in resultados:
                    print(f"- {pais['nombre']} (Pob: {pais['poblacion']} | Sup: {pais['superficie']} km²)")
    elif opcion == "7":
        pass
    elif opcion == "8":
        pass
    