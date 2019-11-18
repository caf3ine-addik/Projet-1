import argparse
import json
from api import lister_parties, débuter_partie, jouer_coup


state_0 = {
    "joueurs": [
        {"nom": "1725", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}

def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - Phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joeur.')
    parser.add_argument('-l', '--lister', metavar='', help= 'Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    analyser_commande.idul = args.idul
    if args.lister:
        return lister_parties(args.idul)
    return args

if __name__ == "__main__":
    analyser_commande()

#Fonction 2
def afficher_damier_ascii(state_0):
    haut = f'Légende: 1 = {state_0["joueurs"][0]["nom"]}, 2 = automate\n'
    haut += '   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas += '  | 1   2   3   4   5   6   7   8   9'
    dam_vide = []
#creation damier vide
    for i in range(18, 1, -1):
        pair = list(f"{i // 2} | .   .   .   .   .   .   .   .   . |")
        impair = list('  |                                   |')
        if i%2 == 0:
            dam_vide.append(pair)
        else:
            dam_vide.append(impair)
#position joueurs       
    for i in range(2):
        dam_vide[18 - 2 * state_0["joueurs"][i]["pos"][1]][4 * state_0["joueurs"][i]["pos"][0]] = f'{1 + i}'
#position des murs horizontaux
    for i in range(len(state_0["murs"]["horizontaux"])):
        for j in range(7):
            dam_vide[19 - 2* state_0["murs"]["horizontaux"][i][1]][4 * state_0["murs"]["horizontaux"][i][0] + j - 1] = '-'
#position murs verticaux
    for x, y in state_0['murs']['verticaux']:
        dam_vide[18 - 2 * y][x * 4 - 2] = "|"
        dam_vide[17 - 2 * y][x * 4 - 2] = "|"
        dam_vide[16 - 2 * y][x * 4 - 2] = "|"
#rendu final  
    cadre = [] 
    for ligne in dam_vide:
        cadre += ligne + ['\n']
    damier = ''.join(cadre)
    print(haut + damier + bas)

tuple_id_état = débuter_partie(analyser_commande.idul)
if len(tuple_id_état) > 1:
    afficher_damier_ascii(tuple_id_état[1])
    while True:
        a = input('type de coup (D, MH, MV): ')
        b = input('''position de l'action (x,y): ''')
        move = jouer_coup(tuple_id_état[0], a, b)
        if type(move) == str:
            afficher_damier_ascii(move)
            print(move)
            break
        afficher_damier_ascii(move)
            
            
else:
    print(tuple_id_état)