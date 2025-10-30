#1- CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la 
#conversión. Muestre por pantalla el resultado de las conversiones.  
"""
valorDecimal = float(input("Ingrese un número decimal: "))
#entero
valorEntero = int(valorDecimal)
#string
valorTexto = str(valorDecimal)
#booleano
valorBooleano = bool(valorDecimal)  # False si es 0.0, True si es distinto de 0
#lista
valorLista = list(valorTexto)
#resultados
print("Valor original (float):", valorDecimal)
print("Convertido a entero (int):", valorEntero)
print("Convertido a texto (str):", valorTexto)
print("Convertido a booleano (bool):", valorBooleano)
print("Convertido a lista (list):", valorLista)


#3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
#y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
#efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
#14. Plantee el algoritmo planteando métodos para su resolución.

numero=int(input("ingrese un numero de 3 digitos "))
suma=0
if numero >99 and numero < 1000:
    while numero > 0:
        digito=numero%10
        suma=suma+digito
        numero=int(numero//10)
else:   
    print("El número debe ser entre 100 y 999")
    
print(f"La suma del valor ingresado es {suma}")

#5- Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre 
#la cadena resultante.

frase=input("Ingrese una frase ")
frase_sin_espacios =frase.replace(" ","") #metodo para remplazar
print(f"Su frase sin espacios es: {frase_sin_espacios}")

#7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas 
#vocales tiene en total. 

frase = input("Ingrese una frase ").lower()

print(f"El tamaño de su cadena es de {len(frase)}")

total_vocales=0

for v in "aeiou": #recorre la frase tomando cada vocal en v.
    total_vocales+=frase.count(v)

print(f"El total de las vocales en la frasa es de: {total_vocales}")

#9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
#Muéstralos en línea recta, separados por un espacio entre cada carácter.
 
cadena = "La lluvia en Mendoza es escasa"

for caracter in cadena:
    print(ord(caracter), end=" ")  
    # ord transforma un caracter en un ASCII, devuelve un numero entero
    #end=" " evita el salto de línea y pone un espacio

print()  # para dejar una línea vacía al final

#11- Pedir dos palabras por teclado, indicar si son iguales. 

palabra1 =input("Ingrese la primer palabra")
palabra2 =input("Ingrese la segunda palabra")

if palabra1 == palabra2:
    print("las frases son identicas")
else:
    print("las Frases son diferentes") 
    
#13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera.  

cad1 = input("Ingrese la primera cadena: ")
cad2 = input("Ingrese la segunda cadena: ")

if cad1.count(cad2) > 0:
    print("La segunda cadena SE ENCUENTRA dentro de la primera.")
else:
    print("La segunda cadena NO se encuentra dentro de la primera.")

#15- Indique que sucede si realizo la siguiente declaración de variable:  
#x = None print(x)  
#Explique y ejemplifique el uso de None 
# None es un objeto especial que representa la ausensia de un valor o un valor nulo
#Se usa como valor por defecto en funciones cuando no se devuelve nada.

resultado = None #se inicializa pero no se asigna valor
resultado = 25

#La función imprime el saludo, pero como no hay return, su valor es None.
def saludar():
    print("Hola!")

resultado = saludar()
print(resultado)  

"""
#17- Cree una clase FuncionesPrograma y codifique una función estática getFechaString 
#que reciba como parámetro una fecha y retorne la fecha como una cadena literal.  
#Ejemplo recibo 15/10/1900, la salida debe ser 
#Quince de Octubre de mil novecientos. 
#Cree una clase Principal que contenga un método main y haga uso de la función 
#getFechaString. 
from datetime import datetime
from num2words import num2words #hay qye instalar esta libreria, pip install num2words 



class FuncionesPrograma:
    @staticmethod
    def getFechaString(fecha_str: str) -> str:
        # Diccionarios de días y meses
        dias = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince",
            16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve", 20: "Veinte",
            21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco",
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta",
            31: "Treinta y uno"
        }

        meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        # convertir y asignar valores 
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y") #metodo que convierte un string de fecha en numero (objeto) segun el orden asignado
        dia = dias[fecha.day]
        mes = meses[fecha.month]
        anio_literal = num2words(fecha.year, lang='es') #encontre un metodo que transorma cualquier año en letra, disculpe que no iba a hacer un diccionario con todos los años, y no podia dejarlo con un par de años

        return f"{dia} de {mes} de {anio_literal}"

#metodo main static
class Principal:
    @staticmethod
    def main():
        fecha_entrada = "26/10/1995"
        print(FuncionesPrograma.getFechaString(fecha_entrada))

#metodo main
if __name__ == "__main__":
    Principal.main()

"""
19- Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un 
atributo de nombre operación. 
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:  
sumarNumeros() 
restarNumeros() 
multiplicarNumeros() 
dividirNumeros() 
El quinto método será el siguiente:  
aplicarOperacion(operacion){  
…………………..  
}  
Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las 
operaciones. 

class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = None

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: división por cero"

    def aplicarOperacion(self, operacion):
        self.operacion = operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"


class Calculo:
    @staticmethod
    def main():
        # Crear instancia de OperacionMatematica
        op = OperacionMatematica(10, 5)

        # Probar operaciones
        print("Suma:", op.aplicarOperacion("+"))
        print("Resta:", op.aplicarOperacion("-"))
        print("Multiplicación:", op.aplicarOperacion("*"))
        print("División:", op.aplicarOperacion("/"))


# Ejecutar main
if __name__ == "__main__":
    Calculo.main()
"""

#codigo comentado para probar el codigo en bloques y que ninguna variable repetida entre en conflicto