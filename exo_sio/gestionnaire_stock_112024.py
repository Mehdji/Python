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
#+ Ajout couleurs plus quelques mises en formes.
#_____________________________________________________________________________________
#import de la bibliothèque rich pour les couleurs et mises en formes.
from rich import print 
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich import box

#import time pour les emojis animés.
import time



#Variabes et listes.
list_products: list[list[str,int]] = [["pomme",10],["banane",20],["cerise",30]]
product_name: str = ""

product_quantity: int = 0

#Méssages .
menu_list: list[str] = ["[menu]1[/menu]. :clipboard: Afficher la liste des produits en stock","[menu]2[/menu]. :heavy_plus_sign: Ajouter un produit ou modifier la quantité","[menu]3[/menu]. :mag: Vérifier si un produit est en stock","[menu]4[/menu]. :wastebasket: Supprimer un produit en stock","[menu]5[/menu]. :abc: Trier les produits par ordre alphabétique","[menu]6[/menu]. :door: Quitter"]
welcome: str = "Bienvenue dans le gestionnaire de stock."
list_msg: str = "Voici la liste des produits en stock :"
#add_product_msg: str  = "Entrez le nom du produit que vous souhaitez ajouter ou modifier :"
add_change_msg: str = "Entrez le nom du produit que vous souhaitez [white bold]ajouter[/white bold] ou [white bold]modifier[/white bold] : "
add_or_minus_quantity_msg: str = "Voulez vous ajouter ou soustraire une quantité ? (Entrez 'a' ou 's') : "
product_minus_quantity_msg: str = "Entrez la quantité que vous souhaitez ajouter à {product[0]} qui est actuellement de {product[1]} : "
product_add_quantity_msg: str = "Entrez la quantité que vous souhaitez ajouter à {product[0]} qui est actuellement de {product[1]} : "
delete_product_msg: str = "Entrez le nom du produit que vous souhaitez supprimer :"
product_check_name: str = "Entrez le nom du produit à vérifier : "
no_stock_msg: str = "Aucun produit en stock."
product_name_error_msg: str = "Le nom du produit doit être une chaine de caractères."
product_quantity_error_msg: str = "La quantité doit être une valeur numérique."
product_already_in_stock_msg: str = "est déjà en stock."
is_in_stock_msg: str = " est en stock."
is_not_in_stock_msg: str = " n'est pas en stock."
error_handle_msg: str = "Choix invalide, veuillez réessayer."
#add_change_msg: str = "Voulez vous ajouter un produit presser 'a' pour modidifer une quantité presser 'q' : " 

#Création d'une console et d'un avec la bibliothèque rich ainsi qu'un dictionnaire nommé theme contnant des couleurs.
console = Console()
custom_theme = Theme({
    # Couleurs principales pour différents types de messages
    'titre': 'bold cyan',              # Pour les titres et en-têtes
    's_titre': 'italic orange_red1',           # Pour les sous titres
    'success': 'bold green',           # Pour les succès (ajout, modification)
    'warning': 'bold yellow',          # Pour les avertissements
    'error': 'bold red',               # Pour les erreurs
    'info': 'bold blue',               # Pour les informations générales
    'menu': 'bold white',            # Pour les options du menu
    'product': 'cyan',                 # Pour les noms de produits
    'quantity': 'yellow'               # Pour les quantités
})
console = Console(theme=custom_theme)

#Vérifie la présence de la bibliothèque rich sur la machine.
def test_rich():
    try:
        from rich.table import Table
    except ImportError:
        print("La bibliothèque rich n'est pas installée sur votre machine.\nRich permet une meilleur experience utilisateur.\nEntrer 'pip install rich' pour l'installer.")
        return 0
    return 1

#Création d'une table.
def create_table(list_products: list[list[str,int]]) -> Table:
    table = Table(title="Liste des produits en stock",show_header=True,header_style="bold magenta",box=box.ROUNDED,min_width=50,show_lines=True)

    table.add_column("Produit",style="cyan bold")
    table.add_column("Quantité",style="yellow bold")
    for product in list_products:
        table.add_row(str(product[0]),str(product[1]))
    return table

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
    
    console.print(create_table(list_products),style="s_titre")
    return 0

