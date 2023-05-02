import sys

def prime_number():
    try:
        nb_entier = int(sys.argv[1])
        # Vérification du nombre d'arguments
        if len(sys.argv) != 2:
            print("Erreur, il ne peut y avoir qu'un seul argument.")
            sys.exit()
        # Vérification d'un entier positif
        if nb_entier <= 1:
            print("Erreur, l'argument donné doit être positif.")
            sys.exit()

    except (ValueError, IndexError):
        print("Erreur, l'argument donné doit être un nombre entier.")
        sys.exit()

    # écrire une boucle qui divise le nb_entier, de 2 jusqu'à sa racine carrée, si un des résultats ne laisse pas de reste, alors nb_entier n'est pas un nombre premier.
    else:
        if nb_entier == 2:
            print(nb_entier, "est un nombre premier.")
            sys.exit()
        #gagner du temps, si nb_entier est pair, alors nb_entier n'est pas un nombre premier
        elif nb_entier % 2 == 0:
            print(nb_entier, "n'est pas un nombre premier.")
            sys.exit()
	   #ne tester que les chiffres impair
        else:
            count = 3
            result = nb_entier ** 0.5
        
            while count <= result:
                if nb_entier % count == 0:
                    print(nb_entier, "n'est pas un nombre premier.")
                    sys.exit()
                count += 2
            print(nb_entier, "est un nombre premier.")
prime_number()