# fonction 1

import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help= 'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

if __name__ == "main":
    analyser_commande()

#Fonction 2

def damier():
    ligne = ''
    for i in range(0,20):
        if i == 0:
            ligne += '   -----------------------------------'
        if i % 2 == 0 and i != 18:
            ligne += '  |                                   |'
        if i == 18:
            ligne += '--|----------------------------------- \n'
        if i == 19:
            ligne += '  | 1   2   3   4   5   6   7   8   9\n'
        if (i % 2) != 0:
            ligne += '  | .   .   .   .   .   .   .   .   . |\n'
    print(ligne)
print(damier())