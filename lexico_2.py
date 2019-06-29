import ply.lex as lex
import ply.yacc as yacc
from tkinter import *
import subprocess

# resultado del analisis
result_lex = []
result_sem=[]

# Palabras reservadas
reserved = {
    'import': 'IMPORT',  #
    'as' : 'AS',
    'from': 'FROM',  #
    'input': 'INPUT',  #
    'split': 'SPLIT',  #
    'find': 'FIND',  #
    'index': 'INDEX',  #
    'isdigit': 'ISDIGIT',  #
    'isalpha': 'ISALPHA',  #
    'len': 'LEN',  #
    'sum' : 'SUM',
    'strip': 'STRIP',  #
    'count': 'COUNT',  #
    'slice': 'SLICE',  #
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'range':'RANGE',
    'print' : 'PRINT',
    'random':'RANDOM',
    'randint': 'RANDINT',
    'int': 'INT',
    'float':'FLOAT',
    'str':'STR',
    'and':'AND',
    'or':'OR',
    'not':'NOT',
}

# tokens del programa
tokens = list(reserved.values()) + [
    'IDENTIFICADOR',  # string
    'NUMBER',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MENOSIGUAL',
    'MASIGUAL',

    # operadores logicos
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',

    # Simbolos
    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

    # estructuras
 #   'LISTA',
    'LISTA_SIMPLE',
    'LISTA_DOBLE',
    'LISTA_TRIPLE',
    'LISTA',
    #'TUPLA',
    'TUPLA_SIMPLE',
    'TUPLA_DOBLE',
    'TUPLA_TRIPLE',
    'TUPLA',
    'CONJUNTO',

    # valores primitivos
    'FLOTANTE',
    'INTEGER',
    'BOOLEAN',
    'CADENA',

    # Varios
    'COMA',
    'COMDOB',  # "
    'PUNTO',
    'DOSPUNTOS',
]

# Expresiones regulares para tokens

t_SUMA = r'\+'
t_RESTA = r'-'
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'\-='
t_PUNTO = r'\.'
t_DOSPUNTOS = r'\:'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='

# Definicion de Expresiones Logicas
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'


# def t_NUMBER(t):
#     r'\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %d", t.value)
#         t.value = 0
#     return t


def t_FLOTANTE(t):
    r'-?\d*[.]\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_BOOLEAN(t):
    r'True|False'
    return t

def t_IDENTIFICADOR(t):  # variable
    r'\w+(_\d\w)*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Check for reserved words
    return t


def t_CADENA(t):
    r'\"+.*\"+'
    return t

# def t_LISTA(t):
#     r'\[(\w,|\w)+\]'
#     return t

def t_LISTA_SIMPLE(t):
    r'\[-?\w+\]'
    return t
def t_LISTA_DOBLE(t):
    r'\[-?\w+,-?\w+\]'
    return t

def t_LISTA_TRIPLE(t):
    r'\[-?\w+,-?\w+\,-?\w+]'
    return t

def t_LISTA(t):
    r'\[(-?\w+,|-?\w+)+\]'
    return t

# def t_TUPLA(t):
#     r'\((\w,|\w)+\)'
#     return t


def t_TUPLA_SIMPLE(t):
    r'\(\w+\)'
    return t


def t_TUPLA_DOBLE(t):
    r'\(\w+,\w+\)'
    return t


def t_TUPLA_TRIPLE(t):
    r'\(\w+,\w+,\w+\)'
    return t

def t_TUPLA(t):
    r'\((\w,|\w)+\)'
    return t


def t_CONJUNTO(t):
    r'\{(\w,|\w)+\}'
    return t


def t_NUMERAL(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")


def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = ' \t'


def t_error(t):
    global result_lex
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                    str(t.lexpos))
    result_lex.append(estado)
    t.lexer.skip(1)


analizador=lex.lex()
result_lex_malo=[]


