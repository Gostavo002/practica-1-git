def validar_letra(msj,letra1,letra2):
    while True:
        print(msj)
        letra=input().upper()
        if (letra==letra1 or letra==letra2) and len(letra)==1:
            return letra
        else:
            print(f"Ingrese una letra: {letra1} o {letra2}")

def validar_cadena(msj):
    while True:
        print(msj)
        cadena=input()
        if (not cadena.isalpha() and len (cadena)>1):
            return cadena
        else:
            print("Solo se admiten letras")


nombre=validar_cadena("ingresa nombre")
