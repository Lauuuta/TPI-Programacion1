#Funciones base
def agregar_pais(paises):
    sobreescribir = ""
    nombre = input("Nombre del país: ")
    while nombre.strip() == "":
        nombre = input("Ingrese un nombre valido: ")
    pais_existente = buscar_pais(paises,nombre)
    if not pais_existente == None:
        print("¡El pais ya se encuentra en la lista!")
        sobreescribir = input("¿Desea sobreescribirlo? (Si / No) : ").lower()
        while not sobreescribir == "si" and not sobreescribir == "no":
            sobreescribir = input("Ingrese una respuesta valida: ")
    if sobreescribir == "" or sobreescribir == "si":
        while True:
            try:
                poblacion = int(input("Población: "))
                if poblacion < 0:
                    print("La población no puede ser negativa. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("El valor ingresado no es valido. Intente nuevamente")
        while True:
            try:
                superficie = float(input("Superficie: "))
                if superficie < 0:
                    print("La superficie no puede ser negativa. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("El valor ingresado no es valido. Intente nuevamente")
        if sobreescribir == "":
            continente = input("Continente: ")
            while continente.strip() == "":
                continente = input("Ingrese un nombre valido: ")
            pais = {
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            }
            paises.append(pais)
        else:
            pais_existente["nombre"] = nombre
            pais_existente["poblacion"] = poblacion
            pais_existente["superficie"] = superficie
            pais_existente["continente"] = continente
    else:
        print("Operación cancelada")
        return


def buscar_pais(paises, nombre):
    if len(paises) == 0:
        return None

    for pais in paises:
        if  pais["nombre"].lower() == nombre.lower():
            return pais
    return None

def actualizar_poblacion_superficie_pais(paises):
    nombre = input("Nombre del pais: ")
    while nombre.strip() == "":
        nombre = input("Ingrese un nombre valido: ")
    pais_existente = buscar_pais(paises, nombre)
    if pais_existente == None:
        print("El pais ingresado no existe.")
        return

    while True:
        try:
            poblacion = int(input("Población: "))
        except ValueError:
            print("El valor ingresado no es valido. Intente nuevamente")
            continue
        if poblacion<0:
            print("La poblacion no puede ser negativa. Intente nuevamente")
            continue
        else:
            break
    while True:
        try:
            superficie = float(input("Superficie: "))
        except ValueError:
            print("El valor ingresado no es valido. Intente nuevamente")
            continue
        if superficie<0:
            print("La superficie no puede ser negativa. Intente nuevamente")
            continue
        else:
            break

    pais_existente["poblacion"] = poblacion
    pais_existente["superficie"] = superficie

def filtrar_por_continente(lista, continente):
    paises_filtrados = []
    for pais in lista:
        if pais['continente'].lower() == continente.lower():
            paises_filtrados.append(pais)
    return paises_filtrados
def filtrar_por_poblacion(lista, maxima, minima):
    paises_filtrados = []
    for pais in lista:
        if minima <= pais['poblacion'] <= maxima    :
            paises_filtrados.append(pais)
    return paises_filtrados
def filtrar_por_superficie(lista, maxima, minima):
    paises_filtrados = []
    for pais in lista:
        if minima <= pais['superficie'] <= maxima:
            paises_filtrados.append(pais)
    return paises_filtrados

def ordenar_por_paises(lista, criterio, descendente=False):
    descendente = descendente if isinstance(descendente, bool) else False
    criterio_limpio = criterio.strip().lower()
    if criterio_limpio not in ['nombre', 'poblacion', 'superficie']:
        print("Criterio de ordenación no válido. Se ordenará por nombre de forma ascendente.")
        return lista 
    return sorted(lista, key=lambda x: x[criterio_limpio], reverse=descendente)
