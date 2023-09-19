# -*- coding: utf-8 -*-

"""
    reproductor de video
    
    ante errores primero comprobar driver basicos y gratuitos de video actualizados 
            descargar gratis K-Lite Codec Pack de https://www.codecguide.com/
            
    a mejorar:
            comprobar extensiones de archivo de video
            fulls screen
            control de volumen ¿ya es logarítmico?   
"""

"""
    para pruebas
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
                             QLabel, QSlider, QStyle, QSizePolicy, QFileDialog)
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(100, 100, 600, 600)
        self.setWindowIcon(QIcon('player.png'))

        # color
        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()
        #self.show()

    def init_ui(self):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        videowidget = QVideoWidget()

        # open button
        openBtn = QPushButton('Load')
        openBtn.clicked.connect(self.load)

        # play button
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play)

        # stop button
        self.stopBtn = QPushButton()
        self.stopBtn.setEnabled(False)
        self.stopBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopBtn.clicked.connect(self.stop)

        # slider posicion video
        self.progressSlider = QSlider(Qt.Horizontal)
        self.progressSlider.setRange(0,0)
        self.progressSlider.sliderMoved.connect(self.set_position)

        # slider volumen
        self.volumeSlider = QSlider(Qt.Horizontal)
        
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)
        
        self.volumeSlider.setTickPosition(QSlider.TicksBothSides)
        self.volumeSlider.valueChanged.connect(self.set_volume)

        # label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # layout Horizontal
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.stopBtn)
        hboxLayout.addWidget(self.volumeSlider)

        # layout Vertical
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        hboxLayout.addWidget(self.progressSlider)
        vboxLayout.addLayout(hboxLayout)        # incluye el horizontal
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def load(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(
                    self, 
                    "Load", 
                    "", 
                    "Video (*.mp4 *.avi *.mkv);; (*)", 
                    options=options)
        if self.fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileName)))
            self.playBtn.setEnabled(True)
            self.stopBtn.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def stop(self):
        self.mediaPlayer.stop()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.progressSlider.setValue(position)

    def duration_changed(self, duration):
        self.progressSlider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.set_position(position)
    
    def set_volume(self):
        volume = self.volumeSlider.value()
        self.mediaPlayer.setVolume(volume)
    
    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())
        # no registra muchos errores

    def closeEvent(self, event):
        """
        # dialogo al pulsar x
        close = QMessageBox.question(self,
                                     "quit",
                                     "sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            self.mediaPlayer.stop()   # stop, especialmente el audio, si se cierra la ventana
        else:
            event.ignore()
        """
        self.mediaPlayer.stop()   # stop, especialmente el audio, si se cierra la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())




