from math import sqrt

age_1 = int(input("Entrer l'âge 1 : "))
age_2 = int(input("Entrer l'âge 2 : "))
age_3 = int(input("Entrer l'âge 3 : "))

NBRE_AGE = 3

list_age = []

list_age.append(age_1)
list_age.append(age_2)
list_age.append(age_3)

moyenne_age = age_1 + age_2 + age_3 / 3
print("L'age minimum est ",min(list_age))
print("L'age minimum est ",max(list_age))
print(f"Moyenne des ages {moyenne_age:0.2f}")
print(f"Moyenne des ages a la racine carré {sqrt(moyenne_age):0.2f}")






