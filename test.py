# -*- coding: utf-8 -*-

#Header
"""
Ce programme est le programme testant l'intégralité des fonctions dans fichier.py et fonctionTerminal.py
Programme fait par Clément Leclercq
Fait le 03/12/2020
TO DO: améliorer les tests pour voir plus de cas spéciaux
"""
from fichier import fileReading #Permet d'ouvrir un fichier et de créer une liste avec comme élément chaque ligne 
from fonctionTerminal import newTry,checkInput,inputLetter,hiddenWord,playerWord,listIntoWord
#newTry renvoie vrai si nous mettons un mot commençant par O (comme pour dire oui) et faux sinon
#checkInput renvoie vrai si nous envoyons une lettre de l'alphabet sans accent / cédille, faux sinon
#inputLetter procède à la saisie d'une lettre en vérifiant qu'elle n'ai pas été déjà présente dans une liste
#hiddenWord permet de renvoyer le mot qu'on lui a donné avec des _ sauf la première lettre qui est en claire (si d'autres lettres sont la même que la première elles sont aussi en claires)
#playerWord permet de remplacer les _ dans un mot caché par hiddenWord si nous lui donnons la bonne lettre
#listIntoWord permet de créer une chaîne de caractère continue avec les éléments d'une liste

print("Test de fileReading:")
print("Nous devons avoir la liste suivante: ['je','suis','un test'] et ici nous obtenons:")
print(fileReading("test.txt"))
print("Test de newTry")
print(newTry())
print("Test checkInput")
print("Nous donnons 'a' et devons avoir True:")
print(checkInput("a"))
print("Nous donnons '1' et devons avoir False:")
print(checkInput("1"))
print("Nous donnons 'ç' et devons avoir False:")
print(checkInput("ç"))
print("Test inputLetter")
print("Nous donnons comme liste ['A'] tester avec 1,a,b ")
print(inputLetter(['A']))
print("Test hiddenWord")
print("Donner test et normalement on a t__t")
print(hiddenWord("test"))
print("Test playerWord")
print("Nous donnons ('e','test','t__t') et nous devons avoir te_t")
print(playerWord('e','test','t__t'))
print("Test listIntoWord")
print("Nous donnons ['ceci','est',1,['test']] et nous devons obtenir 'ceciest1['test']'")
print(listIntoWord(['ceci','est',1,['test']]))
