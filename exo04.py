import sys

# j'ajoute l'instruction "try-except" dans le cas où l'argument donné n'est pas un bn entier

try:
    var = int(sys.argv[1]) # je convertis l'argument donné en nb entier (int)

    if var % 2 == 0:
        print("pair")

    else:
        print("impair")

# si argument donné n'est pas un nb entier, alors cette string sera print

except (IndexError, ValueError):
    print("Tu ne me la mettras pas à l’envers.")
