import pandas as pd 
import numpy as np
from os import system
system('cls')
# 77 - 105
#--------
#Eliminar fila
#df = pd.DataFrame(data = {'nombre':['Olivia','Daniela','Juan','German','Edward','Alex','Julio','Edgar','Angie','Irlesa'],'puntaje':[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18],'Intentos':[1,3,2,3,2,3,1,1,2,1],'califico':['Si','No','Si','No','No','Si','Si','No','No','Si']},index = ['a','b','c','d','e','f','g','h','i','j'])
#print(df.drop('h'))
#--------
#ordenar en modo descendente por diferentes columnas
#df = df.sort_values(by=['nombre','puntaje'],ascending = [False,True])
#--------
#reemplazar valores de una columna con map
#df['califico'] = df['califico'].map({'Si':True,'No':False})
#print(df)
#--------
#reemplazar valores de una columna con replace
#df['nombre'] = df['nombre'].replace('Alex','Alexander')
#--------
#Guardar registros en un archivo CSV
#df.to_csv('jugadores.csv',index = False)
#--------
#Agregar fila nueva con notación slicing
#colores = ['negro','blanco','azul','lila','cafe','verde','rojo','amarillo','gris','naranja']
#df['color'] = colores 
#--------
#Seleccionar registros donde se cumplan una condición para valores de una columna
#print(df.loc[df['califico'] == 'Si'])
#--------
#iterar cada fila con iterrows
#for indice,fila in df.iterrows():
#    print(fila['nombre'],fila['califico'])
#--------
####df = pd.DataFrame({'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]})
#---------
#Iterar con la funcion itertuples, a modo de tuplas nombradas
#for registro in df.itertuples():
#print(registro.X,registro.Z,registro.Y * registro.X)
#--------
#Agregar fila con append
#nuevo_registro = {'X':6,'Y':0,'C':13}
#df = df.append(nuevo_registro,ignore_index=True)
#--------
#Aplicar una función a todos los elementos con apply
#print(df.apply(np.sqrt))
#print(df.apply(lambda x:x**x))
#print(df.apply(np.sum,axis = 0))
#--------
#Extraer y removere una columna por su nombre a traves de pop
#print(df.pop('Y'))
#--------
#Valodar con isin si un elemento se halla dentro de un DataFrame
#print(df.isin([10,3]))
#print(df.isin({'Z': [10,3]}))
#--------
#reemplazar valores que no cumplan una condicion con where
#print(df.where(df % 2 == 0,-df))
#--------
#Usar mask para modificaar los valores que cumplan una condición
#print(df.mask(df > 3,0))
#--------
#realizar consusltas con la funcion query
#print(df.query('X > Y'))
#print(df[df.X > df.Y]) #Mismo resultado
#--------
#realizar operaciones aritmeticas basicas entre dos objetos DF
#print(df.add(2))
#df.sub(df)
#df.mul(df)
#--------
#Obtener como una lista python los nombres de las columnas
#print(list(df.columns.values))
#--------
#Calcular modulo sobre cada elemento de un objeto DF
#print(df.mod(2))
#--------
#renombrar columnas
#df.rename(columns = 'escribir diccionario con los nuevos nombramientos')
#--------
#Producto punto
#df_1 = pd.DataFrame([[1,2,3,4,5],[5,4,3,2,1],[2,3,4,7,11]])
#df_2 = pd.DataFrame([[1,2,4],[9,8,7],[1,1,1],[3,2,1],[8,5,2]])
#print(df_1.dot(df_2))
#--------
#Usar operadores relacionares para comparar elementos
#print(df_1 < df_2)
#--------
#Metodos de instancia comparaciones
#df_1 = pd.DataFrame({'X':[1,2,3,4,5],'Y':[5,4,3,2,1],'Z':[2,3,5,7,11]})
#df_2 = pd.DataFrame({'X':[8,9,3,2,1],'Y':[0,2,0,1,1],'Z':[2,4,13,2,11]})
#print(df_1.eq(df_2))
#print(df_1.ne(df_2))
#---------
#Cambiar orden de las columnas 
#df_1 = df_1[['X','Z','Y']]
#print(df_1)
#---------
#Combinas dos DF y dejar en cada columna el valor minimo de la suma por columna
#df1 = pd.DataFrame({'A':[1,1],'B':[5,5]})
#df2 = pd.DataFrame({'A':[3,3],'B':[2,2]})
#minimo_columna = lambda s1,s2: s1.sum() if s1.sum() < s2.sum() else s2.sum()
#print(df1.combine(df2,minimo_columna))
#---------
#generar una representacion de los elementos con applymap
#df = pd.DataFrame([[3.1415,2.717],[1.41,1]])
#print(df.applymap(lambda x:len(str(x))))
#print(df.applymao(lambda x:x**2)) == df**2
#--------
#Usar groupby para agrupar datos por una columna especifica y contar la cantidad de elementos 
#df.groupby(['lengguaje']).size().reset_index(name = 'numero_preferencias')
#--------
#Usar agg para realizar varias operaciones por un eje
#df = pd.DataFrame({'W':[1,2,3,4,5],'X':[2,3,5,7,11],'Y':[5,4,3,2,1],'Z':[np.nan,np.nan,np.nan,np.nan,np.nan]})
#print(df.agg(['sum','min','max']))
#print(df.agg({'W':['sum'],'X':['sum','min','max'],'Y':['min','max'],'Z':['sum']}))
#--------
#agregar prefijos o sufijos a nombres de columnas
#df.add_prefix('columna')
#df.add_suffix('_col')