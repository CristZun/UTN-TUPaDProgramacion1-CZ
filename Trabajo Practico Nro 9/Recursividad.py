# Ejercicio 1: Factorial
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)

limite = int(input("Ingrese un número: "))

for valor in range(1, limite + 1):
    print(f"El factorial de {valor} es: {calcular_factorial(valor)}")


# Ejercicio 2: Fibonacci
def serie_fibonacci(pos):
    if pos <= 1:
        return pos
    else:
        return serie_fibonacci(pos - 1) + serie_fibonacci(pos - 2)

longitud = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))

for indice in range(longitud + 1):
    print(f"{serie_fibonacci(indice)},", end="")


# Ejercicio 3: Potencia recursiva
def calcular_potencia(num, exp):
    if exp == 0:
        return 1
    else:
        return num * calcular_potencia(num, exp - 1)

base_valor = int(input("\nIngrese la base: "))
exponente_valor = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base_valor, exponente_valor)
print(f"{base_valor} elevado a la {exponente_valor} es: {resultado}")


# Ejercicio 4: Conversión a binario (recursivo)
def a_binario(n):
    if n < 2:
        return str(n)
    else:
        return a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número para convertirlo a binario: "))
print(f"El número {numero_decimal} en binario es: {a_binario(numero_decimal)}")


# Ejercicio 5: Palíndromo
def verificar_palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] == texto[-1]:
        return verificar_palindromo(texto[1:-1])
    else:
        return False

cadena = input("Ingrese una palabra: ").lower()

if verificar_palindromo(cadena):
    print("Es palíndromo")
else:
    print("No es palíndromo")


# Ejercicio 6: Suma de dígitos
def sumar_digitos(num):
    num = abs(num)
    if num == 0:
        return 0
    else:
        return (num % 10) + sumar_digitos(num // 10)

valor_num = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"La suma de los dígitos es: {sumar_digitos(valor_num)}")


# Ejercicio 7: Contar bloques
def total_bloques(niveles):
    if niveles == 0:
        return 0
    else:
        return niveles + total_bloques(niveles - 1)

niveles_torre = int(input("Ingrese la cantidad de niveles: "))
print(f"Total de bloques necesarios: {total_bloques(niveles_torre)}")


# Ejercicio 8: Contar ocurrencias de un dígito
def contar_ocurrencias(num, buscado):
    num = abs(num)
    if num == 0:
        return 0
    elif num % 10 == buscado:
        return 1 + contar_ocurrencias(num // 10, buscado)
    else:
        return contar_ocurrencias(num // 10, buscado)

numero_principal = int(input("Ingrese un número: "))
digito_buscado = int(input("Ingrese el dígito que desea contar: "))

print(f"El dígito {digito_buscado} aparece {contar_ocurrencias(numero_principal, digito_buscado)} veces.")
