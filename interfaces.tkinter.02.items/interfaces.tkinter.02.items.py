# -*- coding: utf-8 -*-

"""

"""

import tkinter as tk
from tkinter import ttk, messagebox

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo Tkinter")
        self.inicializar_interfaz()

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje", "Hola, ¡esto es un mensaje!")

    def inicializar_interfaz(self):
        # etiqueta
        etiqueta = tk.Label(self, text="Hola Tkinter!", font=("Helvetica", 16))
        etiqueta.pack(pady=10)

        # caja de texto
        caja_texto = tk.Entry(self, width=30)
        caja_texto.pack(pady=5)

        # boton
        boton = tk.Button(self, text="Mostrar Mensaje", command=self.mostrar_mensaje)
        boton.pack(pady=10)

        # cuadro de selección
        opciones = ["Opción 1", "Opción 2", "Opción 3"]
        opcion_var = tk.StringVar(value=opciones[0])
        cuadro_seleccion = tk.OptionMenu(self, opcion_var, *opciones)
        cuadro_seleccion.pack(pady=5)

        # checkbutton
        check_var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(self, text="Aceptar términos y condiciones", variable=check_var)
        checkbutton.pack(pady=5)

        # radiobuttons
        radio_var = tk.StringVar(value="1")
        radio1 = tk.Radiobutton(self, text="Opción 1", variable=radio_var, value="1")
        radio2 = tk.Radiobutton(self, text="Opción 2", variable=radio_var, value="2")

        radio1.pack()
        radio2.pack(pady=10)
            # 10 píxeles arriba y abajo

        # tabla (Treeview)
        tabla = ttk.Treeview(self, columns=("Nombre", "Edad", "Ciudad"), show="headings")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Edad", text="Edad")
        tabla.heading("Ciudad", text="Ciudad")

        # datos en la tabla
        datos_tabla = [("Juan", 25, "Ciudad A"),
                       ("Ana", 30, "Ciudad B"),
                       ("Carlos", 22, "Ciudad C")]

        for dato in datos_tabla:
            tabla.insert("", "end", values=dato)

        tabla.pack(pady=10)

        # bucle principal
        self.mainloop()

if __name__ == "__main__":
    app = VentanaPrincipal()

