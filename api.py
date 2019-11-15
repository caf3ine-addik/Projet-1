import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help= 'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

if __name__ == "main":
    analyser_commande()