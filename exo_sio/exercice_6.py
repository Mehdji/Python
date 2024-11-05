import random

A = random.randrange(1,100)

while True:

    if A <= (50*0.666):
        print("Pile")
    else:
        print("Face")
    A = random.randrange(1,100)
    input("Press enter...")
