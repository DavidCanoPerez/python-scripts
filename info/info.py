# -*- coding: utf-8 -*-

"""
    muestra info del equipo y red
"""

import platform
import os
import socket
import psutil

#-------------------------------------------------------------------------------------
# sistema operativo
#-------------------------------------------------------------------------------------

print("Información del sistema:")


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
print(f"Directorio del script: {CURRENT_DIR}")
#DATA_PATH = os.path.join(CURRENT_DIR, 'data.ext')

sistema_operativo = platform.system()
print(f"Sistema operativo: {sistema_operativo}")

version_sistema = platform.version()
print(f"Versión del sistema: {version_sistema}")

arquitectura_sistema = platform.architecture()
print(f"Arquitectura del sistema: {arquitectura_sistema}")
    
#-------------------------------------------------------------------------------------
# usuario y máquina
#-------------------------------------------------------------------------------------

print("\nInformación del usuario y máquina:")

nombre_usuario = os.getlogin()
print(f"Nombre de usuario: {nombre_usuario}")

nombre_maquina = socket.gethostname()
print(f"Nombre de la máquina: {nombre_maquina}")

direccion_ip = socket.gethostbyname(socket.gethostname())
print(f"Dirección IP de la máquina: {direccion_ip}")

#-------------------------------------------------------------------------------------
# red
#-------------------------------------------------------------------------------------     

print("\nInformación de la red:")

direcciones_ip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
print(f"Direcciones IP de la máquina: {', '.join(direcciones_ip)}")

#puertos abiertos
puertos_abiertos = [conn.laddr.port for conn in psutil.net_connections(kind='inet')]
print("\nInformación de los puertos abiertos:")
print(f"Puertos abiertos: {', '.join(map(str, puertos_abiertos))}")






