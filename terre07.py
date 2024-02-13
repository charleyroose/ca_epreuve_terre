'''
Taille d'une chaîne

Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.


Exemples d’utilisation :
$> python exo.py “Hello world!”
12


$> python exo.py
erreur.


$> python exo.py “Bonjour” “Aurevoir”
erreur.

$> python exo.py 10
erreur.

fonction interdite : length
'''

import sys

def string_size():
    if len(sys.argv) != 2:
        return "erreur, insérez un seul argument"
    elif len(sys.argv[1]) < 1:
        return "erreur, l'argument ne peut pas être vide"
    else:
        argument = sys.argv[1]
        # gestion de la nature de l'argument
        if argument.isdigit():
            return "erreur, l'argument doit être une chaîne de caractères"
        count = 0
        for index in argument:
            count += 1
    return count

print(string_size())