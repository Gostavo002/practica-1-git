def procesar():
    #variable auxiliar
    nota_mayor=0
    nota_menor=100
    nombremayor=0
    nombremenor=0
    for i in range(4):
        nombre=input("como se llama el estudiante")
        nota=float(input(f"cuanto saco {nombre}?"))
        if nota>nota_mayor:
            nota_mayor=nota
            nombremayor=nombre
        if nota<nota_menor:
            nota_menor
            nombremenor=nombre

    return nota_mayor, nombremenor, nota_menor, nombremayor

def imprimir(nota_mayor, nombremayor, nota_menor, nombremenor):
    print(f"{nombremayor} obtuvo la mayor nota{nota_mayor}")
    print(f"{nombremenor} la nota menor fue{nota_menor} ")
          
nota_mayor,nombremenor, nota_menor, nombremayor=procesar()

imprimir(nota_mayor,nota_menor, nombremayor, nombremenor)