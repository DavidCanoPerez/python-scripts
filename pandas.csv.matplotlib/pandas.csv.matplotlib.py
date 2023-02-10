# -*- coding: utf-8 -*-

"""
    el archivo csv es como un excell pero delimitado por comas
"""

import matplotlib.pyplot as plt
import pandas as pd

# especificar el directorio, ver usuario
temperaturas = pd.read_csv(
    'C:/Users/usuario/Documents/Python Scripts/pandas.csv.matplotlib/temperaturas.csv',
    encoding="utf8"
    )

plt.scatter(temperaturas['Celsius'],temperaturas['Fahrenheit'])
plt.title("titulo gráfico")
plt.xlabel("titulo eje x")
plt.ylabel("titulo eje y")
plt.show()
