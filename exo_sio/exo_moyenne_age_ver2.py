
from math import sqrt
somme_age = 0
list_age = []
NBRE_AGE = 3
moyenne_age = 0



for i in range(0,3):
    #print("index i",i,)
    list_age.append(int(input(f"Entrer l'âge {i + 1} : ")))
    #print("index i",i,"liste age",list_age[i - 1])
    somme_age += list_age[i]
   



moyenne_age = somme_age / NBRE_AGE
print("L'age minimum est ",min(list_age))
print("L'age minimum est ",max(list_age))
print(f"Moyenne des ages: {moyenne_age:0.2f}")
print(f"Moyenne de la racine carrées de la somme des ages : {sqrt(moyenne_age):0.2f}")






