import sys

try:
    if len(sys.argv) < 3:
        print("Erreur, la liste doit contenir au moins 2 arguments.")
        sys.exit()
    #stocker l'état du tri
    est_triee = True

    #convertir la première entrée en entier
    int(sys.argv[1])

    #parcourir la liste d'arguments
    for n in range(2, len(sys.argv)):
        if int(sys.argv[n]) < int(sys.argv[n-1]):
            est_triee = False
            break

    if est_triee:
        print("Triée !")
    else:
        print("Pas triée !")

except (ValueError, IndexError):
    print("Erreur, la liste ne doit contenir que des nombres entiers.")