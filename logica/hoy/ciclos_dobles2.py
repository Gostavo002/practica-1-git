
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
        print("Datos que representa una serie de valores ")
        nota=int(input("ingrese la nota "))
        sumatoria=sumatoria+nota
        resp=input("presione espacio para detener ")
        if resp==" ":
            break

print(f"el estudiante {nombre} registro {cant_notas} notas")
promedio=sumatoria/cant_notas
print(f"promedio {promedio}")
print("***************************************")