# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet de manipuler des fichiers notamment d'en récupérer 
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: fichier de test complet
"""
def fileReading(nomFichier): #Pas de description de la fonction car tout est dis dans le header
    fichier = open(nomFichier,'r')
    listeMot = fichier.readlines()
    for i,element in enumerate(listeMot):
        if "\n" in element:
            listeMot[i] = element[:-1]
    listeMot.sort()
    listeMot.sort(key = lambda item:len(item))
    return listeMot
