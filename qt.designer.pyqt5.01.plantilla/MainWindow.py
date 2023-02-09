# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi("MainWindow.ui", self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # cancela procesos al cerrar ventana

