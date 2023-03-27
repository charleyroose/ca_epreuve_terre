import sys

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Erreur, il ne peut y avoir qu'un seul argument")
else:
    arg = sys.argv[1]

    # Vérification de la nature de l'argument
    if not isinstance(arg, str):
        print("Erreur, l'argument doit être une chaîne de caractères")
    elif arg.isdigit():
    	print("Erreur, l'argument ne doit pas être un nombre entier")
    else:
        nb_character = 0
        for x in arg:
        	nb_character += 1
        print(nb_character)
