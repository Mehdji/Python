#Mehdi NAOUI
#BTS SIO
#SLAM
#16/10/2024
#
#Exercice 2 : Compter les nombres pairs et impairs dans une séquence
#Énoncé :
#Demande à l'utilisateur d'entrer un nombre entier n. Le programme doit ensuite compter
#combien de nombres pairs et combien de nombres impairs existent dans la plage allant
#de 1 à n (inclus).
#_____________________________________________________________________________________
while True:
	nbre_entier = 0
	nbre_impairs = 0
	nbre_pairs = 0


	nbre_entier = int(input("Entrer un nombre entier: "))
	for x in range(1,nbre_entier + 1):
		if x % 2 == 0:
			nbre_pairs += 1
		else:
			nbre_impairs += 1
	print(f"Nombre impair: {nbre_impairs}\nNombre pairs: {nbre_pairs}") 
		

