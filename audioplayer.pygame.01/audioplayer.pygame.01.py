# -*- coding: utf-8 -*-

"""
   reproductor mínimo usando pygame
   busca un archivo llamado file.mp3 en el directorio del programa
"""

from pygame import mixer
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, 'file.mp3')

mixer.init()
mixer.music.load(FILE_PATH)
mixer.music.play()
