"""
| Función                 | Descripción                                       | Ejemplo                            |
| ----------------------- | ------------------------------------------------- | ---------------------------------- |
| `len(lista)`            | Devuelve la cantidad de elementos                 | `len([1,2,3]) → 3`                 |
| `sum(lista)`            | Devuelve la suma de los elementos (numéricos)     | `sum([1,2,3]) → 6`                 |
| `max(lista)`            | Devuelve el mayor valor                           | `max([1,4,2]) → 4`                 |
| `min(lista)`            | Devuelve el menor valor                           | `min([1,4,2]) → 1`                 |
| `sorted(lista)`         | Devuelve una **nueva lista** ordenada             | `sorted([3,1,2]) → [1,2,3]`        |
| `list(objeto_iterable)` | Convierte un iterable en lista                    | `list("hola") → ['h','o','l','a']` |
| `any(lista)`            | Devuelve True si **algún elemento es True**       | `any([0,0,1]) → True`              |
| `all(lista)`            | Devuelve True si **todos los elementos son True** | `all([1,2,3]) → True`              |


| Método             | Descripción                                                | Ejemplo                           |
| ------------------ | ---------------------------------------------------------- | --------------------------------- |
| `append(x)`        | Agrega un elemento al final                                | `[1,2].append(3) → [1,2,3]`       |
| `extend(iterable)` | Agrega varios elementos                                    | `[1,2].extend([3,4]) → [1,2,3,4]` |
| `insert(i, x)`     | Inserta un elemento en el índice `i`                       | `[1,2].insert(1,99) → [1,99,2]`   |
| `remove(x)`        | Elimina la **primera aparición** de `x`                    | `[1,2,2,3].remove(2) → [1,2,3]`   |
| `pop(i=-1)`        | Elimina y devuelve el elemento en `i` (último por defecto) | `[1,2,3].pop() → 3`               |
| `index(x)`         | Devuelve la posición de la primera aparición de `x`        | `[1,2,3].index(2) → 1`            |
| `count(x)`         | Devuelve cuántas veces aparece `x`                         | `[1,2,2].count(2) → 2`            |
| `sort()`           | Ordena la lista **modificándola**                          | `lista.sort()`                    |
| `reverse()`        | Invierte la lista **modificándola**                        | `[1,2,3].reverse() → [3,2,1]`     |
| `copy()`           | Devuelve una copia superficial de la lista                 | `nueva = lista.copy()`            |
| `clear()`          | Elimina todos los elementos de la lista                    | `lista.clear()`                   |
  
    """

#1Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
#suma de todos los elementos en la lista.

entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [float(x) for x in entrada.split()] #split, separa la cadena en partes dividido por espacios y los ingresa en una lista

promedio = sum(numeros)

print("La suma de los elementos es:", promedio)

#3Escribe un programa que permita al usuario ingresar una lista y la invierta.

entrada = input("Ingrese los elementos de la lista separados por espacios: ")

lista = entrada.split()

lista.reverse()

print("La lista invertida es:", lista)

#5Escribe un programa que multiplique cada elemento de una lista de números por un 
#valor ingresado por el usuario. 

entrada = input("Ingrese una lista de números separados por espacios: ")

lista = [float(x) for x in entrada.split()]

multiplicador = float(input("Ingrese el valor por el cual quiere multiplicar: "))

resultado = [num * multiplicador for num in lista]

print("La lista resultante es:", resultado)

#7Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
#promedio de los elementos. 

entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [float(x) for x in entrada.split()] #split, separa la cadena en partes dividido por espacios y los ingresa en una lista
cant_numeros= len(numeros)

promedio = sum(numeros)/cant_numeros

print("La suma de los elementos es:", promedio)

#9Escribe un programa que permita al usuario ingresar una lista de números y filtre los 
#números primos. 
#Pista: Usa una función para verificar si un número es primo.

""" lista por compresion

[nuevo_elemento for elemento in iterable if condición]

*elemento in iterable → recorre cada elemento de la lista original.

*if condición → filtra los elementos según una condición.

*nuevo_elemento → decide qué se pone en la nueva lista.

"""

#Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos():
    entrada = input("Ingresa una lista de números separados por espacios: ")
    numeros = list(map(int, entrada.split())) #funcion que cambia valor por valor de la lista en este caso un int
    primos = [num for num in numeros if es_primo(num)]

    print("Números primos en la lista:", primos)

# Ejecutamos la función
filtrar_primos()

#11Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
#cuántas veces aparece ese número en la lista. 

entrada = input("Ingresa una lista de números separados por espacios: ")
lista = list(map(int, entrada.split()))

numero = int(input("Ingresa el número a contar en la lista: "))

cantidad = lista.count(numero)

print(f"El número {numero} aparece {cantidad} veces en la lista.")

#TP Listas Bidimensionales
import numpy as np 

