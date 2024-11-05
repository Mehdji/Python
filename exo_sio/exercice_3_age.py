#Calcule l'annee de naissance en fontion de l'aga
#Import le module 'datetime' afin de connaitre l'année en cours.
#Mehdi NAOUI 
#BTS SIO
#09/10/2024
#________________________________________________________________

#import datetime
from datetime import datetime 

#Invoque datetime.now().year et attribue ca valeur retour a 
#la variable 'anne_en_cours'
annee_en_cours = int(datetime.now().year)

#Boucle continuant tant que l'utilisateur n'a pas rentré une valeur numérique positive.
while True:
    #collecte l'age de l'utilisateur
    age = input("\n\tQuel est votre âge? (entrer 'q'/'quit' pour quitter...) ")
    
    #Si il entre 'quit'37,'q'... le programme s'arrête.
    if age in ("q","quit","Q","QUIT"):
        quit()
    
    #Dans le cas ou l'utilisateur entre une autre valeur qu'un nombre la boucle reviens au début
    if age.isdigit():
        age = int(age)
        
        break
    else:
        #Le message s'affiche si une valeur différente d'un nombre est entrée.
        print("\n\tUne erreur est survenu.\n\tEntrer une valeur numérique ou bien positive...")
        pass

#Calcule l'annee de naissance en effectuant une soustraction.
annee_naissance = annee_en_cours - age 
#Affiche un méssage accompagnée de l'année de méssage.
print(f"\nVous ête née en {annee_naissance}.")