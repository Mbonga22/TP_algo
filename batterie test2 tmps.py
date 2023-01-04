# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:09:16 2023

@author: Gloire MBONGA et Joseph DZAPILI
"""

from time import*

from TP_algo2 import*

class forme_geometrique:
        debut=time()
   
        print("le perimetre et la aire du rectangle donne")
        rect=rectangle(5,7)
        print("la aire du rectangle : ",rect.aire())
        print("le perimetree du rectangle : ",rect.perimetre())
        
    
        print("le perimetre et la aire du triangle donne")
       
        tri=triangle(6,8,5,4)
        print("la aire du triangle est :  ",tri.aire())
        print("le perimetre du triangle est : ",tri.perimetre())
   
        print("le perimetre et la surface du cercle donne")
        cer=cercle(7)
        print("la aire du cercle : ",cer.aire())
        print("le perimetre du cercle : ",cer.perimetre())
         
    
        print("la aire et du perimetre d'un carré donne")
        car=carre(5)
        print("la aire du carré est :  ",car.aire())
        print("le perimetre du carré est : ",car.perimetre())
    
    
        print("le perimetre et la aire du triangle_rectangle donne")
    
        triRe=triangle_rectangle(7,4,5)
        print("la aire du triangle est :  ",triRe.aire())
        print("le perimetre du rectangle est : ",triRe.perimetre())

        fin=time()
        temps= fin-debut
        print("le temps  d'execution est {:.2f}".format(temps))
