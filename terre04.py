'''
Pair ou impair

Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


Exemples d’utilisation :
$> python exo.py 2
pair

$> python exo.py 5
impair


$> python exo.py Bonjour
Tu ne me la mettras pas à l’envers.

$> python exo.py
Tu ne me la mettras pas à l’envers.


Attention : gérez aussi les entiers négatifs.
'''

import sys

def even_or_odd():
    if len(sys.argv) < 2 :
        return "tu ne me la mettras pas à l'envers"
    else:
        argument = sys.argv[1]
        # si entier négatif, prendre tout ce qu'il y a après le signe "-" 
        # et le transformer en integer negatif
        if argument[0] == "-":
            argument = int(argument[1:]) * -1
        else:
            argument = int(argument)
    if (argument % 2 == 0):
        return "pair"
    else:
        return "impair"

print(even_or_odd())