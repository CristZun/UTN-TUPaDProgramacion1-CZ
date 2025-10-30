#Trabajo Practico POO
#Nombre: Andrés Fabre, Cristian Zuñiga

#Ejercicio Nro 1

class celda:

    def __init__(self, valor, fila, columna):
        
        self.valor=valor
        self.fila=fila
        self.columna=columna                
        

class matriz:

    def __init__(self):

        self.celdasMatriz = []
    
    def agregar_elemento(self,elemento):

        self.celdasMatriz.append(elemento)

def devolver_fila_columna(fila1,columna1,instancia):

    encontrado=False
    for celda in instancia:
        if celda.fila==fila1 and celda.columna==columna1:
            print(f"Valor: {celda.valor}")
            encontrado=True
    if encontrado==False:
        print("La fila y columna indicada no ha sido asignada en ninguna celda")    

def validar_celda(fila, columna, instancia):
    for celda in instancia.celdasMatriz:
        if celda.fila == fila and celda.columna == columna:
            return True  # Ya hay una celda en esa posición
    return False  # Está libre
    
instancia2=matriz()

while(True):
    
    while True:
        temp=input("Ingrese el valor de la celda: ")
        if not temp:
            print("El valor no puede ser vacio")
        else:
            break
    if str(temp)=="FIN":
        break
    valor=float(temp)
    
    while True:
        temp=input("Ingrese la fila de la celda: ")
        if not temp:
            print("El valor no puede ser vacio")
        else:
            break
    fila=int(temp)
    while True:
        temp=input("Ingrese la columna de la celda: ")
        if not temp:
            print("El valor no puede ser vacio")
        else:
            break
    columna=int(temp)

    if validar_celda(fila,columna,instancia2):
        print("Espacio ya ocupado")
    else :
        instancia1=celda(valor,fila,columna)
    
        instancia2.agregar_elemento(instancia1)

for p in instancia2.celdasMatriz:
    print(f"Valor: {p.valor} Fila: {p.fila} Columna: {p.columna}")

while True:
    temp=input("Ingrese la fila a buscar: ")
    if not temp:
        print("No puede ser un valor vacio")
    else:
        break
fila1=int(temp)
while True:
    temp=input("Ingrese la columna a buscar: ")
    if not temp:
        print("No puede ser un valor vacio")
    else: 
        break
columna1=int(temp)

devolver_fila_columna(fila1,columna1,instancia2.celdasMatriz)