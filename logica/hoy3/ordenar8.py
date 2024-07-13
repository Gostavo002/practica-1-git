def ordenar(arreglo):
    for i in range(len(arreglo)):
        for j in range(len(arreglo)-1):
            if arreglo[j]>arreglo[j+1]:
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]+aux

def mostrar(arreglo1):
    for i in range(len(arreglo1)):
        print(f" {arreglo1[i]}")

nombres=["Jenny", "Maria", "Fabiana", "Tulio", "Jesus", "Patricio"]
mostrar(nombres)
ordenar(nombres)
print("--------------")
mostrar(nombres)