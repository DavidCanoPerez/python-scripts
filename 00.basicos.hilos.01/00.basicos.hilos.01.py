# -*- coding: utf-8 -*-

"""
    python admite muy numerosas posibilidades a la hora de trabajar con hilos
    de hecho las características mas avanzadas del lenguaje se desarrollan en 
    este interesante área
    
    este ejemplo intenta ser lo mas básico posible
        hilo formato script sin main
    
    documentacion
        https://docs.python.org/3.10/library/threading.html
"""


import threading

def func_example(num):
    while num<11:   # while 1-10
        print(num)  # en general no se puede hacer un print simple desde hilos
        num+=1

# hilo example
# en general sería diferente del hilo main o principal del programa
num=1   # try change the value

thread1 = threading.Thread(name="thread_example", 
                           target=func_example,
                           args=[num]  # único dato corchetes/varios paréntesis
                           )

thread1.start()

