# -*- coding: utf-8 -*-

"""
    interfaz para comandos y mostrar datos en base a pyqt5
    probar comandos: print, ejemplo y exit
"""

import os
import sys
from PyQt5.Qt import (QApplication, QWidget, QLabel, QLineEdit,  
                      QTextEdit, QVBoxLayout, QCoreApplication,
                      QScrollBar
                      )

def main():
    app = QApplication(sys.argv)    # objeto app tipo QA
    w = CommandLogWindow()          # objeto w tipo clase QWidget
    w.show()                        # mostrar ventana
    sys.exit(app.exec_())           # ejecutar aplicacion
    
class Example():
    def example():
        procesar_datos = 2 + 2
        global output_for_gui
        output_for_gui = str(procesar_datos)
        
class CommandLogWindow(QWidget):
    
    def text_to_show(self, msg):
        self.output.append(msg) 
        
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # tamaño inicial, minimo y titulo de ventana
        self.resize(500, 500)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("LogWindow")

        # crea objetos de componentes
        label = QLabel(self.tr("Enter command and press INTRO"))
        self.input = QLineEdit()
        self.output = QTextEdit()

        # layout y componentes a layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.input)
        layout.addWidget(self.output)
        self.setLayout(layout)

        # crea conexion y llama
        self.input.returnPressed.connect(self.run_command)
        
        # imprime linea inicial
        msg = "Interfaz iniciada"
        self.text_to_show(msg)
        
    def run_command(self):
        cmd = str(self.input.text())    # comando a variable
        self.input.setText("")          # limpia texto
        if cmd == "exit":                               # ejemplo salir, cierra interfaz
            QCoreApplication.quit()
        elif cmd == "ejemplo":                          # ejemplo procesar dato en clase externa
            Example.example()
            self.print_output()
        elif cmd == "print":                            # ejemplo print consola
            print("print")
        else:
           self.output.append("Comando irreconocible")  # comando irreconocible
    
    def print_output(self):
        self.output.append(output_for_gui)
        
    def update_widgets(self):                           # focus siempre en ultima linea
        self.output.setValue(self.outuput.maximum())

if __name__ == "__main__":
    output_for_gui = ""
    main()
    

    
    
    