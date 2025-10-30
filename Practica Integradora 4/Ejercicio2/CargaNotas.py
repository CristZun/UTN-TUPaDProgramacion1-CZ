from Nota import Nota 
from Alumno import Alumno


class CargaNotas:
    def __init__(self):
        self.alumnos = []
    
    def cargar_alumnos(self, datos):
        
        self.alumnos.append(datos)

    def validar_legajo(self,legajo):

        for ob in self.alumnos:
            if legajo==ob.legajo:
                return True
        return False
    
    def validar_materia(self,materia,instancia):

        for ob in instancia.notas:
            if materia==ob.catedra:
                return True
        return False



    def Main(self):


        while True:
            
            print("Ingrese datos del alumno")
            while True:
                nombreCompleto=input("Ingrese el Nombre del alumno: ")
                if not nombreCompleto:
                    print("Error, valor vacio")
                else:
                    break
            while True:    
                legajo=input("Ingrese el legajo: ")
                if not legajo:
                    print("Error, valor  vacio")

                else:
                    try:
                        legajo = int(legajo)
                    except ValueError:
                        print("Debe ingresar un número entero para el legajo")
                        continue

                    if self.validar_legajo(legajo):
                        print("¡El legajo ya existe!")
                    else:
                        break
            instaciaAlumno=Alumno(nombreCompleto,legajo)
            self.cargar_alumnos(instaciaAlumno)

            while True:

                print("Ahora ingrese las notas del alumno")
                while True:
                    catedra=input("Ingrese el nombre de la catedra: ")
                    if not catedra:
                        print("Error, valor vacio")
                    elif self.validar_materia(catedra,instaciaAlumno):
                        print("La materia ya existe")
                    else:
                        break
                while True:
                    notaExamen=input("Ingrese la nota del examen: ")
                    if not notaExamen:
                        print("Error, valor vacio")
                    elif float(notaExamen)<1 or float(notaExamen)>10:
                        print("La nota debe estar entre 1 y 10")
                    else:
                        notaExamen=float(notaExamen)
                        break
                instanciaNota=Nota(catedra,notaExamen)
                instaciaAlumno.agregar_elemento(instanciaNota)
                
                while True:
                    salirNota=input("¿Desea cargar otra nota? SI/NO ")
                    if not salirNota:
                        print("Error, valor vacio")
                    elif salirNota!="NO" and salirNota!="SI":
                        print("Error, solo se acepta SI/NO")
                    else:
                        break
                if salirNota=="NO":
                    break
                elif salirNota=="SI":
                    pass
                
                
                
            while True:
                salirAlumno=input("¿Desea cargar otro alumno? SI/NO ")
                if not salirAlumno:
                    print("Error, valor vacio")
                elif salirAlumno!="NO" and salirAlumno!="SI":
                    print("Error, solo se acepta SI/NO")
                else:
                    break

            if salirAlumno=="NO":
                break
            elif salirAlumno=="SI":
                pass
           
        print("--------------------------")
        for p in self.alumnos:
            print(f"Nombre: {p.nombreCompleto} legajo: {p.legajo}")

            for o in p.notas:
                print(f"Catedra: {o.catedra} Nota: {o.notaExamen}")
            print(f"El promedio es: {p.promedio()}")
        print("--------------------------")


instanciaMain=CargaNotas()
instanciaMain.Main()
          
 
