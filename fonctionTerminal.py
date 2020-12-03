# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet de prendre un élément aléatoirement dans une liste donnée
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: fichier de test complet
"""
from random import randint #On importe le module qui nous permet de générer un nombre entier aléatoire

def randomElement(liste): #Cette fonction prend un élément aléatoire dans une liste
    randomNumber = randint(0,len(liste)-1)
    return liste[randomNumber]

def newTry(): #Cette fonction demande à l'utilisateur s'il veut rejouer et renvoie True ou False en fonction de la réponse (Oui ou Non)
    valRen = False
    reponse = input("Voulez vous rejouer (Oui ou Non) ?\n")
    if reponse[0].upper() == "O":
        valRen = True
    return valRen

def checkInput(lettre): #Cette fonction vérifie que c'est bien une seule lettre qui a été rentrée
    if (len(lettre) == 1 and lettre.upper() in "AZERTYUIOPQSDFGHJKLMWXCVBN"):
        return True
    else:
        return False

def inputLetter(listeLettre): #Cette fonction permet la saisie d'une lettre par l'utilisateur et vérifie qu'elle n'a pas déjà été utilisée
    lettre = ""
    while checkInput(lettre) == False or lettre in listeLettre:
        print("La liste des lettres déjà utilisées:")
        print(listeLettre)
        lettre = input("Merci d'entrer une lettre (sans accent) et qui n'a pas encore été utilisée:\n").upper()
    return lettre

def hiddenWord(mot): #Cette fonction permet de renvoyer le mot à deviner avec des _ sauf la première lettre qui est en claire (si d'autres lettres sont la même que la première elles sont aussi en claires)
    liste = []
    for element in mot:
        test = mot[0]
        if element == test:
            liste.append(element)
        else:
            liste.append("_")
    valRen = listIntoWord(liste)
    return valRen

def playerWord(lettre,mot,motcache): #Cette fonction permet de construire le mot du joueur au fur et à mesure qu'il joue
    liste = []
    for element in mot:
        if element == lettre or element in motcache:
            liste.append(element)
        else:
            liste.append("_")
    valRen = listIntoWord(liste)
    return valRen

def listIntoWord(liste): #Cette fonction permet de construire un mot à partir d'une liste
    valRen = ""
    for element in liste:
        valRen += str(element)
    return valRen
