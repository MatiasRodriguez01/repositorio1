# 22/08/23                                      PROGRAMACION 1
#   TEMA : CONDICIONALES 

#EJERCICIO 1: 
print("EL INSTITUTO DE INGLES NESESITA SABER EL DIA QUE CUSAS:")
fecha = input("Ingrese la fecha actual en formato dia,DD/MM: ")

dia = fecha[0:fecha.find(",")]
dd = fecha[fecha.find(" ")+1:fecha.find("/")]
mm = fecha[fecha.find("/")+1:]

dd = int(dd)
mm = int(mm)

print("dia: ", dia)
print("dd: ", dd)
print("mm: ", mm)

if (dd > 31) or (mm > 12): 
    print("Se produjo un error")
elif (dia.lower() == "lunes"):
    print("nivel inicial:")
    examen = input("Este dia se tomo examen? <<si/no>>: ")
    if examen.lower() == "si":
        print("EXAMEN:")
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
        suma = aprobados + desaprobados
        porc = (aprobados/suma)*100
        print(f"Hubo un porcentaje del {porc}% de aprobados.")
elif (dia.lower() == "martes"):
    print("nivel intermedio")
    examen = input("Este dia se tomo examen? <<si/no>>: ")
    if examen.lower() == "si":
        print("EXAMEN:")
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
        suma = aprobados + desaprobados
        porc = (aprobados/suma)*100
        print(f"Hubo un porcentaje del {porc}% de aprobados.")
elif (dia.lower() == "miercoles"):
    print("nivel avanzado")
    examen = input("Este dia se tomo examen? <<si/no>>: ")
    if examen.lower() == "si":
        print("EXAMEN:")
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
        suma = aprobados + desaprobados
        porc = (aprobados/suma)*100
        print(f"Hubo un porcentaje del {porc}% de aprobados.")
elif (dia.lower() == "jueves"):
    print("practica hablada")
    asistencias = int(input("Ingrese su porcentaje de asistencias: "))
    if (asistencias < 0) or (asistencias > 100):
        print("El valor ingresado es incorrecto!!!")
    elif (asistencias > 0) and (asistencias <= 100):
        if (asistencias > 50):
            print("asistio la mayoria!")
        else:
            print("no asistio la mayoria!")
elif (dia.lower() == "viernes"):
    print("Ingles para viajeros")
    if (dd == 1 and mm == 1) or (dd == 1 and mm == 7):
        print("¡Comieno de nuevo ciclo!")
        arancel = int(input("Ingrese la cuota del arancel que debe pagar: "))
        print(f"Debera pagar ${arancel} por el arancel")
else:
    print("El dia ingresado es incorrecto")