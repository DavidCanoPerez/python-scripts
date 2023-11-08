# -*- coding: utf-8 -*-

"""
    https://recursospython.com/guias-y-manuales/palabras-reservadas-del-lenguaje/
    https://ellibrodepython.com/palabras-reservadas-python
"""

"""
    practicar estos ejemplos también en intérprete, 

    palabras reservadas en python
    
    el módulo keyword (keyword.py) se distribuye junto con la librería estándar 
    es generado automáticamente a partir del archivo graminit.c 
    perteneciente al código de fuente del intérprete 
    incorpora una lista que contiene el conjunto de palabras resevadas, 
    permite comprobar la definición de un keyword
    
    comprobar en intérprete:
        >>> from keyword import iskeyword, kwlist
        >>> kwlist
        >>> iskeyword("and")
        >>> iskeyword("print")
    
    además la función help() puede recibir como argumento el 
    nombre de una palabra reservada como una cadena y mostrar su uso
        >>> help("import")

    sobre el orden
        comienza por mayúscula: False, None y True
        comienza en guión bajo: __peg_parser__
        todo minúscula: and ... yield
"""

""" ---------------------------------------------------------------------------------------------
    False
        valor booleano, 
        resultado de operaciones de comparación u operaciones lógicas
"""

""" ---------------------------------------------------------------------------------------------
    None
        representa a un valor nulo
"""

# se devuelve por defecto cuando una función no cuenta con un return
def function_none():
    pass
print("NONE ejemplo:", function_none())


""" ---------------------------------------------------------------------------------------------
    True
        valor booleano, contrario a False, 
        resultado de operaciones de comparación u operaciones logicas
"""

""" ---------------------------------------------------------------------------------------------
    __peg_parser__
        Llamado huevo de pascua, relacionado con el lanzamiento del nuevo analizador PEG no 
        está definido aún.
"""

""" ---------------------------------------------------------------------------------------------
    and
        operador lógico
"""

condition1= True
condition2= True   # probar a cambiar a False
if condition1 and condition2 == True:
    print("AND ejemplo, True")

""" ---------------------------------------------------------------------------------------------
    as
        crea un alias al importar un módulo.
"""

# ejemplo 1
import tkinter as tk

# ejemplo 2, tratar un objeto con encapsulacion a partir de un import, ver ejemplo with
import socket
with socket.socket() as s:
    ...
    s.close()


""" ---------------------------------------------------------------------------------------------
    assert
        se utiliza con fines de depuración
"""

""" ---------------------------------------------------------------------------------------------
    async
        se utiliza en código concurrente
        se emplea para definir una función como asíncrona 
"""

async def a_f():
    pass


""" ---------------------------------------------------------------------------------------------
    await
        se utiliza en código concurrente
        proporcionada por la biblioteca 'asyncio'
        
        sólo puede ser invocada desde una función asíncrona
        pausa la ejecución de la función hasta que el resultado esté disponible
"""

"""
import asyncio
async def e():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
asyncio.run(e())
"""



""" ---------------------------------------------------------------------------------------------
    break
        se utiliza en el interior de los bucles for y while para alterar su comportamiento normal
"""

# bucle infinito
while True:
    print("BREAK bucle infinito roto")
    break  # puede romper el bucle infinito

# ejemplo for
for i in range(10):
    if i == 4:
        break
    else:
        print("BREAK for roto en 4 de 10", i)
        # out: su salida normal sería de 0 a 9
        # out: con este break es de 0 a 4


""" ---------------------------------------------------------------------------------------------
    class
        define una nueva clase
"""

class Ejemplo:
    def __init__(self):     # metodo que se ejecuta inmediatamente al crear objeto de la clase
        print("CLASE de ejemplo")
e = Ejemplo()


""" ---------------------------------------------------------------------------------------------
    continue
        se utiliza en el interior de los bucles for y while
"""

for i in range(5):  # bucle de 0 a 4
    if i == 3:
        continue
    print("CONTINUE for", i)
    # notese que break rompería el bucle. out: 0,1,2,3
    # continue vuelve a la primera linea del bucle. out: 0,1,2,4
    
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:   # cuando el número es par se vuelve al princio sin print
        continue
    print("CONTINUE while", num)


""" ---------------------------------------------------------------------------------------------
    def 
        define una función 
"""

def func(a):
    print(a)
func("DEF ejemplo")


