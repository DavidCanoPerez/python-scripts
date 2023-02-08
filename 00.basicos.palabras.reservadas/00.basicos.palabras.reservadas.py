# -*- coding: utf-8 -*-

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
        Representa a un valor nulo
"""

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

""" ---------------------------------------------------------------------------------------------
    as
        crea un alias al importar un módulo.
"""

import tkinter as tk

""" ---------------------------------------------------------------------------------------------
    assert
        se utiliza con fines de depuración
"""

""" ---------------------------------------------------------------------------------------------
    async
        proporcionada por la biblioteca 'asyncio' 
        se utiliza para escribir código concurrente
"""

""" ---------------------------------------------------------------------------------------------
    await
        Proporcionada por la biblioteca ‘asyncio’ 
        Se utiliza para escribir código concurrente
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
        se usa en declaraciones condicionales, igual ‘else’ e ‘if’
"""



""" ---------------------------------------------------------------------------------------------
    else
        se usa en declaraciones condicionales, igual ‘elif’ e ‘if’ 
"""


""" ---------------------------------------------------------------------------------------------
    except
        se usa para crear excepciones
        qué hacer cuando ocurre una excepción, igual que ‘raise’ y ‘try’
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
    print("FINALLY Ha ocurrido un error.")
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
        para crear una función anónima
"""


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
        Se usa para crear excepciones, qué hacer cuando ocurre una excepción, 
        igual que 'except' y 'try'
"""

""" ejemplo en intérprete
    raise NameError
    out: NameError
    """

""" ---------------------------------------------------------------------------------------------
    return
        se usa dentro de una función para salir y devolver un valor. 
"""

def r():
    return 1
r()

""" ---------------------------------------------------------------------------------------------
    try
        se usa para crear excepciones, 
        qué hacer cuando ocurre una excepción, 
        igual que 'raise' y 'except'
"""


""" ---------------------------------------------------------------------------------------------
    while
        Se usa para realizar bucles.
"""

# bucle infinito
while True:
    print("WHILE bucle inifinito")
    break  # puede romper el bucle infinito

# otro bucle
var = 1
while var < 2:
    print("WHILE procesando")
    var += 1 # incrementa valor de variable var en 1


""" ---------------------------------------------------------------------------------------------
    with
        se usa para simplificar el manejo de excepciones
"""

""" ---------------------------------------------------------------------------------------------
    yield
        se comporta de forma similar a return, con la diferencia que en lugar de retornar un valor, 
        retorna elementos que conforman un generador 
        (un objeto iterable que puede recorrerse una vez, 
         ya que el contenido no es almacenado en la memoria), 
        por lo que puede emplearse múltiples veces en una misma función.
"""

def f():
    yield 1
    yield 2
    yield 3

obj = f()
for i in obj:
    print("YIELD ejemplo", i)







