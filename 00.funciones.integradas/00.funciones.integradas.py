# -*- coding: utf-8 -*-

"""
    funciones integradas (built-in functions)
        https://docs.python.org/3.11/library/functions.html
        están disponibles sin necesidad de importar ninguna biblioteca
        son:
            __import__()
            abs() aiter() all() anext() any() ascii()
            bin() bool() breakpoint() bytearray() bytes()
            callable() chr() classmethod() compile() complex()
            delattr() dict() dir() divmod()
            enumerate() eval() exec()
            filter() float() format() frozenset()
            getattr() globals()
            hasattr() hash() help() hex()
            id() input() int() isinstance() issubclass() iter()
            len() list() locals()
            map() max() memoryview() min()
            next()
            object() oct() open() ord()
            pow() print() property()
            range() repr() reversed() round()
            set() setattr() slice() sorted() staticmethod() str() sum() super()
            tuple() type()
            vars()
            zip()
        pero típicamente están disponibles muchísimas más, como lower()
        no se incluyen en algunos listados porque 
        no serían funciones integradas de forma clásica
        hay diferentes formas de estudiarlas, como clasificándolas, 
        por ejemplo las destinadas a trabajar con tipos de datos:

                ejemplo string
                    len() longitud de una cadena.
                    str() convierte a cadena.
                    lower() todos los elementos de cadena en minúsculas.
                    upper(): cadena o componentes de cadena en mayúsculas.
                    replace(): reemplaza caracter o toda la cadena de elementos.

                ejemplos
                    cadena = "¡Hola, mundo!"
                    print(len(cadena))                # 13
                    print(str(1234))                  # "1234"
                    print(cadena.lower())             # "¡hola, mundo!"
                    print(cadena.upper())             # "¡HOLA, MUNDO!"
                    print(cadena.replace("¡", "¿"))   # "¿Hola, mundo!"

        a continuación sólo ejemplos sin agrupar o clasificar
"""

# ---------------------------------------------------------------------------------------------
#   __import__()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   abs()
# ---------------------------------------------------------------------------------------------
#       en general devuelve el valor absoluto de un número
#       aplicado a diferentes tipos de numeros  
#           integers - integer absolute value is returned
#           floating numbers - floating absolute value is returned
#           complex numbers - magnitude of the number is returned
#               en el caso de los complejos devuelve su magnitud con 
#               ayuda del teorema de Pitágoras
#               complejo = parte_real + parte_imaginaria*j
#       puede llegar a aplicarse a objetos a través de __abs__()

print("abs------")

print(abs(-2)) 
# output: 2

floating = -10.55
print(abs(floating))
# output: 10.55

complex = (3 - 4j)
print(abs(complex))
# output: 5.0

# ---------------------------------------------------------------------------------------------
#   aiter()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   all()
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
#   any()
# ---------------------------------------------------------------------------------------------
#       devuelve True si alguno de los elementos de un 
#       iterable (cadenas, listas, tupla, diccionario, set, etc) es verdadero, 
#       si no, devuelve False
            
print("any------")

boolean_list = ['True', 'False', 'True']
result = any(boolean_list)
print('ejemplo1', result)
# output: True

lista = [0,0,0,1,0,0,0,0]
print('ejemplo2', any(lista))
# output: True

l = []
print('ejemplo3', any(l))
# output: False

str1 = 'Hello World'
print('ejemplo4', any(str1))
# output: True

str2 = '0'
print('ejemplo5', any(str2))    # '0' CUIDADO se considera una cadena válida
# output: True

str3 = ''
print('ejemplo6', any(str3))    # cadena vacía
# output: False

dict1 = {0: 'False', False: 0}      # key 0 and False are False
print('ejemplo7', any(dict1))
# output: False

dict2 = {1: 'John', 2: 'David', 3: 'Kim'} # all keys are True
print('ejemplo8', any(dict2))
# output: True

dict3 = {0: 'False', 1: 'True'}     # few keys are True
print('ejemplo9', any(dict3))
# output: True

dict4 = {}      # empty dict
print('ejemplo10', any(dict4))
# output: False

dict5 = {'0': False, 'False': 1}    # ATTENTION a key of string is True
print('ejemplo11', any(dict5))
# output: True

# ---------------------------------------------------------------------------------------------
#   anext()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   ascii()
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
#   bin()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   bool()
# ---------------------------------------------------------------------------------------------
#       a partir de objeto obtiene el valor booleano correspondiente 
#       por defecto devuelve valor True
#       devuelve False ante 0, False, None o está vacío [], (), {}

print("bool------")

a_bool = bool(None)
print("a_bool:", a_bool)
# output: False

b_bool = None
bool(b_bool)
print("b_bool:", b_bool)
# CUIDADO, aquí el problema es que no se ha llegado a llamar a bool() sobre b
# output: None

c_bool = bool(1)
print("c_bool:", c_bool)
# output: True

d_bool = bool(0)
print("d_bool:", d_bool)
# output: False

e_bool = bool(False)
print("e_bool:", e_bool)
# output: False

f_bool = bool("False")
print("f_bool:", f_bool)
# CUIDADO, se considera objeto string cadena válida y verdadera
# output: True

g_bool = bool("")
print("g_bool:", g_bool)
# output: False

h_bool = []
i_bool = bool(h_bool)
print("i_bool:", i_bool)
# output: False

j_bool = bool(99.2 == 2)
print("j_bool:", j_bool)
# output: False
# puede utilizarse para realizar comparaciones

# ---------------------------------------------------------------------------------------------
#   breakpoint()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   bytearray()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   bytes()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   callable()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   chr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   classmethod()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   compile()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   complex()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   delattr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   dict()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   dir()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   divmod()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   enumerate()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   eval()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   exec()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   filter()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   float()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   format()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   frozenset()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   getattr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   globals()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   hasattr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   hash()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   help()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   hex()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   id()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   input()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   int()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   isinstance()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   issubclass()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   iter()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   len()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#    list()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   locals()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   map()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   max()
# ---------------------------------------------------------------------------------------------
#       devuelve el máximo valor

print("max------")

m = [1, 4, -2, 7, 3]
print(max(m))
# outuput: 7

print(max("a", "g", "c", "z"))
# outuput: z

# ---------------------------------------------------------------------------------------------
#   memoryview()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   min()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   next()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   object()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   oct()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   open()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   ord()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   pow()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   print()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   property()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   range()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   repr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   reversed()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   round()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   set()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   setattr()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   slice()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   sorted()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   staticmethod()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   str()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   sum()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   super()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   tuple()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   type()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   vars()
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#   zip()
# ---------------------------------------------------------------------------------------------





