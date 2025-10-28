from pathlib import Path
base = Path(__file__).parent
direccion = base / "productos.txt"

# Ejercicio 2
with open(direccion, "r") as archivo:
    for linea in archivo:
        partes = linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")


# Ejercicio 3
with open(direccion, "r") as archivo:
    for linea in archivo:
        partes = linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")

print("Ingrese un nuevo producto")
nombre = input("Ingrese el nombre: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

with open(direccion, "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")


# Ejercicio 4
with open(direccion, "r") as archivo:
    for linea in archivo:
        partes = linea.split(",")
        print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")

print("Ingrese un nuevo producto")
nombre = input("Ingrese el nombre: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

with open(direccion, "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

with open(direccion, "r") as archivo:
    productos = []
    for linea in archivo:
        almacen = linea.split(",")
        productos.append({
            "nombre": almacen[0].strip(),
            "precio": almacen[1].strip(),
            "cantidad": almacen[2].strip()
        })

print(productos)


# Ejercicio 5
with open(direccion, "r") as archivo:
    buscar = input("Ingrese un producto para buscarlo: ")
    producto_encontrado = False

    for linea in archivo:
        if buscar.lower() in linea.lower():
            partes = linea.split(",")
            print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")
            producto_encontrado = True

    if not producto_encontrado:
        print("Error, producto no encontrado")


# Ejercicio 6
def crear_lista():
    productos = []
    with open(direccion, "r") as archivo:
        for linea in archivo:
            almacen = linea.split(",")
            productos.append({
                "nombre": almacen[0].strip(),
                "precio": almacen[1].strip(),
                "cantidad": almacen[2].strip()
            })
    return productos


def actualizar_productos(productos):
    with open(direccion, "w") as archivo:
        for filas in productos:
            temporal = list(filas.values())
            archivo.write(",".join(map(str, temporal)) + "\n")


def mostrar_archivo():
    with open(direccion, "r") as archivo:
        for linea in archivo:
            partes = linea.split(",")
            print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")


def agregar_producto():
    print("Ingrese un nuevo producto")
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    with open(direccion, "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")


def buscar_producto():
    with open(direccion, "r") as archivo:
        buscar = input("Ingrese un producto para buscarlo: ")
        producto_encontrado = False

        for linea in archivo:
            if buscar.lower() in linea.lower():
                partes = linea.split(",")
                print(f"Producto: {partes[0].strip()} | precio: ${partes[1].strip()} | Cantidad: {partes[2].strip()}")
                producto_encontrado = True

        if not producto_encontrado:
            print("Error, producto no encontrado")


# Programa principal (menú)
crear_lista()
menu = False

while not menu:
    opcion = int(input("\n1- Mostrar Archivo  2-Agregar Producto  3-Buscar Producto  4-Salir\n"))
    if opcion == 1:
        mostrar_archivo()
        actualizar_productos(crear_lista())

    elif opcion == 2:
        agregar_producto()
        actualizar_productos(crear_lista())

    elif opcion == 3:
        buscar_producto()
        actualizar_productos(crear_lista())

    elif opcion == 4:
        menu = True
    else:
        print("Opción incorrecta, intente nuevamente.")
