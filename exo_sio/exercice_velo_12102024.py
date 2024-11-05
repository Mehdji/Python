#Mehdi NAOUI, BTS SIO, 2024
#Exercice_velo_121024.py
#
#Exercice : Location de vélos
#
#______________________________________________________________________________________________
#Le but de cet exercice est de permettre à un service de location de vélos (tournant 24 heures
#sur 24) de facturer ses clients. Le programme demandera à l’utilisateur d’entrer les heures de
#début et de fin de location sous la forme d’entiers (on ne se préoccupe pas des minutes pour
#simplifier).
#Les tarifs de location sont définis comme suit :
#▪ 1 euro par heure si le vélo est loué entre 0h et 7h ou entre 17h et 24h ;
#▪ 2 euros par heure si le vélo est loué entre 7h et 17h.
#Votre programme que vous allez nommer Velo.py demandera à l’utilisateur de quelle
#heure à quelle heure se fait la location et calculera le prix de la location en conséquence.
#Vous adopterez les simplifications suivantes :
#"▪ Les heures de début et fin de location sont des entiers (pas de demi ni de quart, toute
#heure entamée est due) ;
#▪ L’heure du début de la location est toujours inférieure à l’heure de la fin de la location ;
#cela implique que la location ne peut pas se faire sur plus de 24 heures ; elle doit se faire
#dans la même journée.
#Si les données introduites sont correctes, votre programme affichera simplement le coût de
#la location en respectant strictement les formats donnés dans les exemples de déroulement
#ci-dessous.
#En cas de donnée incorrecte, votre programme devra afficher un message d’erreur et inviter
#l’utilisateur à corriger ces erreurs. Utilisez strictement les messages suivants :
#▪ « Les heures doivent être comprises entre 0 et 24 ! » suivi d’un saut de ligne, si une des
#heures introduites par l’utilisateur n’est pas comprise entre 0 et 24 (inclus) ;
#▪ « Attention ! l’heure de fin est identique à l’heure de début. » suivi d’un saut de ligne, si
#les heures de début et fin de location sont identiques ;
#▪ « Attention ! le début de la location est après la fin ... » suivi d’un saut de ligne si l’heure
#de début de la location est supérieure à l’heure de fin.Exemples de déroulement :
#Il est impératif que votre code respecte le format de réponse suivant :
#1) Exemple où la durée de location implique les deux tarifs :
#Donnez l’heure de début de la location (un entier) : 10
#Donnez l’heure de fin de la location (un entier) : 19
#Vous avez loué votre vélo pendant
#2 heure(s) au tarif horaire de 1.0 euro(s)
#7 heure(s) au tarif horaire de 2.0 euro(s)
#Le montant total à payer est de 16.0 euro(s).
#2) Exemple où la durée de location n’implique qu’un seul tarif :
#Donnez l’heure de début de la location (un entier) : 18
#Donnez l’heure de fin de la location (un entier) : 20
#Vous avez loué votre vélo pendant
#2 heure(s) au tarif horaire de 1.0 euro (s)
#Le montant total à payer est de 2.0 euro (s).
#
#__________________________________________________________________________________________________
#Constant:
TARIF_1 = 2
TARIF_2 = 1
#Variable:
heure_deb = 0
heure_fin = 0
duree_tarif_1 = 0
duree_tarif_2 = 0
prix_total = 0
#____________________________________________________________________________
#Error message:
MSG_0_24 = "Les heures doivent être comprises entre 0 et 24!"
MSG_DEB_FIN_EGALE = "Attention! l'heure de fin est identique à l'heure de début."
MSG_DEB_APR_FIN = "Attention! le début de la location est aprés la fin..."

#____________________________________________________________________________
#Message:

MSG_HEUR_DEB_INPUT = "Donnez l’heure de début de la location (un entier) : "
MSG_HEUR_FIN_INPUT = "Donnez l’heure de fin de la location (un entier) : "
MSG_LOUER_PENDANT = "Vous avez loué votre vélo pendant: "
MSG_AU_TARIF = " heure(s) au tarif horaire de "
MSG_TARIF_TOTAL = "Le montant total à payer est de "
#MSG_TOTAL_TARIF_1= (f"{MSG_LOUER_PENDANT}\n{duree_tarif_2}{MSG_AU_TARIF}{TARIF_2} euro(s)")
#MSG_TOTAL_TARIF_2= (f"{MSG_LOUER_PENDANT}\n{duree_tarif_1}{MSG_AU_TARIF}{TARIF_1} euro(s)")
#MSG_TARIF_TOTAL = (f"Le montant total à payer est de {prix_total}")
 
def int_test(heure_deb, heure_fin):
	"""Test si une valeur entrée par l'utilisateur est 
	est un nombre entier"""

    #Cet fonction pouvait être intégré directement au bloc heure_deb_fin()
    #Toutefois pour une question d'évolution du code dans de prochaine version
    #j'ai décidé de la gardé autonome.Si nous souhaitons implémenter des valeurs
    #décimal par éxemple et les tester...
	if heure_deb.isdigit() and heure_fin.isdigit():
		return True
	else:
		return False

def heure_deb_fin():
	"""Demande a l'utilisateur d'entrée l'heure 
	de début et de fin de la location."""
	while True:
		heure_deb = input(MSG_HEUR_DEB_INPUT)
		heure_fin = input(MSG_HEUR_FIN_INPUT)
		
		if int_test(heure_deb,heure_fin):
			pass
			heure_deb = int(heure_deb)
			heure_fin = int(heure_fin)
		else:
			print(MSG_0_24)
			continue
	
	
		if test_heure(heure_deb,heure_fin):
		
			return heure_deb,heure_fin
		else:
			continue 

	return False	

