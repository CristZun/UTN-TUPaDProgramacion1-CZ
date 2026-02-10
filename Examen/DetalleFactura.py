
class DetalleFactura:
    
    def __init__(self, cantidad, articulo):
        self.cantidad = int(cantidad) 
        self.articulo = articulo  
        self.subtotal = self.calcular_subtotal()
    def calcular_subtotal(self):
        return self.articulo.precio_venta * self.cantidad
        
    def __str__(self):
        return (f"  - Art. Cód: {self.articulo.codigo}, Denom: {self.articulo.denominacion[:30]:<30}, "
                f"Cant: {self.cantidad}, Subtotal: ${self.subtotal:.2f}")