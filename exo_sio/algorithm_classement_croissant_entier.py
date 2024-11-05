#Classe les valeurs entrees par l'utilisateur par ordre croissant.
#Mehdi NAOUI, BTS SIO SLAM
#07/10/24
a = int(input("entrer un premier entier: "))
b = int(input("entrer un second entier: "))
c = int(input("entrer un troisieme entier: "))
 
if a > b:
    z = a
    a = b
    b = z
if c < a:
    z = c
    c = b
    b = a
    a = z
else:
    if c < b:
        z = c
        c = b
        b = z

print(" Voici les nombres classé par ordre croissant: ",a,b,c)

