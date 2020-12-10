# -*- coding: utf-8 -*-

#Header
"""
Ce programme est le programme principal de notre jeu en mode fenêtre, il permet de lancer le jeu et la création de la fenêtre avec tous les widgets
Programme fait par Clément Leclercq
Fait le 10/12/2020
TO DO: Rajouter les high scores / Mettre en forme un peu mieux fenêtre
"""
#Importation des bibliothèques tkinter nécessaires
from tkinter import Tk, Button, Label, StringVar, Entry, Canvas, PhotoImage, NW
from tkinter import messagebox #permet la boite de dialogue
#Importation des fonctions du module dont on a besoin
from fichier import fileReading
from fonctionUtile import randomElement,hiddenWord,newTry,playerWord,checkInput

def motJoueur(lettre,mot,motcache):
    global texte
    texte.set(playerWord(lettre,mot,motcache))
    
def verification():
    global texte2
    global motcache
    global vie
    global filename
    global texte
    guess = lettre.get().upper()
    if checkInput(guess):
        if guess in mot:
            if playerWord(guess,mot,motcache) != mot:
                motcache = playerWord(guess,mot,motcache)
                motJoueur(guess,mot,motcache)
            else:
                texte.set("Vous avez gagné, le mot était "+mot+" !")
                newButton()
        elif vie != 1:
            vie -= 1
            filename = "images/bonhomme"+str(vie)+".gif"
            Ouvrir()
            texte2.set("Il vous reste "+str(vie)+" vies")
        else:
            texte.set("Dommage vous avez perdu, le mot était "+mot+" !")
            texte2.set("Il vous reste 0 vies")
            newButton()
    else:
        messagebox.showwarning("Erreur","Veuillez entrer une lettre et non pas un mot")

def newButton():
    global boutonVerif
    boutonVerif.destroy()
    boutonVerif = Button(penduWindow,text = "Rejouer ?",command = jouer)
    boutonVerif.grid(row = 4, column = 1)

def Ouvrir():
    global photos
    canevasPendu.delete()
    photo = PhotoImage(file = filename)
    photos.append(photo)
    canevasPendu.create_image(0,0,anchor = NW, image = photo)

def jouer():
    global motcache
    global texte
    global texte2
    global boutonVerif
    global mot
    global lettre
    global vie
    global filename
    global photos
    global canevasPendu
    global labelMot
    global labelVie
    global champLettre

    canevasPendu.destroy()
    labelMot.destroy()
    labelVie.destroy()
    champLettre.destroy()
    boutonVerif.destroy()

    photos=[]
    mot = randomElement(fileReading("word.txt"))
    motcache = hiddenWord(mot)
    lettre = ""
    vie = 8
    filename = "images/bonhomme"+str(vie)+".gif"
    texte = StringVar()
    motJoueur(lettre,mot,motcache)

    canevasPendu = Canvas(penduWindow, width = 300, height = 300,bg="white")
    
    Ouvrir()

    labelMot = Label(penduWindow, textvariable = texte)
    
    texte2 = StringVar()
    texte2.set("Il vous reste "+str(vie)+" vies")
    labelVie = Label(penduWindow, textvariable = texte2)
    
    lettre = StringVar()

    champLettre = Entry(penduWindow, textvariable = lettre)
    champLettre.focus_set()
    
    boutonVerif = Button(penduWindow, text = "Valider", command = verification)

    labelMot.grid(row = 1, column = 1)
    labelVie.grid(row = 2, column = 1)
    champLettre.grid(row = 3, column = 1)
    boutonVerif.grid(row = 4, column = 1)
    canevasPendu.grid(row = 1, column = 2, rowspan = 4, sticky = "NE")
    

    
    
    
    

    



penduWindow = Tk()
penduWindow.title("Jeu du pendu")
penduWindow.geometry("600x300+0+0")
"""
photos=[]
mot = randomElement(fileReading("word.txt"))
motcache = hiddenWord(mot)
lettre = ""
vie = 8
filename = "images/bonhomme"+str(vie)+".gif"
texte = StringVar()
motJoueur(lettre,mot,motcache)

canevasPendu = Canvas(penduWindow, width = 300, height = 300,bg="white")
canevasPendu.pack()
Ouvrir()

labelMot = Label(penduWindow, textvariable = texte)
labelMot.pack()

texte2 = StringVar()
texte2.set("Il vous reste "+str(vie)+" vies")
labelVie = Label(penduWindow, textvariable = texte2)
labelVie.pack()

lettre = StringVar()

champLettre = Entry(penduWindow, textvariable = lettre)
champLettre.focus_set()
champLettre.pack()

boutonVerif = Button(penduWindow, text = "Valider", command = verification)
boutonVerif.pack()
"""
boutonVerif=Label(penduWindow)
champLettre = Entry(penduWindow)
labelMot = Label(penduWindow)
canevasPendu = Canvas(penduWindow)
labelVie = Label(penduWindow)

jouer()

penduWindow.mainloop()
