

print("\033[1;317;40m ")
user_name = input("what's your name?:")

message =  f"Hello,{user_name} would you like to learn some python today?\n"

print(message)

print(user_name.lower())
print(user_name.upper())

print(user_name.title(),"\n")

quote = "La guerre, un massacre de gens qui ne se connaissent pas, au profit de gens qui se connaissent mais ne se massacrent pas."


author_name = "paul valery"

message = f"{author_name.title()} once said \" {quote} \""
print(message)

user_name_2 = " John "
print("\nName with space:",user_name_2)
user_name_2_Nolspace = user_name_2.lstrip()
user_name_2_Norspace = user_name_2.rstrip()

print("\n\tName with spaces :\n",user_name_2)
print("\n\tName with left space removed:\n",user_name_2_Nolspace)
print("\n\tName without right space:\n",user_name_2_Norspace)
print("\n\tName without space:\n",user_name_2.strip())

filename = "python_notes.txt".removesuffix(".txt")

#filename.removesuffix(".txt")

print(filename)
