#Generate an Ip V4 adress.
#Mehdi NAOUI
#BTS SIO slam
#2024
#_________________________

#import 'getrandbits' from random 
#'getrandbits' method generate random bit.
#bit's lenght is set in method's argument.
from random import getrandbits

def gen_adress_ipv4():
    """Generate Ip version 4 adress.
    Retun a list with four string elements."""
    adresse_ip_v4 = []

    #Loop four times through where each iteration create an 'octet'.
    for i in range(4):
        random_octets = str(getrandbits(8))
        adresse_ip_v4.append(random_octets)
    return adresse_ip_v4

welcome = "IP Generator v0.1\nGenerate Ip v4 adress.\nPress enter..." 
input(welcome)

while True:
   #Loop through while user doesn't type 'no'.
    
    #Format the list returned by gen_adress_ipv4()
    #in a string where each octets is sepratated 
    #by dots using .jion() method

    formatted_address = '.'.join(gen_adress_ipv4())
    
    print("\tYour IP v4 adress: ", formatted_address)
    
    #print(formatted_address)
    
    cont_loop = input("Do you to generate an new adress? (type 'n' to quit) ")
    
    if  cont_loop in ('no','NO','N','n'):
        break


