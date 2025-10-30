from Habitacion import Habitacion

class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total_cubierto = sum(h.metrosCuadrados for h in self.habitaciones)
        if total_cubierto > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total_cubierto
