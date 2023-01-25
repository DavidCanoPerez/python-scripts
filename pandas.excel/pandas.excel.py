# -*- coding: utf-8 -*-

"""
    importar xlsx
"""

try:
    import pandas as pd
    import os.path
except ImportError:
    print("Error importando")

# directorio de archivo
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
path = CURRENT_DIR + r'\muestra03.xlsx'

# cargar dataframe en pandas
df = pd.read_excel(path)

# imprime dataframe en terminal
print("\nDatos en dataframe:") 
print(df.head())
print ("\nnombres de columnas:")
print(df.columns)

# calcular estadísticos descriptivos para cada variable
print("\nEstadísticos descriptivos por variable:") 
totalstats = df.describe()
#totalstats = df.describe(include = 'all') 
print(totalstats)

