# -*- coding: utf-8 -*-

"""
    programa tipo agenda con interfaz y base de datos
    
    sqlite
    https://docs.python.org/es/3/library/sqlite3.html#sqlite3-howtos
"""

import os
import sqlite3
import tkinter as tk
from tkinter import ttk

def main():
    # ubicación actual del programa y base de datos
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    DATABASE_PATH = os.path.join(CURRENT_DIR, 'usuarios.db')

    crear_base_de_datos(DATABASE_PATH)

    # conexión a la base de datos
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # ventana principal
    ventana = tk.Tk()
    ventana.title("Gestión de Usuarios")

    # etiquetas y campos de entrada
    nombre_label = tk.Label(ventana, text="Nombre:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    edad_label = tk.Label(ventana, text="Edad:")
    edad_label.pack()
    edad_entry = tk.Entry(ventana)
    edad_entry.pack()

    # botones
    agregar_button = tk.Button(
            ventana, 
            text="Añadir Usuario", 
            command=lambda: agregar_usuario(conn, cursor, nombre_entry, edad_entry, tabla))
    agregar_button.pack()
    eliminar_button = tk.Button(
            ventana, 
            text="Eliminar Usuario", 
            command=lambda: eliminar_usuario(conn, cursor, tabla))
    eliminar_button.pack()

    # tabla
    tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Edad"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Edad", text="Edad")
    tabla.pack()

    # actualizar inicialmente la tabla
    update_table(cursor, tabla)

    # iniciar la aplicación
    # la ejecucion estara aqui salvo que se pase a alguna de las funciones fuera de main
    ventana.mainloop()

    # cerrar la conexión a la base de datos al cerrar la ventana
    conn.close()

def agregar_usuario(conn, cursor, nombre_entry, edad_entry, tabla):
    nombre = nombre_entry.get()
    edad = edad_entry.get()

    if nombre and edad:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
        conn.commit()
        update_table(cursor, tabla)
        nombre_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)

def eliminar_usuario(conn, cursor, tabla):
    selected_item = tabla.selection()
    if selected_item:
        item = tabla.item(selected_item)
        user_id = item['values'][0]
        cursor.execute("DELETE FROM usuarios WHERE id=?", (user_id,))
        conn.commit()
        update_table(cursor, tabla)

def update_table(cursor, tabla):
    tabla.delete(*tabla.get_children())
    # ejecuta consulta a base de datos
    cursor.execute("SELECT * FROM usuarios")
    # itera sobre consulta
    for row in cursor.fetchall():
        tabla.insert('', 'end', values=row)

def crear_base_de_datos(DATABASE_PATH):
    # si el archivo .db no existe se crea
    if not os.path.isfile(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                edad INTEGER
            )
        ''')
        conn.commit()
        conn.close()

if __name__ == "__main__":
    main()

