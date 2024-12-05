def procesar():
    #variable auxiliar
    nota_mayor=-1
    nota_menor=100
    nombremayor=""
    nombremenor=""
    cant_est=0
    cant_aprobados=0
    cant_reprobados=0
    notas_100=0
    suma_aprobados=0
    while True:
        cant_est=cant_est+1
        nombre=input("como se llama el estudiante")
        nota=float(input(f"cuanto saco {nombre}?"))
        notas=notas+nota
        if nota>nota_mayor:
            nota_mayor=nota
            nombremayor=nombre
            
        if nota<nota_menor:
            nota_menor=nota
            nombremenor=nombre
        if nota==100:
            notas_100=notas_100+1
        if nota>=80:
            cant_aprobados=cant_aprobados+1
        else:
            cant_reprobados=cant_reprobados+1

        resp=input("ingresa espacio para detener en procesamiento")
        if resp==" ":
            break

    return nota_mayor, nombremayor, nombremenor, nota_menor, cant_est,cant_aprobados,cant_reprobados, notas_100, suma_aprobados

def imprimir(nota_mayor, nombremayor, nota_menor, nombremenor , cant_est,cant_aprobados,cant_reprobados, notas_100, suma_aprobados):
    print()
    print(f"De {cant_est}")
    print(f"{nombremayor} obtuvo la mayor nota{nota_mayor}")
    print(f"{nombremenor} la nota menor fue{nota_menor} ")
    print("")
    print(f"de {cant_est}, {notas_100} obtuvieron 100 puntos")
    print(f"todas las notan suman {notas_100}")
    print(f"las notas de los aprobados suman {suma_aprobados}")
          
nota_mayor, nombremayor, nombremenor, nota_menor, cant_est,cant_aprobados,cant_reprobados,nota_100, suma_aprobados=procesar()

imprimir(nota_mayor,nota_menor, nombremayor, nombremenor , cant_est,cant_aprobados, cant_reprobados, nota_100, suma_aprobados)