import argparse
import json
from api import lister_parties, débuter_partie, jouer_coup


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    analyser_commande.idul = args.idul
    if args.lister:
        return lister_parties(args.idul)
    return args

if __name__ == "__main__":
    analyser_commande()

#Fonction 2
def afficher_damier_ascii(rep):
    haut = f'Légende: 1 = {rep["joueurs"][0]["nom"]}, 2 = automate\n'
    haut += '   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas += '  | 1   2   3   4   5   6   7   8   9'
    dam_vide = []
#creation damier vide
    for i in range(18, 1, -1):
        pair = list(f"{i // 2} | .   .   .   .   .   .   .   .   . |")
        impair = list('  |                                   |')
        if i % 2 == 0:
            dam_vide.append(pair)
        else:
            dam_vide.append(impair)
#position joueurs       
    for i in range(2):
        dam_vide[18 - 2 * rep["joueurs"][i]["pos"][1]][4 * rep["joueurs"][i]["pos"][0]] = f'{1 + i}'
#position des murs horizontaux
    for i in range(len(rep["murs"]["horizontaux"])):
        for j in range(7):
            dam_vide[19 - 2 * rep["murs"]["horizontaux"][i][1]][4 * rep["murs"]["horizontaux"][i][0] + j - 1] = '-'
#position murs verticaux
    for x, y in rep['murs']['verticaux']:
        dam_vide[18 - 2 * y][x * 4 - 2] = "|"
        dam_vide[17 - 2 * y][x * 4 - 2] = "|"
        dam_vide[16 - 2 * y][x * 4 - 2] = "|"
#rendu final  
    cadre = [] 
    for ligne in dam_vide:
        cadre += ligne + ['\n']
    damier = ''.join(cadre)
    print(haut + damier + bas)

id_state = débuter_partie(analyser_commande.idul)
if len(id_state) > 1:
    afficher_damier_ascii(id_state[1])
    while True:
        a = input('type de coup (D, MH, MV): ')
        b = input('''position de l'action (x,y): ''')
        move = jouer_coup(id_state[0], a, b)
        if type(move) == str:
            afficher_damier_ascii(move)
            print(move)
            break
        afficher_damier_ascii(move)
            
            
else:
    print(id_state)