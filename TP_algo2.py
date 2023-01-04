# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:39:38 2023

@author: Gloire MBONGA et Joseph DZAPILI
"""

import math
class rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def aire(self):
        return self.longueur*self.largeur
    def perimetre (self):
        return (self.longueur+self.largeur)*2
    
class cercle:
    def __init__(self,rayon):
        self.rayon=rayon
    def aire(self):
        return math.pi*self.rayon**2
    def perimetre (self):
        return 2*math.pi*self.rayon
class triangle:
    def __init__(self,AB,BC,AC,hauteur_de_AC):
        self.AB=AB
        self.BC=BC
        self.AC=AC
        self.hauteur_de_AC=hauteur_de_AC
    def aire(self):
        return self.hauteur_de_AC*self.AC/2
    def perimetre (self):
        return self.AB+self.BC+self.AC
class carre:
     def __init__(self,cote):
        self.cote=cote
     def aire(self):
        return self.cote**2
     def perimetre(self):
        return self.cote*4
class triangle_rectangle:
    def __init__(self,AB,AC,hauteur_de_AC):
        self.AB=AB
        self.AC=AC
        self.hauteur_de_AC=hauteur_de_AC
    def aire(self):
        return self.AC*self.hauteur_de_AC/2
    def perimetre (self):
        return self.AB+self.hauteur_de_AC+self.AC
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
