#MEHDI NAOUI
#BTS SIO SLAM
#21.10.24
#EXERCICE(LISTE) 1 MULTIPLCATION
#________________________________________

user_value: str = ""


def multiplcation(user_value):
    """Retourne valeur utilisateur en argument multiplié jusqu'a 10"""
    result: float = 0
    list_result: list = []
    i =0
    for x in range(0,11):
        result = x * user_value
        #print(list_result)
        list_result.append(result)

    for x in list_result:
        
        print(f"{user_value} x {list_result.index(int(x))}= ",x)
        i +=1
    return list_result

while True:
    user_value = int(input("Entrer une valeur: "))

    multiplcation(user_value)
   


