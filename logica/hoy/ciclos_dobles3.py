acumulador_notas_seccion=0
for i in range(1,3):
    print("--------------------------------------")
    print(f"Datos de cada entidad,que son unicos {i}")
    nombre=input("como se llama el estudiante ")
    cedula=input("ingrese la cedula del estudiante")
    print(f"estudiante: {nombre} CI {cedula}")
    sumatoria=0
    cant_notas=0
    while True:
        cant_notas=cant_notas+1
        print()
        nota=int(input("ingrese la nota "))
        sumatoria=sumatoria+nota
        if nota>10:
            notas_aprob_secc=notas_aprob_secc+1
        resp=input("presione espacio para detener ")
        if resp==" ":
            break


    print(f"acumulo {sumatoria} de {cant_notas}")
    acumulador_notas_seccion=acumulador_notas_seccion+cant_notas
    print(f"se lleva acumulado {acumulador_notas_seccion}")
    print(f"de {contador_notas_seccion} notas")
    print("***************************************")

