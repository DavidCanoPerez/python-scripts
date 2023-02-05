# -*- coding: utf-8 -*-

"""
    estructuras de control
        iterativa
            while
            for
        condicional
            if
            else
            if elif
"""


""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    while
"""
a = 1
while a <= 4:
    print("bucle while: ", str(a))
    a += 1  # incrementa en 1


""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    for
"""
for i in range(1, 11):
    print("bucle for: ", str(i))


""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    if
"""
var = 5
if var == 5:
    print("valor 5")
else:
    print("no vale 5")


nombres = ["Daniel", "Juan", "Olga"]
if "Olga" in nombres:
  print("El nombre Olga esta en la lista")


""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    elif
"""
print("ingresa numero")
n = input()
if n == "1":
    print("numero 1")
elif n == "2":
    print("numero 2")
elif n == "3":
    print("numero 3")
else:
    print("entrada irreconocible")
    
    