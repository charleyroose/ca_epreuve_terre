'''
L'alphabet

Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle.
'''

def alphabet_string():
    alphabet = ""
    for i in range(97, 123):
        alphabet += chr(i)
    # ajoute un retour à la ligne à la fin de la chaine
    alphabet += "\n"
    # affiche la chaine sans retour à la ligne
    print(alphabet, end="")
alphabet_string()