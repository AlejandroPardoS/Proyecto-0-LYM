"""Archivo para resolver el Proyecto 0 de LYM"""

#CAMBIAR TODO EL TEXTO A MINUSCULAS, EL LENGUAJE ES "NOT CASE-SENSITIVE", NO DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS
#DEFINIR EN LISTAS LOS COMANDOS DEL LENGUAJE CON SUS PARAMETROS/ SEPARADOS EN LOS Q RECIBEN 1 PARAMETRO Y LOS Q RECIBEN 2
#DEFINIR ESTRUCTURAS UNICAS(TOKENS) PARA ALGUNOS SIMBOLOS. EJ(#) PARA CUALQUIER NUMERO, (DIR) PARA CUALQUIER DIRECCION (ORI), (VAR), (PROC)
#CAMBIAR DIGITO POR DIGITO EN TOKENS, ENTRE MAS SIMPLE MEJOR
#EN CASO DE VARIABLES DEFINIDAS, ALMACENAR LAS VARIABLES EN UN DICCIONARIO CON SU RESPECTIVO VALOR (VAR:VAL)
#COMPARAR CON LAS LISTAS DE COMANDO LOS NUEVOS COMANDOS PARA CONOCER SINTACTICAMENTE SI SON CORRECTOS
#IMPORTA EL ORDEN DE VERIFICACION DEL CODIGO

#EJ LISTA DE COMANDOS

com_simples = ["walk(#)","leap(#)","turn(#)","turnto(#)","drop(#)","get(#)","grab(#)","letgo(#)"]
com_conjuntos = ["TODOS LOS COMANDOS QUE RECIBAN MAS DE 1 PARAMETRO"]
com_not = ["not: cond"]

#EJ SI defvar nom 0 ENTONCES, COMO CUALQUIER NÚMERO ES #
#defvar nom #
variables = {"nom":"#"}

#EJ LISTA DE TOKENS
"#" = ["1","2","3","4","5","6","7","8","9","0"]
"ORI" = ["north","south","east","west"] 
"DIR" = ["front, left, right, back"]

programa = str(input("Ingrese el programa: "))
def funcion1 (programa):
    return programa
#print("El programa es: ", parser(programa))

def lexer (programa):
    programa.replace("\t", "")
    programa.replace("\n", "")
    #cambiar todo a minusculas  
    lista = programa.split(" ")
    print(lista)
    tokens = []
    for palabra in lista:
        if "jump" in palabra:
            tokens.append(("jump", palabra))
            
    print(tokens)
lexer(programa)