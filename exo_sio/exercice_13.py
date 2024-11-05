age = input("Quelle est votre âge? (entrer 'q' ou 'quit' pour quitter)")

if age in ('q','quit'):
    quit()

while True:
    age = int(age)
    if age < 18:
        if age < 0:
            print("Entrer une valeur positif")
            pass
            
        print("Vous êtes mineur.")
    elif age <= 65:
        print("Vous ête majeur.")
    else:
        print("Vous êtes senior.") 
    
    age = input("Quelle est votre âge? (entrer 'q' ou 'quit' pour quitter)")

    if age in ('q','quit'):
        quit()
    
