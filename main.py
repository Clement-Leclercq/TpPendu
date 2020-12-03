# -*- coding: utf-8 -*-

#Header
"""
Ce programme est le programme principal de notre jeu, il permet de lancer des parties
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: Rajouter les high scores
"""
from fonctionTerminal import randomElement,hiddenWord,inputLetter,newTry,playerWord
from fichier import fileReading

def startGame(): #Cette fonction lance simplement le jeu
    mot = randomElement(fileReading("word.txt"))
    motcache = hiddenWord(mot)
    vie = 8
    test = False
    while vie > 0 and test == False:
        print("Le mot que vous devez trouver est:")
        print(motcache)
        print("Il est composé de "+str(len(mot))+" lettres.")
        print("Il vous reste "+str(vie)+" essais pour trouver le mot.")
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
    if test:
        print("Bravo vous avez trouvé le mot "+mot+" !")
        print("Il vous reste "+str(vie)+" vies.")
    else:
        print("Dommage vous n'avez pas réussi à trouver le mot qui était:")
        print(mot)
    if newTry():
        startGame()

startGame()