# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:34:58 2022

@author: Santiago Correa
"""

#%% crera db
from validation import class_validation
import requests
import pickle
import pandas as pd

#%%

def fun_ingresar_info():
    
    val=class_validation
    
    id1=input('Ingresar id: ')
    b_id=val.fun_id(id1)
    
    name=input('Ingresar nombre completo: ')
    b_nam=val.fun_name(name)
    
    email=input('Ingresar email: ')
    b_mai=val.fun_mail(email)
    
    gender=input('Ingresar genero: ')
    b_gen=val.fun_gen(gender)
    
    cellphone=input('Ingresar Telefono: ')
    b_tel=val.fun_tel(cellphone)
    
    return int(id1),name,email,gender,cellphone

#%%

def fun_savedb(df_db):
    ## save
    with open('database', 'wb') as handle:
        pickle.dump(df_db, handle, protocol=pickle.HIGHEST_PROTOCOL)

def fun_loaddb():
    ## load
    with open('database', 'rb') as handle:
        df = pickle.load(handle)
        
    return df

def fun_creardb():
    
    try: 
        df_db=fun_loaddb()
    except:
        df_db=pd.DataFrame(columns=['id','name','email','gender','phone'])
    
    response = requests.get('https://gorest.co.in/public/v2/users').json() 
    
    for res in response:    
        lt_user=list(res.values())[0:4]
        lt_user.append('')
        
        search1=df_db[df_db['id']==lt_user[0]]        
        if len(search1)==0:
            df_db.loc[len(df_db)]=lt_user
    
    fun_savedb(df_db)
        
    return df_db
    
    
#%% borrar db

def fun_borrardb(id1,df_db):
    try:
        ind1=df_db[df_db['id']==int(id1)].index[0]
        df_db=df_db.drop(index=ind1).reset_index(drop=True)
        
        fun_savedb(df_db)
    except:
        print('No se encuentra usuario')
    return df_db

#%% insertar en db

def fun_insertdb(id1,name,email,gender,cellphone,df_db):    
    
    search1=df_db[df_db['id']==id1]    
    
    if len(search1)==0:
        df_db.loc[len(df_db)]=id1,name,email,gender,cellphone
        fun_savedb(df_db)
    else:
        print('ya se encuentra registrado')
    
    return df_db

#%% actualizar

def fun_updatedb(id1,name,email,gender,cellphone,df_db):
    try:
        ind2=df_db[df_db['id']==id1].index[0]
        df_db.loc[ind2]=int(id1),name,email,gender,cellphone
        fun_savedb(df_db)        
    except:
        print('No se encuentra registro')
        
    return df_db