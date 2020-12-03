# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet de prendre un élément aléatoirement dans une liste donnée
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: fichier de test complet
"""
from random import randint #On importe le module qui nous permet de générer un nombre entier aléatoire
from fichier import fileReading #On importe la fonction nous permettant


def randomElement(liste): #Cette fonction prend un élément aléatoire dans une liste
    randomNumber = randint(0,len(liste)-1)
    return liste[randomNumber]

def startGame(): #Cette fonction lance simplement le jeu
    mot = randomElement(fileReading("word.txt"))
    motcache = hiddenWord(mot)
    vie = 8
    test = False
    while vie > 0 and test == False:
        print("Le mot que vous devez trouver est:\n")
        print(motcache)
        print("Il est composé de "+len(mot)+" lettres.")
        print("Il vous reste "+vie+" essais pour trouver le mot.")
        if motcache != mot:
            lettre = inputLetter()
            if lettre not in mot:
                vie -= 1
                print("Dommage la lettre "+lettre+" n'est pas dans le mot !")
            else:
                print("Bravo la lettre "+lettre+" était bien dans le mot !")
                motcache = playerWord(lettre,mot,motcache)
        else:
            test = True


def checkInput(lettre): #Cette fonction vérifie que c'est bien une seule lettre qui a été rentrée
    if (len(lettre) == 1 and lettre in "AZERTYUIOPQSDFGHJKLMWXCVBN"):
        return True
    else:
        return False

def inputLetter(): #Cette fonction permet la saisie d'une lettre par l'utilisateur
    lettre = "test"
    while (not checkInput(lettre)):
        lettre = input("Merci d'entrer une lettre:\n").upper()
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