""" ---------------------------------------------------------------------------------------------
    del
        eliminar un objeto
"""

example_list = [1, 2, 3, 4, 5]
del example_list[1]
print("DEL en lista", example_list) #out: ejemplo del en lista [1, 3, 4, 5]

example_dictionary = { 'name': 'David',
                       'age': 37,
                       'id': '0328783'
                     }
del example_dictionary['age']
print("DEL en diccionario", example_dictionary)
# out: ejemplo del en diccionario {'name': 'David', 'id': '0328783'}

# a diferencia de las listas y diccionarios, no se admite borrar elemento en tuplas
tupla = (1, 2, 3)
# del tupla[1] # produce error
# sin embargo, como cualquier objeto si se puede eliminar toda la tupla
del tupla


""" ---------------------------------------------------------------------------------------------
    elif
        se usa en declaraciones condicionales, igual 'else' e 'if'
"""



""" ---------------------------------------------------------------------------------------------
    else
        se usa en declaraciones condicionales, igual 'elif' e 'if'
        también se utiliza en excepciones
"""


""" ---------------------------------------------------------------------------------------------
    except
        se usa para crear excepciones
        qué hacer cuando ocurre una excepción, igual que 'raise' y 'try'
"""


""" ---------------------------------------------------------------------------------------------
    finally 
        Su uso garantiza que el bloque de código dentro de él se ejecute incluso si 
        hay excepción no controlada
"""

def control_exception_func():
    print("FINALLY función control del posible error")
try:
    func()  # no ha sido definida, pero no se produce error en ejecución
except Exception:
    print("FINALLY Ha ocurrido un error")
else:
    print("Ejecutado exitosamente.")
finally:
    control_exception_func()


""" ---------------------------------------------------------------------------------------------
    for
        uno de los bucles principales junto con while
"""

# ejemplo 1
for i in (1, 2, 3):     # bucle de 1 a 3
    print("FOR ejemplo1", i)

# ejemplo 2
for i in range(5):      # bucle de 0 a 4
    print("FOR ejemplo2", i)


""" ---------------------------------------------------------------------------------------------
    from
        importa partes específicas de un módulo
"""

from PyQt5.QtWidgets import QApplication


""" ---------------------------------------------------------------------------------------------
    global
        declarar una variable global
"""


""" ---------------------------------------------------------------------------------------------
    if
        declaraciones condicionales, 
        se complementa con 'elif' y 'else' también reservadas
"""

var = 1     # probar valores 1,2,3 y otros
if var == 1:
    print("IF ejemplo, valor 1")
elif var == 2:
    print("IF ejemplo, valor 2")
elif var == 3:
    print("IF ejemplo, valor 3")
else:
    print("IF ejemplo, valor 4")

""" ---------------------------------------------------------------------------------------------
    import
        importa un módulo
"""

import numpy

import tkinter as tk

""" ---------------------------------------------------------------------------------------------
    in
        comprueba si un valor está presente en una lista, tupla, etc. 
        devuelve True si el valor está presente, por el contrario devuelve False
"""

""" ---------------------------------------------------------------------------------------------
    is
        Se usa para probar si las dos variables se refieren al mismo objeto. 
        Devuelve True si los objetos son idénticos y False si no
"""

""" ---------------------------------------------------------------------------------------------
    lambda
        equivale a una función
        que puede ser anónima, también se puede declarar su nombre
        
    sintaxis: 
            lambda args: result
            func_name = lambda args: result
    equivalente a:
            def func_name(args):
                return result
            
"""

def f(x, y, z=1):
    return (x+y) * z
re1 = f(1, 2, 3)
print(f"LAMBDA function no lambda: {re1}")


f = lambda x, y, z=1: (x+y) * z
re2 = f(1, 2, 3)
print(f"LAMBDA function lambda: {re2}")


""" ---------------------------------------------------------------------------------------------
    nonlocal
        declara una variable u objeto no local
"""

def a():
    i = 1
    def b():
        nonlocal i # permite modificar i
        i = 2
    b()
    print("NONLOCAL", i)
a()

""" ---------------------------------------------------------------------------------------------
    not
        operador lógico    
"""

# ejemplo 1
print("NOT ejemplo", not True)
print("NOT ejemplo", not False)

# ejemplo 2
""" ejemplo not intérprete:
    >>> not True        out: False
    >>> not False       out: True
    """

