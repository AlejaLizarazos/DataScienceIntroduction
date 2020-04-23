import pandas as pd 
import numpy as np
from string import ascii_lowercase
from os import system
system('cls')
# 106 - 132
#--------
#Eliminar registros que no cumplan con una condicion en una columna específica
#df = pd.DataFrame({'X':[1,2,3,4,5],'Y':[3,2,5,0,-1],'Z':[2,3,5,7,11]})
#df = df[df['Y'] !=5 ]
#--------
#Funciones all y any
#df = (df <= 5).all()
#df = (df <= 5).any()
#--------
#usar iat,at para cambiar un elemento especifico
#df.iat[0,0] = 0
#df.at['e','Z'] = 29
#--------
#calcular promedio y mediana por cada fila y columna
#df = df.median(axis =1)
#df = df.median(axis =0)
#df = df.median(axis =1)
#--------
#agregar un indice nuevo
#df.index = list(ascii_lowercase[:5])
#print(df)
#--------
#Trasformar los valores con la funcion Transform
#df = df.transform(lambda x: x+2)
#--------
#df = df.iloc[[1,3]]
#--------
# max
#df = df.max(axis = 1) #max por cada fila
#--------
####df = pd.DataFrame({'animal':['aguila','alcon','aguiña','alcon'],'velocidad':[160,390,120,385]})
#df = df.groupby(['animal']).mean()
#--------
#Ampliar filas y columnas visibles 
#pd.set_option('display.max_columns',100)
#pd.set_option('display.max_row',200)
#--------
#reemplazar los NaN con un valor especifico usando fillna
#####df = pd.DataFrame(data = {'nombre':['Olivia','Daniela','Juan','German','Edward','Alex','Julio','Edgar','Angie','Irlesa'],'puntaje':[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18],'Intentos':[1,3,2,3,2,3,1,1,2,1],'califico':['Si','No','Si','No','No','Si','Si','No','No','Si']},index = ['a','b','c','d','e','f','g','h','i','j'])
#df = df.fillna(0)
#--------
#seleccionar registros que cumplan con una hora especifica con at_time
#df = pd.DataFrame({'A':list(range(1,9))},pd.date_range('2013-08-16',periods = 8,freq ='6H'))
#print(df.at_time('06:00'))
#--------
#Contar elementos nulos 
#df = df.isnull().values.sum()
#--------
#Eliminar filas o registros con drop
#df = df.drop(['f','h'])
#df = df.drop(df.index[[5,7]])
#--------
#seleccionar un conjunto de registros a partir de un rango horario
#df.between_time('00:30','01:00')
#--------
#combinar los objetos con concat
#df1 = pd.DataFrame({'programador':['Fd','Ger','Dan','John','Ger','Dan']})
#df2 = pd.DataFrame({'lenguaje':['C++','Java','Scala','Python','PHP','JavaScript']})
#df = pd.concat([df1,df2],axis = 1)
#print(df)
#--------
#eliminar registros duplicados
#df = df.drop_duplicates('programador',keep='last')
#--------
#cambiar orden filas de forma aleatoria
#df.sample(frac = 1)
#--------
#convertir columna de tipo cadena a fecha con to_datetime
#serie = pd.Series(['2018/12/31','2019/01/31','2023/05/21'])
#serie = pd.to_datetime(serie)
#print(serie)

