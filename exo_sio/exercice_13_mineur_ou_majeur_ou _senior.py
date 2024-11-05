#Exercice 13 - mineur ou majeur ou senior
#Mehdi NAOUI 
#BTS SIO
#09/10/2024
#________________________________________________________________

#Demande à l'utilisateur d'entrer son âge.
age = input("Quelle est votre âge? (entrer 'q' ou 'quit' pour quitter): ")

#Permet à l'utilisateur de quitter la séssion en préssant 'q'.
if age in ('q','quit'):
    quit()

#Boucle tanque l'utilisateur n'a pas pressé 'q'.
while True:
    #Transtype mon entré utilisateur de type caractère en type entier.
    age = int(age)

    #Block if elif else qui test l'entrée afin de determiner 
    #si l'utilisateur est mineur , majeur ou senior.
    #Si la valeur entrée est inférieur à 0 alors l'utilisateur est
    #notifié de ne pas entrer de valeur infèrieur à 0.
    if age < 0:
        print("Entrer une valeur positif")
        pass
    elif age < 18:
        print("Vous êtes mineur.")
    elif age <= 65:
        print("Vous ête majeur.")
    else:
        print("Vous êtes senior.") 
    
    age = input("Quelle est votre âge? (entrer 'q' ou 'quit' pour quitter): ")

    if age in ('q','quit'):
        quit()
    
