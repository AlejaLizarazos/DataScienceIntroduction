import pandas as pd
import numpy as np
#from os import system
#system('cls')
#----------GROUP BY--------------------
df = pd.DataFrame({'age':[15,16,16,15],'name':['adam','bob','dave','fred'],'test1':[95,81,89,np.nan],'test2':[80,82,84,88],'teacher':['ashby','ashby','jones','jones']})
df.groupby('teacher').median()[['test1','test2']]
df.groupby(['teacher','age']).median()
df.groupby(['teacher','age']).agg(['min','max'])
df = df.pivot_table(index = ['teacher','age'],values = ['test1','test2'],aggfunc=[len,sum],margins = True)
print(df)
#----------MERGE DATA FRAMES ----------
df1 = pd.DataFrame({'name': ['John', 'George', 'Ringo'],\
                    'color': ['Blue', 'Blue', 'Purple']})
df2 = pd.DataFrame({'name': ['Paul', 'George', 'Ringo'],\
                    'carcolor': ['Red', 'Blue', np.nan]},\
                    index=[3, 1, 2])
df = pd.concat([df1,df2],axis = 1)
df = df1.merge(df2)
df1.merge(df2,how = 'outer')
df1.merge(df2,how = 'left')
df1.merge(df2,how = 'right')
#-----------
df = pd.DataFrame({'age':[15,16,16,15],'test1':[95,81,89,np.nan],'test2':[80,82,84,88]},index = ['adam','bob','dave','fred'])
print(df.mean(axis = 1))