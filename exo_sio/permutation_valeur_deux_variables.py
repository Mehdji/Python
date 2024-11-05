#Cet algorithme permute les varibale A et B
#avec deux variables uniquement
#Mehdi NAOUI BTS SIO SLAM
#07/10/24

a = int(input("Entrer un entier pour la variable A: "))
b = int(input("Entrer un entier pour la variable B: ")) 

print("Voici vos valeurs: A=",a,"B=",b)

a = a + b
b = a - b
a = a - b

print("Voici les valeurs suite a la permutation:\n a=",a,"b=",b)

