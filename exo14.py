import sys

def est_triee(liste):
    # Vérifie si la liste est triée
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

try:
    if len(sys.argv) < 3:
        print("Erreur, la liste doit contenir au moins 2 arguments.")
        sys.exit()

    # Convertir les arguments en entiers
    liste_entiers = [int(arg) for arg in sys.argv[1:]]

    if est_triee(liste_entiers):
        print("Triée !")
    else:
        print("Pas triée !")

except (ValueError, IndexError):
    print("Erreur, la liste ne doit contenir que des nombres entiers.")
    sys.exit()
