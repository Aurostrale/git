##!/usr/local/bin/python3
## -*- coding:utf-8 -*-

from random import randrange
from math import ceil
print ("====Bienvenue dans notre casino====")

#definition des variables
cagnotte=500
continuer="o"
			
while cagnotte>0 and continuer == "o":
	random=randrange(50) #il donne un nombre random
	print(random) #on l'affiche pour le test
	choix=int(input("Choisissez un nombre entre 0 et 49 : ")) #on demande un nombre au joueur
	print("Votre cagnotte est de", str(cagnotte), "€") #rappelle de la cagnotte
	while choix < 0 or choix > 49 : #tant que le nombre choisit n'est pas compris entre 0 et 49
		choix=int(input("Choisissez un nombre entre 0 et 49 : ")) # on lui redemande un nombre compris entre 0 et 49
	else: #ici on sort de la boucle while car il nous donne un nombre compris entre 0 et 49 
		mise=int(input("Choisissez une somme à miser : ")) #quelle est la mise voulue
		while mise > cagnotte : # si la mise est supérieure à la cagnotte, on rentre dans une boucle 
			print("Vous ne pouvez pas miser plus que votre cagnotte")
			continuer=input("Voulez-vous continuer ? [o/n] : ")
			if continuer == "n":
				print("Tant pis, à bientôt !")
				break
			else: #ici le continuer sera égal à "o"
				mise=int(input("Choisissez une somme à miser : "))	
	if (choix==random):
		gain=mise*3
		print("Bravo, vous avez gagné ", int(gain), "€ !")
		cagnotte=cagnotte+gain
		print("Votre cagnotte est de", int(cagnotte), "€")
		continuer=input("Voulez-vous continuer ? [o/n] : ")
	elif ((random % 2) == 0 and (choix % 2) == 0) or ((random % 2) == 1 and (choix % 2) == 1):
		gain=mise*0.5
		print("Bravo, vous avez gagné ", int(gain), "€ !")
		cagnotte=cagnotte+gain
		print("Votre cagnotte est de", int(cagnotte), "€")
		continuer=input("Voulez-vous continuer ? [o/n] : ")
	else:
		print("Vous avez perdu :( ")
		cagnotte=cagnotte-mise
		print("Votre cagnotte est de", int(cagnotte), "€")
		if cagnotte==0: # on stop la boucle si la cagnotte est égale à zéro
			print("Vous êtes fauché, au revoir.")
			break
		continuer=input("Voulez-vous continuer ? [o/n] : ")	 # on continue tant que la cagnotte n'est pas à zéro

