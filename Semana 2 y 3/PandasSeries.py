import pandas as pd
import numpy as np
from os import system
system('cls')
##### 1 - 25 #####
#-------
#datos = pd.Series(['100','200','python','300.15','500.8'])
#datos = pd.to_numeric(datos,errors = 'coerce')
#-------
#Obtener una columna de un objeto DataFrame como un objeto Series
#datos = {'A':[1,2,3,4,5],'B':[9,8,7,6,5],'C':[2,3,5,7,11]}
#df = pd.DataFrame(data = datos)
#columna = df['B']
#-------
#Extraer una fila de un DataFrame como un objeto Series
#datos = {'A':[1,2,3,4,5],'B':[6,5,4,3,2],'C':[2,3,4,7,11]}
#df = pd.DataFrame(data = datos)
#fila = df.iloc[2,:]
#-------
#Convertir objeto series con multuples listas en un unico objeto series
#datos = [['Colombia','Perú','Argentina'],['Bolivia','Uruguay'],['Chile']]
#serie = pd.Series(datos)
#serie = serie.apply(pd.Series).reset_index(drop=True)
#print(serie)
#-------
#Ordenar los valores de un objeto series con el metodo sort_values
#datos = ['1.1','python','0.5','pandas','2.8']
#series = pd.Series(datos).sort_values().reset_index(drop=True)
#-------
#Agregar datos a un objeto series existente 
#datos = ['python','C#','C++','Java','PHP']
#series = pd.Series(datos)
#serie = series.append(pd.Series(['JavaScript','Perl']))
#-------
#Crear un objeto series a partir de un filtro aplicado a otrro objeto series
#datos = [0,1,2,3,4,5,6,7,8,9]
#serie = pd.Series(datos)
#n = 6
#serie_nueva = serie[serie < n]
#-------
#Cambiar el orden del indice de un objeto series
#datos = [1,2,3,4,5]
#indices = ['A','B','C','D','E']
#serie = pd.Series(data = datos, index = indices)
#serie = serie.reindex(index = ['B','A','C','D','E'])
#-------
#Calcular valores minimo y maximo de objeto series
#datos = [19,2,13,0,23,29,11,7]
#serie = pd.Series(datos)
#serie.min()
#-------
#Obtener elementos pares e impares de objeto Series numérico
#datos = list(range(10))
#serie = pd.Series(datos)
#pares = serie[serie%2 == 0]
#-------
#Estraer los datos de un objeto series como un objeto numpy
#datos = list(range(10))
#serie = pd.Series(datos)
#arreglo = serie.values
#-------
#Comprobar si objeto series tiene valores NaN
#datos = ['20','30','python','50','100']
#serie = pd.Series(datos)
#serie = pd.to_numeric(serie,errors ='coerce')
#serie.hasnans
#--------
#Operaciones aritmericas con metodos de la clase series
#serie1 = pd.Series(list(range(1,11)))
#serie2 = pd.Series(list(range(10,0,-1)))
#print(serie1*serie2)
#--------
#Eliminar valores NaN de una serie con dropna
#datos = pd.Series(['1.1','python','0.5','pandas','2.8',np.nan,'0.5','0.9'])
#serie = pd.to_numeric(datos,errors = 'coerce')
#serie = serie.dropna()
#--------
#Valor absoluto
#serie.abs()







