#L'entrée de l'utilisateur est testée pour savoir si la valeur 
#est positif ou négative et pair ou impair.
#Mehdi NAOUI BTS SIO SLAM
#09/10/24
#__________________________________________

while True:
    A = input("Entrer un entier (entrer 'q' or 'quit' to quit): ")

    if A in ("quit","q"):
        quit()

    A = int(A)

    if A < 0 :
        if A % 2 == 0:
        
            print(A,"est un nombre pair négatif")

        else:
        
            print(A,"est un impair négatif.")

    elif A > 0 :
        if A % 2 == 0:
        
            print(A,"est un nombre pair positif")

        else:
        
            print(A,"est un nombre impair positif")
    else:
        print("Zero est pair et positif.")