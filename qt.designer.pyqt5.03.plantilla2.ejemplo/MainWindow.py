# -*- coding: utf-8 -*-

"""

"""

import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "MainWindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle("Título de ventana")
        
        # plantilla hasta aquí
        
        # poner texto inicial en textEdit_1
        self.textEdit_1.setPlaceholderText("Introduce entrada")

        # si evento de boton llamar a función
        self.pushButton.clicked.connect(self.send_text)

    def send_text(self):
        print("boton pulsado")                     # print en terminal spyder
        text = self.textEdit_1.toPlainText()       # recoge texto de textEdit_1
        self.textEdit_2.append(text)               # coloca texto en textEdit_2
        self.textEdit_1.setText("")                # limpia texto de textEdit_1

if __name__ == "__main__":
    main()

    