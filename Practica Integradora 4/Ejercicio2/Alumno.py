class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto=nombreCompleto
        self.legajo=legajo
        self.notas=[]

    def agregar_elemento(self,elemento):

        self.notas.append(elemento)

    def promedio(self):
        if not self.notas:
            return 0  # Evita división por cero

        suma = 0
        contador = 0

        for ob in self.notas:
            suma += float(ob.notaExamen)  # Se asegura que sea número
            contador += 1

        return suma / contador
                  