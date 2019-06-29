import ply.lex as lex
import ply.yacc as yacc
from tkinter import *

# resultado del analisis
result_lex = []


# Palabras reservadas
reserved = {
    'import': 'IMPORT',  #
    'from': 'FROM',  #
    'input': 'INPUT',  #
    'split': 'SPLIT',  #
    'find': 'FIND',  #
    'index': 'INDEX',  #
    'isdigit': 'ISDIGIT',  #
    'isalpha': 'ISALPHA',  #
    'len': 'LEN',  #
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
    'MINUSMINUS',
    'PLUSPLUS',

    # operadores logicos
    'AND',
    'OR',
    'NOT',
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
t_MINUSMINUS = r'\-\-'
t_PUNTO = r'\.'
t_DOSPUNTOS = r'\:'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='

# Definicion de Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
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

def t_LISTA(t):
    r'\[(\w,|\w)+\]'
    return t
#
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
                | casting
                | CADENA """
    p[0] = p[1]

####################################################

def p_estructura_de_control(p):
    """ estructura_de_control : condicional_if
                              | condicional_else
                              | condicional_if_else
                              | bucle_for """
    p[0] = p[1]
def p_condicional_else(p):
    """condicional_else : ELSE DOSPUNTOS"""
    p[0] = p[1]

def p_condicional_if_else(p):
    """ condicional_if_else : condicional_if ELSE DOSPUNTOS"""
    p[0] = p[1]

def p_condicional_if(p):
    """condicional_if : IF expresion_logica DOSPUNTOS
                        | IF BOOLEAN DOSPUNTOS
                        | IF IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS"""
    p[0] = p[1]

def p_bucle_for(p):
    """ bucle_for : FOR IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS
                  | FOR IDENTIFICADOR IN range DOSPUNTOS"""
    p[0] = p[1]
#####################################################

def p_expresion_logica(p):
    """expresion_logica : dato comparador dato"""
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
                | DIV """
    p[0] = p[1]

####################################


#####################################

def p_funcion(p):
    """ funcion : funcion_print
                | funcion_random_randint
                | funcion_input"""
    p[0] = p[1]

def p_funcion_print(p):
    """ funcion_print : PRINT PARIZQ PARDER
                        | PRINT PARIZQ CADENA PARDER
                        | PRINT TUPLA_SIMPLE
                        | PRINT TUPLA_DOBLE
                        | PRINT TUPLA_TRIPLE
                        | PRINT TUPLA """
    p[0] = p[1]

def p_funcion_random_randint(p):
    """funcion_random_randint : RANDOM PUNTO RANDINT TUPLA_SIMPLE
                             | RANDOM PUNTO RANDINT TUPLA_DOBLE """
    p[0] = p[1]

def p_funcion_input(p):
    """ funcion_input : INPUT PARIZQ CADENA PARDER
                        | INPUT PARIZQ PARDER"""
    p[0] = p[1]

def p_range(p):
    """ range : RANGE TUPLA_SIMPLE
                | RANGE TUPLA_DOBLE
                | RANGE TUPLA_TRIPLE"""
    p[0] = p[1]

###############################
def p_dato(p):
     """ dato : IDENTIFICADOR
                | FLOTANTE
                | INTEGER
                | CADENA"""
     p[0] = p[1]


parser = yacc.yacc()

#------------------------------------prueba del yacc por consola---------------------

prop = """sueldo = int(input("Ingrese su sueldo mensual sin decimales: "))
anual = sueldo*12
if anual>11310:
    print("tiene que pagar impuesto")
else:
    print("no tiene que pagar impuestos")"""

for linea in prop.split("\n"):
    parser.parse(linea)
    print(linea + ': OC')
while True:
    s = input('> ')
    parser.parse(s)
