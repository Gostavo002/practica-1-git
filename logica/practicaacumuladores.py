def procesar():
    precio=0
    precio_puma=0
    while True:
            marca=input("ingrese la marca de los zapatos")
            precio=float(input("ingrese el precio"))
            if marca.upper=="P":
                  precio_puma=precio_puma+precio
            resp=input("precio x para finalizar el procediminento")
            if resp==" ":
                  break
            return marca, precio, precio_puma
def imprimir( marca, precio, precio_puma):
      print(f"marca del zapatos es: {marca}")
      print(f"el precio del zapato es: {precio}")
      print(f"el precio del zapato puma es: {precio_puma}")

sumatoria_precio, sumatoria_puma=procesar()
print("todos los zapatos suman el total de")
      
      

