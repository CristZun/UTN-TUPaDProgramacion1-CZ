from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        return sum(v.superficieTerreno for v in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        return sum(v.superficieTerreno for v in self.viviendas if v.manzana == manzana)

    def getSuperficieTotalCubierta(self):
        total_cubierta = 0
        for v in self.viviendas:
            total_cubierta += v.getMetrosCuadradosCubiertos()
        return total_cubierta
