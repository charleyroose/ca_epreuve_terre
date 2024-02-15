'''
Racine carrée d’un nombre

Créez un programme qui affiche la racine carrée d’un entier positif.


Exemples d’utilisation :
$> python exo.py 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


Fonctions interdites: 
-La fonction sqrt
'''

import sys

def square_root():
    if len(sys.argv) != 2:
        return "erreur, veuillez insérer un argument"
    elif not sys.argv[1].isdigit():
        return "erreur, veuillez insérer un nombre entier positif"
    else:
        argument = int(sys.argv[1])
        result = argument ** 0.5
        return result
    
print(square_root())