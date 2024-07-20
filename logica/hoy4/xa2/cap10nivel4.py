def cargar(arreglo,arreglo2,arreglo3):
    while True:
        print("Ingrese el dato")
        dato=input()
        dato2=validar_positivo("Ingrese la edad")
        dato3=validar_positivo("Entradas al cine")
        arreglo.append(dato)
        arreglo2.append(dato2)
        arreglo3.append(dato3)
        resp=input("Presione espacio para detener la carga")
        if resp==" ":
            break

def imprimir(arreglo,arreglo2,arreglo3):
    print("Lista de datos")
    for i in range (len(arreglo)):
        print(f"{arreglo[i]} edad: {arreglo2[i]} cantidad:{arreglo3[i]} ")
    
def validar_positivo(mensaje):
    num=-1
    while not (num>0):
        print(mensaje)
        num=int(input())
        if not (num>0):
            print("Debe ser positivo")
        else:
            return num
        
def validar_rango(msj,min,max):
    while True:
        print(msj)
        dato=int(input())
        if dato>min and dato<max:
            return dato
        if not (dato>=min and dato<max):
            print(f"Debe estar entre {min} y {max}")

def menu_opciones():
    print("1) Registar")
    print("2) Imprimir")
    print("3) Salir")
    print("Ingrese la opcion")


#def mostrar():
    

nombres=[]
edades=[]
while True:
    menu_opciones()
    opcion=int(input())
    match opcion:
        case 1: cargar(nombres, edades)
        case 2: print()
        case 3: print()
        case _: print("Opcion cerrada")
    if opcion==3:
        break        
