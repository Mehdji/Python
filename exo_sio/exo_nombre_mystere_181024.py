#Mehdi NAOUI
#18/10/24
#BTS SIO
#
#Exercice 3: Jeu du nombre mystère.
#Profésseur: M.SAMARRA
#________________________________
#Début du code
#vvvvvvvvvvvvvv

#Import randint pour génerer un chiffre entier pseudo aléatoire.
from random import randint

#Déclaration de mes variables (et leur typages qui n'est pas obligatoire en python.)
x: int = randint(0,100)
user_value: str = ""
count: int = 1
flag: bool = True

#Chaine de caractère pour les méssages à présenter sur l'écran utilisateur:
welcome: str = "Bienvenue dans IRMA.\nPresser entrer... "
win: str = "Vous avez gagné!Vous avez trouvé "
more: str = "Le nombre à mystère est supèrieur à "
less: str = "Le nombre à mystère est inférieur à "
count_mess = "Tentative numéro: "

def test_result(x,user_input):
	"""Si la valeur utilisateur entrée est 
		supèrieur ou infèrieur la fontion retourne 0
		sinon si la valeur est égale au nombre aléatoire 
		la valeur retourné est égale a 1"""

	if user_input == x:
		return 0
	elif user_input > x:
		return 1
	else:
		return -1

#Méssage de bienvenue à l'utilisateur.
input(welcome)
print("('q' pour quitter):\n") 

#La boucle suivante est le point d'entrée du script.
#Tant que que le résultat n'est pas trouvé ou bien 'q' n'est 
#pas entrée par l'utilisateur la boucle continue.
while flag:
	user_value = input("Devinez le nombre mystére:")
	
	#Quitte si l'utilisateur tape 'q'.
	if user_value in ("q","Q"):
		break
	
	#Test si la valeur est un caractère numérique
	#Si ce n'est pas le cas un méssage s'affiche et 
	#la boucle retourne au début(while).
	if not user_value.isnumeric():
		print("Caractère numérique uniquement S'il vous plait...")
		continue
	else:
		#Maintenant que nous savons l'entrée utilisateur valide(un chiffre/nombre)
		#Nous transtyper cette variable puis la tester succesivement afin de savoir
		#si elle est inférieur, égale ou supèrieur à notre la valeur dans x(entier aléatoire).
		#Le nombre de tour (count) est incémenter a chaque passage.

		user_value = int(user_value)
		
		if test_result(x,user_value) == 0:

			print(win + str(user_value) + ".\n" + count_mess + str(count) + "\n")
			flag = False

		elif test_result(x,user_value) == 1:
			print(less + str(user_value) + ".\n" + count_mess + str(count) + "\n")		
			count += 1
		else: 
			print(more + str(user_value) + ".\n" + count_mess + str(count) + "\n")
			count += 1



#^^^^^^^^^^
#Fin du code
