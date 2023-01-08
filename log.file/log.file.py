# -*- coding: utf-8 -*-

"""
    crea archivo log
    registra fecha y variables que incluyamos
    ejemplo con fibonacci
"""

import os
from datetime import datetime

def func_calculate_fibonacci(n_f):
    n1, n2 = 0, 1
    index_while = 1
    while index_while < n_f:
        print(n1, end=" ")
        # imprimir nueva linea en archivo temporal log usando f-strings
        temp_log_file.write(f"{datetime.now()} >>>> " 
                            f"valorN1:{n1}" 
                            "\n")
            # \n nueva linea
            # f"" para incluir {variable}
        n1, n2 = n2, n1+n2
        index_while += 1 # incrementa en 1
         

if __name__ == '__main__':
    
    # obtener fecha
    #print(datetime.now())
    
    # obtener directorio actual
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    #print('Directorio actual: ' + CURRENT_DIR)
    
    # crea archivo log o temporal
    # python tiene un modulo propio para crear temporales pero no se usará
    # ver https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile
    temp_log_file = open(CURRENT_DIR + "/temp.log.txt", 
                         "a")
        # a para añadir texto, no se borra log anterior
        # alternativa: w se borra log anterior
        # puede darse otra extension al archivo
    
    # calcula 99 numeros de la sucesion de fibonacci
    func_calculate_fibonacci(100)
    
    temp_log_file.close()
    
    
    
    