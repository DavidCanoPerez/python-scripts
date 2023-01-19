# -*- coding: utf-8 -*-

"""
    comando consola spyder parar ejecucion: exit
    
    genera números aleatorios uno por uno en cada ciclo del thread
    números de función gauss (con parámetros media, desviación estandar)
    
    documentacion
        numpy.random
            https://docs.python.org/es/3/library/random.html
"""

import threading
import time
import random

def main():
    
    x_tiempo = 0
    y = 50
    
    # hilo1
    thread1 = threading.Thread(name="hilo_simulacion", 
                               target=gauss_simulation,
                               args=(x_tiempo, y)
                               )
    thread1.start()
    
    print("inicia hilo secudario")

def t_print(msg):
    # necesario para print por consola desde thread
    print(msg)

def gauss_simulation(x_tiempo, y):
    infinite = True
    while infinite == True:
        time.sleep(1)       # pausar cada segundo
        t_print("tick de ejecucion hilo_simulacion")
        x_tiempo += 1
        nuevo_y = y
        # genera números aleatorios uno por uno en cada ciclo del thread
        # números de función gauss (media, desviación estandar)
        variacion = random.gauss(0,2)
        # añade variación a y
        nuevo_y = nuevo_y + variacion
        y = nuevo_y
        cadena = f"x={x_tiempo} y={y}"
        t_print(cadena)

if __name__ == '__main__':
    main()
    
        


