#Exercice 4 
#Mehdi NAOUI 
#BTS SIO
#09/10/2024
#________________________________________________________________
valeur_temp = 0

"""
def stock_value(a,b,c):
    
   a ,b ,c = c ,a ,b

    return a,b,c

"""

def stock_value(a,b,c):
    
    valeur_temp = a
    
    a = c

    c = b

    b = valeur_temp

    return a,b,c


valeur_a = int(input("Entrer valeur A:"))
valeur_b = int(input("Entrer valeur B:"))
valeur_c = int(input("Entrer valeur C:"))

print("\n\tAvant permutation :\n Valeur A=",valeur_a,"\nValeur B=",valeur_b,"\nValeur C=",valeur_c)

valeur_a, valeur_b, valeur_c = stock_value(valeur_a,valeur_b,valeur_c)

print("\n\tAprés permutation : A= {} B={} C={}".format(valeur_a,valeur_b,valeur_c))