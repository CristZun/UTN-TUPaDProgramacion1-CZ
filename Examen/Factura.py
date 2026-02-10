
from datetime import date

class Factura:
    _siguiente_numero = 1

    def __init__(self, lista_detalles):
        self.fecha = date.today() 
        self.numero = Factura._siguiente_numero
        Factura._siguiente_numero += 1 
        
        self.lista_detalles = lista_detalles 
        self.total = self.calcular_total() 
    
    def calcular_total(self):
        total_acumulado = 0
        for detalle in self.lista_detalles:
            total_acumulado += detalle.subtotal
        return total_acumulado
    
    