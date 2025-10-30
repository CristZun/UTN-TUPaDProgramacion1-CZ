from ComponenteCPU import ComponenteCPU

class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente: ComponenteCPU):
        self.componentes.append(componente)

    def calcular_costo_total(self):
        return sum(c.calcular_subtotal() for c in self.componentes)

    def calcular_precio_venta(self):
        costo_total = self.calcular_costo_total()
        if costo_total < 50000:
            return costo_total * 1.40
        else:
            return costo_total * 1.30

    def mostrar_informacion(self):
        print("\n-----------Computadora----------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes:\n")
        print(f"{'Componente':<20} {'Marca':<15} {'Cant.':<8} {'Precio':<10} {'Subtotal'}")
        for c in self.componentes:
            subtotal = c.calcular_subtotal()
            print(f"{c.componente:<20} {c.marca:<15} {c.cantidad:<8} ${c.precio:<10.2f} ${subtotal:.2f}")

        costo_total = self.calcular_costo_total()
        precio_venta = self.calcular_precio_venta()
        print(f"\nCosto Total: ${costo_total:.2f}")
        print(f"Precio sugerido de venta: ${precio_venta:.2f}")
        print("-------------------------------------\n")
