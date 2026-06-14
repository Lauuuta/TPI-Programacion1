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
                break
            except ValueError:
                print("El valor ingresado no es valido. Intente nuevamente")
        while True:
            try:
                superficie = int(input("Superficie: "))
                break
            except ValueError:
                print("El valor ingresado no es valido. Intente nuevamente")
        continente = input("Continente: ")
        while continente.strip() == "":
            continente = input("Ingrese un nombre valido: ")
        if sobreescribir == "":
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
    for pais in paises:
        if pais["nombre"].title() == nombre.title():
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
            superficie = int(input("Superficie: "))
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

#Funciones para ordenar paises
def ordenar_por_nombre():
    pass

def ordenar_por_poblacion():
    pass

def ordenar_por_superficie():
    pass