def add_product() -> int:
    """Ajouter un produit ou modifier la quantité d'un produit éxistant."""

    while True:
        show_products()
        console.print(add_change_msg,style="s_titre")
        product_name = input()
        for product in list_products:
            #Test si le produit existe dans la liste.
            if product_name in product:
                console.print(add_or_minus_quantity_msg,style="s_titre")
                choice = input()
                if choice == "a":
                    console.print((product_add_quantity_msg).format(product=product),style="s_titre")
                    product_quantity = input()
                elif choice == "s":
                    console.print((product_minus_quantity_msg).format(product=product),style="s_titre")
                    product_quantity = input()
                if test_value(product_quantity) == 2:
                    console.print(product_quantity_error_msg,style="error")
                    break
            
                if choice == "a":
                    product[1] += int(product_quantity)
                elif choice == "s":
                    if product[1] - int(product_quantity) < 0:
                        console.print("La quantité ne peut pas être négative.",style="error")
                        break
                    product[1] -= int(product_quantity)
                console.print(f"{product_name} a été modifié avec succès.",style="success")
                return 1
        #Si le produit n'éxiste pas il est ajouté dans la liste.
        console.print(f"You added {product_name} to the stock.",style="success")
        product_quantity = input(f"Entrez la quantité pour {product_name} : ")
        if test_value(product_quantity) == 2:
            console.print(product_quantity_error_msg,style="error")
            break
    
        list_products.append([product_name,int(product_quantity)])
        console.print(f"{product_name} a été ajouté avec succès.",style="success")
        break
                    

    return 1

def check_product() -> bool:
    """Vérifier si un produit est en stock"""
    show_products()
    console.print(product_check_name,style="s_titre")
    product_name = input()
    for product in list_products:
        if product_name in product:
            console.print(f"{product_name}{is_in_stock_msg}",style="success")
            return True
    console.print(f"{product_name} {is_not_in_stock_msg}",style="error")
    return False

def delete_product() -> int:
    """Supprimer un produit"""
    show_products()
    product_name = input("Entrez le nom du produit à supprimer : ")
    for product in list_products:
        if product_name in product:
            list_products.remove(product)
            print(f"{product_name} a été supprimé.")
            return 0
    print(f"{product_name} n'est pas en stock.")
    return 0

def sort_products() -> int:
    """Trier les produits par ordre alphabétique"""
    console.print(create_table(sorted(list_products)),style="s_titre")

    return 0

def error_handling() -> int:
    """Gérer les erreurs"""
    console.print(error_handle_msg,style="error")
    return 0

def menu() -> int:
    """Affiche le menu"""
    for i in menu_list:
        console.print(Panel(i,style="titre",expand=False,title=':arrow_heading_down:'))
    """
    for i in menu_list:
       console.print(i,style="menu")
    """
    return 0

def animation(anim_type: str) -> int:
    """Animation de chargement"""
    if anim_type == "welcome":
        with console.status(
            "[s_titre]Presser [menu]'ENTRER'[/menu] pour continuer et afficher le menu...[/s_titre]",spinner="circle"
        ) as status:
            input()
    elif anim_type == "menu":
        with console.status(
            "[s_titre]Menu en cours...[/s_titre]",spinner="aesthetic"
            ) as status:
            time.sleep(1)
    return 1

def main():
    """Fonction principale.Point d'entrée du programme."""
    #Test si rich est bien installé.
    if test_rich() == 0:
        return 0
    #Méssage de bienvenue.
    console.print(welcome,style="titre")
    #Animation de bienvenue.
    animation("welcome")


    while True:
        #Animation du menu.
        animation("menu")
        #Affichage du menu.
        menu()
        #Choix de l'utilisateur.
        console.print("[s_titre]Entrez votre choix : [/s_titre]",style="s_titre")
        choice = input()
        
        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            
            check_product()
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
