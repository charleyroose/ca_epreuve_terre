'''
Trié ou pas

Créez un programme qui détermine si une liste d’entiers est triée ou pas.


Exemples d’utilisation :
$> python exo.py 9 8 3
Pas triée !

$> python exo.py 3 8 9 12
Triée !

$> python exo.py “Salut”
erreur.

Fonctions interdites: 
-La fonction sort
'''

import sys

def sorted_or_not():
    if (len(sys.argv) < 3 or
        not all(n.isdigit() for n in sys.argv[1:])):
        return "erreur, veuillez n'insérer que des nombres entiers."
    else:
        #itérer chaque argument donné, puis le convertir en entier
        lst = []
        for x in sys.argv[1:]:
            lst.append(int(x))
        #comparer chaque entier avec le suivant
        for n in range(len(lst)-1):
            if lst[n] > lst[n+1]:
                return "Pas triée"
        return "Triée"
            
print(sorted_or_not())