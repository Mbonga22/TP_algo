# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:09:16 2023

@author: Gloire MBONGA
"""



from TP_algo2 import*

class forme_geometrique:
    
    
    print("menu : ")
    print(" 1° rectangle \n 2° triangle \n 3° cercle \n 4° carré \n 5° triangle_rectangle")
    print("veuillez effectuer votre choix pour le test du calcul du perimetre et de la surface ")
    try:
    
        choix=int(input("choix : "))

        while (choix !=1 and choix !=2 and choix !=3 and choix !=4 and choix !=5 ):
            print("veuillez faire le bon choix")
            choix=int(input("choix : ")) 
    except:
        print("entrer des valeurs numerique")
    
    if choix==1:
        print("le perimetre et la aire du rectangle donne")
        rect=rectangle(5,7)
        print("la aire du rectangle : ",rect.aire())
        print("le perimetree du rectangle : ",rect.perimetre())
        
    elif choix==2  :
        print("le perimetre et la aire du triangle donne")
       
        tri=triangle(6,8,5,4)
        print("la aire du triangle est :  ",tri.aire())
        print("le perimetre du triangle est : ",tri.perimetre())
    elif choix==3  :
        print("le perimetre et la surface du cercle donne")
        cer=cercle(7)
        print("la aire du cercle : ",cer.aire())
        print("le perimetre du cercle : ",cer.perimetre())
         
    elif choix==4:
        print("la aire et du perimetre d'un carré donne")
        car=carre(5)
        print("la aire du carré est :  ",car.aire())
        print("le perimetre du carré est : ",car.perimetre())
    
    elif choix==5  :
        print("le perimetre et la aire du triangle_rectangle donne")
    
        triRe=triangle_rectangle(7,4,5)
        print("la aire du triangle est :  ",triRe.aire())
        print("le perimetre du rectangle est : ",triRe.perimetre())    
