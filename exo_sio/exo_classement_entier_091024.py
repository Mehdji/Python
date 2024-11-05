#Classe les nombres réels d'une liste créer par l'utilisateur en ordre croissant.
#Mehdi NAOUI
#BTS SIO SLAM
#2024
#09/10/24
#____________________________________________________


list = []
i = 0
j = 0

msg = "___Bienvue dans le trieur de liste SORTATOR 0.1.___"
instruction = "\n\t-Entrer 's' pour trier votre liste.\n\t-Entrer 'q' pour quitter."

def test_float(user_value):
    """Retourne False si la valeur en argument 
    ne peut pas être transformer en float"""
    try: 
        float(user_value)
    except ValueError:
        return False
    else:
        return True  

def create_list():
    """Create a list from user's input"""
    while True:
        user_value = input("Entrer un nombre ('s' pour trier la liste / 'q' pour quitter) : ")
        
        if user_value in ("q","quit","Q","QUIT"):
            quit()
        elif user_value in ("s","S"):
            print("s a été entré")
            return list
        
        if test_float(user_value):
            pass
        else:
            print("Veuillez entrer un nombre...\n{} n'est pas un nombre.".format(user_value))
            continue

        list.append(float(user_value))
        print("\t\nVoici la liste actuel non trié: {:s}.Vous avez ajouté {}.".format("".join(str(list)),user_value)) 
    
def sort_list_ascending(input_list,output_list=None):
    """Sort interger's list element in ascending order"""
    create_list()
    for i in range(len(input_list)):
        #print("\tINDICE I:",i)
        
        for j in range(len(input_list)):
            #print("index j:",j)
            #print(f"{list[i]} < {list[j]} : ",(list[i]>list[j]))
            if input_list[i] < input_list[j]:
                
                input_list[i],input_list[j] = input_list[j] ,input_list[i]
    return input_list
            
def main():
    print(msg + instruction)
    sort_list_ascending(create_list())

    print("\tVoici votre liste trié: ", end ="") 
    for element in list:
        print(element, end=" ")
    



if __name__ == "__main__":
    main()
    

        
