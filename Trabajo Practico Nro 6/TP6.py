
#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    print(f"Hola {nombre}¡")

nombre=input("Ingresa tu nombre: ")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados

def informacion_personal(nombre, apellido, edad, residencia):

    print(f"Soy {nombre}{apellido}, tengo {edad} años y vivo en {residencia}")

print("Ingresa tus datos")
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
edad=int(input("Ingresa tu edad: "))
residencia=input("Ingresa tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
       
       return math.pi*(radio)**2



def calcular_perimetro_circulo(radio):
       
       return 2*math.pi*radio

radio=float(input("Ingrese el radio del circulo: "))

print(f"El area es: {calcular_area_circulo(radio)}")
print(f"El perimetro es: {calcular_perimetro_circulo(radio)}")

#5Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

def segundos_a_horas(segundos):

    return segundos/60/60

segundos=int(input("Ingrese los segundos: "))
print(f"Son {segundos_a_horas(segundos)} horas ")

#6 Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción

def tabla_multiplicar(numero):

    for i in range(1,10):
        print(f"{numero}x{i}={i*numero}")

numero=int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#7Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara

def operaciones_basicas(a, b):
   suma=a+b
   resta=a-b
   division=a/b
   multiplicacion=a*b
   
   return suma,resta,division, multiplicacion

print("Ingrese 2 numeros")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: ")) 

print(operaciones_basicas(numero1,numero2))

#8 Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    
    return peso/(altura*altura)

print("Calculadora de iMC")
peso=float(input("Ingresa tu peso: "))
altura=float(input("Ingresa tu estatura: "))

print(f"Tu IMC es: {calcular_imc(peso,altura)}")

#9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función

def celsius_a_fahrenheit(celsius):
    F = (celsius * 9/5) + 32

    return F

temperatura=int(input("Ingrese los grados celsius: "))
print(f"Son {celsius_a_fahrenheit(temperatura)} grados Fahrenheit")

#10 Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

def calcular_promedio(a, b, c):

    return (a+b+c)/3

print("Ingrese 3 numeros para calcular el promedio")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

print(f"El promedio es: {calcular_promedio(numero1,numero2,numero3)}")