'''
Nom du programme

Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> python exo.py
exo.py

$> python crevette.py
crevette.py
'''

import sys

def script_name():
    result = sys.argv[0]
    return result

print(script_name())