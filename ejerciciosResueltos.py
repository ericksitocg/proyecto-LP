'''
1.	Realice un programa en Python que permita el ingreso por teclado del sueldo de un trabajador sin decimales y
determine si debe o no pagar impuesto.
Se considera que un trabajador debe pagar impuesto si el total de sueldo anual sobrepasa la cantidad de $11.310.
'''
sueldo= int(input("Ingrese su sueldo mensual sin decimales: "))
anual=sueldo*12
if(anual>11310):
    print("tiene que pagar impuesto")
else:
    print("no tiene que pagar impuestos")

'''
=========================================================================================================================
2.	Realice un programa en Python que imprima por pantalla la serie de números pares del 0 hasta el 100.
'''
for i in range(0,101,2):
    print(i)

'''
=========================================================================================================================
3.	Realice un programa en Python que permita el ingreso de la nota final del estudiante, la cual puede se entero o tener hasta 2 decimales y determine si aprobó la materia, en caso de no haber pasado, calcule la cantidad de puntos que faltaron.
Para aprobar la materia, el estudiante debe obtener una nota final de al menos 6 puntos de 10.
'''
nota=float(input("Ingrese su nota con decimales: "))
if nota>=6.00 :
    print("Aprobo la materia!")
else:
    falta= 6.00-nota
    print("Te falta %.2f para pasar"%falta)

'''
=========================================================================================================================
4.	Realice un programa en Python que permita el ingreso de una placa en el formato ABC-XY y verifique si la placa es válida.
Una placa se considera correcta si la primera parte (antes del guion) sea solo letras y la segunda parte (después del guion) sean solo números.
'''
placa=input("Ingrese una placa con el formato ABC-XY: ")
partes=placa.split("-")
if partes[0].isalpha() and partes[1].isdigit():
    print("Es una placa válida")
else:
    print("No es una placa válida")


'''
=========================================================================================================================
5.	Realice un programa en Python que permita el cálculo de IMC, pidiendo por teclado el ingreso de la estatura en metros y el peso en Kg mostrando un mensaje en pantalla para  determinar si está por encima del IMC recomendado el cual es menor 	que 25, en caso que el ICM sea mayor a 30 se muestra un mensaje indicando sobrepeso.
'''
estatura= float(input("Ingrese su estatura en metros (m): "))
peso= float(input("Ingrese su peso en Kilogramos (kg) " ))

IMC = peso/(estatura**2)
print("Su masa corporal es %.2f"%IMC)
if IMC > 25:
    print("Su indice de masa corporal NO es el correcta para su estatura y peso")
    if IMC > 30:
        print("Nivel de IMC: critico")
    else:
        print("Nivel de IMC: Tratable")
else:
    print("Su indice de masa corporal es el correcta para su estatura y peso")
'''
=========================================================================================================================
6.	Realice un programa en Python que pida una cantidad determinada de trabajadores a los que se le va solicitar el ingreso de su nombre y sueldo (puede ser decimal)en el formato nombre,sueldo y calcule cuál de ellos paga mayor cantidad de impuestos.
'''
impuesto_mayor = 0
nombre_mayor = ""

n_trabajadores =  input("Ingrese el numero de trabajores a procesar: ")
if n_trabajadores.isdigit():
    n_trabajadores = int(n_trabajadores)

    for trabajador in range(n_trabajadores):
        print("Ingrese el nombre y sueldo del trabajador con el siguiente formato: nombre,sueldo")
        nombre=input("Nombre empleado  :")
        sueldo= input("Sueldo empleado :")
        
        sueldo=float(sueldo)

        impuesto = sueldo*0.05

        if impuesto > impuesto_mayor:
            impuesto_mayor = impuesto
            nombre_mayor = nombre
print("El trabajador que paga mas impuestos es %s  que paga %.2f"%(nombre_mayor,impuesto_mayor))

'''
=========================================================================================================================
7.	Desarrollar en Python un programa que permita adivinar un numero del 1 al 50, este será generado de forma aleatoria con la librería random y le dará al usuario 5 intentos para que ingrese por teclado un número a adivinar, el programa debe decirle si el numero ingresado es mayor o menor que el numero aleatorio generado 
'''
import random as rd
ale = rd.randint(0,50)
juego_terminado = False
for vida in range(5):
    if not juego_terminado:
        n = int(input("Que numero del 1 al 50 crees que salio?: "))
        if n==ale:
            juego_terminado = True
        else:
            if n <ale:
                print("Su numero es menor que el objetivo")
            else:
                print("Su numero es mayor que el objetivo")