########################## Prueba de ingreso########################3
def prueba(data):
    result_lex_malo.clear()
    result_lex.clear()

    p=analizador.input(data)


    while True:
        tok = analizador.token()
        if not tok:
            result_lex_malo.append(str(p))
            #return result_lex
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Tipo {}| Valor {}| Posicion {}".format(str(tok.type), str(tok.value), str(tok.lexpos))
        result_lex.append(estado)
    return result_lex


datos_prueba = """
if a == 5.9:
if True:
if False:
if b!= 6:
if a > b:
if b < c:
if a>=6:
else:
for i in range(a):
for i in L:
for j in in [1,2,3,4]:
for i in (1,2,3,4):
for i in range(8):
for i in range(8,2):
for i in range(8,2,9):
for i in range(8,2,1,2):
"""

# instanciamos el analizador lexico
# if __name__ == '__main__':
#     # while True:
#     # data = input("ingrese: ")
#     prueba(datos_prueba)
#     for lex in result_lex:
#         print(lex)
#         if ":" in lex:
#             print()

# dictionary of names
names = {}


#                   ANALIZADOR SINTÁCTICO
# Definiendo las gramaticas
# def p_RULNAME

def p_entrada(p):
    """ entrada : asignacion
                | operacion
                | estructura_de_control
                | funcion
                | empty
                | importar_libreria"""
    # p[0] = ('entrada', p[1])

####################################################

def p_estructura_de_control(p):
    """ estructura_de_control : condicional_if
                              | condicional_else
                              | condicional_if_else
                              | bucle_for
                              | operacion_compuesta"""
    p[0] = p[1]
def p_condicional_else(p):
    """condicional_else : ELSE DOSPUNTOS"""
    p[0] = p[1]

def p_condicional_if_else(p):
    """ condicional_if_else : condicional_if ELSE DOSPUNTOS"""
    p[0] = p[1]

def p_condicional_if(p):
    """condicional_if : IF expresion_logica DOSPUNTOS
                        | IF expresion_logica_compuesta DOSPUNTOS
                        | IF BOOLEAN DOSPUNTOS
                        | IF IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS
                        | IF NOT expresion_logica DOSPUNTOS
                        | IF identificador_slicing DOSPUNTOS"""
    p[0] = p[1]

#    if usuario[-1]:


def p_bucle_for(p):
    """ bucle_for : FOR IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS
                  | FOR IDENTIFICADOR IN range DOSPUNTOS
                  | FOR IDENTIFICADOR IN coleccion DOSPUNTOS"""
    p[0] = p[1]
#####################################################

def p_expresion_logica_compuesta(p):
    """expresion_logica_compuesta : expresion_logica operador_logico expresion_logica"""
    p[0] = p[1]

def p_operador_logico(p):
    """operador_logico : AND
                        | OR
                        | NOT """
    p[0] = p[1]

def p_expresion_logica(p):
    """expresion_logica : dato comparador dato
                        | IDENTIFICADOR
                        | identificador_atributo"""
    p[0] = p[1]
    # if p[2] == '==': p[0] = p[1] == p[3]
    # if p[2] == '!=': p[0] = p[1] != p[3]
    # if p[2] == '>': p[0] = p[1] > p[3]
    # if p[2] == '<': p[0] = p[1] < p[3]
    # if p[2] == '>=' : p[0] = p[1] >= p[3]
    # if p[2] == '<=' : p[0] = p[1] <= p[3]

def p_comparador(p):
    """ comparador : IGUAL
                    | DISTINTO
                    | MAYORQUE
                    | MENORQUE
                    | MENORIGUAL
                    | MAYORIGUAL """
    p[0] = p[1]


def p_asignacion(p):
    """ asignacion : IDENTIFICADOR ASIGNAR operacion
                    | IDENTIFICADOR ASIGNAR operacion_compuesta
                    | IDENTIFICADOR ASIGNAR dato
                    | IDENTIFICADOR ASIGNAR funcion
                    | IDENTIFICADOR ASIGNAR casting
                    | IDENTIFICADOR ASIGNAR CORIZQ coleccion CORDER
                    | IDENTIFICADOR ASIGNAR  coleccion """
    # p[0] = ('asignacion',p[1],p[3])
    names[p[1]] = p[3]


