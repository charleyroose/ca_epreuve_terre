'''
Trouver la Suisse

Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.


Exemples d’utilisation :
$> python exo.py 11 40 34
34

$> python exo.py 2 1 3
2

$> python exo.py 2 2 2
erreur.

Fonctions interdites: 
-La fonction sort
'''

import sys

def find_switzerland():
    if (len(sys.argv) != 4 or
        not sys.argv[1].isdigit() and not sys.argv[2].isdigit() and not sys.argv[3].isdigit() or
        int(sys.argv[1]) == int(sys.argv[2]) or int(sys.argv[2]) == int(sys.argv[3]) or int(sys.argv[1]) == int(sys.argv[3])):
        return "erreur, veuillez insérer 3 nombres entiers positifs différents"
    else:
        a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

        if (a < b and a > c or
            a > b and a < c ):
            return a
        elif (b < a and b > c or
              b > a and b < c ):
            return b
        elif (c < a and c > b or
              c > a and c < b ):
            return c
        
print(find_switzerland())