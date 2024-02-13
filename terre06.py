'''
Inverser une chaîne

Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


Exemples d’utilisation :
$> python exo.py “Hello world!”
!dlrow olleH


$> python exo.py “lehciM”
Michel

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.
'''

import sys

def reverse_string():
    if len(sys.argv) != 2 or len(sys.argv) == 1:
        return "erreur, inserez un seul argument"
    elif len(sys.argv[1]) < 1 :
        return "erreur, l'argument ne peut pas être vide"
    else:
        argument = str(sys.argv[1])
        return argument[::-1]

print(reverse_string())