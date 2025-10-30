from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

class CostoComputadora:
    @staticmethod
    def main():
        while True:
            print("Hola, bienvenido al cotizador de computadoras.")
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo: ")
            print("Ahora ingrese los componentes de la computadora.")
            print("Para finalizar la entrada de componentes, ingrese 'FIN' como nombre del componente.")
            computadora = Computadora(marca, modelo)

            while True:
                componente = input("Ingrese el nombre del componente: ")
                if componente.upper() == "FIN":
                    break
                marca_comp = input("Ingrese la marca del componente: ")

                # Validación de cantidad
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad: "))
                        if cantidad < 1:
                            print("Error: la cantidad debe ser un número entero positivo.")
                            continue
                        break
                    except ValueError:
                        print("Error: ingrese un número entero válido para la cantidad.")

                # Validación del precio unitario
                while True:
                    try:
                        precio = float(input("Ingrese el precio unitario: "))
                        if precio < 0:
                            print("Error: el precio no puede ser negativo.")
                            continue
                        break
                    except ValueError:
                        print("Error: ingrese un número válido para el precio unitario.")

                print("-----------------------------")
                print("Recuerde ingresar 'FIN' para terminar de agregar componentes.")

                comp = ComponenteCPU(componente, marca_comp, cantidad, precio)
                computadora.agregar_componente(comp)

            computadora.mostrar_informacion()

            continuar = input("¿Desea cotizar otra computadora? (SI/NO): ")
            if continuar.upper() != "SI":
                print("Programa finalizado.")
                break


if __name__ == "__main__":
    CostoComputadora.main()