# ejemplo 3
""" ejemplo not intérprete:
    >>> x = 1
    >>> y = 10
    >>> x > y           out: False
    >>> not x > y       out:True
    """

""" ---------------------------------------------------------------------------------------------
    or
        operador lógico
"""

print("OR", True or False)
print("OR", True or True)
print("OR", False or False)


""" ejemplo or intérprete:
    >>> True or False    #out: True
    >>> True or True     #out: True
    >>> False or False   #out: False
    """

""" ---------------------------------------------------------------------------------------------
    pass
        es utilizada para rellenar espacios requeridos por sintaxis para evitar errores
        
        en ocasiones se considera una declaración nula, ya que no pasa nada cuando se ejecuta 
        
"""

def f():
    pass
        # no se puede escribir una función vacía    
        # empleada temporalmente hasta programar definitivamente la función
f()

def f_finalizada():
    pass
    print("PASS ejemplo")
f_finalizada()

""" ---------------------------------------------------------------------------------------------
    raise
        se usa para crear excepciones, qué hacer cuando ocurre una excepción, 
        igual que 'except' y 'try'
"""

""" ejemplo en intérprete
    raise NameError
    out: NameError
    """


""" ---------------------------------------------------------------------------------------------
    return
        se usa en una función para devolver un valor como resultado de operaciones

    posibilidades:
        return de un valor
        return de varios valores
        return None
        return vacío (return void).
        función sin return
        
    el valor puede ser:
        cadena o string
        un número
        un booleano
        una lista
        un diccionario
        ...
"""

# ejemplo 1, enteros a sumar
n1=1
n2=2
def s():
    suma = n1 + n2 
    return suma
print("RETURN ejemplo1, la suma da:", s())

# ejemplo 2, return string a variable
def filter():
    if n1 % 2 == 0:
        return "par"
    if n1 % 2 != 0:
        return "impar"
filter_result = filter()      # recoger string
print("RETURN ejemplo2:", filter_result)

# ejemplo 3, None
    # mismo ejemplo visto en palabra reservada None
    # se devuelve por defecto cuando una función no cuenta con un return
def function_none():
    pass
print("RETURN ejemplo3:", function_none())


""" ---------------------------------------------------------------------------------------------
    try
        se usa junto con 'except' para crear excepciones 
"""

try:
    this_func_does_not_exist()
except Exception:
    print("TRY error indicado sin excepción propagada")


""" ---------------------------------------------------------------------------------------------
    while
        Se usa para realizar bucles.
"""

# bucle infinito
while True:
    print("WHILE bucle inifinito")
    break  # break puede romper el bucle infinito

# otro bucle
var = 1
while var < 3:
    print("WHILE procesando", var)
    var += 1 # incrementa valor de variable var en 1


""" ---------------------------------------------------------------------------------------------
    with
        se usa para simplificar el manejo de excepciones
        de forma compleja encapsula bloques de código
"""

# uso, simple, 
import socket
with socket.socket() as s:
    print("WITH uso simple")
    ...
    s.close()

# uso, complejo
    # encapsula ejecución de un bloque de código, de modo que
    # la inicialización y finalización de un objeto es realizada automáticamente 
    # automatizando las funciones __enter__ y __exit__
    # ver:      https://peps.python.org/pep-0343/
    
    # se usa mucho al manejar ficheros
    # en este ejemplo cerraría el archivo antes de propagarse la excepción
    
try:
    with open("file.txt") as f:
        raise Exception
except Exception:
    print ("WITH uso complejo")


""" ---------------------------------------------------------------------------------------------
    yield
        se comporta de forma similar a return, con la diferencia de que en lugar de 
        retornar un valor, retorna elementos que forman parte un generador, 
        es la palabra yield la que transforma la función en un generador,
        
        https://docs.python.org/3/reference/expressions.html#yieldexpr
"""

def f():
    yield 1
    yield 2

obj = f()
for i in obj:
    print("YIELD ejemplo1, resultado", i)

print("YIELD ejemplo2")
def generador(max):
    print("  --Dentro de generador - empezando")
    n=0
    while n < max:
        print(f"  --Dentro de generador - yield con n={n}")
        yield n
        print("  --Dentro de generador - después de yield")
        n=n+1
    print("  --Dentro de generador - terminando")
 
mycont = generador(2)
print("  Contador instanciado") 

for i in mycont:
    print(f"  valor leido del iterador={i}") 
print("  Fin")





