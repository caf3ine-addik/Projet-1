# fonction 1

import argparse
import json


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help= 'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

if __name__ == "main":
    analyser_commande()

#Fonction 2
def afficher_damier_ascii():
    haut = f'Légende: 1=idul, 2=automate\n'
    haut +='   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas +='  | 1   2   3   4   5   6   7   8   9'
    dam_vide = []
    for i in range(18, 1, -1):
        pair = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
        impair = list('  |                                   |')
        if i%2 == 0:
            dam_vide.append(pair)
        else:
            dam_vide.append(impair)
    
    
    cadre = []
    for ligne in dam_vide:
        cadre += ligne + ['\n']
    damier = ''.join(cadre)

    print(haut + damier + bas)

afficher_damier_ascii()