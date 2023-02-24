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
        

if __name__ == "__main__":
    main()

    