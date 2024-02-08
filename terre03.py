'''
L’alphabet à partir de

Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle.
'''

import sys

def print_alphabet_from():
    letter = sys.argv[1]
    alphabet_from = ""
    # met l'argument sous son code ascii
    for n in range(ord(letter), 123):
        alphabet_from += chr(n)
    return alphabet_from
print(print_alphabet_from())