"""
Creación de arreglos
| Función                                               | Descripción                                                            |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| `np.array([1,2,3])`                                   | Crea un arreglo a partir de una lista o tupla.                         |
| `np.zeros((filas, columnas))`                         | Matriz llena de ceros.                                                 |
| `np.ones((filas, columnas))`                          | Matriz llena de unos.                                                  |
| `np.arange(inicio, fin, paso)`                        | Arreglo de números consecutivos con un paso definido.                  |
| `np.linspace(inicio, fin, num)`                       | Arreglo de `num` valores igualmente espaciados entre `inicio` y `fin`. |
| `np.eye(n)`                                           | Matriz identidad de tamaño `n x n`.                                    |
| `np.random.rand(filas, columnas)`                     | Matriz con valores aleatorios entre 0 y 1.                             |
| `np.random.randint(min, max, size=(filas, columnas))` | Matriz con enteros aleatorios dentro de un rango.                      |

Propiedades de arreglos
| Propiedad | Descripción                                   |
| --------- | --------------------------------------------- |
| `.shape`  | Dimensiones del arreglo `(filas, columnas)`.  |
| `.size`   | Número total de elementos.                    |
| `.dtype`  | Tipo de datos del arreglo (int, float, etc.). |
| `.ndim`   | Número de dimensiones.                        |

Operaciones matemáticas
| Función / Método              | Descripción                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| `np.sum(arr)`                 | Suma todos los elementos.                                     |
| `np.sum(arr, axis=0/1)`       | Suma por columnas (`axis=0`) o filas (`axis=1`).              |
| `np.mean(arr)`                | Media aritmética de los elementos.                            |
| `np.min(arr)` / `np.max(arr)` | Valor mínimo / máximo.                                        |
| `np.sqrt(arr)`                | Raíz cuadrada de cada elemento.                               |
| `np.exp(arr)`                 | Exponencial de cada elemento.                                 |
| `np.dot(a, b)`                | Producto punto entre arreglos/matrices.                       |
| `arr + 2`, `arr * 3`          | Operaciones element-wise (sumar/multiplicar a cada elemento). |

Indexación y selección
| Función / Sintaxis | Descripción                                            |
| ------------------ | ------------------------------------------------------ |
| `arr[0]`           | Primer elemento de un arreglo 1D o primera fila de 2D. |
| `arr[:,0]`         | Primera columna de una matriz 2D.                      |
| `arr[1:3]`         | Subarreglo desde índice 1 hasta 2.                     |
| `arr[arr > 5]`     | Filtrado booleano (elementos mayores a 5).             |

Transformación y reestructuración
| Función                           | Descripción                                |
| --------------------------------- | -------------------------------------------|
| `.reshape(filas, columnas)`       | Cambia la forma del arreglo.               |
| `.flatten()`                      | Convierte un arreglo 2D o más en 1D.       |
| `np.transpose(arr)` o `arr.T`     | Transpone la matriz (filas ↔ columnas).    |
| `np.concatenate((a,b), axis=0/1)` | Une arreglos por filas o columnas.         |
| `np.stack((a,b), axis=0/1)`       | Apila arreglos en una nueva dimensión.     |
| `np.fliplr()`                     | “voltea” la matriz de izquierda a derecha  |
| `np.identity()`                   | Crea una matriz identidad normal (1 en la diagonal principal). |

Otras funciones útiles
| Función                                                  | Descripción                                        |
| -------------------------------------------------------- | -------------------------------------------------- |
| `np.unique(arr)`                                         | Devuelve los elementos únicos de un arreglo.       |
| `np.sort(arr)`                                           | Ordena los elementos.                              |
| `np.argsort(arr)`                                        | Devuelve los índices que ordenarían el arreglo.    |
| `np.where(condición)`                                    | Devuelve los índices donde se cumple la condición. |
| `np.copy(arr)`                                           | Crea una copia del arreglo.                        |
| `np.save('archivo.npy', arr)` / `np.load('archivo.npy')` | Guardar / cargar arreglos en archivos.             |



"""
#1Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
#debe generar una matriz de ese tamaño, donde los valores son números enteros 
#consecutivos empezando desde 1. 

def generar_matriz(filas, columnas):
    # np.arange genera números consecutivos desde 1 hasta filas*columnas
    # reshape organiza esos números en una matriz de tamaño filas x columnas
    matriz = np.arange(1, filas * columnas + 1).reshape(filas, columnas)
    return matriz
filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

resultado = generar_matriz(filas, columnas)
print(resultado)

#3Modifica el programa anterior para que imprima la suma de cada fila de la lista 
#bidimensional.

lista_bidimencional = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

suma_total = np.sum(lista_bidimencional)
print(f"La suma total es: {suma_total}")

#Suma por filas (axis=1 significa sumar en las columnas de cada fila)
suma_filas = np.sum(lista_bidimencional, axis=1)
for i, suma in enumerate(suma_filas, start=1):
    print(f"La suma de la fila {i} es: {suma}")

#5Escribe un programa que encuentre el valor más grande en una lista bidimensional.

lista_bidimencional = np.array([
    [1, 2, 3],
    [10, 5, 6],
    [7, 8, 9]])

#Encontrar el valor máximo
maximo = np.max(lista_bidimencional)
print(f"El valor más grande en la lista bidimensional es: {maximo}")

#7Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
#cuadrada. 

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

#Extraer la diagonal principal
diagonal = np.diag(matriz)

print(f"La matriz es:\n{matriz}")
print(f"La diagonal principal es: {diagonal}")

#9Crea un programa que genere una matriz identidad inversa de tamaño n. 

n = int(input("Ingrese el tamaño de la matriz identidad inversa: "))

# Generar matriz identidad inversa
matriz_identidad_inversa = np.fliplr(np.identity(n, dtype=int))

print("La matriz identidad inversa es:")
print(matriz_identidad_inversa)

#11Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido 
#de las agujas del reloj.

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

# Rotar 90° en sentido de las agujas del reloj k=-1 → 90° clockwise k=1 rota 90 antihorario
matriz_rotada = np.rot90(matriz, k=-1)  

print("Matriz original:")
print(matriz)
print("\nMatriz rotada 90° en sentido horario:")
print(matriz_rotada)