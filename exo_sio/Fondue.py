




"""
nouvelleQuantite_fromage = (fromage) * nbre_personne / BASE
nouvelleQuantite_ail = (ail) * nbre_personne / BASE
nouvelleQuantite_eau = (eau) * nbre_personne / BASE
nouvelleQuantite_pain = (pain) * nbre_personne / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbre_personne} personnes, il vous faut: ")
print(f"_Fromage: {nouvelleQuantite_fromage:0.1f} gr de fromage")
print(f"_ail: {nouvelleQuantite_ail:0.1f} gousse d'ail")
print(f"_eau: {nouvelleQuantite_eau:0.1f} dl d'eau")
print(f"pain: {nouvelleQuantite_pain:0.1f} de pain")
"""
BASE = 4
fromage = 800.0 * BASE
eau = 2 * BASE
ail = 2 * BASE
pain = 400 * BASE

nbre_personne = float(input("Entrer le nombre d'inviter: "))

def nouvelle_quantite(nbre_pers,ingredient):
    nouvelle_quant =  nbre_pers * ingredient / BASE
    return nouvelle_quant

print(f"Pour faire une fondue fribourgeoise pour {nbre_personne} personnes, il vous faut: ")
print(f"_Fromage: {nouvelle_quantite(nbre_personne,fromage):0.1f} gr de fromage")
print(f"_ail: {nouvelle_quantite(nbre_personne,ail):0.1f} gousse d'ail")
print(f"_eau: {nouvelle_quantite(nbre_personne,eau):0.1f} dl d'eau")
print(f"_pain: {nouvelle_quantite(nbre_personne,pain):0.1f} de pain")



