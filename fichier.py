# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet de manipuler des fichiers en récupérant des données
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO:
    - fichier de test complet
    - gestion du fichier des highscores
"""
def fileReading(nomFichier): #Permet d'ouvrir un fichier dans lequel on va prendre chaque ligne et retirer 
    fichier = open(nomFichier,'r')
    listeMot = fichier.readlines()
    for i,element in enumerate(listeMot):
        if "\n" in element:
            listeMot[i] = element[:-1]
    listeMot.sort()
    listeMot.sort(key = lambda item:len(item))
    return listeMot
