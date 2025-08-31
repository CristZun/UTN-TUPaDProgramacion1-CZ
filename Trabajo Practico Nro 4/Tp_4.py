#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
numeroSinSigno= abs(numero)  #abs sirve para sacarle el signo a los numeros
contador = 0

if numeroSinSigno == 0:  #verificamos excepcion de 0
    contador = 1
else:
    
    while numeroSinSigno > 0: 
        numeroSinSigno //= 10   # // divide y descarta el decimal, borrando el ultimo numero y sumando contador 1
        contador += 1

print(f"El número {numero} tiene {contador} dígito(s).")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = 0

if numero1 > numero2:  #el codigo no me funcionaba si el primer numero era mas grande, aplicamos intercambio de variables
    temp = numero1
    numero1 = numero2
    numero2 = temp

for i in range(numero1 + 1, numero2): #sumamos
    suma += i

print(f"La suma de los números entre {numero1} y {numero2} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

print("Ingrese números enteros. Ingrese 0 para detener el programa.")
total = 0

while True:  # bucle infinito, se detiene con un break
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break  # salimos del bucle cuando el usuario ingresa 0
    total += numero  # sumamos 

print(f"El total acumulado es: {total}")
   

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeroRandom =random.randint(0, 9) #numero aleatorio
intento = 0
print("adivina un número entre 0 y el 9")
print(numeroRandom) #solo es para ver cual es el random y probar el codigo

while True: #bucle infinito, se detiene con un break
    numero_usuario = int(input("ingrese su numero "))
    intento +=1  #suma intentos
    if numeroRandom == numero_usuario:  #verifica el numero
        print(f"Adivinaste el numero en el intento N° {intento}")
        break
    else:
        print("No es correcto, intenta nuevamente")
        
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100,1,-2): #segui la consigna tal cual, entiendo que otra forma mas "correcta" seria con un if numero % 2 == 0: y cambiar unos valores del for
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i 

print(f"La suma de los números de 0 a {numero} es: {suma}")  

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_par = 0
num_impares = 0
num_pos = 0
num_neg = 0

for contador in range(100): 
    num_usuar = int(input(f"Ingrese el número {contador+1}: "))

    if num_usuar > 0:
        num_pos += 1
    elif num_usuar < 0:
        num_neg += 1

    if num_usuar != 0:
        if num_usuar % 2 == 0:
            num_par += 1
        else:
            num_impares += 1
    if num_usuar == 0: #Es para no tener que ingresar si o si los 100 num y verificar si funciona el codigo
        break

print(f"Hay {num_par} números PARES")
print(f"Hay {num_impares} números IMPARES")
print(f"Hay {num_pos} números POSITIVOS")
print(f"Hay {num_neg} números NEGATIVOS")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma=0
contador=0
for i in range(100): 
    num_usuar = int(input(f"Ingrese el número {i+1}: "))
    suma= suma+ num_usuar
    contador+=1
    if num_usuar == 0: #Es para no tener que ingresar si o si los 100 num y verificar si funciona el codigo
        break 
    
media = suma / contador

print(f"La media de los {contador} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero != 0:
    digito = numero % 10        #devuelve el resto (ultimo digito)    
    numero_invertido = numero_invertido * 10 + digito #lo ubica en la posicion que corresponde con el *10
    numero = numero // 10       #elimina el numero original , sino es un bucle infinito    

print(f"El número invertido es: {numero_invertido}")