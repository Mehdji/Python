#Cet algorithme permute les varibale A et B
#avec deux variables uniquement
#Mehdi NAOUI BTS SIO SLAM
#07/10/24
#_________________________________

#Voici différentes solutions a cet éxercice.
#_____________________________________________________________
#1. Par éxémple dans le premier nous utilisons une 
#suite d'poérateur logique 'or' afin de définr les encadrements.

"""
while True:
    x = float(input ("Entrer une valeur: "))

    if (x >= 2.0 and x < 3.0) or (x > 0 and x <= 1.0 )  or (x >= -10.0 and x < -2.0):
        print("x est inclue dans l'ensemble I.")
    else:
        print("x est exclue de l'ensemble I.")
"""
#_____________________________________________________________
#2.Dans le second nous utilisons une une suite de 'if' et 'elif'. 

"""

while True:
    x = input ("Entrer une valeur ('q' ou 'quit' pour quitter...): ")

    if x in ('q','quit'):
            quit()

    x = float(x)

    if (x >= 2.0 and x < 3.0):
        print("x est inclue dans l'ensemble I.")
    elif (x > 0 and x <= 1.0 ):
        print("x est inclue dans l'ensemble I.")
    elif(x >= -10.0 and x < -2.0):
        print("x est inclue dans l'ensemble I.")
    else:
        print("x est exclue l'ensemble.")
"""
#_____________________________________________________________
#3.Le trosième ressemble fortement au permier. 
#En revanche ici le 'x' est encadrer ce qui nous évite d'ajouter un opérateur 'and'.
while True:
    x = float(input ("Entrer une valeur: "))

    if ( 2.0 <= x < 3.0) or ( 0 < x <= 1.0 ) or (-10.0 <= x <= -2.0):
        print("x est inclue dans l'ensemble I.")
    else:
        print("x est exclue de l'ensemble I.")