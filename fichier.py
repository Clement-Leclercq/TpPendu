# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet de prendre les mots dans un fichier de les classer par longueur et par ordre alphabétique et de renvoyer la liste de mots classés
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: fichier de test complet
"""
def fileReading(nomFichier):
    fichier = open(nomFichier,'r')
    listeMot = fichier.readlines()
    for i,element in enumerate(listeMot):
        if "\n" in element:
            listeMot[i] = element[:-1]
    listeMot.sort()
    listeMot.sort(key = lambda item:len(item))
    return listeMot
