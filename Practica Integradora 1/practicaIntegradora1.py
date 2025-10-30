golosinas=[[1,"KitKat",20],
           [2,"Chicles",50],
           [3,"Caramelos de Menta",50],
           [4,"Huevos Kinder",10],
           [5,"Chetoos",10],
           [6,"Twix",10],
           [7,"MYM'S",10],
           [8,"Papas Lays",2],
           [9,"Milkybar",10],
           [10,"Alfajor Tofi",15],
           [11,"Lata Coca",20],
           [12,"Chitos",10]]

empleados={
        1100: "José Alonso",
        1200: "Federico Pacheco",
        1300: "Nelson Pereira",
        1400: "Osvaldo Tejada",
        1500: "Gastón Garcia"

}

clavesTecnico=("admin","CCCDDD",2020)

golosinasPedidas=[]

apagar= False

while apagar != True: 

    menu=input("A-Pedir Golosinas  B-Mostrar Golosinas  C-Rellenar Golosinas  D-Apagar Maquina \n ")
    
    if menu=="A":
        verificar_legajo=int(input("Ingrese su numero de legajo: ")) 
        if verificar_legajo in empleados:       #Verificamos si es un empleado
            verificar_golosina=int(input("Ingrese el codigo de la golosina: "))
            if any(verificar_golosina in sublista for sublista in golosinas): #Verificamos si el codigo de la golosina esta en la lista
                if golosinas[verificar_golosina-1][2]>0: #Verificamos si queda la golosina X
                    golosinas[verificar_golosina-1][2]-=1
                    if any(golosinas[verificar_golosina-1][1] in sublista for sublista in golosinasPedidas): #Verificamos si golosina esta en golosinasPedidas
                         nombre_busqueda=golosinas[verificar_golosina-1][0]
                         for i in range(len(golosinasPedidas)):        #Buscamos el indice de la fila
                             if nombre_busqueda==golosinasPedidas[i][0]:
                                 indice_busqueda=i
                                                         
                         golosinasPedidas[indice_busqueda][2]+=1 #Aumentamos +1 la cantidad de la golosina
                    else:
                         sublista=[]
                         sublista.append(golosinas[verificar_golosina-1][0])
                         sublista.append(golosinas[verificar_golosina-1][1])
                         sublista.append(1)
                         golosinasPedidas.append(sublista)

                else :
                    print(f"Lo sentimos la golosina {golosinas[verificar_golosina-1][1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
            else:
                print("No se encuentra la golosina")  
        else:
            print("No se encuentra el legajo")        

    elif menu=="B":

        for codigo, nombre, stock in golosinas:
         print(f"Código: {codigo} | {nombre} | Stock: {stock}")
     
    elif menu=="C":
     
        print("Ingrese la contraseña en 3 pasos")
        contraseña1=input("Ingrese la primer contraseña: ")
        if contraseña1==clavesTecnico[0]:
            contraseña2=input("Ingrese la segunda contraseña: ")
            if(contraseña2==clavesTecnico[1]):
                contraseña3=int(input("Ingrese la tercer contraseña: "))
                if contraseña3==clavesTecnico[2]:
                    verificar_golosina=int(input("Ingrese el codigo de la golosina: "))
                    if any(verificar_golosina in sublista for sublista in golosinas): #Verificamos si el codigo de la golosina esta en la lista
                        cantidad_a_recargar=int(input("ingrese cuanto quiere recargar: "))
                        if cantidad_a_recargar>0:

                             golosinas[verificar_golosina-1][2]+=cantidad_a_recargar #cargamos las golosinas

                        else:
                            print("La cantidad debe ser mayor que cero")


                    else:
                        print("No se encuentra la golosina")    

                else:
                    print("No tiene permiso para ejecutar la función de recarga")    
            
            else:
                print("No tiene permiso para ejecutar la función de recarga")

        else:  
            print("No tiene permiso para ejecutar la función de recarga")  


    elif menu=="D":
     
        apagar=True
        for codigo, nombre, cantidad_pedida in golosinasPedidas:
            print(f"Código: {codigo} | {nombre} | Cantidad Pedida: {cantidad_pedida}")

    else:

        print("Opcion Incorrecta")



    