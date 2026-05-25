import math
from math import trunc


# ----------------------------------------------------------------------
# Clase que nos ayuda a representar una variable
# -----------------------------------------------------------------------
class Variable:
    def __init__(self, nombre, tipo, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor


# ----------------------------------------------------------------------
# Función para leer por teclado el valor para una asignarlo a una variable
# (Le agregue que no se puede asignar un valor string a una variable entera o real)
# -----------------------------------------------------------------------
def read(tabla_var, a):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    simbolos = "+-*/()<>=!&|^%$#@~{}"
    # se verifica la existencia de la variable a la que se le va a asignar el valor
    if (existe_var(tabla_var, a)):
        for var in tabla_var:
            if (var.nombre == a):
                # Se convierte el valor que se lee por teclado en el tipo correcto
                entrada = convertir_valor(input("Ingrese el valor de la variable: "))
                # se verifica que el tipo de la variable sea entero o real
                if (var.tipo == "integer" or var.tipo == "real"):
                    for e in str(entrada):
                        # si el caracter de la cadena es letra o simbolo no se puede asignar ese valor
                        if (e in letras or e in simbolos):
                            print("Error en la linea", numero_linea,
                                  "No se puede asignar un valor string a una variable entera o real :(")
                            break
                    else:
                        # si no se ha encontrado ningun caracter que no sea letra o simbolo se puede asignar el valor
                        var.valor = entrada
                        print("Se guardo el valor", var.valor, "en la variable", var.nombre)
                else:
                    # si directamente se lee un valor string se le asigna ese valor
                    var.valor = entrada
                    print("Se guardo el valor", var.valor, "en la variable", var.nombre)
    else:
        # Si no existe la variable se muestra un mensaje de error
        print("Error en la linea", numero_linea, "La variable con el nombre ", a,
              "no ha sido encontrada :( esto es de read")
    pass


# ----------------------------------------------------------------------
# Función para calcular el seno de una variable numerica
# -----------------------------------------------------------------------
def calcular_seno(tabla_var, a):
    # se verifica la existencia de la variable en la tabla
    if (existe_var(tabla_var, a)):
        for var in tabla_var:
            if (var.nombre == a):
                # se calcula el seno de la variable en radianes
                return math.sin(var.valor)


# ----------------------------------------------------------------------
# Función para calcular el coseno de una variable numerica
# -----------------------------------------------------------------------
def calcular_coseno(tabla_var, a):
    # se verifica la existencia de la variable en la tabla
    if (existe_var(tabla_var, a)):
        for var in tabla_var:
            if (var.nombre == a):
                # se calcula el coseno de la variable en radianes
                return math.cos(var.valor)


# ----------------------------------------------------------------------
# Función para calcular el logaritmo natural de una variable numerica
# -----------------------------------------------------------------------
def calcular_logaritmo(tabla_var, a):
    if (existe_var(tabla_var, a)):
        for var in tabla_var:
            if (var.nombre == a):
                return math.log(var.valor)


# ----------------------------------------------------------------------
# Función que agrega una variable a la tabla de variables
# -----------------------------------------------------------------------
def agrega_var(tabla_var, nombre, tipo):
    # Crea un objeto Variable y lo inicializa
    tabla_var.append(Variable(nombre, tipo, 0))
    pass


# ----------------------------------------------------------------------
# Función que verifica si un variable ya existe dentro de la tabla de variables
# -----------------------------------------------------------------------
def existe_var(tabla_var, nombre):
    # bandera para indicar si ya se encontro la variable
    encontrado = False
    for var in tabla_var:
        if (var.nombre == nombre):
            # si el nombre de la variable actual es igual a el nombre del parametro entonces
            # se encontro la variable
            encontrado = True
    return encontrado


# ----------------------------------------------------------------------
# Función para asignar un valor a una variable dentro de la tabla de variables
# -----------------------------------------------------------------------
def set_var(tabla_var, nombre, valor):
    # se verifica la existencia de la variable en la tabla
    if (existe_var(tabla_var, nombre)):
        # Se va buscando la variable en la tabla
        for var in tabla_var:
            # si coincide el nombre de alguna variable de la tabla con el nombre parametro entonces
            # se asigna el valor a la variable
            if (var.nombre == nombre):
                var.valor = valor
    else:
        print("Error en la linea", numero_linea, "La variable con el nombre ", nombre,
              "no ha sido encontrada :( esto es de set")
    return None


# ----------------------------------------------------------------------
# Función que retorna el tipo de una variable que se encuentra en la tabla de variables
# -----------------------------------------------------------------------
def get_tipo(tabla_var, nombre):
    # Se recorre la tabla en busca de la variable que tenga el nombre igual a el parametro nombre
    for var in tabla_var:
        if (var.nombre == nombre):
            # al localizar la variable se retorna su tipo
            return var.tipo
    print("Error en la linea", numero_linea, "La variable con el nombre ", nombre,
          "no ha sido localizada esto es Get tipo")
    pass


# ----------------------------------------------------------------------
# Función para retornar el valor de una variable dentro de la tabla de variables
# -----------------------------------------------------------------------
def get_valor(tabla_var, nombre):
    # se busca la variable solicitada
    for var in tabla_var:
        if (var.nombre == nombre):
            # se retorna el valor segun sea el tipo de dato correcto
            return convertir_valor(var.valor)
    print("Error en la linea", numero_linea, "La variable con el nombre ", nombre,
          "no ha sido localizada esto es get tipo")
    pass


# ----------------------------------------------------------------------
# Función que imprime las variables dentro de la tabla de variables
# -----------------------------------------------------------------------
def imprime_tabla_var(tabla_var):
    # para darle formato a la tabla
    print()
    print("Tabla de variables")
    print("nombre\t\ttipo\t\tvalor")
    # para cada variable imprime su nombre, tipo y valor
    for e in tabla_var:
        print(e.nombre, "\t\t", e.tipo, "\t\t", e.valor)
    return None


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es simbolo especial
# -----------------------------------------------------------------------
def es_simbolo_esp(cad):
    simbolos_especiales = "+-*\";,.:!#=%&/(){}[]<><=>=="
    # si la cadena esta en simbolos entonces retorna true
    return cad in simbolos_especiales


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es un operador
# -----------------------------------------------------------------------
def es_operador(cad):
    operadores = ["*", "/", "+", "-"]
    # si la cadena esta en operadores retorna true , en otro caso false
    return cad in operadores


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es un entero
# -----------------------------------------------------------------------
def es_entero(cad):
    # se intenta convertir la cadena a entero , si no se puede entonces se regresa
    # false y si se puedo retorna true
    try:
        int(cad)
        return True
    except:
        return False


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es un separador
# -----------------------------------------------------------------------
def es_separador(cad):
    sepadores = " \t\n"
    # retorna true si cad esta en separadores y si no entonces false
    return cad in sepadores


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es un id
# -----------------------------------------------------------------------
def es_id(cad):
    letras = "abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # si el primer caracter de la cadena es una minuscula o una mayuscula
    return (cad[0] in letras)


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es un tipo de dato
# -----------------------------------------------------------------------
def es_tipo(cad):
    tipos = ["boolean", "integer", "real", "string"]
    # si la cadena es alguno de los tipos validos entomces retorna true
    return (cad in tipos)


# ----------------------------------------------------------------------
# Función que ayuda a verificar si una cadena es una palabra reservada
# -----------------------------------------------------------------------
def es_palabra_res(cad):
    tipos = ["boolean", "integer", "real", "string"]
    control = ["for", "while", "end", "var"]
    io = ["write", "read"]
    palabras_reservadas = control + tipos + io
    # si la cadena es algun tipo valido o alguna palabra de control o de I/O
    # retorna true , en caso contrario retorna false
    return (cad in palabras_reservadas)


# ----------------------------------------------------------------------
# Función que ayuda a obtener la prioridad de los operadores
# -----------------------------------------------------------------------
def get_prioridad(operador):
    # retorna la clave correspondiente del diccionario segun el operador que se pasa como parametro
    return {"(": 1, ")": 2, "+": 3, "-": 3, "*": 4, "/": 4, "^": 5}.get(operador)


# ----------------------------------------------------------------------
# Función que pasa de una expresiín infija a una posfija
# -----------------------------------------------------------------------
def infija_a_posfija(infija):
    '''Convierte una expresión infija a una posfija'''
    pila = []
    salida = []
    # se recorre la expresión infija
    for e in infija:
        # si encontramos un ( entonces lo agregamos a la pila
        if e == '(':
            pila.append(e)
        elif e == ')':
            # mientras el ultimo elemento de la pila sea diferente de un ( se le agrega el valor en la pila a la salida
            # para formar la expresión correcta y al final se saca el (
            while pila[len(pila) - 1] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            # si e es un operador se verifica que la pila no sea vacia y que la prioridad del ultimo elemento en la pila
            # sea mayor o igual a la prioridad de e y si es así se le agrega a la salida el valor proxima de la pila
            while (len(pila) != 0) and (get_prioridad(e)) <= get_prioridad(pila[len(pila) - 1]):
                salida.append(pila.pop())
                # se agrega el nuevo operador (e)
            pila.append(e)
        else:
            # se agrega el valor e directamente a la pila
            salida.append(e)
            # este codigo es por si sobran elementos en la pila despues de hacer el proceso anterior
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida


# ----------------------------------------------------------------------
# Función que ayuda a convertir una cadena a el mejor tipo que pueda tomar
# -----------------------------------------------------------------------
def convertir_valor(valor):
    # intenta convertir a entero
    try:
        return int(valor)
    # si no puede simplemente pass
    except ValueError:
        pass

    # Intenta convertir a flotante
    try:
        return float(valor)
    # si no puede simplemente pass
    except ValueError:
        pass

    # Si no es un valor numerico solamente regresa la cadena original
    return valor


# ----------------------------------------------------------------------
# Función que resuelve una expresión posfija y retorna el valor correspondiente
# -----------------------------------------------------------------------
def evalua_posfija(tabla_var, posfija):
    pila = []
    if len(posfija) == 1:  # la expresion solo tiene un valor
        valor = convertir_valor(posfija[0])
        if type(valor) == 'str':  # es una variable
            return get_valor(tabla_var, valor)
        else:
            return valor
    else:  # la expresión tiene más de un elemento
        # se recorre la expresión
        for e in posfija:
            # si es un operador entonces se obtienen los operandos
            if es_operador(e):
                op2 = pila.pop()
                op1 = pila.pop()
                # se selecciona el operador correcto segun se requiera y se hace la operación
                if e == '*':
                    resultado = op1 * op2
                elif e == '+':
                    resultado = op1 + op2
                elif e == '/':
                    resultado = op1 / op2
                elif e == '-':
                    resultado = op1 - op2
                pila.append(resultado)
            else:  # es operando
                valor = convertir_valor(e)
                if type(valor) == str:  # es una variable
                    pila.append(get_valor(tabla_var, valor))
                else:
                    pila.append(valor)  # es un valor
    return (pila[0])


# ----------------------------------------------------------------------
# Función que ayuda a separar las instrucciones introducidas por tokens
# -----------------------------------------------------------------------
def tokeniza(linea):
    # si la instrucción es menor a 3 en longitud entonces regresa una lista vacia
    if len(linea) < 3:
        return []
    else:
        tokens = []
        tokens2 = []
        dentro = False
        # se recorré caracter por caracter de la linea
        for l in linea:
            # si es simbolo especial y no estamos dentro entonces se agrega a los tokens ese simbolo especial
            if es_simbolo_esp(l) and not (dentro):
                tokens.append(l)
            if (es_simbolo_esp(l) or es_separador(l)) and dentro:
                # si es simbolo especial o es esperador pero estamos dentro entonces se agrega la cadena formada a tokens
                # y dentro se hace falso
                tokens.append(cad)
                dentro = False
                if es_simbolo_esp(l):
                    # se agrega el simbolo especial que revisamos para no perderlo
                    tokens.append(l)
                    # Se comienza a formar una nueva palabra/token
            if not (es_simbolo_esp(l)) and not (es_separador(l)) and not (dentro):
                dentro = True
                cad = ""
                # Se agrega el caracter actual a la cadena que forma el token
            if not (es_simbolo_esp(l)) and not (es_separador(l)) and dentro:
                cad = cad + l

        # aqui se verifica si en la instruccion se presentan situaciones como == , <=, >= , etc
        compuesto = False
        for c in range(len(tokens) - 1):
            # si es compuesto entonces se niega la bandera y continuamos
            if compuesto:
                compuesto = False
                continue
                # si el caracter actual es un = , >, > , ! y el siguiente es un = entonces es un token compuesto
                # se agrega a tokens2 el simbolo inicial y despues se agrega el =
            if tokens[c] in "=<>!" and tokens[c + 1] == "=":
                tokens2.append(tokens[c] + "=")
                compuesto = True
            else:
                # si no es compuesto solo se agrega el token de tokens a tokens2
                tokens2.append(tokens[c])
                # si no hay tokens se regresa una lista vacia
        if not tokens:
            return []
        tokens2.append(tokens[-1])
        for c in range(1, len(tokens2) - 1):
            # si encontramos un . y lo que esta antes del punto encontramos un numero y tambien despues del punto entonces
            # se concatena el valor de el primer valor numerico , el punto y el segundo valor numerico y se colocá
            # borrar a las posiciones donde estaban los valores numericos
            if tokens2[c] == "." and es_entero(tokens2[c - 1]) and es_entero(tokens2[c + 1]):
                tokens2[c] = tokens2[c - 1] + tokens2[c] + tokens2[c + 1]
                tokens2[c - 1] = "borrar"
                tokens2[c + 1] = "borrar"
        porBorrar = tokens2.count("borrar")
        for c in range(porBorrar):
            # para eliminar los tokens con valor "borrar"
            tokens2.remove("borrar")
        tokens = []
        dentroCad = False
        cadena = ""

        for t in tokens2:
            # si verificamos que estamos dentro de una cadena entonces:
            if dentroCad:
                # verificamos que el ultimo caracter de la cadena sea " y si si:
                if t[-1] == '"':
                    # # Se termina de formar la cadena y se agrega sin las comillas
                    cadena = cadena + " " + t
                    tokens.append('"')
                    tokens.append(cadena[1:-1])
                    dentroCad = False
                else:
                    # Se sigue construyendo la cadena mientras no aparezca la comilla de cierre
                    cadena = cadena + " " + t
            elif ((t[0] == '"')):
                # Se detecta el inicio de una cadena entre comillas
                cadena = t;
                dentroCad = True
            else:
                tokens.append(t)

    if dentro:
        tokens.append(cad)
    return tokens


# ----------------------------------------------------------------------
# Función que abre un archivo txt y nos da las instrucciones linea por linea
# -----------------------------------------------------------------------
def cargar_Archivo(nombre):
    archivo = open(nombre, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

# ----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
def compara_valores(tabla_var, valor1, valor2, simbolo):
    if (existe_var(tabla_var, valor1)):
        primero = get_valor(tabla_var, valor1)
    else:
        primero = convertir_valor(valor1)
    if (existe_var(tabla_var, valor2)):
        segundo = get_valor(tabla_var, valor2)
    else:
        segundo = convertir_valor(valor2)
    if(simbolo == ">"):
        return primero > segundo
    elif(simbolo == "<"):
        return primero < segundo
    elif(simbolo == "=="):
        return primero == segundo
    elif(simbolo == ">="):
        return primero >= segundo
    elif(simbolo == "<="):
        return primero <= segundo
    elif(simbolo == "!="):
        return primero != segundo



# Aquí inicia el programa principal

# variables importantes para el programa
tabla_var = []
ren = ""
entro = False
rangos = []
indice_permitido = math.inf
lineas = cargar_Archivo("Programa1Final.txt")
numero_linea = 1
indice = 0
# se recorre linea por linea dentro del archivo txt
while(indice < len(lineas)):
    # se separa la linea actual en tokens



    datos = tokeniza(lineas[indice])




    # verificamos que la linea tenga información
    if (len(datos) > 0):


        if(len(rangos) > 1):
            if(indice >= rangos[0] and indice <= rangos[1] ):
                indice += 1
                continue
            if(indice > rangos[1]):
                rangos.pop(0)
                rangos.pop(0)
        elif(len(rangos) == 1):
            if(indice <= rangos[0] and not(entro) ):
                indice += 1
                continue


        # si en la instrucción se comienza con una palabra var verificamos si no existe ya y si no esta aun la
        # agregamos a la tabla de variables
        if(datos[0] == "end"):
            indice += 1
            continue
        if (datos[0] == 'var'):
            if not existe_var(tabla_var, datos[1]):
                agrega_var(tabla_var, datos[1], datos[2])
            else:
                print("Error en la linea", numero_linea, "La variable con el nombre ", datos[1], "ya ha sido declarada")
        elif (datos[0] == "read"):
            # si la instrucción comienza con read entonces se llama a la función read que lee el valor por teclado y
            # se lo asigna a la variable indicada
            read(tabla_var, datos[2])
        elif (datos[0]) == 'show_var':
            # si la instrucción comienza por show_var entonces se llama a la instruccioón necesaria para imprimir la tabla
            imprime_tabla_var(tabla_var)
            # si la instrucción comienza con un id pero que no es palabra reservada
        elif (datos[0] == "if"):
            if (datos[2] == ">"):

                entro = compara_valores(tabla_var, datos[1], datos[3], datos[2])
                if(entro):
                    indice_permitido = indice
                    datos = tokeniza(lineas[indice_permitido])
                    while(datos[0] != "else" and indice_permitido < len(lineas)):
                        indice_permitido += 1
                        if(indice_permitido < len(lineas)):
                            datos = tokeniza(lineas[indice_permitido])
                            if(len(datos) == 0):
                                indice_permitido += 1
                                if (indice_permitido < len(lineas)):
                                    datos = tokeniza(lineas[indice_permitido])

                    indice_permitido = indice_permitido

                    if(indice_permitido != len(lineas)):
                        rangos.append(indice_permitido)
                        encontre_else = True
                    else:
                        indice_permitido = indice
                        datos = tokeniza(lineas[indice_permitido])


                    while(datos[0] != "end"):
                        indice_permitido += 1
                        datos = tokeniza(lineas[indice_permitido])
                    #print(indice_permitido)
                    rangos.append(indice_permitido)
                    indice += 1
                    #print(rangos)
                    continue
                elif not(entro):
                    indice_permitido = indice
                    datos = tokeniza(lineas[indice_permitido])
                    while (datos[0] != "else" and indice_permitido < len(lineas)):
                        indice_permitido += 1
                        if (indice_permitido < len(lineas)):
                            datos = tokeniza(lineas[indice_permitido])
                            if (len(datos) == 0):
                                indice_permitido += 1
                                if (indice_permitido < len(lineas)):
                                    datos = tokeniza(lineas[indice_permitido])
                    if (indice_permitido != len(lineas)):
                            rangos.append(indice_permitido)
                            print(rangos)
                            encontre_else = True
                    else:
                        indice_permitido = indice
                        datos = tokeniza(lineas[indice_permitido])

                        while(datos[0] != "end" and indice_permitido < len(lineas)):
                            indice_permitido += 1
                            datos = tokeniza(lineas[indice_permitido])
                        rangos.append(indice_permitido)
                        indice += 1
                    continue





        elif (es_id(datos[0]) and not (es_palabra_res(datos[0]))):
            # y si en la posición 1 tiene un = y tambien un cos en la posición 2 entonces:
            if (datos[1] == "=" and datos[2] == "cos"):
                # se verifica que el tipo de la variable a asignar el valor no sea string y si es asi entonces se le
                # asigna el valor de llamda a la función de calcular coseno
                if not (get_tipo(tabla_var, datos[0]) == "string"):
                    set_var(tabla_var, datos[0], calcular_coseno(tabla_var, datos[4]))
                else:
                    print("No se puede asignar un valor real a una variable string de cos")
                # y si en la posición 1 tiene un = y tambien un sin en la posición 2 entonces:
            elif (datos[1] == "=" and datos[2] == "sin"):
                # se verifica que el tipo de la variable a asignar el valor no sea string y si es asi entonces se le
                # asigna el valor de llamda a la función de calcular seno
                if not (get_tipo(tabla_var, datos[0]) == "string"):
                    set_var(tabla_var, datos[0], calcular_seno(tabla_var, datos[4]))
                else:
                    print("No se puede asignar un valor real a una variable string de sin")
                # y si en la posición 1 tiene un = y tambien un log en la posición 2 entonces:
            elif (datos[1] == "=" and datos[2] == "log"):
                # se verifica que el tipo de la variable a asignar el valor no sea string y si es asi entonces se le
                # asigna el valor de llamda a la función de calcular logaritmo natural
                if not (get_tipo(tabla_var, datos[0]) == "string"):
                    set_var(tabla_var, datos[0], calcular_logaritmo(tabla_var, datos[4]))
                else:
                    print("No se puede asignar un valor real a una variable string de log")
            elif (datos[1] == "=" and datos[2] == '"'):
                if (existe_var(tabla_var, datos[0])):
                    set_var(tabla_var, datos[0], '"' + datos[3][1:-1] + '"')
                else:
                    print("Error en la linea", numero_linea, "La variable", datos[0], "no existe")
            elif (datos[1] == '='):  # es una asignacion de la forma a = expresion
                # Se convierte la expresion introducida a posfija
                posfija = infija_a_posfija(datos[2:])
                # se resuelve la expresion posfija y obtenemos el resultado
                resultado = evalua_posfija(tabla_var, posfija)
                # se le asigna el valor obtenido a la variable indicada(datos[0])
                set_var(tabla_var, datos[0], resultado)

        elif (datos[0]) == 'write':
            if datos[2] == '"':  # es de la forma write("hola")
                # se imprime en pantalla solamente lo que estan entre las comillas
                print(datos[3][1:-1])
            else:  # es de la forma write(valor)
                # se convierte el valor a el mejor tipo
                valor = convertir_valor(datos[2])
                # si el tipo de valor es string entonces se va a imprimir el valor de una variable
                if type(valor) == str:  # es de la forma write(variable)
                    print(get_valor(tabla_var, valor))
                else:
                    print(valor)

    #numero_linea += 1
    indice += 1
