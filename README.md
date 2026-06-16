** Trabajo Practico Integrador -- Programación 1**
Tecnicatura Universitaria en Programación - UTN 

La aplicación consiste en la gestión informacion sobre países: Permite agregar, buscar, filtrar, ordenar y obtener estadísticas a partir de un archivo CSV.

Intregrantes 
Flores Alejo - DNI: 44785707
Delgadillo Lautaro - DNI: 45543682

Instruciones 
Para ejecutar el programa se debe correr el archivo main.py

Opciones del menu:
1. Agregar un nuevo país
2. Actualizar datos de población o superficie
3. Buscar un país por nombre
4. Filtrar países (por continente, población o superficie)
5. Ordenar países (por nombre, población o superficie)
6. Estadísticas
7. Salir

Estructura 
TPI-Programacion1/
    -main.py: menú principal y punto de inicio del programa 
    -funciones.py: lógica de búsqueda, filtros y ordenamiento 
    -archivos.py: lectura y escritura del CSV
    -estadisticas.py: cálculos de estadísticas 
    -paises.csv: archivos con los datos 

Ejemplos de funcionalidades 
** Buscar un pais por su numbre 
    Ingrese el nombre del país a buscar: argentina
    ✅ País encontrado: Argentina
** Filtrar por continente, poblacion o superficie 
    por continente 
    Ingrese el continente a filtrar: asia 
    ✅ Se encontraron 1 países:
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    por poblacion
    Ingrese la población mínima: 45376760
    Ingrese la población máxima: 45376770
    ✅ Se encontraron 1 países:
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    por superficie 
    Ingrese la superficie mínima: 85157660
    Ingrese la superficie máxima: 85157680
    ✅ Se encontraron 1 países:
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
**Ordenar por nombre, población o superficie
    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): nombre
    ¿Desea ordenar de forma descendente? (si/no): si
    ✅ Países ordenados por nombre en forma descendente
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
    - Australia (Pob: 25690000 | Sup: 76920240 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)

    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): nombre
    ¿Desea ordenar de forma descendente? (si/no): no
    ✅ Países ordenados por nombre en forma ascendente
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Australia (Pob: 25690000 | Sup: 76920240 km²)
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)

    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): poblacion
    ¿Desea ordenar de forma descendente? (si/no): si
    ✅ Países ordenados por poblacion en forma descendente
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Australia (Pob: 25690000 | Sup: 76920240 km²)

    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): poblacion
    ¿Desea ordenar de forma descendente? (si/no): no

    ✅ Países ordenados por poblacion en forma ascendente
    - Australia (Pob: 25690000 | Sup: 76920240 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)

    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): superficie 
    ¿Desea ordenar de forma descendente? (si/no): si
    ✅ Países ordenados por superficie en forma descendente
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
    - Australia (Pob: 25690000 | Sup: 76920240 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)

    Ingrese el criterio por el cual desea ordenar (nombre, poblacion, superficie): superficie
    ¿Desea ordenar de forma descendente? (si/no): no
    ✅ Países ordenados por superficie en forma ascendente
    - Alemania (Pob: 83149300 | Sup: 3570220 km²)
    - Japon (Pob: 125800000 | Sup: 3779750 km²)
    - Sudafrica (Pob: 59308000 | Sup: 12210370 km²)
    - Argentina (Pob: 45376763 | Sup: 27804000 km²)
    - Australia (Pob: 25690000 | Sup: 76920240 km²)
    - Brasil (Pob: 213993437 | Sup: 85157670 km²)
**Estadisticas 
    Estadísticas disponibles:
    1. País con mayor población
    2. País con menor población
    3. Promedio de población
    4. Promedio de superficie
    Ingrese el número de la estadística que desea ver: 1
    El pais con mayor poblacion es: Brasil con 213993437 habitantes.

    Ingrese el número de la estadística que desea ver: 2
    El paiscon menor poblacion es: Australia con 25690000 habitantes.

    Ingrese el número de la estadística que desea ver: 3
    El promedio de la poblacion es de 92219583.33333333 habitantes. 

    Ingrese el número de la estadística que desea ver: 4
    El promedio de la superficie es de 34907041.666666664 km².