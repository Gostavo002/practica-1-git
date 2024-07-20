def validar_positivo(mensaje):
    num=-1
    while not (num>0):
        print(mensaje)
        num=int(input())
        if not (num>0):
            print("Debe ser positivo")
        else:
            return num

edades=[]
edad= validar_positivo("Ingrese la edad")
edades.append(edad)
print(f"La edad ingresada es {edad}")