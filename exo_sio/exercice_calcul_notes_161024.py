#Mehdi NAOUI
#BTS SIO
#SLAM
#16/10/2024
#
#Exercice 1 : Calcul des notes et détermination du résultat final
#Énoncé :
#Demande à l'utilisateur de saisir 5 notes. Le programme calcule la moyenne de ces
#notes et détermine si l'utilisateur a réussi ou échoué. La condition de réussite est
#d'obtenir une moyenne supérieure ou égale à 10.
#______________________________________________________________________________________

import pyfiglet

notes = 0
nbre_notes= 0

print(pyfiglet.figlet_format("Moyenne calculator"))

while True:
		
	for x in range(5):
		notes += float(input(f"Veuillez ajouter la note {x}/5: "))
		nbre_notes += 1

	moyenne = notes / nbre_notes
	print(f"Votre moyenne: {moyenne:0.2f}")

	if moyenne >= 10:
		print("Félicitation vous avez la moyenne!")
	else:
		print("Echoué: Vous n'avez pas la moyenne...") 

	if input("Pressez 'r' pour reommencer ou 'q' pour quitter...") in ("q"):
		quit()
	notes = 0
	nbre_notes = 0
