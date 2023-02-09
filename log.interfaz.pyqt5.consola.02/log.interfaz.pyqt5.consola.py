# -*- coding: utf-8 -*-

"""
    consola para comandos y mostrar datos en base a pyqt5
    probar comandos: print, ejemplo y exit
"""

import os
import sys
from PyQt5.Qt import (QApplication, QWidget, QLabel, QLineEdit,  
                      QTextEdit, QVBoxLayout, QCoreApplication,
                      QScrollBar, QColor, QGridLayout
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
        
        # tamaño inicial, minimo, titulo de ventana y color
        self.resize(500, 500)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Console")
        self.setStyleSheet("background-color: black;")  # probar a comentar
        
        # crea objetos de componentes
        self.output = QTextEdit()
        self.input = QLineEdit()
        self.output.setReadOnly(True)
        self.lbl = QLabel("Command >")

        # layout para 2 componentes en horizontal
        grid = QGridLayout()
        grid.setSpacing(0)    # sin espacio entre lbl e input
        grid.addWidget(self.lbl, 0, 0)
        grid.addWidget(self.input, 0, 1)
        
        # layout general y componentes a layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.output)
        layout.addLayout(grid)      # añade layout horizontal
        self.setLayout(layout)      # construye layout general

        # cambiar tamaño de letra 
        font = self.output.font()
        font.setPointSize(11)
        self.output.setFont(font)
        self.input.setFont(font)
        self.lbl.setFont(font)
        
        # cambiar color de fondo
                # probar a comentar
        self.output.setStyleSheet("background-color: black; border: 1px solid black;")
        
        # color de letra
        #self.output.setTextColor(QColor(0, 255, 0))
        self.output.setStyleSheet(
            "background-color: black; color: rgb(0, 255, 0); border: 1px solid black;")
        self.input.setStyleSheet(
            "background-color: black; color: rgb(0, 255, 0); border: 1px solid black;")
        self.lbl.setStyleSheet(
            "background-color: black; color: rgb(0, 255, 0); border: 1px solid black;")

        # crea conexion y llama si se pulsa intro
        self.input.returnPressed.connect(self.run_command)
        
        # imprime linea inicial
        msg = "Interfaz iniciada"
        self.text_to_show(msg)
        
        # pone foco inicialmente en input
        self.input.setFocus()
        
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
    