
def leer_alumnos(direccion):

    with open(direccion, "r") as archivo: 
    
        for linea in archivo:        
            partes=linea.split(";")    
            print(f"Nombre: {partes[0].strip()} | Apellido: {partes[1].strip()} | Legajo: {partes[2].strip()} | promedio: {partes[3].strip()}")
            print("")

def generar_diccionario():
    with open(direccion, "r") as archivo:
        diccionario={}
        for linea in archivo:
            partes=linea.split(";")
            diccionario[partes[2]]=partes[0]+partes[1]
        
        return diccionario
    
def agregar_alumno(diccionario):

    while True:
        nombre=input("Ingrese el nombre: ")
        if nombre.isalpha():
            break        
        else:
            print("Debe Ingresar unicamente caracteres")
    while True:
        apellido=input("Ingrese el Apellido: ")
        if apellido.isalpha():
            break
        else:
            print("Debe Ingresar unicamente caracteres")
    while True:
        legajo=int(input("Ingrese el legajo: "))
        if len(str(legajo))==5:
            if str(legajo) in diccionario:
                print(f"El legajo {legajo} ya existe en el archivo, no se permite su escritura\n")
                return False
            else:
                break
        else: 
            print("El numero de legajo solo debe tener 5 numeros")
    while True:
        nota_promedio=int(input("Ingrese el promedio del alumno: "))
        if 1<=nota_promedio<=10:
            break
        else:
            print("La nota debe estar comprendida entre 1 y 10")
    
    with open(direccion, "a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota_promedio}\n")
        print("Hecho¡¡")

def guardar_aprobados():
    with open(direccion, "r") as archivo_lectura, open(direccion2, "w") as archivo_escritura:

        for linea in archivo_lectura:
            temporal=linea.split(";")
            if int(temporal[3])>=6:
                archivo_escritura.write(f"{temporal[0]} {temporal[1]}\n" )

    with open(direccion2, "r") as archivo_escritura:
        print("")
        print("------------------------")
        print("Alumnos aprobados")
        print("------------------------")
        for linea in archivo_escritura:
            print(linea)


        
direccion=r"c:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\Practica Integradora 3\alumnos.txt"
direccion2=r"c:\Users\andre\Documents\GitHub\UTN-TUPaDProgramacion1\Practica Integradora 3\aprobados.txt"

menu=False
generar_diccionario()

while menu==False:
    print("    -----------------------------------")
    opcion=input("""    1-Ver alumnos  
    2-Agregar alumno 
    3-Generar y mostrar archivo de aprobados
    4-Salir
    -----------------------------------\n""")
    
    if opcion=='1':

        leer_alumnos(direccion)

    elif opcion=='2':
        
        agregar_alumno(generar_diccionario())


    elif opcion=='3':

        guardar_aprobados()

    elif opcion=='4':
        menu=True

    elif not opcion:
        print("El menu no puede ser un valor vacio")
        
    
    else:
        print("Error de menu, intente nuevamente")

