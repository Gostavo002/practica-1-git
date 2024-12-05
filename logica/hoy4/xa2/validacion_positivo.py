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

precio=validar_rango("Ingresen el precio", 1, 5)