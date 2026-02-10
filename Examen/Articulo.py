class Articulo:
    def __init__(self, codigo, denominacion, rubro, marca, precio_venta):
        self.codigo = int(codigo)
        self.denominacion = denominacion
        self.rubro = rubro
        self.marca = marca
        self.precio_venta = float(precio_venta) 

    def __str__(self):
        return f"Código: {self.codigo} - {self.denominacion} ({self.marca}) - Precio: ${self.precio_venta:.2f}"