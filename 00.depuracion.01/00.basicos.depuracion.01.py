# -*- coding: utf-8 -*-

"""
    ejemplo depuración
        utilizando la libreria pdb
    
    documentación
        https://docs.python.org/es/3/library/pdb.html
    
    comprobar comandos
        v
            para ver valor de variable
        n
            (next) continua ejecución de programa
        q 
            (quit) finaliza depuración
        h
            (help)
"""

import pdb

v = 0
while v < 2:
    pdb.set_trace()     # punto de interrupcion dentro de bucle
    v += 1
    print("linea final de bucle, valor de v:", v)
print("fin")

