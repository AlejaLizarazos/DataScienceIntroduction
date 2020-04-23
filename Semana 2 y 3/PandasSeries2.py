import pandas as pd
import numpy as np
from math import sqrt
from os import system
system('cls')
##### 26 - 44 #####
#-------
#Funcion de agregación agg (min,max,sqrt,abs,hex,...)
#datos = [0,1,2,3,4,5,6,7,8,9]
#serie = pd.Series(datos)
#print(serie.agg(lambda x:x**3))
#print(serie.agg(np.sin))
#-------
#Remplazar valores Nan(null) de una serie con valor arbitrario
#serie = pd.Series([1,3,7,11,'python','-0.5',np.nan])
#serie = pd.to_numeric(serie,errors = 'coerce')
#serie.fillna(0,inplace = True)
#-------
#Obtener los primeros y ultimos n elementos de un objeto Series
#series = pd.Series(list(range(1,101)))
#print(series.head(10))
#print(series.tail(10))
#-------
#Reemplazar por un valor arbitrario valors que no cumplan condicion
#series = pd.Series(list(range(1,6)))
#series = series.where(series>1,-1)
#-------
#Remover valors que no cumplan condicion
#series = pd.Series(list(range(1,11)))
#series = series.where(series>=5).dropna()
#-------
#Contar valores repetidos en una serie
#series = pd.Series([5,3,5,7,7,3,1,2,3,0])
#print(series.value_counts())
#-------
#serie.to_json()
#-------
#Obtener objeto dicc
#serie.to_dict()
#-------
#Crear un objeto DataFrame a partir de Series
#series = pd.Series([2,3,4,7,11,12])
#df = series.to_frame()
#-------
#Series a CSV(comma separated values)

#series = pd.Series(['python','C#','Java','PHP','JavaScript'])
#series.to_csv(index = False)
#-------
#Aplicar funcion sobre elementos
#serie.apply(lambda x:x**2)
#serie.apply(adicionar_temperatura,args=(7,))
#-------
#serie.between(2,5) #Valores entre ese rango
#(2 <= serie) & (serie <= 5)
#serie.between (2,5,inclusive = False)
#-------
#remover valores duplicados
#serie = pd.Series(datos,name='lenguajes')
#serie.drop_duplicates(keep='last)
#-------
#serie1.equals(serie2)
#-------
#Guardar datos de obj series en excel
#series.to_excel('Producción.xlsx',engine = 'xlsxwriter')
#-------
