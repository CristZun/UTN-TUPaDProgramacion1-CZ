#Trabajo Cooperativo numero 2
#Nombre: Daniel Andrés Fabre

#---------------------------------------------------------------------------------
#TP Listas de una dimensión
#---------------------------------------------------------------------------------


#Ejercicio Nro 2 con list comprehsion

lista = [input("Ingrese un numero: ") for x in range(5)]

mayor=max(lista)
menor=min(lista)

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}") 

#Ejercicio Nro 2 con bucle for

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(lista)
mayor=lista[0]
menor=lista[0]

for i in range(1,5):
    if lista[i]>mayor:
        mayor=lista[i]
    if lista[i]<menor:
        menor=lista[i]

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}") 

#Ejercicio Nr 4

print("Ingrese 5 numeros")
pares=0
impares=0

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))
    if lista[i]%2==0:
        pares+=1
    elif lista[i]%3==0:
        impares+=1

print(f"Hay {pares} numeros pares")
print(f"Hay {impares} numeros inpares")

#Ejercicio 4 con compresion de listas

numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))

 #Usar comprensión de listas para separar pares e impares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))


#Ejercicio Nro 6

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

lista_sin_duplicados=[]

for i in lista:

    if i not in lista_sin_duplicados:
        lista_sin_duplicados.append(i)

print(f"Lista sin duplicados: {lista_sin_duplicados}")

#Ejercicio nro 6 con funcion set

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

lista_sin_duplicados=[]

lista_sin_duplicados=list(set(lista))

print(lista_sin_duplicados)

#Ejercicio Nro 8
import random

lista=[random.randint(0, 10) for _ in range(10)]

vistos = set()
repetidos = set()

for elemento in lista:
    if elemento in vistos:
        repetidos.add(elemento)
    else:
        vistos.add(elemento)

print("Lista original:", lista)
print("Elementos repetidos:", list(repetidos))

#Ejercicio Nro 10

print("Ingrese 5 numeros")

lista=[]
for i in range(5):
    lista.append(float(input("Ingrese un numero: ")))

print(f"Lista ingresada: {lista}")

indice=int(input("Ingrese el indice del elemento a elimiar (0 a 5): "))

lista.pop(indice)

print(lista)

#Ejercicio Nro 12

lista1=list(range(0,10,2))
lista2=list(range(0,20,4))
lista_suma=[]

for i in range(5):
    lista_suma.append(lista1[i]+lista2[i])
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista SUMA: {lista_suma}")

#Ejercicio Nro 13

"""NumPy, o "Numerical Python", es una biblioteca de Python que sirve para realizar cálculos numéricos y científicos 
de alta eficiencia, especialmente con arreglos multidimensionales (arrays). Es fundamental en ciencia de datos, inteligencia 
artificial y machine learning, ya que permite manejar grandes volúmenes de datos y realizar operaciones matemáticas 
complejas de forma mucho más rápida y optimizada que con las listas de Python estándar. """
"""""
import numpy as np # Importamos la librería NumPy y la renombramos 'np'

# Creamos un array de Python
lista_python = [1, 2, 3, 4, 5]

# Convertimos la lista a un array de NumPy
array_numpy = np.array(lista_python)

# Realizamos una operación matemática (multiplicar cada elemento por 2)
resultado = array_numpy * 2

print(array_numpy)
print(resultado)

"""

#--------------------------------------------------------------------------------------------------------
#TP Listas Bidimensionales
#--------------------------------------------------------------------------------------------------------

#Ejercicio Nro 2

lista_bidimencional=[[1,2,3],[4,5,6],[7,8,9]]
suma=0

suma=sum(sum(fila) for fila in lista_bidimencional)

print(f"La suma de la lista bidimencional es: {suma}")

#Ejercicio 2 Otra forma con bucle anidado

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

 # Bucle anidado
for fila in matriz:
    for elemento in fila:
        suma += elemento

print("La suma de todos los elementos es:", suma)

#Ejercicio Nro 4

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(transpuesta)


#Ejercicio Nro 4 con un bucle anidado

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

filas = len(matriz)
columnas = len(matriz[0])

 # Crear matriz vacía para la transpuesta (columnas x filas)
transpuesta = []
for j in range(columnas):
    nueva_fila = []
    for i in range(filas):
        nueva_fila.append(matriz[i][j])
    transpuesta.append(nueva_fila)

print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

#Ejercicio Nro 6

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
escalar=(int(input("Ingrese el escalar: ")))
matris_por_escalar = [[matriz[i][j]*escalar for j in range(len(matriz))] for i in range(len(matriz[0]))]

print(f"La mastriz original es: {matriz}")
print(f"La matriz por el escalar es: {matris_por_escalar}")

#Ejercicio Nro 8

n=int(input("Ingrese el tamaño de la matriz: "))
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"La matriz identidad es: {identidad}")

#Ejercicio Nro 10

n=int(input("Ingrese el tamaño de la matriz nxn: "))
matriz = [[int(input(f"Ingrese un numero {i} {j} : ")) for j in range(n)] for i in range(n)]

transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(f"La matriz original es: {matriz}")
print(f"La matriz transpuesta es: {transpuesta}")

if transpuesta==matriz:
    print("La matriz es simétrica")
else:
    print("La matriz no es simetrica")