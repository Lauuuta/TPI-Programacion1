from archivos import cargar_csv, guardar_csv
def test_cargar_csv():
    ruta = 'paises.csv'
    print("Probando cargar_csv...")
    paises = cargar_csv(ruta)
    print("Paises cargados:")
    for pais in paises:
        print(pais)

if __name__ == "__main__":
    test_cargar_csv()