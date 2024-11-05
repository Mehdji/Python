#MEHDI NAOUI
#BTS SIO 2024
#SLAM
#
#Exercice 4: Factorielle iterative
#_________________________________________
from rich import print as rprint
#Variables diverses:
n: int = 0
flag: bool = True
user_value: str = ""
j: int = 0
choice: str = ""

#Variables de méssage:
welcome = "Bienvenue. Ce script trouve la Factorielle d'un nombre entrer par l'utilisateur.\n"
quit_ = "Pour quitter entrer 'q' ou 'Q'...\n"
enter = "Presser entrer pour continuer..."
mess_valeur = "Entrer un nombre ou un chiffre: " 
erreur_num = "Uniquement un nombre ou un chiffe s'il vous plait..."


def factorielle_for(user_value):
	j = 1
	for x in range(1,user_value + 1):

		j *= x
		rprint(f"{j} x {x} =", j)
	return j

def factorielle_while(user_value):
	j = 1
	z = 1
	while z != (user_value + 1):
		
		j *= z
		rprint(f"{j} x {z} =", j)
		z += 1
	return j
	

rprint(welcome + quit_)

while flag:
	
	user_value = input(mess_valeur)
	
	if user_value in ("q","Q"):
		break

	if not user_value.isnumeric():
		rprint(erreur_num)
		continue
	else:
		choice = input("Enrer 'f' pour la méthode for et et 'w' pour la méthode while:")
		if choice in ("f" , "F"): 
			rprint("Méthode 'For':")
			rprint(f"Le factorielle de {str(user_value)} noté {str(user_value)}! est égale {(factorielle_for(int(user_value)))}")
		else:
			rprint("Méthode 'While':")
			rprint(f"Le factorielle de {str(user_value)} noté {str(user_value)}! est égale {(factorielle_while(int(user_value)))}")

