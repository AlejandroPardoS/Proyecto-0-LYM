"""Archivo para resolver el Proyecto 0 de LYM"""

#CAMBIAR TODO EL TEXTO A MINUSCULAS, EL LENGUAJE ES "NOT CASE-SENSITIVE", NO DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS
#DEFINIR EN LISTAS LOS COMANDOS DEL LENGUAJE CON SUS PARAMETROS/ SEPARADOS EN LOS Q RECIBEN 1 PARAMETRO Y LOS Q RECIBEN 2
#DEFINIR ESTRUCTURAS UNICAS(TOKENS) PARA ALGUNOS SIMBOLOS. EJ(#) PARA CUALQUIER NUMERO, (DIR) PARA CUALQUIER DIRECCION (ORI), (VAR), (PROC)
#CAMBIAR DIGITO POR DIGITO EN TOKENS, ENTRE MAS SIMPLE MEJOR
#EN CASO DE VARIABLES DEFINIDAS, ALMACENAR LAS VARIABLES EN UN DICCIONARIO CON SU RESPECTIVO VALOR (VAR:VAL)
#COMPARAR CON LAS LISTAS DE COMANDO LOS NUEVOS COMANDOS PARA CONOCER SINTACTICAMENTE SI SON CORRECTOS
#IMPORTA EL ORDEN DE VERIFICACION DEL CODIGO

#EJ LISTA DE COMANDOS

com_simples = ["walk(#);","leap(#);","turn(#);","turnto(#);","drop(#);","get(#);","grab(#);","letgo(#);"]
com_conjuntos = ["TODOS LOS COMANDOS QUE RECIBAN MAS DE 1 PARAMETRO"]
com_not = ["not: cond"]

#EJ SI defvar nom 0 ENTONCES, COMO CUALQUIER NÚMERO ES #
#defvar nom #
variables = {"nom":"#"}

#EJ LISTA DE TOKENS
NUM = ["1","2","3","4","5","6","7","8","9","0"]
ORI = ["north","south","east","west"] 
DIR = ["front, left, right, back"]

programa = "defVar nom 0\ndefVar x 0\ndefVar y 0\ndefVar one 0\ndefProc putCB (c, b )\n{\n\tdrop(c);\n\tletGo(b);\n\twalk(n)\n}\ndefProc goNorth()\n{\n\twhile can(walk(1, north)) { walk(1 , north)}\n}\ndefProc goWest()\n{\n\tif can(walk(1, west)) { walk(1, west)} else nop()\n}\n{\njump(3 ,3);\nputCB(2 ,1)\n}"
def funcion1 (programa):
    return programa
#print("El programa es: ", parser(programa))

def lexer (programa):
    programa = programa.lower()
    programa = programa.replace("\t", " ")
    programa = programa.replace("\n", " ")
    programa = programa.replace("\r", " ")
    lista_palabras = programa.split()   
    
    print(lista_palabras) #PROBLEMA SE QUEDAN PEGADAS ALGUNAS PALABRAS EJ "(3," O "walk(1," despegar
    for palabra in lista_palabras:
        #if len(palabra) >1:
            #palabra = palabra.split()
            #print(palabra)
        if palabra in NUM:
            #print(palabra)
            programa = programa.replace(palabra, "#")
        if palabra in ORI:
            programa = programa.replace(palabra, "ORI")
            
    print(programa)
    """tokens = []
    for palabra in lista:
        if "jump" in palabra:
            tokens.append(("jump", palabra))
            #ESTO ES EJEMPLO, MEJOR EMPEZAR DESDE 0
            
    print(tokens)"""
lexer(programa)