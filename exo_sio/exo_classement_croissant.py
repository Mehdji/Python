a = input("Entrer un premier nombre entier: ")
b = input("Entrer un second nombre entier: ")
c = input("Entrer un troisiÃme nombre entier: ")

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

print(" Voici les nombres classer par ordre croissant:,a,b,c)

print("")

