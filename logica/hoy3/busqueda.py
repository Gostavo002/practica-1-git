def buscar(dato, arreglo):
    encontro=False
    i=0
    while i<len(arreglo) and not encontro:
        if arreglo[i]==dato:
            encontro=True
        i=i+1
    return encontro

#def buscar_p():


def preguntar(nombres,correos):
    print("Quieres buscar un nombre/correo")
    dato=input()
    existe=buscar(dato, correos)
    if existe:
        print("ya esta registrado en la posicion {indice}")
    else:
        print("no esta registrado")
    

nombres=["Jenny " ,"Maria" ,"Fabiana", "Tulio" ,"Jesus" ,"Betania"]
correos=["abc" "xyz" "bvnvn" "hasd" "hail" "haisp" "correo"]
print("Cual nombre vas a consultar")
nombre=input()
print(buscar(nombre,nombres))
if buscar(nombre,nombres):
    print(f"se encontro el nombre {nombres}")
else:
    print("no se encontro ese nombre")