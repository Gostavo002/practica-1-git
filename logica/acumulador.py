def cargar():
    edades=0
    while True:
        nombres=input("como se llama el estudiante")
        sexo=input("ingrese el genero F/M")
        edad=int(input("ingrese la edad"))
        edades=edades+edad
        if sexo.upper()=="F":
            edades_mujeres=edades_mujeres+edad
        print(f"se registro {nombres}")
        resp=input("presiona espacio para detener el procesamiento")
        if resp==" ":
            break
        return edades
    
sumatoria_edades=cargar()
print(sumatoria_edades)