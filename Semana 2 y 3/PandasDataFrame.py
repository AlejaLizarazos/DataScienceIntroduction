import pandas as pd 
import numpy as np
# 45 - 76
#--------
#datos = {'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]}
#df = pd.DataFrame(datos)
#--------
#Especificar nombres de indices arbitrarios
#datos = {'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]}
#indices = ['a','b','c','d','e']
#df = pd.DataFrame(data = datos,index = indices)
#print(df.loc['c'])
#--------
#Obtener nombre de las filas y columnas 
#df = pd.DataFrame({'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]})
#print(df.columns)
#print(df.index)
#print(df.dtypes)
#--------
#df = pd.DataFrame({'real':[3.1415],'entero':[0],'fecha':[pd.Timestamp('20170121')],'cadena':['python']})
#print(df.select_dtypes(include =['float64','int64']))
#--------
# n filas
# df.iloc[0:6] 
#--------
#df = pd.DataFrame({'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]})
#print(df.to_numpy())
#--------
#Selecionar columnas usando slicing
#df[['nombre','califico']]
#--------
#Seleccionar filas y columnasa especificas con iloc
#df = pd.DataFrame(data = {'nombre':['Olivia','Daniela','Juan','German','Edward','Alex','Julio','Edgar','Angie','Irlesa'],'puntaje':[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18],'Intentos':[1,3,2,3,2,3,1,1,2,1],'califico':['S1','No','Si','No','No','Si','Si','No','No','Si']},index = ['a','b','c','d','e','f','g','h','i','j'])
#print(df.iloc[:,0:3])
#print(df.size)
#print(df.shape)
#print(df.memory_usage())
#--------
#Sleccionar filas y columnas a partir de sus nombre con loc y iloc
#print(df.loc[['a','i'],['nombre','califico']])
#print(df.empty)
#--------
#Selecionar registros o filas con campo nulo
#print(df[df['puntaje'].isnull()])
#--------
#DataFrame a partir de Series
#nombres = pd.Series(['Edward','German','Daniela'])
#edades = pd.Series([27,23,19])
#personas = {'nombre':nombres,'edad':edades}
#df = pd.DataFrame(data = personas)
#print(df)
#---------
#df.astype({'X':'int32'}) #Cambiar tipo de dato a la columna
#---------
#Seleccionar registros de una columna en un rango
#df = pd.DataFrame(data = {'nombre':['Olivia','Daniela','Juan','German','Edward','Alex','Julio','Edgar','Angie','Irlesa'],'puntaje':[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18],'Intentos':[1,3,2,3,2,3,1,1,2,1],'califico':['S1','No','Si','No','No','Si','Si','No','No','Si']},index = ['a','b','c','d','e','f','g','h','i','j'])
#print(df[df['puntaje'].between(13,19)])
#---------
#df.isna()
#df.notna()
#---------
#Acceder a un valor o entrada especifico de un objeto DataF usando at
#df = pd.DataFrame(data = {'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]},index = ['a','b','c','d','e'])
#print(df.at['b','Y'])
#print(df.at['e','Z'])
#---------
#modificar valor o entrada especifico usando at
#df.at['b','Y']=29
#print(df)
#---------
#Modificar valor o entrada usando loc
#df.loc['a','Z'] = 12
#print(df)
#---------
#Acceder a una netrada utilizando iat
#df.iat[0,2]
#---------
#Promedio
#df['puntaje'].mean() #Sobre valores que no son nulos
#---------
#Insentar nueva columna en posicion especifica
#df = pd.DataFrame(data = {'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]},index = ['a','b','c','d','e'])
#df.insert(1,'x',[9,5,1,7,3])
#---------
#Nueva fila
#df = pd.DataFrame(data = {'nombre':['Olivia','Daniela','Juan','German','Edward','Alex','Julio','Edgar','Angie','Irlesa'],'puntaje':[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18],'Intentos':[1,3,2,3,2,3,1,1,2,1],'califico':['S1','No','Si','No','No','Si','Si','No','No','Si']},index = ['a','b','c','d','e','f','g','h','i','j'])
#df.loc['k']  = ['Sebastian',17.9,2,'Si']
#---------
#recorrer cada una de las columnas con items
#df = pd.DataFrame(data = {'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]},index = ['a','b','c','d','e'])
#print(df)
#for etiqueta, contenido in df.items():
#    print('Nombre columna: ', etiqueta)
#    print('Contenido: ',contenido,sep ='\n')


