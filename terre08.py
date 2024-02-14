'''
Puissance d'un nombre

Créez un programme qui affiche le résultat d’une puissance.


L’exposant ne pourra pas être négatif.


Exemples d’utilisation :
$> node exo.js 2 3
8

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

Fonction interdite : **
'''

import sys

def exponant_func():
    if len(sys.argv) != 3:
        return "erreur, veuillez donner deux arguments"
    
    #convertir en entier puis vérifier si la conversion est réussie

    elif not (isinstance(int(sys.argv[1]), int) and isinstance(int(sys.argv[2]), int)):
        return "erreur, veuillez insérer deux nombres"
    
    elif int(sys.argv[2]) < 1:
        return "erreur, veuillez insérer un exposant >= 1"
    
    else:
        result = int(sys.argv[1])
        initial_argument = int(sys.argv[1])
        exponant = int(sys.argv[2])

        for n in range(1, exponant):
            result *= initial_argument
    return result

print(exponant_func())