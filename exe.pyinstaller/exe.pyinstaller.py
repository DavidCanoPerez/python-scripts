# -*- coding: utf-8 -*-

"""
    pyinstaller
    
    https://pyinstaller.org/en/stable/
    
    PyInstaller bundles a Python application and all its dependencies into a single package. 
    The user can run the packaged app without installing a Python interpreter or any modules.
    
    instalar pyinstaller
        pip install -U pyinstaller
        
        Problema en anaconda: 
            The 'pathlib' package is an obsolete backport of a standard library package and 
            is incompatible with PyInstaller. Please remove this package 
            (located in C:\ Users\...\anaconda3\Lib\site-packages) using 
            conda remove then try again.
        Solución:
            pip uninstall pathlib
    
    si se ha instalado pyinstaller en el pip de anaconda
        desplazarse con la terminal prompt al directorio del .py
        cd C:\ Users\...\Documents\Python Scripts\...
    
    comando para empaquetar o compilar
        pyinstaller your_program.py
    
    
"""