# def p_lista_coleccion(p):
#     """ lista_coleccion : CORIQZ coleccion CORDER
#                         | coleccion COMA
#                         | CORIQZ coleccion COMA
#                         | coleccion COMA CORDER
#                         | lista_coleccion
#                         """

# L_tienda = [("cafe",3.50),("leche",1.50),("pan",0.25),("azucar",0.50),("pastel",5)]

def p_casting(p):
    """ casting : tipo_dato PARIZQ asignacion PARDER
                | tipo_dato PARIZQ operacion PARDER
                | tipo_dato PARIZQ funcion PARDER
                | tipo_dato TUPLA_SIMPLE"""
    p[0] = p[1]

def p_tipo_dato(p):
    """ tipo_dato : FLOAT
                    | INT
                    | STR"""
    p[0] = p[1]
#
def p_operacion_compuesta(p):
    """ operacion_compuesta : operacion operador operacion
                            | IDENTIFICADOR operador operacion
                            | IDENTIFICADOR operador PARIZQ operacion PARDER
                            | operacion operador IDENTIFICADOR
                            | PARIZQ operacion PARDER operador IDENTIFICADOR
                            | PARIZQ operacion PARDER operador PARIZQ operacion PARDER"""
    p[0] = p[1]

def p_operacion(p):
    """ operacion : dato operador dato
    | IDENTIFICADOR operador dato"""
    p[0] = p[1]
    # if p[2] == '+': p[0] = p[1] + p[3]
    # if p[2] == '-': p[0] = p[1] - p[3]
    # if p[2] == '*': p[0] = p[1] * p[3]
    # if p[2] == '/': p[0] = p[1] / p[3]

def p_operador(p):
    """ operador : SUMA
                | RESTA
                | MULT
                | DIV
                | POTENCIA
                | MODULO"""
    p[0] = p[1]

def p_coleccion(p):
    """coleccion : LISTA_SIMPLE
                    | LISTA_DOBLE
                    | LISTA_TRIPLE
                    | LISTA
                    | TUPLA_SIMPLE
                    | TUPLA_DOBLE
                    | TUPLA_TRIPLE
                    | TUPLA
                    | coleccion COMA"""

    p[0] = p[1]
####################################

def p_funcion(p):
    """ funcion : funcion_print
                | funcion_random_randint
                | funcion_input
                | funcion_sum
                | funcion_len"""
    p[0] = p[1]

def p_funcion_print(p):
    """ funcion_print : PRINT PARIZQ PARDER
                        | PRINT PARIZQ CADENA PARDER
                        | PRINT PARIZQ CADENA MODULO IDENTIFICADOR PARDER
                        | PRINT PARIZQ CADENA MODULO TUPLA_DOBLE PARDER
                        | PRINT TUPLA_SIMPLE
                        | PRINT TUPLA_DOBLE
                        | PRINT TUPLA_TRIPLE
                        | PRINT TUPLA """
    p[0] = p[1]

# print("El trabajador que paga mas impuestos es %s  que paga %.2f"%(nombre_mayor,impuesto_mayor))

def p_funcion_random_randint(p):
    """funcion_random_randint : RANDOM PUNTO RANDINT TUPLA_SIMPLE
                             | RANDOM PUNTO RANDINT TUPLA_DOBLE
                             | IDENTIFICADOR PUNTO RANDINT TUPLA_SIMPLE
                             | IDENTIFICADOR PUNTO RANDINT TUPLA_DOBLE"""
    p[0] = p[1]

def p_funcion_input(p):
    """ funcion_input : INPUT PARIZQ CADENA PARDER
                        | INPUT PARIZQ PARDER
                        | INPUT PARIZQ CADENA MODULO IDENTIFICADOR PARDER"""
    p[0] = p[1]

def p_funcion_sum(p):
    """funcion_sum : SUM TUPLA_SIMPLE"""
    p[0] = p[1]

