import sys

try:						#on vérifie que 2 arguments ont été donné
    var1 = int(sys.argv[1])
    var2 = int(sys.argv[2])
except (IndexError, ValueError):
    print("Erreur : deux arguments entiers sont nécessaires")
else:						#ici on vérifie que les arguments remplissent certaines conditions
    if var2 == 0:
        print("Erreur : division par zéro")
    elif var1 < var2:
        print("Erreur : le premier nombre doit être supérieur ou égal au deuxième")
    else:
        result = var1 // var2 #double symbole de division pour ne pas avoir un résultat à virgule
        rest = var1 % var2
        print("Résultat :", result)
        print("Reste :", rest)
