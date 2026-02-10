
import os
from Articulo import Articulo
from DetalleFactura import DetalleFactura
from Factura import Factura


articulos_data = {} # Diccion
lista_fact = []     # Lista de obj


def leer_articulos_venta():
    try:
        print("Cargando base de datos de artículos...")
        with open('articulos_venta.txt', 'r') as file:
            file.readline() 
            for linea in file:
                datos = [d.strip() for d in linea.strip().split(';')]
                if len(datos) == 5:
                    try:
                        articulo = Articulo(datos[0], datos[1], datos[2], datos[3], datos[4])
                        articulos_data[articulo.codigo] = articulo
                    except ValueError:
                        print(f"Error de formato en línea, saltando: {linea.strip()}")
                else:
                    print(f"Línea con formato incorrecto, saltando: {linea.strip()}")
        print(f"Carga completa. {len(articulos_data)} artículos cargados.")
    except FileNotFoundError:
        print("El archivo 'articulos_venta.txt' no se encontró.")
        exit() 
    except Exception as e:
        print(f"Ocurrió un error durante la lectura del archivo: {e}")
        exit()


def ver_facturas_cargadas():
    print("\n--FACTURAS CARGAAS--")
    if not lista_fact:
        print("No hay facturas cargadas en la lista.")
        return

    for factura in lista_fact:
        print(factura)
    print("-" * 30)


def cargar_detalle_factura(articulo_db):
    lista_detalles_nueva_factura = []
    ingresar_nuevo_detalle = 'S'
    primer_detalle_ingresado = False

    while ingresar_nuevo_detalle.upper() == 'S':
        print("\n--- Carga de Detalle ---")
        
        
        while True:
            try:
                codigo = int(input("Ingrese Código del Artículo (o '0' para cancelar detalle): "))
                if codigo == 0:
                    brea 
                if codigo in articulo_db:
                    articulo_seleccionado = articulo_db[codigo]
                    print(f"Artículo: {articulo_seleccionado.denominacion}")
                    break
                else:
                    print(" El código de artículo no existe. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número para el código")
        if codigo == 0:
            if primer_detalle_ingresado:
                ingresar_nuevo_detalle = input("¿Dese cargar otro detalle? S/N:").upper()
            continue
        while True:
            try:
                cantidad = int(input("Ingrese Cantidad mayor a cero "))
                if can
            