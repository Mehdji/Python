#Ask user for a value and print absolute value
#|a| = a
#|-a| = a
#|a-b| = |b-a|

message_intro_1 = "Welcome to Absolutor 1.0\n"
message_intro_2 = "This program return abolute value of the given number."

print(message_intro_1 + message_intro_2)
tempo = input("(press enter...)")

flag = True

while flag:
    x = input("Enter a number please: ")
    
    x = int(x)
    
    if x > 0:
        print(f"Absolute value of {x} is {x}.")
    elif x < 0:
        print(f"Absolute value of {x} is", x*-1)
    elif x in ("quit","q","Q","QUIT"):
        flag = False
        continue
    else:
         print("Enter non null number only please.")