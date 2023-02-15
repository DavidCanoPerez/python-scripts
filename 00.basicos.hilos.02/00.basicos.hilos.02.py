# -*- coding: utf-8 -*-

"""
    hilo simple ya diferenciado de main
"""

import threading
import time
import os,sys

def main():
    print("main")
    
    num=1
    thread1 = threading.Thread(name=None, 
                               target=func_example,
                               args=[num]  # único dato corchetes/varios paréntesis
                               )
    thread1.start()

    
    thread1.join()  # espera a que finalice el hilo, probar a comentar
    print("end main")
    
def func_example(num):
    print("hilo iniciado")
    while num<11:   # while 1-10
        time.sleep(1) # espera 1 segundo
        print(num)  # en general no se puede hacer un print simple desde hilos
        num+=1

if __name__ == '__main__':
    main()

