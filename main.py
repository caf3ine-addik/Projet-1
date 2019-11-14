# fonction 1

import argparse


def analyser_commande():
    parser = arparse.ArgumentParser(description= "Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help= 'Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ == "main":
    analyser_commande()