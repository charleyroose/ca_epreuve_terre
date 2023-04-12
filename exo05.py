import sys

def division_result():
        try:						             #on vérifie que 2 arguments ont été donné
            first_var = int(sys.argv[1])
            second_var = int(sys.argv[2])
            if len(sys.argv) != 3:
                print("Erreur : entrez 2 arguments")
                sys.exit()
        except (IndexError, ValueError):
            print("Erreur : deux arguments entiers sont nécessaires")
            sys.exit()

        else:						             #ici on vérifie que les arguments remplissent certaines conditions
            if second_var == 0:
                print("Erreur : division par zéro")
            elif first_var < second_var:
                print("Erreur : le premier nombre doit être supérieur ou égal au deuxième")
            else:
                result = first_var // second_var #double symbole de division pour ne pas avoir un résultat à virgule
                rest = first_var % second_var
                print("Résultat :", result)
                print("Reste :", rest)
                sys.exit()
division_result()