# -*- coding: utf-8 -*-

"""
    se puede conservar este main.py como plantilla de ejecucion de los .py generados de qtdesigner
"""

import sys

from ejemplo import Ui_MainWindow
#from ejemplo import *

from PyQt5.QtWidgets import ( QApplication, QMainWindow 
                             )

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        