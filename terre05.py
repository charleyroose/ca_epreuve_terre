'''
Divisions

Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.


Exemples d’utilisation :
$> python exo.py 5 2
résultat: 2
reste: 1


$> python exo.py 10 0
erreur.


$> python exo.py 3 5
erreur.
'''

import sys

def divide_func():
    dividend = int(sys.argv[1])
    divider = int(sys.argv[2])

    if dividend < divider or divider < 1 :
        return "erreur."
    else:
        result = dividend / divider
        rest = dividend % divider
        return f"résultat: {int(result)} \nreste: {rest}"

print(divide_func())