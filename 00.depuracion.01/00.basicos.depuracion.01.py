# -*- coding: utf-8 -*-

"""
    ejemplo depuracion
        utilizando la libreria pdb
    
    documentacion
        https://docs.python.org/es/3/library/pdb.html
    
    comprobar comandos
        v
            para ver valor de variable
        n
            (next) continua ejecucion de programa
        q 
            finaliza depuracion
"""

import pdb

v = 0
while v < 5:
    pdb.set_trace()     # punto de interrupcion
    v += 1
print("fin")

