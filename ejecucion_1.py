# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:00:52 2022

@author: Santiago Correa

dudas, espacio en nombre completo, la api no tiene telefono
"""
from validation import class_validation
from database_script import *
import pandas as pd

#%% Iniciación de tabla
df_db=fun_creardb()

#%%
print('''Primer Versión ingreso de información
      1. insertar nuevo
      2. actualizar informacion
      3. eliminar registro
      ''')
      
tipo=input()

if tipo=='1':
    id1,name,email,gender,cellphone=fun_ingresar_info()
    df_db=fun_insertdb(id1,name,email,gender,cellphone,df_db)
elif tipo=='2':
    id1,name,email,gender,cellphone=fun_ingresar_info()
    df_db=fun_updatedb(id1,name,email,gender,cellphone,df_db)
elif tipo=='3':
    id1=input('Ingresar ID: ')
    df_db=fun_borrardb(id1,df_db)
else:
    print('Opcion no valida')
    
    
#%%

    
    



    
