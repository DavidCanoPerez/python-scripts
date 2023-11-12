# -*- coding: utf-8 -*-

"""
    reproductor de audio (pygame) con interfaz (tk)
"""

import pygame
import tkinter as tk
from tkinter import filedialog

class ReproductorAudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Audio")
        self.root.geometry("400x250")

        self.estado_reproduccion = "detenido"  # Puede ser "detenido", "reproduciendo" o "pausado"

        self.inicializar_gui()
        self.inicializar_pygame()

        # configura el manejo del evento de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def inicializar_gui(self):
        # Botón para seleccionar un archivo de audio
        self.btn_seleccionar = tk.Button(self.root, 
                                         text="Seleccionar Archivo", 
                                         command=self.seleccionar_archivo)
        self.btn_seleccionar.pack(pady=10)

        # control deslizable de volumen
        self.slider_volumen = tk.Scale(self.root, 
                                       from_=0, 
                                       to=1, 
                                       orient=tk.HORIZONTAL, 
                                       resolution=0.01, 
                                       label="Volumen",
                                       command=self.actualizar_volumen)
        self.slider_volumen.set(0.5)  # valor predeterminado del volumen a 0.5
        self.slider_volumen.pack(pady=10)

        # botones de reproducción
        self.btn_play = tk.Button(self.root, text="▶ Play", command=self.play)
        self.btn_play.pack(side=tk.LEFT, padx=10)

        self.btn_pause = tk.Button(self.root, text="⏸ Pause", command=self.pause)
        self.btn_pause.pack(side=tk.LEFT, padx=10)
        self.btn_pause["state"] = tk.DISABLED

        self.btn_stop = tk.Button(self.root, text="⏹ Stop", command=self.stop)
        self.btn_stop.pack(side=tk.LEFT, padx=10)
        self.btn_stop["state"] = tk.DISABLED

    def inicializar_pygame(self):
        pygame.init()
        pygame.mixer.init()

    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(
            defaultextension=".mp3", 
            filetypes=[("Archivos de Audio", "*.mp3;*.wav")])
        if archivo:
            pygame.mixer.music.load(archivo)
            self.btn_play["state"] = tk.NORMAL
            self.btn_pause["state"] = tk.DISABLED
            self.btn_stop["state"] = tk.DISABLED
            self.estado_reproduccion = "detenido"

    def play(self):
        pygame.mixer.music.set_volume(self.slider_volumen.get())

        if self.estado_reproduccion == "detenido":
            pygame.mixer.music.play()
            self.estado_reproduccion = "reproduciendo"
            self.btn_pause["state"] = tk.NORMAL
            self.btn_stop["state"] = tk.NORMAL
        elif self.estado_reproduccion == "pausado":
            pygame.mixer.music.unpause()
            self.estado_reproduccion = "reproduciendo"

    def pause(self):
        pygame.mixer.music.pause()
        self.estado_reproduccion = "pausado"

    def stop(self):
        pygame.mixer.music.stop()
        self.btn_play["state"] = tk.NORMAL
        self.btn_pause["state"] = tk.DISABLED
        self.btn_stop["state"] = tk.DISABLED
        self.estado_reproduccion = "detenido"

    def actualizar_volumen(self, value):
        pygame.mixer.music.set_volume(float(value))

    def cerrar_ventana(self):
        pygame.mixer.music.stop()
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    reproductor = ReproductorAudio(root)
    root.mainloop()