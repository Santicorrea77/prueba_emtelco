# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:00:49 2022

@author: Santiago Correa
"""


class class_validation:
    
    def __init__(self):
        print('validación')

    def fun_id(id1):
        if len(id1)>=4 and len(id1)<=11 and id1.isdigit():
            print('id valido')        
            ban_id=True
            
        else:
            print('id no valido')
            ban_id=False
        
        return ban_id



    def fun_name(name):
        if len(name)>=1 and len(name)<=100 and name.replace(' ','').isalpha():
            print('nombre valido')
            ban_nam=True
            
        else:
            print('nombre no valido')
            ban_nam=False
        
        return ban_nam



    def fun_gen(gender):
        
        list_gen=["masculino", "femenino", "otro"]
        
        if gender in list_gen:
            print('genero valido')
            ban_gen=True
        else:
            print('genero no valido')
            ban_gen=False
        
        return ban_gen


    def fun_tel(cellphone):
        
        if len(cellphone)==10 and cellphone.isdigit() and cellphone[0] in ['6','3']:
            print('telefono valido')
            ban_tel=True
            
        else:
            print('telefono no valido')
            ban_tel=False
        
        return ban_tel


    def fun_mail(email):
            
        if '@' in email:
            print('correo valido')
            ban_mail=True
        else:
            print('correo no valido')
            ban_mail=False
        
        return ban_mail