def cargar(arreglo):
    while True:
        print("Ingrese el dato")
        dato=input()
        arreglo.append(dato)
        resp=input("Presione espacio para detener la carga")
        if resp==" ":
            break

def imprimir(arreglo):
    print("Lista de datos")
    for valor in arreglo:
        print(valor)
    

def menu_opciones():
    print("1) Registar")
    print("2) Imprimir")
    print("3) Salir")
    print("Ingrese la opcion")

#def mostrar():
    

nombres=[]
while True:
    menu_opciones()
    opcion=int(input())
    match opcion:
        case 1: cargar(nombres)
        case 2: print()
        case 3: print()
        case _: print("Opcion cerrada")
    if opcion==3:
        break        
