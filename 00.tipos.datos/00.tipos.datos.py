# -*- coding: utf-8 -*-

"""
    https://blog.hubspot.es/website/lista-python
"""

#   tipos de datos:
#       cadenas - strings
#               en python no hay variables tipo char o de un único caracter
#               cadena = "sistema"
#               caracter = "/"
#       números
#               en python los booleanos (bool) son una subclase de los enteros
#               x = 2
#               b = True
#       conjuntos - sets
#               conjunto = {'a', 'b', 'c'}
#       lista - list
#               lista = [4, 5.5, 'a6']
#               muebles = list(("silla", "mesa", "estantería"))
#       tupla - tuple
#               tupla = (1, 2, 3)
#       diccionario (dictionaries)
#                
#       la principal diferencia entre la lista y la tupla 
#       es que la lista es mucho más lenta, pero puede ser editada, 
#       mientras que las tuplas trabajan más rápido, pero no pueden ser modificadas.


# ---------------------------------------------------------------------------------------------
#   string
# ---------------------------------------------------------------------------------------------

print("----Ejemplos string", "")

# puede utilizarse comillas simples, dobles, tripes comillas simples y dobles
cad1 = 'hola'
cad2 = "a"
cad3 = '''todos'''
cad4 = """ellos"""

print(cad1, cad2, cad3 + cad4)
# output: hola a todosellos

cad5 = ""       # string vacío, tamaño 0
print(cad5)     # no provoca error, se imprime como linea vacía

cad6 = None     # NoneType object
print(cad6)     # no provoca error
# output: None

# ---------------------------------------------------------------------------------------------
#   números
# ---------------------------------------------------------------------------------------------

print("----Ejemplos números", "")

# como en python no hace falta especificar el tipo de dato numerico
# una forma de especificar una variable como bool es asignar uno de los valores posibles
# y posteriormente se puede modificar
b = True

# en python los booleanos (bool) son una subclase de los enteros
c = False

c = isinstance(c, int)
print("c:", c)
# output: True
isinstance(True, int)   # ¿es el valor True un tipo de variable entera? si
# output: True
issubclass(bool, int)   # ¿es la variable bool un tipo de variable entera? si
# output: True

# comprobar qué tipo de dato es una variable
d = 29
e = isinstance(d, (str, int, float, set, list, dict, tuple))
print("d:", d)

# ---------------------------------------------------------------------------------------------
#   lista
# ---------------------------------------------------------------------------------------------
#       características:
#           Ordenada: 
#                   Los elementos dentro de ella están indexados y 
#                   se accede a ellos a través de una locación indexada 
#           Editable: 
#                   De forma independiente los elementos pueden editarse, 
#                   pueden añadir otros nuevos o eliminarse 
#           Dinámica: 
#                   Pueden contener diferentes tipos de datos y 
#                   objetos. Esto significa que pueden soportar paquetes 
#                   multidimensionales de datos, como un array o muchos objetos
#           No única: 
#                   Puede contener elementos duplicados
#
#       su índice comienza en 0, el primer elemento de la lista tiene índice 0
#       pueden contener cualquier tipo de dato
#                   enteros, cadenas, booleanos, objetos, listas anidadas, etc 
#          
# ---------------------------------------------------------------------------------------------

print("----Ejemplos listas", "")

lista1 = ["0", "2", "9", "14", "20"]

# append() añade elemento
varl1 = "15"
lista1.append(varl1)
print(f"lista1: {lista1}")

# index() recupera el índice
varl2="9"
print("indice de la variable en lista1:", lista1.index(varl2))
    # recordar que su indice comienza en 0     

# remove() elimina un determinado elemento 
lista1.remove(varl2)
print(f"lista1: {lista1}")

# sort() orden ascendente
lista1.sort()
print(f"lista1 CUIDADO mal ordenada: {lista1}")
    # CUIDADO no es el resultado que se espera porque es una lista de cadenas

lista2 = [20, 14, 9, 2, 0]
lista2.sort()
print(f"lista2 ordenada: {lista2}")

# ---------------------------------------------------------------------------------------------
#   diccionario
# ---------------------------------------------------------------------------------------------

print("----Ejemplos diccionarios", "")







