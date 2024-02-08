'''
Afficheur d’arguments

Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.


Exemples d’utilisation :
$> python exo.py je suis solide !
je
suis
solide
!
'''

import sys

arguments = sys.argv

def print_arguments():
    for n in arguments:
        # ne pas afficher le nom du script
        if n == arguments[0]:
            continue
        else:
            print(n)

print_arguments()