import pandas as pd 
import numpy as np
from string import ascii_lowercase
from os import system
system('cls')

#-------
#Seleccionar todas las columnas excepto 1
#df.loc[:,df.columns != 'name']

#-------
#Obtener registros que empiecen con cierta letra
#resultadpo  = df[df['nombre'].str[:1] == 'J']

#-------
#Obtener registros que no contengan cierta letra
#resultado = df[df['nombre'].str.lower().str.find('h') == -1]

a = 'hola()'

if a.find('(') != 1:
    a = a[0:a.find('(')]

print(a)



