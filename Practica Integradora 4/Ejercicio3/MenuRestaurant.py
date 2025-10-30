from Ingrediente import Ingrediente
from Plato import Plato

class MenuRestaurant:

    def __init__(self):

        self.platos=[]

    def agregar_platos(self,dato):

        self.platos.append(dato)

    def validar_plato(self, plato):

        for ob in self.platos:
            if plato==ob.nombreCompleto:
                return True
        return False
    
    def validar_ingrediente(self,ingrediente,instancia):

        for ob in instancia.lista_de_ingredientes:
            if ingrediente==ob.nombre:
                return True
        return False

    def Main(self):

        while True:
            
            while True:
                nombrecompleto=input("Ingrese el nombre del plato: ")
                if not nombrecompleto:
                    print("Error, valor vacio")
                elif self.validar_plato(nombrecompleto):
                    print("Error, el plato ya se encuentra en el menu")
                else:
                    break
            while True:
                temp=input("Ingrese el precio: ")
                if not temp:
                    print("Error, valor vacio")
                else:
                    precio=float(temp)
                    break
            while True:
                
                while True:
                    bebida=input("¿Es bebida? SI/NO ")
                    if not bebida:
                        print("Error, valor vacio")
                    elif bebida!="SI" and bebida !="NO":
                        print("Error, solo se permite SI/NO")
                    else:
                        break
                if bebida=="SI":
                    esbebida=True
                    break
                elif bebida=="NO":
                    esbebida=False
                    break
                
                    
            
            instanciaplato=Plato(nombrecompleto,precio,esbebida)
            self.agregar_platos(instanciaplato)

            if esbebida==False:
                while True:
                    
                    while True:
                        nombre=input("Ingrese el nombre del Ingrediente: ")
                        if not nombre:
                            print("Error, valor vacio")
                        elif self.validar_ingrediente(nombre,instanciaplato):
                            print("Error, el plato ya tiene el ingrediente")
                        else:
                            break
                    while True:
                        temp=input("Ingrese la cantidad: ")
                        if not temp:
                            print("Error, valor vacio")
                        else:
                            cantidad=float(temp)
                            break
                    while True:
                        unidadmedida=input("Ingrese la unidad de medida: ")
                        if not unidadmedida:
                            print("Error, valor vacio")
                        else:
                            break
                    intanciaingrediente=Ingrediente(nombre,cantidad,unidadmedida)
                    instanciaplato.agregar_ingredientes(intanciaingrediente)

                    while True:
                        opcion1=input("¿Desea cargar otro ingrediente? SI/NO ")
                        if not opcion1:
                            print("Error, valor vacio")
                        elif opcion1!="SI" and opcion1!="NO":
                            print("Error, solo se permite SI/NO")
                        else:
                            break
                    if opcion1=="SI":
                        pass
                    elif opcion1=="NO":
                        break
                    
            while True:
                opcion2=input("¿Desea cargar otro plato? SI/NO ")
                if not opcion2:
                    print("Error, valor vacio")
                elif opcion2!="SI" and opcion2!="NO":
                            print("Error, solo se permite SI/NO")
                else:
                     break
            if opcion2=="SI":
                    pass
            elif opcion2=="NO":
                    break
            

        print("-------MENU-------")   
        for o in self.platos:
              
             print(f"""{o.nombreCompleto}
precio: $ {o.precio}    """)
             if o.esBebida==False:
                  print("Ingredientes:")
                  print("Nombre  Cantidad  Unidad de Medida")
                  for p in o.lista_de_ingredientes:
                      print(f" {p.nombre}    {p.cantidad}       {p.unidadDeMedida} ")
             print("------------------")
             
    
instanciaMain=MenuRestaurant()
instanciaMain.Main()