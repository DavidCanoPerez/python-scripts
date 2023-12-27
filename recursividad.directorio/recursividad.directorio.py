# -*- coding: utf-8 -*-

"""
    comentario
"""

import os
import tkinter as tk
from tkinter import filedialog

def listar_directorio(directorio, listbox):
    listbox.delete(0, tk.END)  # Limpiar el listado actual

    for root, dirs, files in os.walk(directorio):
        # listar carpetas
        for dir_name in dirs:
            listbox.insert(tk.END, os.path.join(root, dir_name))

        # listar archivos
        for file_name in files:
            listbox.insert(tk.END, os.path.join(root, file_name))

def seleccionar_directorio(listbox):
    directorio = filedialog.askdirectory(title="Seleccionar directorio")
    if directorio:
        listar_directorio(directorio, listbox)

def main():
    # crear la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Listado de archivos y directorios")

    # crear un botón para seleccionar el directorio
    boton_seleccionar = tk.Button(ventana, text="Seleccionar directorio", command=lambda: seleccionar_directorio(listbox))
    boton_seleccionar.pack(pady=10)

    # crear un listbox para mostrar el listado
    listbox = tk.Listbox(ventana, width=50, height=20)
    listbox.pack(pady=10)

    # agregar barra de desplazamiento al listbox
    scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # asociar el Scrollbar al Listbox
    listbox.config(yscrollcommand=scrollbar.set)

    # ejecutar la interfaz gráfica
    ventana.mainloop()

if __name__ == "__main__":
    main()
    
    