def p_funcion_len(p):
    """funcion_len : LEN TUPLA_SIMPLE"""
    p[0] = p[1]
######################################

def p_identificador_slicing(p):
    """identificador_slicing : IDENTIFICADOR LISTA_SIMPLE
                                | IDENTIFICADOR CORIZQ INTEGER DOSPUNTOS INTEGER CORDER
                                | IDENTIFICADOR CORIZQ INTEGER DOSPUNTOS INTEGER DOSPUNTOS INTEGER CORDER"""
    p[0] = p[1]

def p_identificador_atributo(p):
    """ identificador_atributo : IDENTIFICADOR PUNTO funcion_atributo
                                | identificador_slicing PUNTO funcion_atributo"""

def p_funcion_atributo(p):
    """ funcion_atributo : funcion_split
                            | funcion_isalpha
                            | funcion_isdigit"""
    p[0] = p[1]

def p_funcion_split(p):
    """funcion_split : SPLIT PARIZQ CADENA PARDER
                    | SPLIT PARIZQ PARDER """
    p[0] = p[1]

def p_funcion_isalpha(p):
    """funcion_isalpha : ISALPHA PARIZQ PARDER"""
    p[0] = p[1]

def p_funcion_isdigit(p):
    """funcion_isdigit : ISDIGIT PARIZQ PARDER"""
    p[0] = p[1]

def p_range(p):
    """ range : RANGE TUPLA_SIMPLE
                | RANGE TUPLA_DOBLE
                | RANGE TUPLA_TRIPLE"""
    p[0] = p[1]

################################
def p_importar_libreria(p):
    """ importar_libreria : IMPORT libreria
                        | IMPORT libreria AS IDENTIFICADOR
                        | FROM libreria IMPORT IDENTIFICADOR"""
    p[0] = p[1]

def p_libreria(p):
    """libreria : RANDOM"""
    p[0] = p[1]

###############################
def p_dato(p):
     """ dato : IDENTIFICADOR
                | FLOTANTE
                | INTEGER
                | CADENA
                | BOOLEAN
                | identificador_atributo
                | identificador_slicing"""
     p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global result_sem
    # estado = "** Semantica no valida en la Linea {:4} Valor {:4} Posicion {:4} Tipo {:4}".format(str(p.lineno-1), str(p.value),str(p.lexpos),str(p.type))
    # estado = "** Semantica no valida Valor {:4} Posicion {:4} Tipo {:4}".format(str(p.value),str(p.lexpos),str(p.type))

    estado="** Sintactica no valida"
    result_sem.append(estado+"\n")


    # print("Syntax error in input! "+ p.type)
    print(estado)

parser = yacc.yacc()



#------------------------------------prueba del yacc por consola---------------------

# print("Ingrese la expresion semantica a evaluar")
# while True:
#     s = input('> ')
#     parser.parse(s)





#------------------------------------------------------------------------------

