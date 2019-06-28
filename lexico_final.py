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
    'int': 'INT',
    'slice': 'SLICE',  #
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'range':'RANGE',
    'print' : 'PRINT',
    'random':'RANDOM',
    'randint': 'RANDINT',
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
    'FLOAT',
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


def t_FLOAT(t):
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
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
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
                | funcion """
    p[0] = p[1]

def p_estructura_de_control(p):
    """ estructura_de_control : condicional_if
                              | condicional_if_else
                              | bucle_for """
    p[0] = p[1]

def p_condicional_if_else(p):
    """ condicional_if_else : condicional_if ELSE DOSPUNTOS entrada"""
    p[0] = p[1]

def p_condicional_if(p):
    """condicional_if : IF expresion_logica DOSPUNTOS entrada
                        | IF BOOLEAN DOSPUNTOS entrada"""
    p[0] = p[1]

def p_bucle_for(p):
    """ bucle_for : FOR IDENTIFICADOR IN IDENTIFICADOR DOSPUNTOS entrada
                  | FOR IDENTIFICADOR IN range DOSPUNTOS entrada"""
    p[0] = p[1]

def p_expresion_logica(p):
    """expresion_logica : dato comparador dato"""
    if p[2] == '==': p[0] = p[1] == p[3]
    if p[2] == '!=': p[0] = p[1] != p[3]
    if p[2] == '>': p[0] = p[1] > p[3]
    if p[2] == '<': p[0] = p[1] < p[3]
    if p[2] == '>=' : p[0] = p[1] >= p[3]
    if p[2] == '<=' : p[0] = p[1] <= p[3]

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
                    | IDENTIFICADOR ASIGNAR dato"""
    names[p[1]] = p[3]


def p_operacion(p):
    """ operacion : dato operador dato"""
    if p[2] == '+': p[0] = p[1] + p[3]
    if p[2] == '-': p[0] = p[1] - p[3]
    if p[2] == '*': p[0] = p[1] * p[3]
    if p[2] == '/': p[0] = p[1] / p[3]

def p_operador(p):
    """ operador : SUMA
                | RESTA
                | MULT
                | DIV """
    p[0] = p[1]

def p_funcion(p):
    """ funcion : funcion_print
                | funcion_random"""
    p[0] = p[1]

def p_funcion_print(p):
    """ funcion_print : PRINT PARIZQ PARDER
                        | PRINT PARIZQ CADENA PARDER
                        | PRINT TUPLA_SIMPLE
                        | PRINT TUPLA_DOBLE
                        | PRINT TUPLA_TRIPLE
                        | PRINT TUPLA """
    p[0] = p[1]

def p_funcion_random(p):
    """funcion_random : RANDOM PUNTO RANDINT TUPLA_SIMPLE
                        | RANDOM PUNTO RANDINT TUPLA_DOBLE """
    p[0] = p[1]

def p_range(p):
    """ range : RANGE TUPLA_SIMPLE
                | RANGE TUPLA_DOBLE
                | RANGE TUPLA_TRIPLE"""
    p[0] = p[1]

def p_dato(p):
     """ dato : IDENTIFICADOR
                | FLOAT
                | INTEGER"""
     p[0] = p[1]


parser = yacc.yacc()

#------------------------------------prueba del yacc por consola---------------------

print("Ingrese la expresion semantica a evaluar")
while True:
    s = input('> ')
    parser.parse(s)





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

L_ejercicios = [ej1,ej2,ej3,ej4,ej5,ej6,ej7,ej8,ej9,ej10]
indice_ejer = 0



colorCajaTexto="azure"
# colorTodo="DodgerBlue4"
# colorTodo="IndianRed4"
colorTodo="DeepSkyBlue2"
# colorTodo="PaleGreen3"
colorTexto="white"
colorTitulo="white"

bdCuadro=5

raiz=Tk()

raiz.title("Analizador de codigo")
raiz.resizable(False,False) #solo permite no cambiar el ancho y no el alto
raiz.geometry("1100x690") #Tama;o de la pantalla
#raiz.wm_state("zoomed") # pantalla completa
# raiz.config(bg="white",bd="5",relief="groove",cursor="hand2")
raiz.config(bg=colorTodo,relief="groove",cursor="hand2",bd=5)


entrada=StringVar()

ast="algo"
ast2="algo"




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


textoResultadoAnalisis=Text(miFrame2,width=55,height=10,wrap=NONE,bd=bdCuadro,bg=colorCajaTexto)
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

textoRetroalimentacion=Text(miFrame3,width=55,height=10,wrap=NONE,bd=bdCuadro,bg=colorCajaTexto)
textoRetroalimentacion.grid(row=1,column=0,padx=0,pady=0)

scrollVert3=Scrollbar(miFrame3,orient=VERTICAL, command=textoRetroalimentacion.yview)
scrollVert3.grid(row=1,column=1,sticky="nsew")

scrollHorizontal3=Scrollbar(miFrame3,orient=HORIZONTAL, command=textoRetroalimentacion.xview)
scrollHorizontal3.grid(row=2,column=0,sticky="nsew")

textoRetroalimentacion.config(yscrollcommand=scrollVert3.set) #solamente se activa si se escribe mas texto del que cabe en el cuadro de texto
textoRetroalimentacion.config(xscrollcommand=scrollHorizontal3.set)





#--------------------------------------------funciones de los botones------------------------------

contador=1
filePath="prueba.py"
archivo=open(filePath,"w")
contador2=0

def validar():
    textoResultadoAnalisis.delete(1.0, END)
    data = textoCodificar.get(1.0, END)
    global contador2
    global ast2

    #----lexico

    prueba(data)
    #lista no vacia
    if result_lex_malo:
        for lex2 in result_lex:
            y=str(lex2)

            # print(type(lex2))
            # print(lex2)
            #si encuentra un error lo imprime en la caja de texto
            if y.startswith("**"):
                textoResultadoAnalisis.insert(1.0, y)
            else:
                contador2=contador2+1
                print("token valido")
            # if ":" in lex:
            #   print()


    #lista vacia
    if len(result_lex)==contador2:
        print("todo bien con el lexico")
        textoResultadoAnalisis.insert(1.0,"todo bien con el lexico")

    #----sintactico


    # print(data)
    #textoResultadoAnalisis.delete(1.0, END)
    #textoResultadoAnalisis.insert(1.0, data)





def siguiente():
    global indice_ejer
    indice_ejer += 1
    if indice_ejer<10:
        lblDescripcion.configure(text=L_ejercicios[indice_ejer])
        textoCodificar.delete('1.0', END)
        textoResultadoAnalisis.delete('1.0', END)
        textoRetroalimentacion.delete('1.0', END)



#-------------------------botones----------------------------------------------------------------------
# botonValidar=Button(raiz, text="Enviar",command=codigoBoton)
# botonValidar.pack()

botonValidar=Button(miFrame, text="Validar",fg="black",font=("Arial",11,"bold"),command=validar)
botonValidar.grid(row=2,column=0,sticky="w",padx=0,pady=0)


botonSiguiente=Button(miFrame, text="Siguiente",fg="black",font=("Arial",11,"bold"),command=siguiente)
botonSiguiente.grid(row=3,column=0,sticky="w",padx=0,pady=0)





raiz.mainloop() #muestra la pantalla

