def cargar(arreglo, arreglo2, arreglo3):
    resp=""
    while resp.lower()!="n":
        print("ingrese el nombre de la persona")
        dato=input()
        arreglo.append(dato)
        print("Ingrese el sexo de la persona F/M")
        sexo=input()
        arreglo2.append(sexo)
        print(f"Cuantos anos tienes {dato}")
        dato3=int(input())
        arreglo3.append(dato3)
        resp=input("Presione n parqa detener la carga")
        if resp.upper()=="N":
            break

def promedio(arreglo):
    acumulador=0
    for valor in arreglo:
        acumulador=acumulador+valor
    prom=acumulador/len(arreglo)
    return prom

def listar(arreglo,arreglo2,arreglo3,valor):
    print("------------------------------")
    print("Chicas con edad mayor al promedio")
    for i in range(len(arreglo)):
        if arreglo[i]>valor and arreglo2[i].upper()=="F":
            print(arreglo3[i])
            





nombres= []
generos=[]
edades=[]
cargar(nombres,generos, edades)
promedio_edades=promedio(edades)
print(f"el promedio de edades es {promedio_edades}")
listar(edades,generos,nombres,promedio_edades)