ej1="1.Realice un programa en Python que permita el ingreso por teclado del sueldo de un trabajador sin decimales y determine si debe o no pagar impuesto. Se considera que un trabajador debe pagar impuesto si el total de sueldo anual sobrepasa la cantidad de $11.310."
ej2="2.Realice un programa en Python que imprima por pantalla la serie de números pares del 0 hasta el 100."
ej3="3.Realice un programa en Python que permita el ingreso de la nota final del estudiante, la cual puede se entero o tener hasta 2 decimales y determine si aprobó la materia, en caso de no haber pasado, calcule la cantidad de puntos que faltaron. Para aprobar la materia, el estudiante debe obtener una nota final de al menos 6 puntos de 10."
ej4="4.Realice un programa en Python que permita el ingreso de una placa en el formato ABC-XY y verifique si la placa es válida. Una placa se considera correcta si la primera parte (antes del guion) sea solo letras y la segunda parte (después del guion) sean solo números."
ej5="5.Realice un programa en Python que permita el cálculo de IMC, pidiendo por teclado el ingreso de la estatura en metros y el peso en Kg mostrando un mensaje en pantalla para  determinar si está por encima del IMC recomendado el cual es menor 	que 25, en caso que el ICM sea mayor a 30 se muestra un mensaje indicando sobrepeso."
ej6="6.Realice un programa en Python que pida una cantidad determinada de trabajadores a los que se le va solicitar el ingreso de su nombre y sueldo (puede ser decimal)en el formato nombre,sueldo y calcule cuál de ellos paga mayor cantidad de impuestos."
ej7="7.Desarrollar en Python un programa que permita adivinar un numero del 1 al 50, este será generado de forma aleatoria con la librería random y le dará al usuario 5 intentos para que ingrese por teclado un número a adivinar, el programa debe decirle si el numero ingresado es mayor o menor que el numero aleatorio generado "
ej8="8.Simular el juego de la lotería, usando la librearía random genere 9 números aleatorios para formar el número ganador de la primera suerte. Para ganar el premio mayor deben acertar los 5 números Para ganar reintegro sólo debe coincidir el último número. Sólo puede ganar un sólo premio de acuerdo a la relevancia del premio. Solicitar al usuario el ingreso de un número e identificar si se lleva el premio mayor, o si al menos gana reintegro."
ej9="9.Realice un programa en Python que simule una tienda, pida por teclado una cantidad de dinero inicial y vaya presentando los productos con su precio, el usuario tendrá la opción de comprar el producto si tiene el dinero suficiente, de tal forma que se le reste del dinero inicial, y se le muestra por pantalla el dinero que le quedo y el producto que compro. Los datos se encuentran en la lista L_tienda, la cual tiene tuplas de la forma (nombre,precio) de cada producto"
ej10="10.Realice un programa en Python que calcule el promedio de edad de trabajadores que tienen sobrepeso, para identificarlos usted debe calcular el IMC de cada empleado, los datos se encuentran en las listas paralelas: L_nombres_trabajadores ,L_estaturas _trabajadores,L_pesos_trabajadores,L_edades_trabajadores , debe presentar un mensaje indicando el IMC y en caso de ser mayor que 25, agregar su edad para posteriormente calcular el promedio de las mismas,al final presenta el promedio de las edades. Que dos listas sean paralelas significa que los elementos de ambas se corresponden por su índice."


sol1='''sueldo= int(input("Ingrese su sueldo mensual sin decimales: "))
anual=sueldo*12
if anual>11310 :
    print("tiene que pagar impuesto")
else:
    print("no tiene que pagar impuestos")
'''

