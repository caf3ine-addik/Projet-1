import argparse
import json


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
    return parser.parse_args()

if __name__ == "main":
    analyser_commande()

#Fonction 2
def afficher_damier_ascii(state_0):
    haut = f'Légende: 1={state_0["joueurs"][0]["nom"]}, 2=automate\n'
    haut +='   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas +='  | 1   2   3   4   5   6   7   8   9'
    dam_vide = []
#creation damier vide
    for i in range(18, 1, -1):
        pair = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
        impair = list('  |                                   |')
        if i%2 == 0:
            dam_vide.append(pair)
        else:
            dam_vide.append(impair)
#position joueurs       
    for i in range(2):
        dam_vide[18-2*state_0["joueurs"][i]["pos"][1]][4*state_0["joueurs"][i]["pos"][1]] = f'{1+i}'
#position des murs horizontaux
    for i in range(len(state_0["murs"]["horizontaux"])):
        for j in range(7):
            dam_vide[19-2*state_0["murs"]["horizontaux"][i][1]][4*state_0["murs"]["horizontaux"][i][0] + j] = '-'
#rendu final   
    cadre = [] 
    for ligne in dam_vide:
        cadre += ligne + ['\n']
    damier = ''.join(cadre)
    print(haut + damier + bas)

afficher_damier_ascii(state_0)