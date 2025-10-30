#Trabajo Practico cooperativo Nro 1
#Nombre: Andrés Fabre

#Ejercicio Nro 2

"""""
En Python, asignar un valor fuera del rango definido de una variable causa un error específico del tipo de dato (por ejemplo, ValueError para caracteres o IndexError para listas), ya que no hay un límite nativo en la asignación de tipos numéricos. Para resolverlo, se debe validar la entrada del valor con condiciones if antes de la asignación, o manejar la posible excepción usando bloques try-except para capturar el error y actuar de manera controlada, evitando que el programa se detenga abruptamente. 
¿Qué ocurre?
No hay un error genérico de "rango" para todos los tipos de variables:
Python no impone un límite de rango para variables numéricas como enteros o flotantes; puedes asignar un número muy grande sin problema. 
Errores específicos:
Los errores ocurren cuando la asignación o el uso de ese valor viola las restricciones de un tipo de dato o estructura específica.
ValueError: Si intentas, por ejemplo, convertir un número a un carácter con chr() y este está fuera del rango de valores ASCII válidos, obtendrás este error. 
IndexError: Si intentas acceder o asignar a un índice de una lista o secuencia que no existe, te encontrarás con un IndexError. 
Otros errores: Dependiendo del contexto, otras funciones o operaciones pueden arrojar errores si un valor está fuera de sus rangos permitidos.
¿Cómo resolverlo? 
Validación de entrada (con if):
Comprobar límites: Usa operadores de comparación (>, >=, <, <=) para verificar si el valor está dentro del rango deseado antes de asignarlo o usarlo.
Ejemplo:
Python

        edad = -5
        if 0 <= edad <= 120:
            print(f"Edad válida: {edad}")
        else:
            print("La edad está fuera de rango.")
Manejo de excepciones (con try-except):
Capturar el error: Envuelve el código que podría generar el error en un bloque try y maneja el error específico en un bloque except. 
Ejemplo:
Python

        try:
            # Código que podría generar un error, por ejemplo, al asignar un índice fuera de rango
            mi_lista = [1, 2]
            print(mi_lista[3]) # Esto causará un IndexError
        except IndexError:
            print("Error: Índice de lista fuera de rango. Se manejará el error.")
            # Puedes asignar un valor por defecto, registrar el error, etc.
Uso de lógica condicional en el uso del valor:
Asegúrate de que la operación o función que recibe el valor pueda manejarlo, o realiza una conversión de tipo si es necesario. 
Ejemplo:
Python

        valor_potencial = "100000000000000000000" # Un número muy grande
        try:
            numero_entero = int(valor_potencial)
            print(f"Número asignado: {numero_entero}")
        except OverflowError:
            print("El valor es demasiado grande para un entero")
""" 

#Ejercicio Nro 4

class vuelto :

    def cambio(self, monto):

       billetes200=0
       billetes100=0
       billetes50=0
       billetes20=0
       billetes10=0
       billetes5=0
       billetes2=0
       billetes1=0
       monedas050=0
       monedas025=0
       monedas010=0
       monedas005=0

       
       while monto>=0.05:
           if monto>=200:
            billetes200=monto//200
            monto=round(monto%200,2)
           elif monto>=100:
            billetes100=monto//100
            monto=round(monto%100,2)
           elif monto>=50:
            billetes50=monto//50
            monto=round(monto%50,2)
           elif monto>=20:
            billetes20=monto//20
            monto=round(monto%20,2)
           elif monto>=10:
            billetes10=monto//10
            monto=round(monto%10,2)
           elif monto>=5:
            billetes5=monto//5
            monto=round(monto%5,2)
           elif monto>=2:
            billetes2=monto//2
            monto=round(monto%2,2)
           elif monto>=1:
            billetes1=monto//1
            monto=round(monto%1,2)
           elif monto>=0.50:
            monedas050=monto//0.50
            monto=round(monto%0.50,2)
           elif monto>=0.25:
            monedas025=monto//0.25
            monto=round(monto%0.25,2)
           elif monto>=0.10:
            monedas010=monto//0.10
            monto=round(monto%0.10,2)
           elif monto>=0.05:
            monedas005=monto//0.05
            monto=round(monto%0.05,2)

       print(f"""Usted necesita {billetes200} billetes de 200
             {billetes100} billetes de 100
             {billetes50} billetes de 50
             {billetes20} billetes de 20
             {billetes10} billetes de 10
             {billetes5} billetes de 5
             {billetes2} billetes de 2
             {billetes1} billetes de 1
             {monedas050} monedas de 0.5
             {monedas025} monedas de 0.25
             {monedas010} monedas de 0.10
             {monedas005} moendas de 0.05""")
       
vuelto1=vuelto()
pago=float(input("Ingrese el monto del pago: "))
vuelto1.cambio(pago)
               
