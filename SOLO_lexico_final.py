import ply.lex as lex
import ply.yacc as yacc
from tkinter import *

# resultado del analisis
result_lex = []


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
    r'\[\w+\]'
    return t
def t_LISTA_DOBLE(t):
    r'\[\w,\w\]'
    return t

def t_LISTA_TRIPLE(p):
    r'\[\w,\w\,\w]'
    return t

def t_LISTA(t):
    r'\[(\w,|\w)+\]'
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
    p[0] = p[1]

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
                        | IF IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS"""
    p[0] = p[1]

def p_bucle_for(p):
    """ bucle_for : FOR IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS
                  | FOR IDENTIFICADOR IN range DOSPUNTOS"""
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
                    | IDENTIFICADOR ASIGNAR casting"""
    names[p[1]] = p[3]

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
    """ operacion : dato operador dato"""
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
                    | TUPLA"""
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
                        | PRINT TUPLA_SIMPLE
                        | PRINT TUPLA_DOBLE
                        | PRINT TUPLA_TRIPLE
                        | PRINT TUPLA """
    p[0] = p[1]

def p_funcion_random_randint(p):
    """funcion_random_randint : RANDOM PUNTO RANDINT TUPLA_SIMPLE
                             | RANDOM PUNTO RANDINT TUPLA_DOBLE
                             | IDENTIFICADOR PUNTO RANDINT TUPLA_SIMPLE
                             | IDENTIFICADOR PUNTO RANDINT TUPLA_DOBLE"""
    p[0] = p[1]

def p_funcion_input(p):
    """ funcion_input : INPUT PARIZQ CADENA PARDER
                        | INPUT PARIZQ PARDER"""
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
                | identificador_atributo
                | identificador_slicing"""
     p[0] = p[1]

def p_empty(p):
    'empty :'
    pass


parser = yacc.yacc()

#------------------------------------prueba del yacc por consola---------------------

prop1 = """sueldo = int(input("Ingrese su sueldo mensual sin decimales: "))
anual = sueldo * 12
if anual > 11310:
    print("tiene que pagar impuesto")
else:
    print("no tiene que pagar impuestos")"""

prop2 = """for i in range(0,101,2):
    print(i)"""

prop3 = """nota = float(input("Ingrese su nota con decimales: "))
if nota>=6.00 :
    print("Aprobo la materia!")
else:
    falta = 6.00 - nota
    print("Te falta %.2f para pasar"%falta)"""

prop4 = """placa=input("Ingrese una placa con el formato ABC-XY: ")
partes=placa.split("-")
if partes[0].isalpha() and partes[1].isdigit():
    print("Es una placa válida")
else:
    print("No es una placa válida")"""

prop5 = """estatura= float(input("Ingrese su estatura en metros (m): "))
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
    print("Su indice de masa corporal es el correcta para su estatura y peso")"""

prop6 = """impuesto_mayor = 0
nombre_mayor = ""

n_trabajadores =  input("Ingrese el numero de trabajores a procesar: ")
if n_trabajadores.isdigit():
    n_trabajadores = int(n_trabajadores)

    for trabajador in range(n_trabajadores):
        print("Ingrese el nombre y sueldo del trabajador con el siguiente formato: nombre,sueldo")
        nombre,sueldo = input("Datos empleado %i :"%trabajador).split(",")
        sueldo=float(sueldo)
        impuesto = sueldo*0.05
        if impuesto > impuesto_mayor:
            impuesto_mayor = impuesto
            nombre_mayor = nombre
print("El trabajador que paga mas impuestos es %s  que paga %.2f"%(nombre_mayor,impuesto_mayor))"""

prop7 = """import random as rd
ale = rd.randint(0,50)
juego_terminado = False
for vida in range(5):
    if not juego_terminado:
        n = int(input("Que numero del 1 al 50 crees que salio?: "))
        if n==ale:
            juego_terminado = True
        else:
            if n < ale:
                print("Su numero es menor que el objetivo")
            else:
                print("Su numero es mayor que el objetivo")
if juego_terminado:
    print("Felicidades ganaste")
else:
    print("Perdiste!, el numero era %d"%ale)"""

prop8 = """
import random as rd

numero_ganador = "."
for i in range(5):
    aleatorio = rd.randint(0,9)
    numero_ganador += str(aleatorio)

usuario = input("Ingrese su numero de loteria: ")

if usuario == numero_ganador:
    print("Usted gano el premio mayor!")
else:
    if usuario[-1]:
        print("Usted gano un reintegro")
    else:
        print("Siga participado")"""

prop9 = """L_tienda = [("cafe",3.50),("leche",1.50),("pan",0.25),("azucar",0.50),("pastel",5)]
dinero = float(input("Ingrese la cantidad de dinero disponible: "))
for tupla in L_tienda:
    nombre = tupla[0]
    valor =tupla[1]
    print("\nProducto: %s valor: %.2f "%(nombre.upper(),valor))
    comprar = input("Desea comprar el producto? Ingrese si o no\n").lower()
    if comprar == "si":
        if dinero >= valor:
            dinero-=valor
            print("==Usted compro: %s y le quedan %.2f en de dinero disponible=="%(nombre,dinero))
        else:
            print("Ya no tiene dinero disponible para comprar")"""

prop10 = """L_nombres_trabajadores = ["Javier", "Estefania", "Joselyn", "Humberto"]
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

print("El promedio de edad de los empleados con IMC elevado es %.2f" % promedio)"""

L_prop = [prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9,prop10]

for i in range(len(L_prop)):
    print("===============Analizando propuesta de solucion %d ============\nReporte de Errores:"%(i+1))
    for linea in L_prop[i].split("\n"):
        parser.parse(linea)
        z = input("Intro para seguiente ejercicio")
        break
        #print(linea + ' <Ok>')
    print()
while True:
    s = input('> ')
    parser.parse(s)
