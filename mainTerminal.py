# -*- coding: utf-8 -*-

#Header
"""
Ce programme est le programme principal de notre jeu, il permet de lancer des parties
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: Rajouter les high scores
"""
from fonctionUtile import randomElement,hiddenWord,inputLetter,newTry,playerWord
from fichier import fileReading
# randomElement nous renvoie un élément aléatoire d'une liste
# hiddenWord permet d'écrire un mot en chiffré: test devient t__t
# inputLetter permet de demander à l'utilisateur d'entrer une lettre
# newTry permet d'avoir True si on répond Oui
# playerWord permet de faire avancer le mot chiffré: si on devine le e dans test on aura te_t
# fileReading permet de lire un fichier et chaque ligne devient un élément d'une liste qui nous est renvoyée







def startGame(): #Cette fonction lance simplement le jeu
    mot = randomElement(fileReading("word.txt"))
    motcache = hiddenWord(mot)
    vie = 8
    listeLettre = []
    test = False
    while vie > 0 and test == False:
        if motcache != mot:
            print("Le mot que vous devez trouver est:")
            print(motcache)
            print("Il est composé de "+str(len(mot))+" lettres.")
            print("Il vous reste "+str(vie)+" essais pour trouver le mot.")
            lettre = inputLetter(listeLettre)
            listeLettre.append(lettre)
            if lettre not in mot:
                vie -= 1
                print("Dommage la lettre "+lettre+" n'est pas dans le mot !")
                print("******************************")
            else:
                print("Bravo la lettre "+lettre+" était bien dans le mot !")
                motcache = playerWord(lettre,mot,motcache)
                print("******************************")
        else:
            test = True
    if test:
        print("Bravo vous avez trouvé le mot "+mot+" !")
        print("Il vous restait "+str(vie)+" vies.")
    else:
        print("Dommage vous n'avez pas réussi à trouver le mot qui était:")
        print(mot)
    if newTry():
        startGame()

startGame()