#Ejercicio Nro 6

cadena="La lluvia en Mendoza es escasa"
palabras=cadena.split() #divide la cadena en una lista de palabras sin espacios
cadena_sin_espacios="".join(palabras) #unimos las palabras con "" para q no haya espacios entre ellas
tamaño=int(len(cadena_sin_espacios))
print(f"El tamaño es: {tamaño}")

#Ejercicio Nro 8

palabra=input("Ingrese una palabra: ")
nueva_palabra=palabra.replace("a","e")
print(f"La nueva palabra es: {nueva_palabra}")

#Ejercicio Nro 10

palabra=input("Ingrese una palabra: ")
menu=int(input("1-Mayusculas 2-Minusculas\n"))

if menu==1:
    nueva_palabra=palabra.upper()
elif menu==2:
    nueva_palabra=palabra.lower()
else:
    nueva_palabra="Error de Menu"

print(nueva_palabra)

#Ejercicio Nro 12

cadena="hipopotamo"
nueva_cadena=cadena[3:5]
print(nueva_cadena)

#Ejercicio Nro 14

"""
En Python, las variables no se pasan ni estrictamente por valor ni por referencia, sino por "asignación" o "paso por objeto". Esto significa que los argumentos pasados a una función son referencias a objetos en memoria. Si un objeto es inmutable (como los números o las tuplas), la asignación dentro de la función creará una nueva variable local y no afectará al original, similar al paso por valor. Sin embargo, si se pasa un objeto mutable (como las listas o diccionarios), las modificaciones dentro de la función sí se reflejarán en el objeto original, similar al paso por referencia. 
Conceptos clave
Inmutabilidad vs. Mutabilidad:
Los tipos de datos inmutables (como los enteros, flotantes, cadenas y tuplas) no se pueden cambiar después de su creación, mientras que los mutables (listas, diccionarios, conjuntos) sí pueden ser modificados. 
Objetos en memoria:
En Python, todo es un objeto. Las variables son nombres que apuntan a estos objetos. 
Asignación:
Cuando asignas una variable ( x = 10 ), estás haciendo que esa variable apunte a un objeto "10" en memoria. Cuando pasas x a una función, la función recibe una copia de esa referencia (una nueva variable local que apunta al mismo objeto). 

"""

#Ejercicio Nro 16

class palabra:

    def analizar_palabra(self, cadena):
        
        for caracter in cadena:
            if caracter.isdigit():
                salida=True
            else:
                salida=False
                
        print(salida)

palabra=palabra()
frase=input("Ingrese una palabra: ")
palabra.analizar_palabra(frase)

#Ejercicio Nro 18

from datetime import date

class FuncionesPrograma:

    @staticmethod

    def getFechaDate(anio,mes,dia):
        
        return date(anio,mes,dia)
    
print("Ingrese una fecha")

dia=int(input("Ingrese el dia: "))
mes=int(input("Ingrese el mes: "))
anio=int(input("Ingrese el año: "))

fecha=FuncionesPrograma.getFechaDate(anio,mes,dia)
print(fecha)

#Ejercicio Nro 20

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


class OperacionesFraccion:
    @staticmethod
    def main():
        n1 = int(input("Numerador 1: "))
        d1 = int(input("Denominador 1: "))
        n2 = int(input("Numerador 2: "))
        d2 = int(input("Denominador 2: "))

        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)

        print("Suma:", Fraccion.sumarFracciones(f1, f2))
        print("Resta:", Fraccion.restarFracciones(f1, f2))
        print("Multiplicación:", Fraccion.multiplicarFracciones(f1, f2))
        print("División:", Fraccion.dividirFracciones(f1, f2))


if __name__ == "__main__":
    OperacionesFraccion.main()

#Otra forma de hacer el 20, tambien con metodos estaticos

# Clase que representa una fracción
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # Método para mostrar la fracción de forma legible
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # Suma de fracciones
    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # Resta de fracciones
    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # Multiplicación de fracciones
    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    # División de fracciones
    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)


# Clase para manejar la ejecución principal
class OperacionesFraccion:
    @staticmethod
    def main():
        print("Ingrese los valores de la primera fracción:")
        n1 = int(input("Numerador: "))
        d1 = int(input("Denominador: "))
        print("Ingrese los valores de la segunda fracción:")
        n2 = int(input("Numerador: "))
        d2 = int(input("Denominador: "))

        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)

        suma = Fraccion.sumarFracciones(f1, f2)
        resta = Fraccion.restarFracciones(f1, f2)
        multiplicacion = Fraccion.multiplicarFracciones(f1, f2)
        division = Fraccion.dividirFracciones(f1, f2)

        print("\nResultados:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")


    # Ejecutar el programa
OperacionesFraccion.main()