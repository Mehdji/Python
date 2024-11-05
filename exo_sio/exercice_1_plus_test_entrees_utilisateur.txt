#L'utilisateur entre son nom et prénom puis ces notes.
#Une moyenne est alors calculé si le type des données entrées correspondent.
#Si les donnés ne sont pas valides alors elle sont redemandés a l'utilisateur.
#Exercice1 < Module 2 -  Introduction à  Python.pdf
#Mehdi NAOUI 
#BTS SIO
#09/10/2024
#________________________________________________________________


#La fonction suivante retourne vrai si c'est in float ou un entier 
# contenu dans la chaîne de caractère en argument.
def test_float(note):
    """Retourne False si la valeur en argument 
    ne peut pas être transformer en float"""
    try: 
        float(note)
    except ValueError:
        return False
    else:
        return True  


#___L'éxecution démarre ici___
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#Message de bienvenue annoncant à l'utilisateur le role du programme ainsi que
#le moyen de quitter.

print("\n\t____Bienvenue dans le calculateur de moyenne...(Entrer 'q' pour quitter...)____")

#Boucle tant que l'utilisateur n'a pas entrer de nom et prenom correcte.
while True:
    
    nom = input("\nQuelle est votre nom ? ")
    prenom = input("\nQuelle est votre prenom ? ")
    
    #Vérifie si l'utilisateur souhaite quitter.
    if (nom in ('q')) or (prenom in ('q')):
        quit()

    #Le method .isalpha() est ici invoqué.
    # Cette method test si la chaîne est constitué de lettres.
    # Si l'une des entrées retournent faux la condition n'est pas remplis.
    #la bouche recommence alor au début.
    if nom.isalpha() and prenom.isalpha():
        break
    else:
        print("\n\tEntrer un prenom et nom valide...(Lettre uniquement)\n\t(Entrer 'q' pour quitter...)")



while True:    

    math = input("\nQuelle est votre note de math ? ")
    anglais = input("\nQuelle est votre note d'anglais ? ")
    info = input("\nQuelle est votre d'informatique ? ")

    #Vérifie si l'utilisateur souhaite quitter.
    if (math in ('q','quit')) or (anglais in ('q','quit')) or (info in ('q','quit')):
        quit()


    #Lea fonction test_float est ici appelé.
    # Cet method test si la chaine est constitué de nombres entier ou float.
    #Si l'une des entrées retournent faux la condition n'est pas remplis.
    #la bouche recommence alor au début.
    if test_float(math) and test_float(anglais) and test_float(info) :
        break
    else:
        print("\n\tEntrer uniquement des nombres...\n\t")
        continue

        

#Quotient de la sommes totales des notes par le nombre de note.
moyenne = (float(math) + float(anglais) + float(info)) / 3

#Chaîne de caractère présentant le nom, prénom et la moyenne sur la sortie standard.
print(f"\n{prenom.title()} {nom.title()} votre moyenne est {(moyenne):0.2f} sur 20.")