if juego_terminado:
    print("Felicidades ganaste")
else:
    print("Perdiste!, el numero era %d"%ale)

'''
=========================================================================================================================
8.	Simular el juego de la lotería, usando la librearía random genere 9 números aleatorios para formar el número ganador de la primera suerte.
Para ganar el premio mayor deben acertar los 5 números
Para ganar reintegro sólo debe coincidir el último número.
Sólo puede ganar un sólo premio de acuerdo a la relevancia del premio.
Solicitar al usuario el ingreso de un número e identificar si se lleva el premio mayor, o si al menos gana reintegro.
'''
#import random as rd

numero_ganador = ""
for i in range(5):
    aleatorio = rd.randint(0,9)
    numero_ganador=str(aleatorio)

usuario = input("Ingrese su numero de loteria: ")

if usuario==numero_ganador:
    print("Usted gano el premio mayor!")
else:
    if usuario[-1]:
        print("Usted gano un reintegro")
    else:
        print("Siga participado")
'''
=========================================================================================================================
9.	Realice un programa en Python que simule una tienda, pida por teclado una cantidad de dinero inicial y vaya presentando los productos con su precio, el usuario tendrá la opción de comprar el producto si tiene el dinero suficiente, de tal forma que se le reste del dinero inicial, y se le muestra por pantalla el dinero que le quedo y el producto que compro.
Los datos se encuentran en la lista L_tienda, la cual tiene tuplas de la forma (nombre,precio) de cada producto
'''
L_tienda = [("cafe",3.50),("leche",1.50),("pan",0.25),("azucar",0.50),("pastel",5)]
dinero = float(input("Ingrese la cantidad de dinero disponible: "))
for tupla in L_tienda:
    nombre = tupla[0]
    valor =tupla[1]
    print("\nProducto: %s valor: %.2f "%(nombre.upper(),valor))
    comprar = input("Desea comprar el producto? Ingrese si o no\n").lower()
    if comprar=="si":
        if dinero >= valor:
            dinero-=valor
            print("==Usted compro: %s y le quedan %.2f en de dinero disponible=="%(nombre,dinero))
        else:
            print("Ya no tiene dinero disponible para comprar")

'''
=========================================================================================================================
10.	Realice un programa en Python que calcule el promedio de edad de trabajadores que tienen sobrepeso, para identificarlos usted debe calcular el IMC de cada empleado, los datos se encuentran en las listas paralelas:
L_nombres_trabajadores ,L_estaturas _trabajadores,L_pesos_trabajadores,L_edades_trabajadores , debe presentar un mensaje indicando el IMC y en caso de ser mayor que 25, agregar su edad para posteriormente calcular el promedio de las mismas,al final presenta el promedio de las edades.
Que dos listas sean paralelas significa que los elementos de ambas se corresponden por su índice.
'''
L_nombres_trabajadores = ["Javier", "Estefania", "Joselyn", "Humberto"]
L_estaturas_trabajadores = [1.5, 1.59, 1.60, 1.55]
L_pesos_trabajadores = [70, 50, 60, 40]
L_edades_trabajadores = [25, 30, 25, 50]

L_edad_mayor_IMC = []

for i in range(len(L_estaturas_trabajadores)):
    nombre_trabajador = L_nombres_trabajadores[i]
    estatura_trabajador = L_estaturas_trabajadores[i]
    peso_trabajador = L_pesos_trabajadores[i]
    edad_trabajador = L_edades_trabajadores[i]

    IMC = peso_trabajador / (estatura_trabajador ** 2)

    print("=" * 5)

    if IMC > 25:
        print("El empleado %s tiene sobrepeso" % nombre_trabajador)
        L_edad_mayor_IMC.append(edad_trabajador)

    else:
        print("El empleado %s tiene un indice de masa corporal correcto" % nombre_trabajador)

promedio = sum(L_edad_mayor_IMC) / len(L_edad_mayor_IMC)

print("El promedio de edad de los empleados con IMC elevado es %.2f" % promedio)