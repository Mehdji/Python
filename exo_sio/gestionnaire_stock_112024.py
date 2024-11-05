#MEHDI NAOUI 
#BTS SIO SLAM
#02/11/2024
#
# Votre mission est de créer un programme Python qui permettra de gérer le stock de 
# produits d'une petite boutique. Ce programme devra permettre à l'utilisateur 
# d'afficher la liste des produits disponibles, d'ajouter de nouveaux produits ou de 
# modifier leurs quantités, de vérifier si un produit est en stock, et de supprimer des 
# produits en fonction de la quantité. Enfin, le programme devra aussi permettre de 
# trier les produits par ordre alphabétique et gérer les erreurs lorsque l'utilisateur 
# essaie de supprimer ou consulter un produit qui n'existe pas.
#_____________________________________________________________________________________


#Variabes et listes.
list_products: list[list[str,int]] = [["pomme",10],["banane",20],["cerise",30]]
product_name: str = ""
product_quantity: int = 0

#Méssages .
menu_list: list[str] = ["1. Afficher la liste des produits en stock","2. Ajouter un produit ou modifier la quantité","3. Vérifier si un produit est en stock","4. Supprimer un produit en stock","5. Trier les produits par ordre alphabétique","6. Quitter"]
welcome: str = "Bienvenue dans le gestionnaire de stock."
list_msg: str = "Voici la liste des produits en stock :"
add_product_msg: str  = "Entrez le nom du produit que vous souhaitez ajouter ou modifier :"
product_quantity_msg: str = "Entrez la quantité de produit: "
delete_product_msg: str = "Entrez le nom du produit que vous souhaitez supprimer :"
no_stock_msg: str = "Aucun produit en stock."
product_name_error_msg: str = "Le nom du produit doit être une chaine de caractères."
product_quantity_error_msg: str = "La quantité doit être une valeur numérique."
product_already_in_stock_msg: str = "est déjà en stock."
is_in_stock_msg: str = "est en stock."
is_not_in_stock_msg: str = "n'est pas en stock."
add_change_msg: str = "Voulez vous ajouter un produit presser 'a' pour modidifer une quantité presser 'q' : " 

#Fonctions.
def test_value(value: str) -> bool:
    """Teste si la valeur est un nombre entier, un float ou bien une chaîne de caractère.
    Retourne 0, la valeur est un entier.
    Retourne 1, la valeur est un float.
    Retourne 2, la valeur est une chaîne de caractères""" 

    if value.isdigit():
        return 0
    else:
        try:
            float(value)
            return 1
        except ValueError:
            return 2

def show_products() -> int:
    """Affiche les produits en stock"""
    
    print(list_msg)
    if not list_products:
        print(no_stock_msg)
    else:
        for i in list_products:
            print(f"-{i[0]} : {i[1]} en stock.")
    return 0

def add_product() -> int:
    """Ajouter un produit ou modifier la quantité d'un produit éxistant."""
    while True:
        if input(add_change_msg) == "q":
            show_products()
            product_name = input("Entrez le nom du produit dont vous voulez changer la quantité: ")
            product_quantity = input("Entrez la nouvelle quantité: ")
            for i in list_products:
                if product_name in i:
                    
                    list_products[i][1] = product_quantity
                else:
                    print(f"{product_name} n'est pas en stock.")
                    break
        else:
            product_name = input(add_product_msg)

            if test_value(product_name) != 2:
                print(product_name_error_msg)
                return 0
        
        product_quantity = input(product_quantity_msg)
        if test_value(product_quantity) == 2:
            print(product_quantity_error_msg)
            return 0

        if product_name in list_products:
            print(f"{product_name} {product_already_in_stock_msg}")
            
        else:
            if test_value(product_quantity) == 1:
                list_products.append([product_name,float(product_quantity)])
            else:
                list_products.append([product_name,int(product_quantity)])
    return 1

def check_product() -> bool:
    """Vérifier si un produit est en stock"""

    product_name = input("Entrez le nom du produit à vérifier : ")
    if product_name in list_products:
        print(f"{product_name}{is_in_stock_msg}")
        return True
    else:
        print(f"{product_name} {is_not_in_stock_msg}")
        return False

def delete_product() -> int:
    """Supprimer un produit"""
    return 0

def sort_products() -> int:
    """Trier les produits par ordre alphabétique"""
    print("Liste des poduits non triés:")
    for i in list_products:
        print(f"-{i[0]} : {i[1]} en stock.")
    print("Voici la liste des produits triée par ordre alphabétique :")
    list_products.sort()
    for i in list_products:
        print(f"-{i[0]} : {i[1]} en stock.")
    return 0

def error_handling() -> int:
    """Gérer les erreurs"""
    print("Choix invalide, veuillez réessayer.")
    return 0

def menu():
    """Affiche le menu"""
    for i in menu_list:
        print(i)
    return 0


def main():
    """Fonction principale.Point d'entrée du programme."""

    #Méssage de bienvenue.
    print(welcome)

    while True:
        input("Presser ENTRER pour continuer...")
        #Affichage du menu.
        menu()
        #Choix de l'utilisateur.
        choice = input("Entrez votre choix : ")
        
        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            product_name = input("Entrez le nom du produit à vérifier : ")
            check_product(product_name)
        elif choice == "4":
            delete_product()
        elif choice == "5":
            sort_products()
        elif choice == "6":
            print("Au revoir !")
            break
        else:
            error_handling()


#Si le script est éxecuté alors la fonction main() est appelée.
#Si le script est importé, la fonction main() n'est pas appelé.
if __name__ == "__main__":
    main()