sol2='''for i in range(0,101,2):
    print(i)
'''
sol3='''nota=float(input("Ingrese su nota con decimales: "))
if nota>=6.00 :
    print("Aprobo la materia!")
else:
    falta= 6.00-nota
    print("Te falta %.2f para pasar"%falta)
'''
sol4='''placa=input("Ingrese una placa con el formato ABC-XY: ")
partes=placa.split("-")
if partes[0].isalpha() and partes[1].isdigit():
    print("Es una placa válida")
else:
    print("No es una placa válida")
'''
sol5='''estatura= float(input("Ingrese su estatura en metros (m): "))
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
sol6='''impuesto_mayor = 0
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
sol7='''import random as rd
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
sol8='''numero_ganador = ""
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
sol9='''L_tienda = [("cafe",3.50),("leche",1.50),("pan",0.25),("azucar",0.50),("pastel",5)]
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
sol10='''L_nombres_trabajadores = ["Javier", "Estefania", "Joselyn", "Humberto"]
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
'''



L_ejercicios = [ej1,ej2,ej3,ej4,ej5,ej6,ej7,ej8,ej9,ej10]
L_soluciones=[sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9,sol10]
indice_ejer = 0

# ------------------------------------------------CONSTANTES graficas---------------------------------------------------------------------

colorCajaTexto="azure"
# colorTodo="DodgerBlue4"
# colorTodo="IndianRed4"
colorTodo="DeepSkyBlue2"
# colorTodo="PaleGreen3"
colorTexto="white"
colorTitulo="white"

bdCuadro=5
# -------------------------------------------------------------------------------

raiz=Tk()

raiz.title("Analizador de codigo")
raiz.resizable(False,False) #solo permite no cambiar el ancho y no el alto
raiz.geometry("1100x690") #Tama;o de la pantalla
#raiz.wm_state("zoomed") # pantalla completa
# raiz.config(bg="white",bd="5",relief="groove",cursor="hand2")
raiz.config(bg=colorTodo,relief="groove",cursor="hand2",bd=5)


#------------------------------------------Cabezera----------------------------------------



# labelEjercicio=Label(raiz,bg="white",text="Ejercicio",fg="red",font=("Comic Sans MS",18)).place(x=10,y=10)
labelEjercicio=Label(raiz,bg=colorTodo,text="Ejercicio:  ",fg=colorTitulo,font=("Arial",18,"bold")).place(x=10,y=10)

# labelDescripcionEjercicio= Label(raiz,text=ej1,fg="black",font=("Comic Sans MS",12)).place(x=10,y=50)
lblDescripcion=Message(raiz,bg=colorTodo, text=ej1,fg=colorTexto, width=700,font=("Arial",12),justify=LEFT,padx=1, pady=20)
lblDescripcion.pack()

labelDescripcionEjercicio2= Label(raiz,bg=colorTodo,fg=colorTexto,text="  Ingrese su código aquí",font=("Arial",9)).place(x=10,y=125)



# ------------------------------------------------------------cajaCodificar------------------------------
miFrame= Frame(raiz,bg=colorTodo,width=15,height=10)
miFrame.pack()  # lo agrega encima de la raiz
miFrame.place(x=20,y=150)


textoCodificar=Text(miFrame,width=120,height=10,wrap=NONE,bd=bdCuadro,bg=colorCajaTexto)
textoCodificar.grid(row=0,column=0,padx=0,pady=0)


scrollVert=Scrollbar(miFrame,orient=VERTICAL, command=textoCodificar.yview)
scrollVert.grid(row=0,column=1,sticky="nsew")

scrollHorizontal=Scrollbar(miFrame,orient=HORIZONTAL, command=textoCodificar.xview)
scrollHorizontal.grid(row=1,column=0,sticky="nsew",pady=0)

textoCodificar.config(yscrollcommand=scrollVert.set) #solamente se activa si se escribe mas texto del que cabe en el cuadro de texto
textoCodificar.config(xscrollcommand=scrollHorizontal.set)


# --------------------------------frame contenedor de botones------------------------
miFrame5=Frame(raiz,bg=colorTodo,width=15,height=5)
miFrame5.pack()
miFrame5.place(x=10,y=350)



# --------------------------------------------------------frame contenedor--------------------------------
miFrame4= Frame(raiz,bg=colorTodo,width=15,height=10)
miFrame4.pack()
miFrame4.place(x=10,y=400)


# ------------------------------------------------------------cajaResultadoAnalisis------------------------------


miFrame2= Frame(miFrame4,bg=colorTodo,width=15,height=10)
miFrame2.pack()  # lo agrega encima de la raiz
miFrame2.place(x=10,y=150)
miFrame2.grid(row=0,column=0,padx=10,pady=10)

labelResultadoAnalisis=Label(miFrame2,bg=colorTodo,text="Resultado de Análisis",fg=colorTitulo,font=("Arial",20,"bold"))
labelResultadoAnalisis.grid(row=0,column=0,padx=10,pady=10)


textoResultadoAnalisis=Text(miFrame2,width=60,height=10,wrap=NONE,bd=bdCuadro,bg=colorCajaTexto)
textoResultadoAnalisis.grid(row=1,column=0,padx=0,pady=0)

scrollVert2=Scrollbar(miFrame2,orient=VERTICAL, command=textoResultadoAnalisis.yview)
scrollVert2.grid(row=1,column=1,sticky="nesw")

scrollHorizontal2=Scrollbar(miFrame2,orient=HORIZONTAL, command=textoResultadoAnalisis.xview)
scrollHorizontal2.grid(row=2,column=0,sticky="nsew")

textoResultadoAnalisis.config(yscrollcommand=scrollVert2.set) #solamente se activa si se escribe mas texto del que cabe en el cuadro de texto
textoResultadoAnalisis.config(xscrollcommand=scrollHorizontal2.set)

# ------------------------------------------------------------cajaRetroalimentacion------------------------------

miFrame3= Frame(miFrame4,bg=colorTodo,width=15,height=10)
#miFrame3.pack()  # lo agrega encima de la raiz
miFrame3.place(x=10,y=600)
miFrame3.grid(row=0,column=1,padx=10,pady=10)

labelRetroalimentacion=Label(miFrame3,bg=colorTodo,text="Retroalimentación",fg=colorTitulo,font=("Arial",20,"bold"))
labelRetroalimentacion.grid(row=0,column=0,padx=10,pady=10)

textoRetroalimentacion=Text(miFrame3,width=60,height=10,wrap=NONE,bd=bdCuadro,bg=colorCajaTexto)
textoRetroalimentacion.grid(row=1,column=0,padx=0,pady=0)

scrollVert3=Scrollbar(miFrame3,orient=VERTICAL, command=textoRetroalimentacion.yview)
scrollVert3.grid(row=1,column=1,sticky="nsew")

scrollHorizontal3=Scrollbar(miFrame3,orient=HORIZONTAL, command=textoRetroalimentacion.xview)
scrollHorizontal3.grid(row=2,column=0,sticky="nsew")

textoRetroalimentacion.config(yscrollcommand=scrollVert3.set) #solamente se activa si se escribe mas texto del que cabe en el cuadro de texto
textoRetroalimentacion.config(xscrollcommand=scrollHorizontal3.set)






# -----------------------------------variables globales------------------------------------
contador=1
filePath="prueba.py"
archivo=open(filePath,"w")
contador2=0
cadenaFinal=""
estaBienLexico=0
estaBienSintactico=0
ast="algo"

#--------------------------------------------funciones de los botones------------------------------

def limpiarTodo():
    global contador2
    global cadenaFinal
    global ast2
    global result_lex
    global result_sem
    global estaBienLexico
    global estaBienSintactico
    global botonSiguiente
    # global indice_ejer
    global textoCodificar
    global textoRetroalimentacion
    global textoResultadoAnalisis

    textoCodificar.delete(1.0, END)
    textoResultadoAnalisis.delete(1.0, END)
    textoRetroalimentacion.delete(1.0, END)

    estaBienLexico = 0
    estaBienSintactico = 0
    result_sem.clear()
    result_lex.clear()
    cadenaFinal = ""

def limpiarSinCajaCodificar():
    global contador2
    global cadenaFinal
    global ast2
    global result_lex
    global result_sem
    global estaBienLexico
    global estaBienSintactico
    global botonSiguiente
    # global indice_ejer
    global textoRetroalimentacion
    global textoResultadoAnalisis

    textoResultadoAnalisis.delete(1.0, END)
    textoRetroalimentacion.delete(1.0, END)

    estaBienLexico = 0
    estaBienSintactico = 0
    result_sem.clear()
    result_lex.clear()
    cadenaFinal = ""

def retroAlimentar():
    global textoRetroalimentacion
    global indice_ejer
    textoRetroalimentacion.delete(1.0,END)
    if indice_ejer < 10:
        textoRetroalimentacion.insert(1.0,L_soluciones[indice_ejer])


def validar():
    limpiarSinCajaCodificar()
    global contador2
    global cadenaFinal
    global ast2
    global result_lex
    global result_sem
    global estaBienLexico
    global estaBienSintactico
    global botonSiguiente
    global indice_ejer
    global textoRetroalimentacion
    global textoResultadoAnalisis


    data = textoCodificar.get(1.0, END)
    result_lex.clear()
    result_sem.clear()
    estaBienLexico=0
    estaBienSintactico=0
    contador2=0


    #----lexico

    prueba(data)
    #lista no vacia
    if result_lex_malo:
        for lex2 in result_lex:
            y=str(lex2)
            # y=y+"\n"

            #si encuentra un error lo imprime en la caja de texto
            if y.startswith("**"):
                L_lineas = y.split("\n")
                textoResultadoAnalisis.insert(1.0, L_lineas[0]+"\n")
                print("NO")
                # result_lex.clear()
                # break
                # return "s"
            else:
                contador2=contador2+1
                print("token valido")

    #lista vacia
    if len(result_lex)==contador2:
        estaBienLexico=1
        print("todo bien con el lexico")
        # cadenaFinal=cadenaFinal+"todo bien con el lexico\n"
        # textoResultadoAnalisis.insert(1.0,)

    #----sintactico de una linea
    # global ast
    # ast=parser.parse(data)
    # if len(result_sem)==0:
    #     estaBienSintactico=1
    #     print("todo bien en la semantica")
    #     cadenaFinal=cadenaFinal+"todo bien en la semantica\n"
    # else:
    #     for i in result_sem:
    #         textoResultadoAnalisis.insert(1.0, str(i))

    # ------------sintactico para cada linea
    global ast
    strina=str(data)
    Lineas=strina.split("\n")
    print(Lineas)
    for linea in Lineas:
        if linea=='':
            print("vacio")
        else:
            parser.parse(linea)



            # ast = parser.parse(linea)
            # if len(result_sem) == 0:
            #     estaBienSintactico = 1
            #     # print("todo bien en la semantica")
            #     # cadenaFinal = cadenaFinal + "todo bien en la semantica\n"
            # else:
            #     for i in result_sem:
            #         textoResultadoAnalisis.insert(1.0, str(i))

    if len(result_sem)==0:
        estaBienSintactico=1
        print("todo bien con el sintactico")
    for i in result_sem:
        textoResultadoAnalisis.insert(1.0, str(i))


    # ------------semantico----------------------
    #ejecuta el programa del chico y ve si da el mismo resultado esperado
    if estaBienLexico and estaBienSintactico:
        textoResultadoAnalisis.insert(1.0, "lexico y sintactico correcto")
        print("todo good")
        print(Lineas)
        archivo = open(filePath, "w")
        for linea in Lineas:
            archivo.write(linea+"\n")
        archivo.close()
        textoResultadoAnalisis.insert(1.0, "su archivo .py se creo con exito\n")

        # t2 = subprocess.run(['python', 'prueba.py'], stdout=subprocess.PIPE)
        # t2.returncode #muestra 0 si fue exitoso 1 si no
        # t2.stdout #muetra el resultado de correr el codigo
        # if t2.returncode:
        #     print("fue exitoso")






def siguiente():
    global indice_ejer
    indice_ejer += 1
    if indice_ejer<10:

        lblDescripcion.configure(text=L_ejercicios[indice_ejer])
        textoCodificar.delete('1.0', END)
        textoResultadoAnalisis.delete('1.0', END)
        textoRetroalimentacion.delete('1.0', END)
    if indice_ejer>=10:
        indice_ejer=9


#-------------------------botones----------------------------------------------------------------------
botonValidar=Button(miFrame5, text="Validar",fg="black",font=("Arial",11,"bold"),command=validar)
botonValidar.grid(row=0,column=0,sticky="w",padx=5,pady=0)


botonLimpiar=Button(miFrame5, text="Limpiar",fg="black",font=("Arial",11,"bold"),command=limpiarTodo)
botonLimpiar.grid(row=0,column=1,sticky="w",padx=5,pady=0)

botonMostrarRetroAlimentacion=Button(miFrame5, text="Retroalimentación",fg="black",font=("Arial",11,"bold"),command=retroAlimentar)
botonMostrarRetroAlimentacion.grid(row=0,column=2,sticky="w",padx=5,pady=0)

botonSiguiente=Button(miFrame5, text="Siguiente",fg="black",font=("Arial",11,"bold"),command=siguiente)
botonSiguiente.grid(row=0,column=3,sticky="w",padx=5,pady=0)




raiz.mainloop() #muestra la pantalla

