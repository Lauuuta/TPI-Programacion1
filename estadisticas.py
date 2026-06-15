#Funciones estadisticas paises
def pais_mayor_poblacion(paises):
    if len(paises) == 0:
        print("No se ingresaron paises.")
        return
    
    pais_max_poblacion = paises[0]["nombre"]
    cantidad_poblacion = paises[0]["poblacion"]

    for pais in paises[1:]:
        if pais["poblacion"] > cantidad_poblacion:
            pais_max_poblacion = pais["nombre"]
            cantidad_poblacion = pais["poblacion"]
        
    print(f"El pais con mayor poblacion es: {pais_max_poblacion} con {cantidad_poblacion} habitantes.")

def pais_menor_poblacion(paises):
    if len(paises) == 0:
        print("No se ingresaron paises.")
        return
    pais_min_poblacion = paises[0]["nombre"]
    cantidad_poblacion = paises[0]["poblacion"]

    for pais in paises[1:]:
        if pais["poblacion"] < cantidad_poblacion:
            pais_min_poblacion = pais["nombre"]
            cantidad_poblacion = pais["poblacion"]
        
    print(f"El pais con menor poblacion es: {pais_min_poblacion} con {cantidad_poblacion} habitantes.")

def promedio_poblacion(paises):
    if len(paises) == 0:
        print("No se ingresaron paises.")
        return
    
    acumulador_poblacion = 0
    contador_paises = 0
    
    for pais in paises:
        acumulador_poblacion+=pais["poblacion"]
        contador_paises+=1
    promedio = acumulador_poblacion / contador_paises
    print(f"El promedio de la poblacion es de {promedio} habitantes.")

def promedio_superficie(paises):
    if len(paises) == 0:
        print("No se ingresaron paises.")
        return
    
    acumulador_superficie = 0
    contador_paises = 0
    
    for pais in paises:
        acumulador_superficie+=pais["superficie"]
        contador_paises+=1
    promedio = acumulador_superficie / contador_paises
    print(f"El promedio de la superficie es de {promedio} km².")