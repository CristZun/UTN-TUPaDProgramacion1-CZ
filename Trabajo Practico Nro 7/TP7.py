#Ejercicio 1 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3

# Crear lista con solo los nombres de las frutas
frutas = list(precios_frutas.keys())

print(frutas)

#Ejercicio 4

agenda = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

# Consultar un número por nombre
nombre_consulta = input("Ingrese el nombre del contacto a buscar: ")

if nombre_consulta in agenda:
    print(f"El número de {nombre_consulta} es {agenda[nombre_consulta]}")
else:
    print(f"No se encontró un contacto con el nombre {nombre_consulta}")

#Ejercicio 5

frase = input("Ingrese una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Palabras únicas usando un set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Contar la cantidad de veces que aparece cada palabra
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", conteo_palabras)

#Ejercicio 6

# Diccionario para almacenar alumnos y sus notas
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    # Pedir 3 notas separadas por espacio
    notas_input = input(f"Ingrese las 3 notas de {nombre}, separadas por espacio: ")
    
    # Convertir las notas a enteros y guardarlas como tupla
    notas = tuple(map(float, notas_input.split()))
    alumnos[nombre] = notas

# Calcular y mostrar promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")


#Ejercicio 7

# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Juan", "Luis", "Marta"}
parcial2 = {"Luis", "Marta", "Carlos", "Lucía"}

# 1. Estudiantes que aprobaron ambos parciales → intersección
ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)

# 2. Estudiantes que aprobaron solo uno de los dos → diferencia simétrica
solo_uno = parcial1 ^ parcial2
print("Aprobó solo uno de los parciales:", solo_uno)

# 3. Estudiantes que aprobaron al menos un parcial → unión
al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial:", al_menos_uno)

#Ejercicio 8

productos = {
    "Banana": 10,
    "Manzana": 15,
    "Naranja": 8
}

while True:
    print("\nOpciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Ingrese una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in productos:
            print(f"El stock de {producto} es {productos[producto]}")
        else:
            print(f"{producto} no existe en el inventario.")
            
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {productos[producto]}")
        else:
            print(f"{producto} no existe en el inventario.")
            
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in productos:
            print(f"{producto} ya existe. Usá la opción 2 para agregar unidades.")
        else:
            cantidad = int(input("Ingrese el stock inicial: "))
            productos[producto] = cantidad
            print(f"{producto} agregado con stock {cantidad}.")
            
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

#Ejercicio 9

# Agenda como diccionario, clave = (día, hora), valor = evento
agenda = {}

# Cargar algunos eventos
agenda[("Lunes", "10:00")] = "Reunión de trabajo"
agenda[("Martes", "15:00")] = "Clase de guitarra"
agenda[("Miércoles", "09:00")] = "Consulta médica"

# Consultar un evento
dia = input("Ingrese el día a consultar: ")
hora = input("Ingrese la hora a consultar (formato HH:MM): ")

clave = (dia, hora)
if clave in agenda:
    print(f"El evento a las {hora} del {dia} es: {agenda[clave]}")
else:
    print(f"No hay eventos programados a las {hora} del {dia}.")

#Ejercicio 10

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"}

capitales = {}


for pais in paises:
    capital = paises[pais]     
    capitales[capital] = pais  

print(capitales)

