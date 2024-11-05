#Mehdi NAOUI
#BTS SIO SLAM
#2024
#
#Exerice liste tâches python.
#____________________________

task: list = [["nom: reviser","description: reviser cejm","Statut: en cours"]]
quit_: list = ("q","Q")
Flag: bool = True
user_value: str = ""
user_value2: str = ""
new_task: str = ""
new_desc: str = ""
new_stat: int = ""
list_del: list = []


menu: str = ("Entrer:\n\t[1] Ajouter une tâche \n\t[2] Afficher les tâches\n\t[3]Changer le statut d'une tâche\n\t[4]Supprimer une tâche)[q] pour quitter.\n")


 
def add_task(task):
	new_task = ("nom: " +  input("Entrer un nom de tache::"))
	new_desc = ("description:" + input("Entrer une descripton:"))
	new_stat = ("Statut:" + input("Entrer un statut('en cours' ,'terminé'):"))
	
	task.append([new_task,new_desc,new_stat])
	return 0;

def change_status(task):
	show_task(task)
	user_value = input("Quel est le numéro de la tâche dont vous voulez changer le statut: ")
	
	if not user_value.isnumeric():
		print("Entrer le numéro de la tache en chiffre UNIQUEMENT...")
	else:
		user_value2 = int(input("Entrer '1' pour appliquer le statut 'en cours' ou '0' pour appliquer 'terminer' : ")) 
		user_value = int(user_value)
		if user_value2 == 1:
			task[user_value][2] = "en cours"
		if user_value2 == 0:
			task[user_value][2] = "terminé"
			
	
	return 0

def show_task(list_task):
	for element in task:
		print(f"Tache n°: {task.index(element)}")
		print(f"\n\t{"\n\t".join(element)}")
	
			

	return 0

def del_task(task):
	show_task(task)
	user_value = input("Entrer le numero de la tache que vous souhaitez supprimer: ")

	if not user_value.isnumeric():
		print("Entrer le numéro de la tache en chiffre UNIQUEMENT...")
	else:
		
		list_del = task.pop(int(user_value))
		print("\nVous avez supprimer: "," ".join(list_del))


	return 0




print("Bienvenue dans le gestionnaire de tâche.")
print("Pour quitter entrer 'q' ou 'Q' lors de la saisie.")
print("Ici vous pouvez enregistrer un tâche avec un nom, une descripton et un statut.")
print("Presser entrer pour continuer...\n")

while Flag:
	print(menu)
	user_value = input("Faite un choix(chiffre de 1-4):")
	if user_value in quit_:
		break	
	if int(user_value) == 1:
		add_task(task)

	elif int(user_value) == 2:
		show_task(task)

	elif int(user_value) == 3:
		change_status(task)

	elif int(user_value) == 4:
		del_task(task)
	
	else:
		Flag = False


		

		
