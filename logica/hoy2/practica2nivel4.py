def cargar(arreglo):
    for i in range(len(arreglo)):
        print(f"ingrese el valor {i+1}")
        dato=input()
        print(F"ingrese el valor {i+1}")
def sumar(notas):
    suma=0
    for valor in notas:
        suma=suma+valor

    return suma

def contar_mayores(arreglo, valor_ref):
    contador=0
    i=0
    while i<len(arreglo):
        if arreglo[i]>valor_ref:
            contador=contador+1
        i=i+1

    return contador

def porcentaje(contadore, arreglo):
    contadorg=len(arreglo)
    porc=contadore/contadorg*100
    return porc

notas=[80,90,100,90,70,80,0,90,0,85,]
nombres=["Maria","Paula","Fabiana","Paola","Jose","Roger", "Italo","Carlos", "Angel"]
suma_notas=sumar(notas)
aprobados=contar_mayores(notas,79)
porc_aprobados=porcentaje(aprobados, notas)
print(f"sumatoria {suma_notas} aprobados: {aprobados}")
print(f"el {porc_aprobados}% son notas aprobadas")