def procesar():
    cant_estudiantes=0
    aprobados=0
    reprobados=0
    masculinos=0
    femeninos=0
    while True:
        print("ingrese la nota")
        nota=int(input())
        sexo=input("ingresa tu sexo F/M").upper
        if nota>=80:
            aprobados=aprobados+1
        if nota<80:
            reprobados=reprobados+1

        if sexo=="M":
            masculinos=masculinos+1
        if sexo=="F":
            femeninos=femeninos+1
         
        resp=input("Presiona espacio para detener")
        if resp==" ":
            break
    print(f"cantidad de aprobados son {aprobados} y reprobados fueron {reprobados}")
    return cant_estudiantes, aprobados, reprobados, masculinos, femeninos
   

def calcularpoc(contadorg, contador):
    if contadorg>0:
        porcentaje=contador/contadorg*100
    else:
        porcentaje=0
    return porcentaje



def calcular(cant_estudiantes, aprobados, reprobados, hombres, mujeres):
    porc_aprobados=calcularpoc(cant_estudiantes, aprobados)
    porc_reprobados=calcularpoc(cant_estudiantes, reprobados)
    porc_M=calcularpoc(cant_estudiantes,hombres)
    porc_F=calcularpoc(cant_estudiantes,mujeres)
    return porc_aprobados, porc_reprobados,porc_M, porc_F

def mostrar(porc_aprobados, porc_reprobados,porc_M,porc_F):
    print(f"el porcentaje de aprobados de la seccion es {porc_aprobados}")
    print(f"el porcentaje de reprobados de la seccion es {porc_reprobados}")
    print(f"{porc_M}% son hombres y {porc_F} son mujeres")


cant_estudiantes, aprobados, reprobados, hombres, mujeres=procesar()
porc_aprobados,porc_reprobados,porc_M,porc_F=calcular(cant_estudiantes, aprobados, reprobados,hombres, mujeres)
mostrar=(porc_aprobados,porc_reprobados,porc_M, porc_F)