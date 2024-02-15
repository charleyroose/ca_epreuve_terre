'''
Nombre premier

Créez un programme qui affiche si un nombre est premier ou pas.


Exemples d’utilisation :
$> python exo.py 5
Oui, 5 est un nombre premier.

$> python exo.py 6
Non, 6 n’est pas un nombre premier.

Attention : 0 et 1 ne sont pas des nombres premiers.

Gérez les erreurs d’arguments.
'''

#for i in range(1, x) if i % n == 0, count += 1
#if count <= 2: x est un nombre premier
#arreter x à sa moitié pour réduire la durée du programme
#éliminer tous les multiples de 2
#éliminer tous les multiples de 5

import sys

def prime_number():
    if len(sys.argv) != 2:
        return "erreur, veuillez insérer un argument"
    elif not sys.argv[1].isdigit():
        return "erreur, veuillez insérer un nombre entier positif"
    else:
        argument = int(sys.argv[1])
        half_argument = argument / 2
        count = 2

        if argument == 1 or argument == 0:
            return f"Non, {argument} n'est pas un nombre premier."
        elif argument % 2 == 0 or argument % 5 == 0:
            return f"Non, {argument} n'est pas un nombre premier."
        else:
            for n in range(3, int(half_argument)):
                if argument % n == 0:
                    count += 1
                    break
        if count <= 2:
            return f"Oui, {argument} est un nombre premier."
        else:
            return f"Non, {argument} n'est pas un nombre premier."

print(prime_number())