def test_heure(heure_deb, heure_fin):
	"""Si la durée totale de location est
	infèrieur est supérieur à 24h affiche 
	un méssage et retourne False.Si l'heure
	début est égale a l'heure de fin,retourne False
	et affiche un méssage a l'utilisateur"""

    #Bloc de débuggage:
	#print(f"{heure_deb}>{heure_fin}")
	#print(heure_deb<heure_fin)
	#print(type(heure_deb))
	#print(type(heure_fin))

	if heure_deb > heure_fin:
		print(MSG_DEB_APR_FIN) 
		return False		
	
	if heure_deb == heure_fin:
		print(MSG_DEB_FIN_EGALE)
		return False	

	return True		


def calc_tarif(heure_deb,heure_fin):
	"""Calcul tarif total location"""
	#Définie les variables suivantes comme 
	#faisant partie du scope global et non pas
	#du scope local de 'calc_tarif'.

	global duree_tarif_1
	global duree_tarif_2
	global duree_total
	global prix_tarif_1
	global prix_tarif_2
	global prix_total
	
	#Reinitialisaton:
	#Les variables doivent être réinitialisé
 	#afin de ne pas ajouter les valeurs du calcul
	#précedent. 
	duree_tarif_1 = 0
	duree_tarif_2 = 0
	duree_total = 0

	prix_tarif_1 = 0
	prix_tarif_2 = 0
	prix_total = 0
		
	
	#print débuggage:
	#print(heure_deb,heure_fin)
	
	#Les contrôles par conditions suivantes établissent les valeurs de chacunes des durées
    # de location en fonction des horaires données par l'utilisateur.
	if 0 < heure_deb < 7:
		duree_tarif_2 = 7 - heure_deb
		print("1 duree_tarif_2 = 7 - heure_deb",duree_tarif_2)
	

	if 17 < heure_fin <= 24:
		duree_tarif_2 += heure_fin - 17

		#print débuggage
		#print("2 duree_tarif_2 += heure_fin - 17",duree_tarif_2)

	if 7 > heure_deb and heure_fin > 17:
		duree_tarif_1 += 10 

		#print débuggage
		#print("3 duree_tarif_1 += 10", duree_tarif_1)  	

	if 7 <= heure_deb <= 17 and 7 <= heure_fin <= 17:
		duree_tarif_1 = heure_fin - heure_deb

		#print débuggage
		#print("4 duree_tarif_1 = heure_fin - heure_deb",duree_tarif_1)

	if 7 <= heure_deb <= 17 and heure_fin > 17:
		duree_tarif_1 += 17 - heure_deb

		#print débuggage
		#print("5 duree_tarif_1 += 17 - heure_deb",duree_tarif_1)
	
	if heure_deb < 7 and  heure_fin < 17:
		duree_tarif_1 += heure_fin - 7
		
		#print débuggage
		#print("6 duree_tarif_1 += 17 - heure_deb",duree_tarif_1)
	
	if heure_deb < 7 and heure_fin <= 17:
		duree_tarif_1 = heure_fin - 7
		#print("7 duree_tarif_1 += heure_fin - 7",duree_tarif_1)
    
    #Les lignes suivantes calcules les prix des durées respectives
    #es tarifs 1 et 2.Puis la duree total et le tarif total.
	prix_tarif_1 = duree_tarif_1 * TARIF_1
	prix_tarif_2 = duree_tarif_2 * TARIF_2
	
	prix_total = prix_tarif_1 + prix_tarif_2
	duree_total = duree_tarif_1 + duree_tarif_2
	#print(duree_tarif_1,duree_tarif_2,duree_total,prix_tarif_1,prix_tarif_2,prix_total)

	return duree_tarif_1,duree_tarif_2,duree_total,prix_tarif_1,prix_tarif_2,prix_total



def main():
	"""Point d'entrée du programme.Ici est définie
	le cours de déroulement du script"""

	#Boucle tant que vrai.Sera stopé si l'utilisateur le souhaite.
	#Sinon une entrée sera demandé(cet fonction n'est pas encore implémenté).
	while True:
		
		heure_deb,heure_fin = heure_deb_fin()
		calc_tarif(heure_deb,heure_fin)
		
		#Débugage:
		#print(duree_tarif_1,duree_tarif_2,duree_total,prix_tarif_1,prix_tarif_2,prix_total)
        
        #Les affichages varies en fonction des heures et tarifs à afficher.
        #Si le tarif_1 n'est pas présent dans les heures de location réclamé par
        #l'utilisateur alors rien n'est affiché pour celui ci.

		if prix_tarif_1 == 0:

			print(MSG_LOUER_PENDANT)
			print(f"{duree_tarif_2}{MSG_AU_TARIF} {TARIF_2}")
			print(f"{MSG_TARIF_TOTAL} {prix_total}euro(s)")

		elif prix_tarif_2 == 0:
			print(MSG_LOUER_PENDANT)
			print(f"{duree_tarif_1}{MSG_AU_TARIF} {TARIF_1}")
			print(f"{MSG_TARIF_TOTAL} {prix_total} euro(s)")

		else:
		
			print(MSG_LOUER_PENDANT)
			print(f"{duree_tarif_1}{MSG_AU_TARIF}{TARIF_1}euro(s)")
			print(f"{duree_tarif_2}{MSG_AU_TARIF}{TARIF_2}euro(s)")
			print(f"{MSG_TARIF_TOTAL}{prix_total}euro(s)")
			

		

				
#Ici nous indiquons à python que nous souhaitons éxecuter 
#la fonction main() en point d'entrée.
if __name__ == "__main__":
	main()	
