#Mehdi NAOUI
#BTS SIO
#SLAM
#16/10/2024
#
#Exercice 3 : Jeu de devinette des nombres
#Énoncé :
#Écris un programme qui choisit un nombre aléatoire entre 1 et 100, puis demande à
#l'utilisateur de deviner ce nombre. À chaque fois que l'utilisateur entre un nombre, le
#programme lui indique si sa devinette est trop élevée, trop basse ou correcte. Le jeu
#continue jusqu'à ce que l'utilisateur trouve le bon nombre.
#Étapes :
#1. Demander à l'utilisateur d'entrer un nombre entre 1 et 100.
#2. Le programme doit comparer ce nombre avec un nombre secret défini dans le
#programme.
#3. Si le nombre est correct, le programme affiche un message de félicitations et
#termine.
#4. Si le nombre est trop élevé ou trop bas, le programme indique à l'utilisateur de
#deviner à nouveau.
#5. L'utilisateur a un maximum de 10 tentatives.
#_____________________________________________________________________________________
from random import randint
from random import choice
from time import sleep
import pyfiglet


print(pyfiglet.figlet_format(f"Irma"))
print("Bienvenue dans 'Irma'.Appuyer sur une touche pour continuer...")

while True:
	point = "."
	wait_char = "."
	rand_numb = 0
	user_number = 0
	solved = True


	input("Presser Entrer pour générer un nombre aléatoire... ")
	print("Génération")

	for x in range(5):
		sleep(0.3)
		print(wait_char)
		wait_char += point

	rand_numb = randint(1,100)

	print("Un nombre a été génèré aléatoirement.A vous de le trouver!")
	count = 10

	while solved:

		user_number = int(input("Proposer un nombre: "))

		if user_number == rand_numb:
			print(pyfiglet.figlet_format(f" {rand_numb} trouvé! Bravo."))

			if input("Presser 'Entrer' pour recommancer ou 'q' pour quitter...") in ("Q",'q'):
				quit()	
			break
		elif user_number > rand_numb:
			print(f"Le nombre à trouver est infèrieur à {user_number}, {count} tentative(s) restante(s).")
		else:	
			print(f"Le nombre à trouver est supèrieur à {user_number}, {count} tentative(s) restante(s).")
				
		count -= 1 
		if count == 0:
			input("Vous avez échoué...Dix temptatives écoulés :(\n (Presser 'q' pour quitter et entrer pour rejouer)")
			solved = False	
			if input("Presser 'Entrer' pour recommancer ou 'q' pour quitter...") in ("Q",'q'):
				quit()	
		
