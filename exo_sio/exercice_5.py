import random

A = random.randrange(1,100)

while True:
    print("Voici un nombre aleatoire: ", A)

    quit= input ("press Q t quit...")
    A = random.randrange(1,100)
    if quit in ('q','quit'):
        quit()
